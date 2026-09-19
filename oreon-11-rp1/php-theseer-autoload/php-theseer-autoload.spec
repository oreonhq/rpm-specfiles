%global source0_hash 464580f0be02900c54a840d19268bf20ccf547e2d83f816499fdc8aca24f7481

# remirepo/fedora spec file for php-theseer-autoload
#
# SPDX-FileCopyrightText:  Copyright 2014-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global gh_commit    c3a22a88ae6bdadbe0c8274a51d29998eb152983
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     theseer
%global gh_project   Autoload
%global php_home     %{_datadir}/php/TheSeer
%global pear_name    Autoload
%global pear_channel pear.netpirates.net

%if 0%{?fedora}
%bcond_without  tests
%else
%bcond_with     tests
%endif

Name:           php-theseer-autoload
Version:        1.29.4
Release:        2%{?dist}
Summary:        A tool and library to generate autoload code

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

# Autoloader path
Patch0:         %{gh_project}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.4
BuildRequires:  php-cli
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-openssl
BuildRequires:  php-phar
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
BuildRequires: (php-composer(theseer/directoryscanner)     >= 1.3.2 with php-composer(theseer/directoryscanner)     < 2)
BuildRequires: (php-composer(zetacomponents/console-tools) >= 1.7   with php-composer(zetacomponents/console-tools) < 2)
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
%endif

# From composer.json, "require": {
#        "php": ">=5.3",
#        "ext-openssl": "*",
#        "theseer/directoryscanner": "^1.3.3",
#        "zetacomponents/console-tools": "^1.7.2"
Requires:       php(language) >= 5.3.1
Requires:       php-openssl
Requires:      (php-composer(theseer/directoryscanner)     >= 1.3.2 with php-composer(theseer/directoryscanner)     < 2)
Requires:      (php-composer(zetacomponents/console-tools) >= 1.7   with php-composer(zetacomponents/console-tools) < 2)
# From phpcompatinfo report for version 1.25.0
Requires:       php-cli
Requires:       php-date
Requires:       php-json
Requires:       php-phar
Requires:       php-spl
Requires:       php-tokenizer
# Optional xdebug

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(theseer/autoload) = %{version}

%description
The PHP AutoloadBuilder CLI tool phpab is a command line application
to automate the process of generating an autoload require file with
the option of creating static require lists as well as phar archives.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm

: drop composer dependencies
sed -e '\:../vendor/:d'    -i src/autoload.php

: add package dependencies
cat <<EOF | tee            -a src/autoload.php
// Dependencies
require '/usr/share/php/TheSeer/DirectoryScanner/autoload.php';
require '/usr/share/php/ezc/Base/base.php';
spl_autoload_register(array('\\ezcBase','autoload'));
EOF

# set version
sed -e 's/@VERSION@/%{version}/' -i phpab.php

%build
# Empty build section, most likely nothing required.

%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{gh_project}

install -Dpm 0755 phpab.php %{buildroot}%{_bindir}/phpab

%check
: Check version
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' phpab.php >t.php
php t.php --version | grep %{version}
php t.php --output foo.php src

%if %{with tests}
: Fix test suite to use installed library
cat <<EOF | tee tests/init.php
<?php
require '%{buildroot}%{_datadir}/php/TheSeer/Autoload/autoload.php';
EOF

ret=0
for cmd in "php %{phpunit}" php81 php82 php83 php84 php85; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done
exit $ret
%endif

%pre
if [ -x %{_bindir}/pear ]; then
  %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi

%files
%license LICENSE
%doc README.md composer.json
%{php_home}/%{gh_project}
%{_bindir}/phpab

%changelog
%autochangelog
