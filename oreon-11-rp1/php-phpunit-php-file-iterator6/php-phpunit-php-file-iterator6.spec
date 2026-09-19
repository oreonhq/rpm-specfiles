%global source0_hash 3633b0582157f564ecf2deb80b8ef8f245302aa6f635cc1111053645beec7b8e

# remirepo/fedora spec file for php-phpunit-php-file-iterator6
#
# Copyright (c) 2009-2025 Christof Damian, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    3d1cd096ef6bea4bf2762ba586e35dbd317cbfd5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-file-iterator
%global gh_date      2026-02-02
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global major        6
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   FileIterator

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        6.0.1
Release:        1%{?dist}
Summary:        FilterIterator implementation based on a list of suffixes, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.3
%if %{with tests}
# From composer.json, "require-dev"
#        "phpunit/phpunit": "^12.0"
BuildRequires:  phpunit12
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require"
#        "php": ">=8.3"
Requires:       php(language) >= 8.3
# From phpcompatinfo report for 4.0.0
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
FilterIterator implementation that filters files based on a list of suffixes.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
%{_bindir}/phpab \
   --template fedora \
   --output   src/autoload.php \
   src

%install
mkdir -p    %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src  %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php83 php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit12 || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%license LICENSE
%doc ChangeLog.md README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
