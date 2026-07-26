%global source0_hash 4c49cf6e38c199461755539194b9a407c82b7095cc2e304a575adb07a06820b3

# remirepo/fedora spec file for php-tecnickcom-tc-lib-barcode
#
# SPDX-FileCopyrightText:  Copyright 2015-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    605b92bfaf8ed2cba18a1c6603d90bc828aa3d5b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global c_vendor     tecnickcom
%global gh_owner     tecnickcom
%global gh_project   tc-lib-barcode
%global php_project  %{_datadir}/php/Com/Tecnick/Barcode
%bcond_without       tests

Name:           php-%{gh_owner}-%{gh_project}
Version:        2.4.24
Release:        1%{?dist}
Summary:        PHP library to generate linear and bidimensional barcodes

License:        LGPL-3.0-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with tests}
# For tests
%global phpunit %{_bindir}/phpunit10
BuildRequires:  phpunit10 >= 10.5.63
BuildRequires:  php(language) >= 8.1
BuildRequires: (php-composer(%{c_vendor}/tc-lib-color) >= 2.3    with php-composer(%{c_vendor}/tc-lib-color) < 3)
BuildRequires:  php-bcmath
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-gd
BuildRequires:  php-pcre
# Optional but required for test
BuildRequires:  php-pecl-imagick
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=8.1"
#        "ext-bcmath": "*",
#        "ext-date": "*",
#        "ext-gd": "*",
#        "ext-pcre": "*",
#        "tecnickcom/tc-lib-color": "^2.3"
Requires:       php(language) >= 8.1
Requires:       php-bcmath
Requires:       php-ctype
Requires:       php-date
Requires:       php-gd
Requires:       php-pcre
Requires:      (php-composer(%{c_vendor}/tc-lib-color) >= 2.3    with php-composer(%{c_vendor}/tc-lib-color) < 3)
# From phpcompatinfo report for version 1.15.5
# none
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{c_vendor}/%{gh_project}) = %{version}
# Upstream package name
Provides:       php-%{gh_project} = %{version}

%description
Provides tc-lib-barcode: PHP classes to generate linear and bidimensional
barcodes: CODE 39, ANSI MH10.8M-1983, USD-3, 3 of 9, CODE 93, USS-93,
Standard 2 of 5, Interleaved 2 of 5, CODE 128 A/B/C, 2 and 5 Digits
UPC-Based Extension, EAN 8, EAN 13, UPC-A, UPC-E, MSI, POSTNET, PLANET,
RMS4CC (Royal Mail 4-state Customer Code), CBC (Customer Bar Code),
KIX (Klant index - Customer index), Intelligent Mail Barcode, Onecode,
USPS-B-3200, CODABAR, CODE 11, PHARMACODE, PHARMACODE TWO-TRACKS, Datamatrix
ECC200, QR-Code, PDF417.

Optional dependency: php-pecl-imagick

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

: Sanity check
grep -q '^%{version}$' VERSION

: Fix the examples
sed -e 's:^require:////require:' \
    -e 's:^//require:require:'   \
    -i example/*php

%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Com/Tecnick/Color/autoload.php',
]);
EOF

%install
mkdir -p   $(dirname %{buildroot}%{php_project})
cp -pr src %{buildroot}%{php_project}

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Test\\', dirname(__DIR__) . '/test');
EOF

ret=0
for cmdarg in "php %{phpunit}" php82 php83 php84 php85; do
   if which $cmdarg; then
      set $cmdarg
      cp phpunit.xml.dist phpunit.xml
      $1 ${2:-%{_bindir}/phpunit10} --migrate-configuration || :
      $1 ${2:-%{_bindir}/phpunit10} \
        --filter '^((?!(testGetSvg|testGetPng)).)*$' \
        --no-coverage --stderr || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc *.md example
%{php_project}

%changelog
%autochangelog
