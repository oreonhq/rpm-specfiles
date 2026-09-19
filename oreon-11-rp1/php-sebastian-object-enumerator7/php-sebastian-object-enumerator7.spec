%global source0_hash 71a3bf069092f711e7a69d4874bc549c35f3c32913114f958bd42fd92118cb0a

# remirepo/fedora spec file for php-sebastian-object-enumerator7
#
# SPDX-FileCopyrightText:  Copyright 2015-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    1effe8e9b8e068e9ae228e542d5d11b5d16db894
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   object-enumerator
%global gh_date      2025-02-07
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   ObjectEnumerator
%global major        7
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        7.0.0
Release:        4%{?dist}
Summary:        Traverses array and object to enumerate all referenced objects, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
BuildRequires:  (php-composer(%{pk_vendor}/object-reflector) >= 5.0   with php-composer(%{pk_vendor}/object-reflector) < 6)
BuildRequires:  (php-composer(sebastian/recursion-context)   >= 7.0   with php-composer(sebastian/recursion-context)   < 8)
# From composer.json"require-dev": {
#        "phpunit/phpunit": "^12.0"
BuildRequires:  phpunit12
%endif

# from composer.json
#        "php": ">=8.3",
#        "sebastian/object-reflector": "^5.0",
#        "sebastian/recursion-context": "^7.0"
Requires:       php(language) >= 8.3
Requires:       (php-composer(%{pk_vendor}/object-reflector) >= 5.0   with php-composer(%{pk_vendor}/object-reflector) < 6)
Requires:       (php-composer(sebastian/recursion-context)   >= 7.0   with php-composer(sebastian/recursion-context)   < 8)
# from phpcompatinfo report for version 5.0.0:
#nothing
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Traverses array structures and object graphs to enumerate all
referenced objects.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader, from composer.json "autoload": {
#        "classmap": [
#            "src/"
%{_bindir}/phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/ObjectReflector5/autoload.php',
    '%{php_home}/%{ns_vendor}/RecursionContext7/autoload.php',
]);
EOF

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with tests}
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests/_fixture

: Run upstream test suite
ret=0
for cmd in php php83 php84; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit12 --bootstrap vendor/autoload.php || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%license LICENSE
%doc README.md composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
