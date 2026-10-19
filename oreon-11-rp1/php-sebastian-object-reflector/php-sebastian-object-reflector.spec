%global source0_hash 177cfd92f427f1a165275cbeff642a2658ac954fd78f17e6f7755e3a24eddd40
%global bootstrap    0
%global gh_commit    1d439c229e61f244ff1f211e5c99737f90c67def
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   object-reflector
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        %nil
%global ns_vendor    SebastianBergmann
%global ns_project   ObjectReflector
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        6.1.0
Release:        1%{?dist}
Summary:        Allows reflection of object attributes, version 1
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 7.0
Requires:       php-reflection
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit8
# /oreon:deps
%description
Allows reflection of object attributes, including inherited
and non-public ones.

This package provides the version 1 of the library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab --template fedora --output src/autoload.php src
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with_tests}
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests/_fixture
cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF
: Fix for phpunit8
find tests/ -name \*php -exec sed -e 's/setUp()/setUp():void/'  -i {} \;
: Run upstream test suite
ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
    %{_bindir}/php -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
    %{_bindir}/phpunit8	  --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
