%global source0_hash 0b62ef8c1417e220c2dc9ac4dc543279f903a8ac0ab93d5c5823ab89d13bd82d

# remirepo/fedora spec file for php-khanamiryan-qrcode-detector-decoder
#
# Copyright (c) 2017-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_without       tests

%global gh_commit    04fdd58d86a387065f707dc6d3cc304c719910c1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     khanamiryan
%global gh_project   php-qrcode-detector-decoder

%global pk_vendor    %{gh_owner}
%global pk_project   qrcode-detector-decoder

%global ns_vendor    %nil
%global ns_project   Zxing
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.0.5.2
Release:        12%{?dist}
Summary:        QR code decoder / reader

Group:          Development/Libraries
# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-gd
BuildRequires:  php-iconv
BuildRequires:  php-mbstring
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.0"
%global phpunit %{_bindir}/phpunit9
%endif
# Required by autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.6"
Requires:       php(language) >= 5.6
# From phpcompatinfo report for version 1
Requires:       php-reflection
Requires:       php-date
Requires:       php-gd
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-spl
Suggests:       php-pecl(imagick)
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
This is a PHP library to detect and decode QR-codes.

This is first and only QR code reader that works without extensions.
Ported from ZXing library.

Autoloader: %{php_home}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
%{_bindir}/phpab \
  --output lib/autoload.php \
  --template fedora \
  lib

cat << 'EOF' | tee -a lib/autoload.php
\Fedora\Autoloader\Dependencies::required([
    __DIR__ . '/Common/customFunctions.php',
]);
EOF

%install
: Library
mkdir -p   %{buildroot}%{php_home}
cp -pr lib %{buildroot}%{php_home}/%{ns_project}

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_project}/autoload.php';
EOF

ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} $filter --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE*
%doc composer.json
%doc README.md
%{php_home}/%{ns_project}

%changelog
%autochangelog
