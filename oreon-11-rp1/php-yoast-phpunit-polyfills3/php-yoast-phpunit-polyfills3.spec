%global source0_hash 8eab0abba41c9e5012e3c7eb8f8f53f25d7472e0dabe174e5a14ceab007a470d
%global gh_commit    9cf2ccd990eadfc4a1e390592d4731e590b2c618
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Yoast
%global gh_project   PHPUnit-Polyfills
%global pk_vendor    yoast
%global pk_project   phpunit-polyfills
%global ns_vendor    Yoast
%global ns_project   PHPUnitPolyfills
%global major        3
%bcond_without       tests
%global php_home     %{_datadir}/php
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.1.2
Release:        1%{?dist}
Summary:        Set of polyfills for changed PHPUnit functionality, version 3
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%endif
%endif
Requires:       php(language) >= 7.0
Requires:       php-reflection
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-reflection
BuildRequires:  phpunit11
BuildRequires:  phpunit8
BuildRequires:  phpunit9
# /oreon:deps
%description
Set of polyfills for changed PHPUnit functionality to allow for creating
PHPUnit cross-version compatible tests.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

# Fix for RPM layout
sed -e 's:src/::' phpunitpolyfills-autoload.php > src/autoload.php

%build

%install
mkdir -p        %{buildroot}/%{php_home}/%{ns_vendor}
cp -pr src      %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Yoast\\PHPUnitPolyfills\\Tests\\', dirname(__DIR__) . '/tests');
require_once '%{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF
: Run upstream test suite
ret=0
if [ -x %{_bindir}/phpunit8 ]; then
  for cmd in php php81 php82 php83; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --no-coverage || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit9 ]; then
  for cmd in php php81 php82 php83 php84; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --no-coverage || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit11 ]; then
  for cmd in php  php82 php83 php84; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit11 --no-coverage || ret=1
    fi
  done
fi
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
