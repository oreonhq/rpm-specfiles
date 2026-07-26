%global source0_hash f92302a60d3cc9a3686ab61eaca4eb510dc3d6ec1566d311ac74efd55ef61373

# remirepo/fedora spec file for php-phpunit-php-invoker2
#
# Copyright (c) 2011-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    9ee24c724374ba355385e98808da8b4343b28f67
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-invoker
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Invoker
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-phpunit-php-invoker2
Version:        2.0.1
Release:        14%{?dist}
Summary:        Invoke callables with a timeout

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
# From composer.json, require-dev
#        "phpunit/phpunit": "^8.5"
BuildRequires:  phpunit8 >= 8.5
%endif

# From composer.json, require
#        "php": ">=7.1",
#        "ext-pcntl": "*"
Requires:       php(language) >= 7.1
Requires:       php-pcntl
# From phpcompatinfo report for version 2.0.0
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpunit/php-invoker) = %{version}

%description
phpunit/php-invoker provides the means to invoke a callable with a timeout.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php

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
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

%if %{with_tests}
%check
: Generate tests autoloader
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests

: Run upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php \
      %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc README.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}

%changelog
%autochangelog
