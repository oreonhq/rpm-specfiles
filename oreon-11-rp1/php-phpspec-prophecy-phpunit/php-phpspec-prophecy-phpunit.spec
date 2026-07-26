%global source0_hash 5dfc8298ffd68b212fe0fd1901d54bd4d835e12a2bd63e04faececf716267e54

# remirepo/fedora spec file for php-phpspec-prophecy-phpunit
#
# SPDX-FileCopyrightText:  Copyright 2020-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    89f91b01d0640b7820e427e02a007bc6489d8a26
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpspec
%global gh_project   prophecy-phpunit

Name:           php-%{gh_owner}-%{gh_project}
Version:        2.5.0
Release:        1%{?dist}
Summary:        Integrating the Prophecy mocking library in PHPUnit test cases

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
%if %{with tests}
BuildRequires: (php-composer(phpspec/prophecy) >= 1.18  with php-composer(phpspec/prophecy) < 2)
BuildRequires:  phpunit13 >= 13.0
BuildRequires:  phpunit12 >= 12.0
BuildRequires:  phpunit11 >= 11.0
BuildRequires:  phpunit10 >= 10.1
BuildRequires:  phpunit9 >= 9.1
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# from composer.json, "requires": {
#        "php": "^7.3 || ^8",
#        "phpspec/prophecy": "^1.18",
#        "phpunit/phpunit":"^9.1 || ^10.1 || ^11.0 || ^12.0 || ^13.0"
Requires:       php(language) >= 7.3
Requires:      (php-composer(phpspec/prophecy) >= 1.18  with php-composer(phpspec/prophecy) < 2)
Requires:      (phpunit9 >= 9.1 or phpunit10 >= 10.1 or phpunit11 >= 11.0 or phpunit12 >= 12.0 or phpunit13 >= 13.0)
# From phpcompatinfo report for version 2.0.1
#none
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}

%description
Prophecy PhpUnit integrates the Prophecy mocking library with PHPUnit
to provide an easier mocking in your testsuite.

Autoloader: %{_datadir}/php/Prophecy/PhpUnit/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Prophecy/autoload.php',
]);
EOF

%install
mkdir -p     %{buildroot}%{_datadir}/php/Prophecy/PhpUnit
cp -pr src/* %{buildroot}%{_datadir}/php/Prophecy/PhpUnit/

%check
%if %{with tests}
: Dev autoloader
mkdir vendor
phpab --output vendor/autoload.php.in fixtures tests

cat << 'EOF' | tee -a vendor/autoload.php.in
require_once '%{buildroot}%{_datadir}/php/Prophecy/PhpUnit/autoload.php';
require_once '%{_datadir}/php/@PHPUNIT@/autoload.php';
EOF

: check autoloader
php %{buildroot}%{_datadir}/php/Prophecy/PhpUnit/autoload.php

: Fix expecteed path
sed -e 's:src/::' -i tests/MockFailure.phpt

: upstream test suite
ret=0
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
	sed -e 's/@PHPUNIT@/PHPUnit9/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit9 --no-coverage|| ret=1

	sed -e 's/@PHPUNIT@/PHPUnit10/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit10 --no-coverage|| ret=1

	sed -e 's/@PHPUNIT@/PHPUnit11/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit11 --no-coverage|| ret=1
  fi
done
for cmd in php php83 php84 php85; do
  if which %{_bindir}/phpunit12 && which $cmd; then
	sed -e 's/@PHPUNIT@/PHPUnit12/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit12 --no-coverage|| ret=1
  fi
done
for cmd in php php84 php85; do
  if which %{_bindir}/phpunit13 && which $cmd; then
	sed -e 's/@PHPUNIT@/PHPUnit13/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit13 --no-coverage|| ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/Prophecy/PhpUnit

%changelog
%autochangelog
