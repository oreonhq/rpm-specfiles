%global source0_hash f861f456ce0bc93a91e540f91ae79d3abf8280a318a75abe6396a8aa6a89f549
%bcond_without       tests
%global gh_commit    aa08b49eac291a49f50e9a094f23b267cc5a9bec
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      20150618
%global gh_owner     sanmai
%global gh_project   phpunit-legacy-adapter
%global ns_project   LegacyPHPUnit
Name:           php-%{gh_owner}-%{gh_project}
Version:        8.2.3
Release:        1%{?dist}
Summary:        PHPUnit Legacy Versions Adapter
License:        Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 7.1
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit10
BuildRequires:  phpunit11
BuildRequires:  phpunit12
BuildRequires:  phpunit8
BuildRequires:  phpunit9
# /oreon:deps
%description
PHPUnit Legacy Versions Adapter.

This version is compatible with phpunit version 7, 8, 9 and 10.

Autoloader: %{_datadir}/php/%{ns_project}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab \
   --template fedora \
   --output src/autoload.php \
   src
%install
mkdir -p   %{buildroot}%{_datadir}/php/
cp -pr src %{buildroot}%{_datadir}/php/%{ns_project}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Tests\\%{ns_project}\\', dirname(__DIR__)  .'/tests');
EOF
: run upstream test suite with all php and phpunit versions
ret=0
for cmd in php80 php81 php82 php83 php84
do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
for cmd in php80 php81 php82 php83 php84
do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
if [ -x %{_bindir}/phpunit10 ]; then
  for cmd in php81 php82 php83 php84
  do
    if which $cmd; then
      $cmd %{_bindir}/phpunit10 || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit11 ]; then
  for cmd in php82 php83 php84
  do
    if which $cmd; then
      $cmd %{_bindir}/phpunit11 || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit12 ]; then
  for cmd in php83 php84
  do
    if which $cmd; then
      $cmd %{_bindir}/phpunit12 || ret=1
    fi
  done
fi
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
