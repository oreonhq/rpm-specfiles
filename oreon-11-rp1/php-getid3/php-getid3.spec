%global source0_hash e458ea7c0dafe8409b157ae8986ba37f578bf192bdb47022b72bf5449e596545

#
# Fedora spec file for php-getid3
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global gh_commit    fefffe762b02be155dcc32eec57feff8a49bc4b5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     JamesHeinrich
%global gh_project   getID3
%global pk_owner     james-heinrich
%global pk_project   getid3

Name:      php-%{pk_project}
Version:   1.9.25
Release:   1%{?dist}
Epoch:     1
License:   GPL-1.0-or-later OR LGPL-3.0-only OR MPL-2.0
Summary:   The PHP media file parser
URL:       https://www.getid3.org/
Source0:   %{name}-%{version}-%{gh_short}.tgz
Source1:   makesrc.sh

BuildArch: noarch
BuildRequires: php-fedora-autoloader-devel

# from composer.json
#        "php": ">=5.3.0"
Requires:  php(language) >= 5.3.0
# from phpcompatinfo for version 1.9.16
Requires:  php-simplexml
Requires:  php-exif
Requires:  php-gd
Requires:  php-iconv
Requires:  php-json
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-xml
Suggests:  php-dba
Suggests:  php-mysqli
Suggests:  php-rar
Suggests:  php-sqlite3
# Autoloader
Requires:  php-composer(fedora/autoloader)

Provides:  php-composer(%{pk_owner}/%{pk_project}) = %{version}

%description
getID3() is a PHP script that extracts useful information 
(such as ID3 tags, bitrate, playtime, etc.) from MP3s & 
other multimedia file formats (Ogg, WMA, WMV, ASF, WAV, AVI, 
AAC, VQF, FLAC, MusePack, Real, QuickTime, Monkey's Audio, MIDI and more).

Autoloader: %{_datadir}/php/getid3/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# From composer.json, "autoload": {
#        "classmap": ["getid3/"]
%{_bindir}/phpab --template fedora --output getid3/autoload.php getid3

%install
mkdir -p %{buildroot}%{_datadir}/php
cp -a getid3 %{buildroot}%{_datadir}/php/

%check
php -r '
require "%{buildroot}%{_datadir}/php/getid3/autoload.php";
$ok = class_exists("getID3");
echo "Autoload: " . ($ok ? "Ok\n" : "fails\n");
echo "Version: " . getID3::VERSION . "\n";
$ok = ($ok && strpos(getID3::VERSION, "%{version}") !== false);
exit ($ok ? 0 : 1);
'

%files
%license licenses license.txt
%doc changelog.txt dependencies.txt readme.txt structure.txt demos
%doc composer.json
%{_datadir}/php/getid3

%changelog
%autochangelog
