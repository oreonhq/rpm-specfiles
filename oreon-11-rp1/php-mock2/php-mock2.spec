%global source0_hash 7c5416cc3ab547e9055ca169af740b32f1878c802e1bd18806e3da39c75d81c2

# remirepo/fedora spec file for php-mock2
#
# SPDX-FileCopyrightText:  Copyright 2016-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    b59734f19765296bb0311942850d02288a224890
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2026-02-06
%global gh_owner     php-mock
%global gh_project   php-mock
%global with_tests   0%{!?_without_tests:1}
%global major        2

Name:           php-mock%{major}
Version:        2.7.0
Release:        1%{?dist}
Summary:        PHP-Mock can mock built-in PHP functions

License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# 7.4 because of phpunit9
BuildRequires:  php(language) >= 7.4
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^5.7 || ^6.5 || ^7.5 || ^8.0 || ^9.0 || ^10.0|| ^11.0 || ^12.0 || ^13.0",
#        "squizlabs/php_codesniffer": "^3.5"
BuildRequires: phpunit8
BuildRequires: phpunit9
BuildRequires: phpunit10
%if 0%{?fedora} || 0%{?rhel} >= 10
BuildRequires: phpunit11
BuildRequires: phpunit12
%endif
%if 0%{?fedora} >= 43 || 0%{?rhel} >= 11
BuildRequires: phpunit13
%endif
%endif
# For autoloader
BuildRequires: php-composer(fedora/autoloader)

# from composer.json, "require": {
#        "php": "^5.6 || ^7.0 || ^8.0",
#        "phpunit/php-text-template": "^1 || ^2 || ^3 || ^4 || ^5 || ^6")
Requires:       php(language) >= 5.6
Requires:      (php-composer(phpunit/php-text-template) >= 1   with php-composer(phpunit/php-text-template) < 6)
# From phpcompatinfo report from version 2.0.0
Requires:       php-date
Requires:       php-reflection
Requires:       php-spl
# For autoloader
Requires:       php-composer(fedora/autoloader)
# from composer.json, "suggest": {
#       "php-mock/php-mock-phpunit": "Allows integration into PHPUnit testcase with the trait PHPMock."
Suggests:       php-composer(php-mock/php-mock-phpunit)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}

%description
PHP-Mock can mock built-in PHP functions (e.g. time()).
PHP-Mock relies on PHP's namespace fallback policy.
No further extension is needed.

Autoloader: %{_datadir}/php/phpmock%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

: Prepare the layout
mv tests/autoload.php testload.php
mkdir -p rpm/tests rpm/php
mv classes rpm/php/phpmock%{major}
mv tests   rpm/tests/phpmock%{major}

: Create autoloader
cat << 'AUTOLOAD' | tee rpm/php/phpmock%{major}/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpmock\\', __DIR__);
\Fedora\Autoloader\Autoload::addPsr4('phpmock\\', dirname(dirname(__DIR__)) . '/tests/phpmock%{major}');
if (PHP_VERSION_ID >= 80400) {
	$deps = [
        '%{_datadir}/php/SebastianBergmann/Template6/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template5/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template4/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template3/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template2/autoload.php',
        '%{_datadir}/php/Text/Template/Autoload.php',
    ];
} else if (PHP_VERSION_ID >= 80300) {
	$deps = [
        '%{_datadir}/php/SebastianBergmann/Template5/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template4/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template3/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template2/autoload.php',
        '%{_datadir}/php/Text/Template/Autoload.php',
    ];
} else if (PHP_VERSION_ID >= 80200) {
	$deps = [
        '%{_datadir}/php/SebastianBergmann/Template4/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template3/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template2/autoload.php',
        '%{_datadir}/php/Text/Template/Autoload.php',
    ];
} else {
	$deps = [
        '%{_datadir}/php/SebastianBergmann/Template3/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template2/autoload.php',
        '%{_datadir}/php/Text/Template/Autoload.php',
    ];
}
\Fedora\Autoloader\Dependencies::required([
	$deps,
]);
AUTOLOAD
grep -v '<?php' autoload.php >>rpm/php/phpmock%{major}/autoload.php
grep -v '<?php' testload.php >>rpm/php/phpmock%{major}/autoload.php

ln -s ../../php/phpmock%{major}/autoload.php rpm/tests/phpmock%{major}/autoload.php

: Fix autoloader path
sed -e 's:../autoload.php:autoload.php:' \
    -i rpm/tests/phpmock2/AbstractMockTest.php&

%build
# Nothing

%install
# Library
mkdir -p         %{buildroot}%{_datadir}
cp -pr rpm/php   %{buildroot}%{_datadir}/php
cp -pr rpm/tests %{buildroot}%{_datadir}/tests

%check
%if %{with_tests}
ret=0
# testDefiningAfterCallingUnqualified and testEnable may fail locally (ok in mock)

if [ -x %{_bindir}/phpunit8 ]; then
	for cmd in php php80 php81 php82 php83 php84 php85;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit8 \
		  --do-not-cache-result \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php --verbose rpm/tests || ret=1
	  fi
	done
fi

if [ -x %{_bindir}/phpunit9 ]; then
	for cmd in php php80 php81 php82 php83 php84 php85;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit9 \
		  --do-not-cache-result \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php --verbose rpm/tests || ret=1
	  fi
	done
fi

if [ -x %{_bindir}/phpunit10 ]; then
	for cmd in php php81 php82 php83 php84 php85;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit10 \
		  --do-not-cache-result \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php rpm/tests || ret=1
	  fi
	done
fi

if [ -x %{_bindir}/phpunit11 ]; then
	for cmd in php  php82 php83 php84 php85;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit11 \
		  --do-not-cache-result \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php rpm/tests || ret=1
	  fi
	done
fi

if [ -x %{_bindir}/phpunit12 ]; then
	for cmd in php php83 php84 php85;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit12 \
		  --do-not-cache-result \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php rpm/tests || ret=1
	  fi
	done
fi

if [ -x %{_bindir}/phpunit13 ]; then
	for cmd in php php84 php85;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit13 \
          --do-not-cache-result \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php rpm/tests || ret=1
	  fi
	done
fi
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/phpmock%{major}
%{_datadir}/tests/phpmock%{major}

%changelog
%autochangelog
