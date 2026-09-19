%global source0_hash 907f56e39a68ef32acfe6d5feda76949d55bc9adcd52542f89c51255a09c2821

# remirepo/fedora spec file for php-sebastian-environment5
#
# Copyright (c) 2014-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Sources
%global gh_commit    830c43a844f1f8d5b7a1f6d6076b784454d8b7ed
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   environment
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global major        5
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Environment

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        5.1.5
Release:        9%{?dist}
Summary:        Handle HHVM/PHP environments, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-pcre
BuildRequires:  php-posix
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3"
BuildRequires:  phpunit9 >= 9.3
%endif

# from composer.json, "require": {
#        "php": ">=7.3"
Requires:       php(language) >= 7.3
# From phpcompatinfo report for 4.0.1
Requires:       php-pcre
Requires:       php-posix
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
This component provides functionality that helps writing PHP code that
has runtime-specific (PHP / HHVM) execution paths.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader
%{_bindir}/phpab \
   --template fedora \
   --output src/autoload.php \
   src

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%if %{with tests}
%check
mkdir vendor
touch vendor/autoload.php

: Run tests
ret=0
for cmd in php php74 php80 php81; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     -d pcov.enabled=1 \
     %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
