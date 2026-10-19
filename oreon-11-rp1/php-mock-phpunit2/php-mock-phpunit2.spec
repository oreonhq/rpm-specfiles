%global source0_hash 51a521de9dfc3da83a26f1d818a1a2fca1721509815bc1643f52c2e07ad619f6
%global gh_commit    701df15b183f25af663af134eb71353cd838b955
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2026-02-06
%global gh_owner     php-mock
%global gh_project   php-mock-phpunit
%global with_tests   0%{!?_without_tests:1}
%global major        2
Name:           php-mock-phpunit%{major}
Version:        2.15.0
Release:        1%{?dist}
Summary:        Mock built-in PHP functions with PHPUnit.
License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with_tests}
%if 0%{?fedora} >= 43 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%endif
%endif
Requires:       php(language) >= 7
Recommends:    (phpunit10 or phpunit11 or phpunit12)
Requires:      (php-composer(php-mock/php-mock-integration) >= 3.0   with php-composer(php-mock/php-mock-integration) < 4)
Requires:      (php-composer(php-mock/php-mock)             >= 2.2   with php-composer(php-mock/php-mock)             < 3)
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(mockery/mockery) >= 1.3.6 with php-composer(mockery/mockery) < 2)
BuildRequires:  (php-composer(php-mock/php-mock) >= 2.2 with php-composer(php-mock/php-mock) < 3)
BuildRequires:  (php-composer(php-mock/php-mock-integration) >= 3.0 with php-composer(php-mock/php-mock-integration) < 4)
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  phpunit10
BuildRequires:  phpunit13
BuildRequires:  phpunit8
BuildRequires:  phpunit9
# /oreon:deps
%description
Mock built-in PHP functions (e.g. time()) with PHPUnit.
This package relies on PHP's namespace fallback policy.
No further extension is needed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

: Create autoloader
cat << 'AUTOLOAD' | tee rpm.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpmock\\phpunit\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    __DIR__ . '/compatibility.php',
    '%{_datadir}/php/phpmock2/autoload.php',
));
AUTOLOAD

%build

%install
mkdir -p             %{buildroot}%{_datadir}/php/
mkdir -p             %{buildroot}%{_datadir}/php/phpmock%{major}
cp -pr classes       %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit
cp -pr compatibility %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/compatibility
cp -p  autoload.php  %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/compatibility.php
cp -p  rpm.php       %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/autoload.php
%oreon_autofiles main

%check

%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/autoload.php';
require_once '%{_datadir}/php/phpmock%{major}/autoload.php';
require_once '%{_datadir}/php/Mockery1/autoload.php';
EOF
ret=0
if [ -x %{_bindir}/phpunit8 ]; then
: Run upstream test suite with phpunit8
for cmd in php php82 php82 php84 php85; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
fi
if [ -x %{_bindir}/phpunit9 ]; then
: Run upstream test suite with phpunit9
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
fi
if [ -x %{_bindir}/phpunit10 ]; then
: Run upstream test suite with phpunit10
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit10 \
       --filter '^((?!(testPreserveArgumentDefaultValue)).)*$' \
       || ret=1
  fi
done
fi
if [ -x %{_bindir}/phpunit11 ]; then
: Run upstream test suite with phpunit11
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit11 \
       --filter '^((?!(testPreserveArgumentDefaultValue)).)*$' \
       || ret=1
  fi
done
fi
if [ -x %{_bindir}/phpunit12 ]; then
: Run upstream test suite with phpunit12
for cmd in php php83 php84 php85; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit12 \
       --filter '^((?!(testPreserveArgumentDefaultValue)).)*$' \
       || ret=1
  fi
done
fi
if [ -x %{_bindir}/phpunit13 ]; then
: Run upstream test suite with phpunit13
for cmd in php php84 php85; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit13 \
       --filter '^((?!(testPreserveArgumentDefaultValue|testExpects)).)*$' \
       || ret=1
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
