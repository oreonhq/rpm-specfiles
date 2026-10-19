%global source0_hash d1302a49a1d04576939814aad6820afa6155f53cd8bc98740f39d44a56543892
%bcond_without       tests
%global gh_commit    b6781316bdcd28260904e7cc18ec983d0d2ef4f6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   global-state
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   GlobalState
%global major        5
%global php_home     %{_datadir}/php
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        7.0.1
Release:        1%{?dist}
Summary:        Snapshotting of global state, version 5
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 7.3
Requires:       (php-composer(sebastian/object-reflector)  >= 2.0     with php-composer(sebastian/object-reflector)  < 3)
Requires:       (php-composer(sebastian/recursion-context) >= 4.0     with php-composer(sebastian/recursion-context) < 5)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sebastian/object-reflector) >= 2.0 with php-composer(sebastian/object-reflector) < 3)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 4.0 with php-composer(sebastian/recursion-context) < 5)
BuildRequires:  php(language)
BuildRequires:  php-dom
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit9
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
    '%{php_home}/%{ns_vendor}/ObjectReflector2/autoload.php',
    '%{php_home}/%{ns_vendor}/RecursionContext4/autoload.php',
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
: Run upstream test suite
ret=0
for cmd in php php81 php82 php83 php84 php85; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit9 \
       --filter '^((?!(testConstructorExcludesAspectsWhenTheyShouldNotBeIncluded|testCanExportGlobalVariablesToCode|testStaticNotInitialisedAttributes)).)*$' \
       --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
