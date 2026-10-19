%global source0_hash 1d17d6518eb5b25f1fe569a21846ce822e917f04e750239ebdb558f79c8e353d
%global gh_commit    41aaac462fbd80feb8dd129e489f4bbc53fe26b0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Yoast
%global gh_project   PHPUnit-Polyfills
%global pk_vendor    yoast
%global pk_project   phpunit-polyfills
%global ns_vendor    Yoast
%global ns_project   PHPUnitPolyfills
%global major        %nil
%bcond_without       tests
%global php_home     %{_datadir}/php
Name:           php-%{pk_vendor}-%{pk_project}1
Version:        1.1.5
Release:        1%{?dist}
Summary:        Set of polyfills for changed PHPUnit functionality, version 1
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 5.4
Requires:       php-reflection
Conflicts:      php-%{pk_vendor}-%{pk_project} < 2
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-reflection
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
  for cmd in php php81 php82 php83 php84 php85; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --no-coverage || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit9 ]; then
  for cmd in php php81 php82 php83 php84 php85; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --no-coverage || ret=1
    fi
  done
fi
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
