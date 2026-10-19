%global source0_hash 898b64fb5549660e11b6cf1cf55cacd71fa12c6fa83c71ae3b12bdde37fcb74a
%bcond_without       tests
%global gh_commit    ef1377171613d09edd25b7816f05be8313f9115d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   global-state
%global gh_date      2025-08-29
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   GlobalState
%global major        8
%global php_home     %{_datadir}/php
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        8.0.2
Release:        1%{?dist}
Summary:        Snapshotting of global state, version 8
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.3
Requires:       (php-composer(sebastian/object-reflector)  >= 5.0     with php-composer(sebastian/object-reflector)  < 6)
Requires:       (php-composer(sebastian/recursion-context) >= 7.0     with php-composer(sebastian/recursion-context) < 8)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sebastian/object-reflector) >= 5.0 with php-composer(sebastian/object-reflector) < 6)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 7.0 with php-composer(sebastian/recursion-context) < 8)
BuildRequires:  php(language)
BuildRequires:  php-dom
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit12
# /oreon:deps
%description
Snapshotting of global state,
factored out of PHPUnit into a stand-alone component.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/ObjectReflector5/autoload.php',
    '%{php_home}/%{ns_vendor}/RecursionContext7/autoload.php',
]);
EOF
phpab --template fedora --output tests/autoload.php tests/_fixture/
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require_once 'tests/autoload.php';
require_once 'tests/_fixture/SnapshotFunctions.php';
EOF
sed -e '/processIsolation/d' -i phpunit.xml
: Run upstream test suite
ret=0
for cmd in php php83 php84 php85; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit12 --bootstrap vendor/autoload.php \
       || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
