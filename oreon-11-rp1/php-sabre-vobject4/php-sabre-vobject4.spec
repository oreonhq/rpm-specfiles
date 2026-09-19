%global source0_hash 830686238d7b9dba3b673b4d6fc571e96ed106a8382e09bd5ff68cdc29c09b66

# remirepo/fedora spec file for php-sabre-vobject4
#
# SPDX-FileCopyrightText:  Copyright 2013-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    d554eb24d64232922e1eab5896cc2f84b3b9ffb1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   vobject
%global with_cmd     1

Name:           php-sabre-vobject4
Summary:        Library to parse and manipulate iCalendar and vCard objects
Version:        4.5.8
Release:        2%{?dist}

URL:            http://sabre.io/vobject/
License:        BSD-3-Clause
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh

# replace composer autloader
Patch0:         %{name}-bin.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-mbstring
BuildRequires:  (php-composer(sabre/xml)    >= 2.1  with php-composer(sabre/xml)     < 5)
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xml
# From composer.json, "require-dev"
#        "friendsofphp/php-cs-fixer": "^2.17.1",
#        "phpunit/phpunit" : "^7.5 || ^8.5 || ^9.6",
#        "phpunit/php-invoker" : "^2.0 || ^3.1",
#        "phpstan/phpstan": "^0.12 || ^1.12 || ^2.0"
BuildRequires:  phpunit9 >= 9.6
%global phpunit %{_bindir}/phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require"
#        "php"          : "^7.1 || ^8.0",
#        "ext-mbstring" : "*",
#        "sabre/xml"    : "^2.1 || ^3.0 || ^4.0"
Requires:       php(language) >= 7.1
Requires:       php-mbstring
#
Requires:       (php-composer(sabre/xml)    >= 2.1  with php-composer(sabre/xml)     < 5)
# From phpcompatinfo report for version 4.1.2
%if %{with_cmd}
Requires:       php-cli
%endif
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xml
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sabre/vobject) = %{version}

%description
The VObject library allows you to easily parse and manipulate iCalendar
and vCard objects using PHP. The goal of the VObject library is to create
a very complete library, with an easy to use API.

This project is a spin-off from SabreDAV, where it has been used for several
years. The VObject library has 100% unittest coverage.

Autoloader: %{_datadir}/php/Sabre/VObject4/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm

phpab -t fedora -o lib/autoload.php lib

cat << 'EOF' | tee -a lib/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Sabre/Xml4/autoload.php',
        '%{_datadir}/php/Sabre/Xml3/autoload.php',
        '%{_datadir}/php/Sabre/Xml2/autoload.php',
    ],
]);
EOF

%build
# nothing to build

%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Sabre
cp -pr lib %{buildroot}%{_datadir}/php/Sabre/VObject4

%if %{with_cmd}
# Install the commands
install -Dpm 0755 bin/vobject \
         %{buildroot}/%{_bindir}/vobject
install -Dpm 0755 bin/generate_vcards \
         %{buildroot}/%{_bindir}/generate_vcards
%endif

%check
: Fix bootstrap
cd tests
sed -e 's:@BUILDROOT@:%{buildroot}:' -i bootstrap.php

: Check version
php -r '
require "%{_datadir}/php/Fedora/Autoloader/autoload.php";
require "bootstrap.php";
echo  Sabre\VObject\Version::VERSION . "\n";
exit (Sabre\VObject\Version::VERSION === "%{version}" ? 0 : 1);
'

%if %{with tests}
opt="--verbose"
if [ $(php -r 'echo PHP_INT_SIZE;') -lt 8 ]; then
  opt="--filter '^((?!(testNeverEnding|testGeneratorBaseObject|testDailyBySetPosLoop|testYearlyBySetPosLoop)).)*$' $opt"
fi

: Run upstream test suite against installed library
ret=0
for cmdarg in "php %{phpunit}" php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} $opt || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif

%files
%license LICENSE
%doc *md
%doc composer.json
%{_datadir}/php/Sabre/VObject4
%if %{with_cmd}
%{_bindir}/vobject
%{_bindir}/generate_vcards
%endif

%changelog
%autochangelog
