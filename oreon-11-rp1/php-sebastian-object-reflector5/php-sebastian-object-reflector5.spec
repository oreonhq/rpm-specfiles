%global source0_hash 1ec554fb341cb646c4572f81056d07fdd68cb5a7dd07db16c41447591986194f

# remirepo/fedora spec file for php-sebastian-object-reflector5
#
# SPDX-FileCopyrightText:  Copyright 2017-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    4bfa827c969c98be1e527abd576533293c634f6a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   object-reflector
%global gh_date      2025-02-07
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   ObjectReflector
%global major        5
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        5.0.0
Release:        4%{?dist}
Summary:        Allows reflection of object attributes, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^12.0"
BuildRequires:  phpunit12
%endif

# from composer.json
#        "php": ">=8.3"
Requires:       php(language) >= 8.3
# from phpcompatinfo report for version 2.0.0
#nothing
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Allows reflection of object attributes, including inherited
and non-public ones.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with tests}
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests/_fixture
cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF

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
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
