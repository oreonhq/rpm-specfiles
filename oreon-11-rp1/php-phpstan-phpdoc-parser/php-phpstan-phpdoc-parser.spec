%global source0_hash b436042bf0d8a3e61df9153078a91746e35a0c2e34457ab8103a1e4693f33440

# remirepo/Fedora spec file for php-phpstan-phpdoc-parser
#
# SPDX-FileCopyrightText:  Copyright 2024-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    a004701b11273a26cd7955a61d67a7f1e525a45a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpstan
%global gh_project   phpdoc-parser
%global php_home     %{_datadir}/php
%global namespace    PHPStan
%global library      PhpDocParser
%global major        %nil

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        2.3.2
Release:        1%{?dist}
Summary:        PHPDoc parser with support for nullable, intersection and generic types

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to retrieve test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with tests}
BuildRequires:  php(language) >= 7.4
BuildRequires:  php-json
BuildRequires:  php-pcre
# From composer, "require-dev": {
# "doctrine/annotations": "^2.0",
# "nikic/php-parser": "^5.3.0",
# "php-parallel-lint/php-parallel-lint": "^1.2",
# "phpstan/extension-installer": "^1.0",
# "phpstan/phpstan": "^2.0",
# "phpstan/phpstan-phpunit": "^2.0",
# "phpstan/phpstan-strict-rules": "^2.0",
# "phpunit/phpunit": "^9.6",
# "symfony/process": "^5.2"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.6
%endif
BuildRequires: (php-composer(nikic/php-parser)     >= 5.3  with php-composer(nikic/php-parser)     < 6)
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
# "php": "^7.4 || ^8.0"
Requires:       php(language) >= 7.4
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.4.2
Requires:       php-json
Requires:       php-pcre

Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}

%description
Next generation phpDoc parser with support for intersection types and generics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
phpab --template fedora --output src/autoload.php src

%install
: library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}%{major}

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// to avoid v5 from PHPUnit
require_once '%{php_home}/PhpParser5/autoload.php';
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}\\%{library}\\', dirname(__DIR__) . '/tests/%{namespace}');
EOF

: ignore tests using symfony/process and abnfgen
rm tests/PHPStan/Parser/FuzzyTest.php
sed -e 's:exec://exec:' -i tests/bootstrap.php

: upstream test suite
# use auto_prepend_file to ensure we use new version (not old one pulled by PHPUnit)
# ignore test using doctrine/annotations
ret=0
for cmdarg in "php %{phpunit}" php82 php83 php84 php85; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d auto_prepend_file=vendor/autoload.php \
      ${2:-%{_bindir}/phpunit9} \
        -d memory_limit=1G \
        --filter '^((?!(testDoctrine)).)*$' \
        --no-coverage \
        --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/%{namespace}
     %{php_home}/%{namespace}/%{library}%{major}

%changelog
%autochangelog
