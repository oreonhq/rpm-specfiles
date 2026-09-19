%global source0_hash bb4bcb08c920d99e23cc0c1c1c7792c0acfa9d928a5ac07109de2bb908d70dac

# spec file for php-sebastian-global-state6
#
# Copyright (c) 2014-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    987bafff24ecc4c9ac418cab1145b96dd6e9cbd9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   global-state
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   GlobalState
%global major        6
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        6.0.2
Release:        5%{?dist}
Summary:        Snapshotting of global state, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-reflection
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
BuildRequires:  (php-composer(sebastian/object-reflector)  >= 3.0     with php-composer(sebastian/object-reflector)  < 4)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 5.0     with php-composer(sebastian/recursion-context) < 6)
# from composer.json, "require-dev": {
#        "ext-dom": "*",
#        "phpunit/phpunit": "^10.0"
BuildRequires:  php-dom
BuildRequires:  phpunit10
%endif

# from composer.json, "require": {
#        "php": ">=8.1",
#        "sebastian/object-reflector": "^3.0",
#        "sebastian/recursion-context": "^5.0"
Requires:       php(language) >= 7.3
Requires:       (php-composer(sebastian/object-reflector)  >= 3.0     with php-composer(sebastian/object-reflector)  < 4)
Requires:       (php-composer(sebastian/recursion-context) >= 5.0     with php-composer(sebastian/recursion-context) < 6)
# from phpcompatinfo report for version 6.0.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Snapshotting of global state,
factored out of PHPUnit into a stand-alone component.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/ObjectReflector3/autoload.php',
    '%{php_home}/%{ns_vendor}/RecursionContext5/autoload.php',
]);
EOF

# For the test suite
phpab --template fedora --output tests/autoload.php tests/_fixture/

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

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
for cmd in php php81 php82 php83; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit10 \
       || ret=1
  fi
done
exit $ret

%else
: bootstrap build with test suite disabled
%endif

%files
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
