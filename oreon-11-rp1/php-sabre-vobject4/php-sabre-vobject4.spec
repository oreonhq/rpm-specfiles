%global source0_hash 830686238d7b9dba3b673b4d6fc571e96ed106a8382e09bd5ff68cdc29c09b66
%bcond_without       tests
%global gh_commit    d554eb24d64232922e1eab5896cc2f84b3b9ffb1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   vobject
%global with_cmd     1
Name:           php-sabre-vobject4
Summary:        Library to parse and manipulate iCalendar and vCard objects
Version:        4.5.8
Release:        1%{?dist}
URL:            http://sabre.io/vobject/
License:        BSD-3-Clause
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh
Patch0:         %{name}-bin.patch
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 7.1
Requires:       php-mbstring
Requires:       (php-composer(sabre/xml)    >= 2.1  with php-composer(sabre/xml)     < 5)
Requires:       php-cli
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xml
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(sabre/vobject) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sabre/xml) >= 2.1 with php-composer(sabre/xml) < 5)
BuildRequires:  php(language)
BuildRequires:  php-date
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xml
BuildRequires:  phpunit9
# /oreon:deps
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

%install
mkdir -p %{buildroot}%{_datadir}/php/Sabre
cp -pr lib %{buildroot}%{_datadir}/php/Sabre/VObject4
install -Dpm 0755 bin/vobject \
         %{buildroot}/%{_bindir}/vobject
install -Dpm 0755 bin/generate_vcards \
         %{buildroot}/%{_bindir}/generate_vcards
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
