%global source0_hash 66e241bfeb652fb8dd1abf7065088dc4399230a55c4d236d3b5a12bc55149aa6

# remirepo/fedora spec file for php-dasprid-enum
#
# SPDX-FileCopyrightText:  Copyright 2019-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%bcond_without       tests

%global gh_commit    b5874fa9ed0043116c72162ec7f4fb50e02e7cce
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     DASPRiD
%global gh_project   Enum

%global pk_vendor    dasprid
%global pk_project   enum

%global ns_vendor    %{gh_owner}
%global ns_project   %{gh_project}
%global php_home     %{_datadir}/php
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.7
Release:        2%{?dist}
Summary:        PHP enum implementation

License:        BSD-2-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to retrieve test suite removed by .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language)
BuildRequires:  php-reflection
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^7 || ^8 || ^9 || ^10 || ^11",
#        "squizlabs/php_codesniffer": "^3.4"
%global phpunit %{_bindir}/phpunit10
BuildRequires:  %{phpunit}
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
# nothing
Requires:       php(language)
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-spl
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
It is a well known fact that PHP is missing a basic enum type, ignoring the
rather incomplete SplEnum implementation which is only available as a PECL
extension. There are also quite a few other userland enum implementations
around, but all of them have one or another compromise. This library tries to
close that gap as far as PHP allows it to.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
EOF

%build
# Empty build section, most likely nothing required.

%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\EnumTest\\', dirname( __DIR__).'/test');
EOF

ret=0
for cmd in "php %{phpunit}" php81 php82 php83 "php84 %{_bindir}/phpunit11" "php85 %{_bindir}/phpunit11"; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit10} || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc README.md
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}

%changelog
%autochangelog
