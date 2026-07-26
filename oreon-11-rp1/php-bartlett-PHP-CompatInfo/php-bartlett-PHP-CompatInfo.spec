%global source0_hash a64e44b616ad690b873e675badd1fd7d7de47b904048178d0e02f020e8877892

# remirepo/fedora spec file for php-bartlett-PHP-CompatInfo
#
# SPDX-FileCopyrightText:  Copyright 2011-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%{!?php_version:  %global php_version  %(php -r 'echo PHP_VERSION;' 2>/dev/null)}
%global gh_commit    56d3215bcf8acb2e822fc9ce21fa934cd6129637
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2025-11-23
%global gh_owner     llaville
%global gh_project   php-compatinfo

%global upstream_version  7.2.5
#global upstream_prever   RC1

Name:           php-bartlett-PHP-CompatInfo
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        2%{?dist}
Summary:        Find out version and the extensions required for a piece of code to run

# SPDX: see bundled libraries list below
License:        BSD-3-Clause and MIT
URL:            https://github.com/llaville/php-compatinfo
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Script for fedora-review
Source1:        fedora-review-check
# Generate the archive will all dependencies
Source9:        makesrc.sh

# Relocate the database
Patch0:         %{name}-7.2.3-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-cli
BuildRequires:  composer-generators

Requires:       php(language) >= 8.1
Requires:       php-cli
Requires:       php-dom
Requires:       php-libxml
Requires:       php-phar
Requires:       php-pdo
Requires:       php-pdo_sqlite
Requires:       php-simplexml
Requires:       php-xmlreader

Provides: phpcompatinfo = %{version}

%description
PHP_CompatInfo will parse a file/folder/array to find out the minimum
version and extensions required for it to run. CLI version has many reports
(extension, interface, class, function, constant) to display and ability to
show content of dictionary references.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm
rm bin/*rpm

# https://github.com/llaville/php-compatinfo-db/issues/112
sed -e 's/touch/@touch/' -i vendor/bartlett/php-compatinfo-db/config/set/default.php

: Gather all license files and cleanup tests
mv vendor/composer/LICENSE composer_LICENSE
for vendor in $(ls vendor)
do
  for proj in $(ls vendor/$vendor)
  do
    [ -d vendor/$vendor/$proj/tests ]   && rm -r vendor/$vendor/$proj/tests
    [ -f vendor/$vendor/$proj/LICENSE ] && mv vendor/$vendor/$proj/LICENSE ${vendor}_${proj}_LICENSE
  done
done
rm -r vendor/bartlett/*/.github
rm -r vendor/bartlett/*/.changes

%build
# Nothing

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
for i in bin config data resources src vendor composer.* autoload.php
do cp -pr $i %{buildroot}%{_datadir}/%{name}/$i
done

mkdir -p %{buildroot}%{_bindir}
ln -s ../share/%{name}/bin/phpcompatinfo %{buildroot}%{_bindir}/phpcompatinfo

mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_datadir}/%{name}/bin/phpcompatinfo.1 \
   %{buildroot}%{_mandir}/man1/phpcompatinfo.1

install -D -p -m 755 %{SOURCE1} \
   %{buildroot}%{_datadir}/%{name}/fedora-review-check

%check
%{buildroot}%{_bindir}/phpcompatinfo --version | grep %{version} && exit 0

%files
%license *LICENSE
%doc *md
%doc docs
%doc examples
%doc composer.json
%doc vendor/composer/installed.json
%{_bindir}/phpcompatinfo
%{_datadir}/%{name}
%{_mandir}/man1/phpcompatinfo.1*

%changelog
%autochangelog
