%global source0_hash 30c7416b40db72407d88a13edcc51512f76ba1cd3c4dba6cbf827f3ce3d4d40c
%global gh_commit    8ceb860f343a143af604efeb66a7a124381cc52e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2025-03-09
%global gh_owner     php-mock
%global gh_project   php-mock-integration
%global with_tests   0%{!?_without_tests:1}
%global major        2
Name:           php-mock-integration%{major}
Version:        3.0.0
Release:        3%{?dist}
Summary:        Integration package for PHP-Mock
License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 5.6
Requires:      (php-composer(php-mock/php-mock)         >= 2.5 with php-composer(php-mock/php-mock)         < 3)
Requires:      (php-composer(phpunit/php-text-template) >= 1   with php-composer(phpunit/php-text-template) < 6)
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(php-mock/php-mock) >= 2.5 with php-composer(php-mock/php-mock) < 3)
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  phpunit10
BuildRequires:  phpunit8
BuildRequires:  phpunit9
# /oreon:deps
%description
This is a support package for PHP-Mock integration into other frameworks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

# Same namespace than php-mock, not specific autoloader needed

%build

%install
mkdir -p       %{buildroot}%{_datadir}/php/
mkdir -p       %{buildroot}%{_datadir}/php/phpmock%{major}
cp -pr classes %{buildroot}%{_datadir}/php/phpmock%{major}/integration
%oreon_autofiles main

%check

%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('phpmock\\', '%{buildroot}%{_datadir}/php/phpmock%{major}');
\Fedora\Autoloader\Autoload::addPsr4('phpmock\\integration\\', dirname(__DIR__) . '/tests');
require_once '%{_datadir}/php/phpmock%{major}/autoload.php';
require_once dirname(__DIR__) . '/tests/autoload.php';
EOF
ret=0
if [ -x %{_bindir}/phpunit8 ]; then
  for cmd in php php80 php81 php82 php83 php84;do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit9 ]; then
  for cmd in php php80 php81 php82 php83 php84;do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit10 ]; then
  for cmd in php php81 php82 php83 php84;do
    if which $cmd; then
      $cmd %{_bindir}/phpunit10 || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit11 ]; then
  for cmd in php php82 php83 php84;do
    if which $cmd; then
      $cmd %{_bindir}/phpunit10 || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit12 ]; then
  for cmd in php php83 php84;do
    if which $cmd; then
      $cmd %{_bindir}/phpunit10 || ret=1
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
