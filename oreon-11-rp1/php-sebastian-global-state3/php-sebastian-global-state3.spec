%global source0_hash 779727207369d0451138e4ea923835d770c2bceac11d1ae7f5447d1fa87a6b63

# spec file for php-sebastian-global-state3
#
# SPDX-FileCopyrightText:  Copyright 2014-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    800689427e3e8cf57a8fe38fcd1d4344c9b2f046
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   global-state
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        3
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   GlobalState
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.6
Release:        2%{?dist}
Summary:        Snapshotting of global state, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

Patch0:         %{name}-tests.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with_tests}
BuildRequires:  (php-composer(sebastian/object-reflector)  >= 1.1.1   with php-composer(sebastian/object-reflector)  < 2)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 3.0     with php-composer(sebastian/recursion-context) < 4)
# from composer.json, "require-dev": {
#        "ext-dom": "*",
#        "phpunit/phpunit": "^8.0"
BuildRequires:  phpunit8
BuildRequires:  php-dom
%endif

# from composer.json, "require": {
#        "php": ">=7.2",
#        "sebastian/object-reflector": "^1.1.1",
#        "sebastian/recursion-context": "^3.0"
Requires:       php(language) >= 7.2
Requires:       (php-composer(sebastian/object-reflector)  >= 1.1.1   with php-composer(sebastian/object-reflector)  < 2)
Requires:       (php-composer(sebastian/recursion-context) >= 3.0     with php-composer(sebastian/recursion-context) < 4)
# from phpcompatinfo report for version 2.0.0
# from composer.json, "suggest": {
#        "ext-uopz": "*"
%if 0%{?fedora} > 21 || 0%{?rhel} >= 8
Suggests:       php-uopz
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Snapshotting of global state,
factored out of PHPUnit into a stand-alone component.

This package provides the version %{major} of the library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1

%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/ObjectReflector/autoload.php',
    '%{php_home}/%{ns_vendor}/RecursionContext3/autoload.php',
]);
EOF

# For the test suite
phpab --template fedora --output tests/autoload.php tests/_fixture/

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with_tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require_once '%{ns_vendor}/%{ns_project}%{major}/autoload.php';
require_once 'tests/autoload.php';
require_once 'tests/_fixture/SnapshotFunctions.php';
EOF

: Run upstream test suite
ret=0
# testCanExportGlobalVariablesToCode reports our autoloader
for cmd in php php81 php82 php83 php84 php85; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit8 \
       --filter "^((?!(testCanExportGlobalVariablesToCode)).)*$" \
       --verbose || ret=1
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
