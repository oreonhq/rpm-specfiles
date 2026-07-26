%global source0_hash 676df4d0a1344d11b3d0deded01362bc70acc604aa487793eeba752846cd52bc

# remirepo/fedora spec file for php-justinrainbow-json-schema5
#
# SPDX-FileCopyrightText:  Copyright 2016-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
# disable test suite until recent phpunit is supported
%bcond_with          tests
%else
%bcond_without       tests
%endif

%global gh_commit    2f7abf648939847a789c55c206d4cb9dd0d53e2c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     justinrainbow
%global gh_project   json-schema
%global php_home     %{_datadir}/php
%global major        5

# Some sample files, only used for tests
#        "json-schema/JSON-Schema-Test-Suite": "1.1.0",
%global ts_commit    f3d5aeb5ffbe9d9a5a0ceb761dc47c7c4c2efa68
%global ts_short     %(c=%{ts_commit}; echo ${c:0:7})
%global ts_owner     json-schema
%global ts_project   JSON-Schema-Test-Suite
%global ts_version   1.2.0

%global eolv1        0
%global eolv2        0

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        5.3.2
Release:        1%{?dist}
Summary:        A library to validate a json schema
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}

# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        https://github.com/%{ts_owner}/%{ts_project}/archive/%{ts_commit}/%{ts_project}-%{ts_version}-%{ts_short}.tar.gz
Source2:        %{name}-autoload.php
Source3:        %{name}-makesrc.sh

# Autoloader
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-curl
BuildRequires:  php-json
BuildRequires:  php-mbstring
# From composer.json, "require-dev": {
#        "json-schema/json-schema-test-suite": "1.2.0",
#        "friendsofphp/php-cs-fixer": "^2.1",
#        "phpunit/phpunit": "^4.8.35"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.8.35
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
# For composer schema
BuildRequires:  composer
%endif

# From composer.json, "require": {
#        "php": ">=7.1"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 4.0.1
Requires:       php-curl
Requires:       php-json
Requires:       php-mbstring
# Autoloader
Requires:       php-composer(fedora/autoloader)
%if %{eolv1}
Obsoletes:      php-JsonSchema < 2
%endif
%if %{eolv2}
Obsoletes:      php-justinrainbow-json-schema < 3
%endif
Requires:       php-cli

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}

%description
A PHP Implementation for validating JSON Structures against a given Schema.

This package provides the library version %{major}.

See http://json-schema.org/

Autoloader: %{php_home}/JsonSchema%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit} -a 1

%patch -P0 -p1 -b .rpm
find src -name \*.rpm -delete -print

cp %{SOURCE2} src/JsonSchema/autoload.php

: Needed for the test suite - use composer default path, as easier
mkdir -p vendor/json-schema/JSON-Schema-Test-Suite
mv %{ts_project}-%{ts_commit}/tests \
   vendor/json-schema/JSON-Schema-Test-Suite/tests

: But without online tests
find vendor/json-schema/JSON-Schema-Test-Suite/tests \
   -name \*.json \
   -exec grep -q 'http://' {} \; \
   -exec rm {} \; \
   -print

%build
# Empty build section, most likely nothing required.

%install
: Library
mkdir -p              %{buildroot}%{php_home}
cp -pr src/JsonSchema %{buildroot}%{php_home}/JsonSchema%{major}

: Schemas
mkdir -p              %{buildroot}%{_datadir}/%{name}
cp -pr dist           %{buildroot}%{_datadir}/%{name}/dist

: Command
install -Dpm 0755 bin/validate-json %{buildroot}%{_bindir}/validate-json%{major}

%check
%if %{with tests}
: Test suite autoloader
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/JsonSchema%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('JsonSchema\\Tests\\', 'tests/');
EOF

export BUILDROOT_SCHEMA=%{buildroot}

: Test the command
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' \
    bin/validate-json > bin/validate-json-test
php bin/validate-json-test \
    composer.json \
    /usr/share/composer/res/composer-schema.json

: Upstream test suite
ret=0
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
   $cmd -d memory_limit=1G %{_bindir}/phpunit -d memory_limit=1G --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc *.md
%{_bindir}/validate-json%{major}
%{php_home}/JsonSchema%{major}
%{_datadir}/%{name}

%changelog
%autochangelog
