%global source0_hash 88538198029a9daca5fc83dd0ca8adfd1429377bcee8bf78e6e41ec53677a116

# remirepo/fedora spec file for php-sebastian-code-unit-reverse-lookup
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    92a1a52e86d34cde6caa54f1b5ffa9fda18e5d54
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   code-unit-reverse-lookup
%global php_home     %{_datadir}/php/SebastianBergmann
%global ns_name      CodeUnitReverseLookup
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-sebastian-%{gh_project}
Version:        1.0.3
Release:        5%{?dist}
Summary:        Looks up which function or method a line of code belongs to, version 1

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^8.5"
BuildRequires:  phpunit8 >= 8.5
%endif

# from composer.json, "require": {
#        "php": ">=5.6"
Requires:       php(language) >= 5.6
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/%{gh_project}) = %{version}

%description
Looks up which function or method a line of code belongs to.

This package provides the version 1 of the library.

Autoloader: %{php_home}/%{ns_name}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{ns_name}

%check
%if %{with_tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_name}/autoload.php \
     %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}
%{php_home}/%{ns_name}

%changelog
%autochangelog
