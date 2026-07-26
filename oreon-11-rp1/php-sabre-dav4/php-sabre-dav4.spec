%global source0_hash 7817aa0c00196eccd592aea4b0f171aa33e27bcfac7351420ec23a7fda8b948b

# remirepo/fedora spec file for php-sabre-dav4
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    074373bcd689a30bcf5aaa6bbb20a3395964ce7a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   dav
# Packagist
%global pk_vendor    sabre
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Sabre
%global ns_project   DAV
%global major        4

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        WebDAV Framework for PHP
Version:        4.7.0
Release:        4%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
# sabre is BSD
# assets/openiconic is MIT
License:        BSD-3-Clause AND MIT
Source0:        %{name}-%{version}-%{gh_short}.tgz
# git snapshot to retrieve tests
Source1:        makesrc.sh

# replace composer autoloader
Patch0:         %{name}-autoload.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires: (php-composer(sabre/vobject)   >= 4.2.1  with php-composer(sabre/vobject)  < 5)
BuildRequires: (php-composer(sabre/event)     >= 5.0    with php-composer(sabre/event)    < 6)
BuildRequires: (php-composer(sabre/xml)       >= 2.0.1  with php-composer(sabre/xml)      < 3)
BuildRequires: (php-composer(sabre/http)      >= 5.0.5  with php-composer(sabre/http)     < 6)
BuildRequires: (php-composer(sabre/uri)       >= 2.0    with php-composer(sabre/uri)      < 3)
BuildRequires: (php-composer(psr/log)         >= 1.0.1  with php-composer(psr/log)        < 4)
BuildRequires: (php-composer(monolog/monolog) >= 1.27 with php-composer(monolog/monolog)  < 3)
BuildRequires:  php-dom
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-simplexml
BuildRequires:  php-mbstring
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-iconv
BuildRequires:  php-libxml
BuildRequires:  php-curl
BuildRequires:  php-pdo
BuildRequires:  php-json
# From composer.json, "require-dev" : {
#        "friendsofphp/php-cs-fixer": "^2.19",
#        "monolog/monolog": "^1.27 || ^2.0",
#        "phpstan/phpstan": "^0.12 || ^1.0",
#        "phpstan/phpstan-phpunit": "^1.0",
#        "phpunit/phpunit": "^7.5 || ^8.5 || ^9.6"
BuildRequires:  phpunit9 >= 9.6
%global phpunit %{_bindir}/phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pdo_sqlite

# From composer.json,    "require": {
#        "php": ">=7.1.0 || ^8.0",
#        "sabre/vobject": "^4.2.1",
#        "sabre/event" : "^5.0",
#        "sabre/xml"  : "^2.0.1",
#        "sabre/http" : "^5.0.5",
#        "sabre/uri" : "^2.0",
#        "ext-dom": "*",
#        "ext-pcre": "*",
#        "ext-spl": "*",
#        "ext-simplexml": "*",
#        "ext-mbstring" : "*",
#        "ext-ctype" : "*",
#        "ext-date" : "*",
#        "ext-iconv" : "*",
#        "lib-libxml" : ">=2.7.0",
#        "psr/log": "^1.0 || ^2.0 || ^3.0",
#        "ext-json": "*"
Requires:       php(language) >= 7.1
Requires:      (php-composer(sabre/vobject) >= 4.2.1  with php-composer(sabre/vobject) < 5)
Requires:      (php-composer(sabre/event)   >= 5.0    with php-composer(sabre/event)   < 6)
Requires:      (php-composer(sabre/xml)     >= 2.0.1  with php-composer(sabre/xml)     < 3)
Requires:      (php-composer(sabre/http)    >= 5.0.5  with php-composer(sabre/http)    < 6)
Requires:      (php-composer(sabre/uri)     >= 2.0    with php-composer(sabre/uri)     < 3)
Requires:      (php-composer(psr/log)       >= 1.0.1  with php-composer(psr/log)       < 4)
Requires:       php-dom
Requires:       php-pcre
Requires:       php-spl
Requires:       php-simplexml
Requires:       php-mbstring
Requires:       php-ctype
Requires:       php-date
Requires:       php-iconv
Requires:       php-libxml
Requires:       php-json
# From composer.json, "suggest" : {
#        "ext-curl" : "*",
#        "ext-pdo" : "*",
#        "ext-imap": "*"
Recommends:     php-curl
Recommends:     php-pdo
Recommends:     php-imap
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
What is SabreDAV

SabreDAV allows you to easily add WebDAV support to a PHP application.
SabreDAV is meant to cover the entire standard, and attempts to allow
integration using an easy to understand API.

Feature list:
* Fully WebDAV compliant
* Supports Windows XP, Windows Vista, Mac OS/X, DavFSv2, Cadaver, Netdrive,
  Open Office, and probably more.
* Passing all Litmus tests.
* Supporting class 1, 2 and 3 Webdav servers.
* Locking support.
* Custom property support.
* CalDAV (tested with Evolution, iCal, iPhone and Lightning).
* CardDAV (tested with OS/X addressbook, the iOS addressbook and Evolution).
* Over 97% unittest code coverage.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
mv lib/DAV/Browser/assets/openiconic/ICON-LICENSE .

%patch -P0 -p1 -b .rpm

: relocate
for dir in CalDAV CardDAV DAV DAVACL; do
    mv lib/${dir} lib/${dir}%{major}
done

: autoloader
phpab -t fedora -o lib/%{ns_project}%{major}/autoload.php lib
cat << 'EOF' | tee -a lib/%{ns_project}%{major}/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/Event5/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/Xml2/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/Uri2/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/HTTP5/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/VObject4/autoload.php',
    [
        '%{_datadir}/php/Psr/Log3/autoload.php',
        '%{_datadir}/php/Psr/Log2/autoload.php',
        '%{_datadir}/php/Psr/Log/autoload.php',
    ],
]);
EOF

# drop executable as only provided as doc
chmod -x bin/*

%build
# nothing to build

%install
# Install as a PSR-0 library
mkdir -p   %{buildroot}%{_datadir}/php/
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}

%check
%if %{with tests}
: Fix bootstrap
cd tests
sed -e 's:@BUILDROOT@:%{buildroot}:' -i bootstrap.php

: Run upstream test suite against installed library
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    for ts in sabre-dav sabre-davacl sabre-caldav sabre-carddav; do
      $1 ${2:-%{_bindir}/phpunit9} \
        --testsuite $ts || ret=1
    done
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif

%files
%license *LICENSE
%doc *md
%doc composer.json
%doc examples bin
%{_datadir}/php/%{ns_vendor}/DAV%{major}
%{_datadir}/php/%{ns_vendor}/DAVACL%{major}
%{_datadir}/php/%{ns_vendor}/CalDAV%{major}
%{_datadir}/php/%{ns_vendor}/CardDAV%{major}

%changelog
%autochangelog
