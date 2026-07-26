%global source0_hash 5959004f69f36edcf0b40bca4af5fbd955cfa07de1a567e5d6ed74b4cd308fff

# remirepo/fedora spec file for php-bacon-qr-code2
#
# Copyright (c) 2017-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_without       tests

%global gh_commit    8674e51bb65af933a5ffaf1c308a660387c35c22
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Bacon
%global gh_project   BaconQrCode

%global pk_vendor    bacon
%global pk_project   bacon-qr-code

%global ns_vendor    %nil
%global ns_project   %{gh_project}
%global php_home     %{_datadir}/php
%global major        2

Name:           php-%{pk_project}%{major}
Version:        2.0.8
Release:        10%{?dist}
Summary:        QR code generator for PHP

Group:          Development/Libraries
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-iconv
BuildRequires:  php-imagick
BuildRequires:  php-ctype
BuildRequires:  php-spl
BuildRequires:  php-xmlwriter
BuildRequires:  php-reflection
BuildRequires: (php-composer(dasprid/enum) >= 1.0    with php-composer(dasprid/enum) < 2)
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^7 | ^8 | ^9",
#        "spatie/phpunit-snapshot-assertions": "^4.2.9",
#        "squizlabs/php_codesniffer": "^3.1",
#        "phly/keep-a-changelog": "^1.4"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.1 || ^8.0",
#        "ext-iconv": "*",
#        "dasprid/enum": "^1.0.3"
Requires:       php(language) >= 7.1
Requires:       php-iconv
# From composer.json, "suggest": {
#        "ext-imagick": "to generate QR code images"
Requires:      (php-composer(dasprid/enum) >= 1.0    with php-composer(dasprid/enum) < 2)
Recommends:     php-imagick
# From phpcompatinfo report for version 2.0.0
Requires:       php-ctype
Requires:       php-spl
Requires:       php-xmlwriter
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
BaconQrCode is a port of QR code portion of the ZXing library.
It currently only features the encoder part, but could later
receive the decoder part as well.

As the Reed Solomon codec implementation of the ZXing library
performs quite slow in PHP, it was exchanged with the implementation
by Phil Karn.

Autoloader: %{php_home}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/DASPRiD/Enum/autoload.php',
]);

EOF

%build
# Empty build section, most likely nothing required.

%install
: Library
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{ns_project}%{major}

%check
%if %{with tests}
if php -r 'exit(PHP_INT_SIZE<8 ? 0 : 1);'
then
  : ignore test suite because of https://github.com/Bacon/BaconQrCode/issues/31
  exit 0
fi

: ignore test using spatie/phpunit-snapshot-assertions
rm test/Integration/ImagickRenderingTest.php

mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_project}%{major}/autoload.php';
EOF

ret=0
for cmd in "php %{phpunit}" php80 php81 php82; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
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
%{php_home}/%{ns_project}%{major}

%changelog
%autochangelog
