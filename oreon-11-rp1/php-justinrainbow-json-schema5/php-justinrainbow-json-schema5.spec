%global source1_hash 676df4d0a1344d11b3d0deded01362bc70acc604aa487793eeba752846cd52bc
%global source0_hash 676df4d0a1344d11b3d0deded01362bc70acc604aa487793eeba752846cd52bc
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
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
%global ts_commit    f3d5aeb5ffbe9d9a5a0ceb761dc47c7c4c2efa68
%global ts_short     %(c=%{ts_commit}; echo ${c:0:7})
%global ts_owner     json-schema
%global ts_project   JSON-Schema-Test-Suite
%global ts_version   1.2.0
%global eolv1        0
%global eolv2        0
Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        6.12.0
Release:        1%{?dist}
Summary:        A library to validate a json schema
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        https://github.com/%{ts_owner}/%{ts_project}/archive/%{ts_commit}/%{ts_project}-%{ts_version}-%{ts_short}.tar.gz
Source2:        %{name}-autoload.php
Source3:        %{name}-makesrc.sh
Patch0:         %{name}-rpm.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 7.1
Requires:       php-curl
Requires:       php-json
Requires:       php-mbstring
Requires:       php-composer(fedora/autoloader)
Requires:       php-cli
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  composer
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires:  php-curl
BuildRequires:  php-json
BuildRequires:  php-mbstring
# /oreon:deps
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

%install
: Library
mkdir -p              %{buildroot}%{php_home}
cp -pr src/JsonSchema %{buildroot}%{php_home}/JsonSchema%{major}
: Schemas
mkdir -p              %{buildroot}%{_datadir}/%{name}
cp -pr dist           %{buildroot}%{_datadir}/%{name}/dist
: Command
install -Dpm 0755 bin/validate-json %{buildroot}%{_bindir}/validate-json%{major}
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
