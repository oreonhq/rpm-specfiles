%global source0_hash ec13c57ac4cdb3c010446137c2a36f72c16bfcffeb432d7ca19d15985080e221

# remirepo/fedora spec file for php-cs-fixer
#
# SPDX-FileCopyrightText:  Copyright 2016-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global gh_commit    7787ceff91365ba7d623ec410b8f429cdebb4f63
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2026-02-20
%global gh_owner     FriendsOfPHP
%global gh_project   PHP-CS-Fixer

Name:           php-cs-fixer
Version:        3.94.2
Release:        1%{?dist}
Summary:        PHP Coding Standards Fixer

# see bundled list below, SPDX
License:        MIT AND BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh

# Use our autoloader
Patch0:         %{name}-autoload.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-cli
BuildRequires:  php-json
BuildRequires:  composer-generators >= 0.1.1

# see composer.json and makesrc.sh
Requires:       php(language) >= 8.1
Requires:       php-json
Requires:       php-tokenizer
# From phpcompatinfo report for version 3.5.0
Requires:       php-dom
Requires:       php-intl
Requires:       php-mbstring

# Package was renamed
Obsoletes:      php-cs-fixer3 < 3.5
Provides:       php-cs-fixer3 = %{version}

%description
The PHP Coding Standards Fixer (PHP CS Fixer) tool fixes your code to follow
standards; whether you want to follow PHP coding standards as defined in the
PSR-1, PSR-2, etc., or other community driven ones like the Symfony one. You
can also define your (team's) style through configuration.

It can modernize your code (like converting the pow function to the ** operator
on PHP 5.6) and (micro) optimize it.

If you are already using a linter to identify coding standards problems in your
code, you know that fixing them by hand is tedious, especially on large
projects. This tool does not only detect them, but also fixes them for you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm

# Fix version
#sed -e '/VERSION/s/3.68.6-DEV/%{version}/' -i src/Console/Application.php
# check version
grep "'%{version}'" src/Console/Application.php

%build
# Empty build section, most likely nothing required.

%install
: Library
mkdir -p      %{buildroot}%{_datadir}/%{name}
cp -pr src    %{buildroot}%{_datadir}/%{name}/src
cp -pr vendor %{buildroot}%{_datadir}/%{name}/vendor

: Command
install -Dpm755 %{name} %{buildroot}%{_bindir}/%{name}

%check
sed -e 's:%{_datadir}:%{buildroot}%{_datadir}:' -i %{name}
PHP_CS_FIXER_IGNORE_ENV=1 ./%{name} --version
PHP_CS_FIXER_IGNORE_ENV=1 ./%{name} --version | grep %{version}

%files
%license LICENSE
%doc composer.json
%doc vendor/composer/installed.json
%doc *.md
%{_datadir}/%{name}
%{_bindir}/%{name}

%changelog
%autochangelog
