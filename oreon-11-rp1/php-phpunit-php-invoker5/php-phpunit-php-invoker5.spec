%global source0_hash b62a266281ff2ae27d7324999f71a176d6a86424597174aae7130dad26c97156

# remirepo/fedora spec file for php-phpunit-php-invoker5
#
# SPDX-FileCopyrightText:  Copyright 2011-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

# disabled until phpunit11 available
%bcond_without       tests

%global gh_commit    c1ca3814734c07492b3d4c5f794f4b0995333da2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-invoker
%global gh_date      2024-07-03
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global major        5
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   Invoker

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        5.0.1
Release:        5%{?dist}
Summary:        Invoke callables with a timeout, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.2
BuildRequires:  php-spl
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# From composer.json, require-dev
#        "ext-pcntl": "*"
#        "phpunit/phpunit": "^11.0"
BuildRequires:  php-pcntl
BuildRequires:  phpunit11
%endif

# From composer.json, require
#        "php": ">=8.2",
Requires:       php(language) >= 8.2
# From phpcompatinfo report for version 4.0.0
Requires:       php-pcntl
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
phpunit/php-invoker provides the means to invoke a callable with a timeout.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate autoloader
%{_bindir}/phpab \
   --template fedora \
   --output  src/autoload.php \
   src

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%if %{with tests}
%check
: Generate tests autoloader
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests

: Run upstream test suite
ret=0
for cmd in php php82 php83 php84; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit11 || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc README.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
