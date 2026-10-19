%global source0_hash 5959004f69f36edcf0b40bca4af5fbd955cfa07de1a567e5d6ed74b4cd308fff
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
Version:        3.1.1
Release:        1%{?dist}
Summary:        QR code generator for PHP
Group:          Development/Libraries
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 7.1
Requires:       php-iconv
Requires:      (php-composer(dasprid/enum) >= 1.0    with php-composer(dasprid/enum) < 2)
Recommends:     php-imagick
Requires:       php-ctype
Requires:       php-spl
Requires:       php-xmlwriter
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(dasprid/enum) >= 1.0 with php-composer(dasprid/enum) < 2)
BuildRequires:  /usr/bin/phpunit9
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-ctype
BuildRequires:  php-iconv
BuildRequires:  php-imagick
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  php-xmlwriter
# /oreon:deps
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

%install
: Library
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{ns_project}%{major}
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
