%global source0_hash 7c5416cc3ab547e9055ca169af740b32f1878c802e1bd18806e3da39c75d81c2
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
Source0:        https://github.com/%{gh_owner}/%{gh_owner}/archive/%{gh_commit}/%{gh_owner}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with_tests}
%if 0%{?fedora} >= 43 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%endif
%endif
Requires:       php(language) >= 5.6
Requires:      (php-composer(phpunit/php-text-template) >= 1   with php-composer(phpunit/php-text-template) < 6)
Requires:       php-date
Requires:       php-reflection
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Suggests:       php-composer(php-mock/php-mock-phpunit)
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  phpunit10
BuildRequires:  phpunit13
BuildRequires:  phpunit8
BuildRequires:  phpunit9
# /oreon:deps
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

%install
mkdir -p         %{buildroot}%{_datadir}
cp -pr rpm/php   %{buildroot}%{_datadir}/php
cp -pr rpm/tests %{buildroot}%{_datadir}/tests
%oreon_autofiles main

%check

%if %{with_tests}
ret=0
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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
