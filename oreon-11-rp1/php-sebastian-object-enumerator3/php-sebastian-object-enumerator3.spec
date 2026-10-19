%global source0_hash b37740ea37769dc7247aa217bcc4f22a0835a776abf8442e6d98326c913214be
%global bootstrap    0
%global gh_commit    ac5b293dba925751b808e02923399fb44ff0d541
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   object-enumerator
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        3
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   ObjectEnumerator
%global with_tests   0%{!?_without_tests:1}
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        8.1.0
Release:        1%{?dist}
Summary:        Traverses array and object to enumerate all referenced objects, version 3
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 7.0
Requires:       (php-composer(%{pk_vendor}/object-reflector) >= 1.1.1 with php-composer(%{pk_vendor}/object-reflector) < 2)
Requires:       (php-composer(sebastian/recursion-context)   >= 3.0   with php-composer(sebastian/recursion-context)   < 4)
Requires:       php-reflection
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sebastian/object-reflector) >= 1.1.1 with php-composer(sebastian/object-reflector) < 2)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 3.0 with php-composer(sebastian/recursion-context) < 4)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit8
# /oreon:deps
%description
Traverses array structures and object graphs to enumerate all
referenced objects.

This package provides the version %{major} of the library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
// Dependencies
require_once '%{php_home}/%{ns_vendor}/ObjectReflector/autoload.php';
require_once '%{php_home}/%{ns_vendor}/RecursionContext3/autoload.php';
EOF
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with_tests}
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests/_fixture
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
