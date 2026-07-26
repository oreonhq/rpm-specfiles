%global source0_hash fe8f57a4a973b705c158570203912e96d26a5e862de807f6f5bc88a8555b3ae7

# remirepo/fedora spec file for php-netresearch-jsonmapper
#
# Copyright (c) 2017-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    8e76efb98ee8b6afc54687045e1b8dba55ac76e5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     cweiske
%global gh_project   jsonmapper

%global pk_vendor    netresearch
%global pk_project   jsonmapper

%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}4
Version:        4.5.0
Release:        4%{?dist}
Summary:        Map nested JSON structures onto PHP classes, version 4

License:        OSL-3.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Git snapshot with tests
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "~7.5 || ~8.0 || ~9.0 || ~10.0",
#        "squizlabs/php_codesniffer": "~3.5"
%global phpunit %{_bindir}/phpunit10
BuildRequires: phpunit10
# Required by autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#        "php": ">=7.1",
#        "ext-spl": "*",
#        "ext-json": "*",
#        "ext-pcre": "*",
#        "ext-reflection": "*"
Requires:       php(language) >= 7.1
Requires:       php-spl
Requires:       php-json
Requires:       php-pcre
Requires:       php-reflection
# From phpcompatinfo report for version 4.4.0
# none
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Takes data retrieved from a JSON web service and converts them into nested
object and arrays - using your own model classes.

Starting from a base object, it maps JSON data on class properties, converting
them into the correct simple types or objects.

It's a bit like the native SOAP parameter mapping PHP's SoapClient gives you,
but for JSON. It does not rely on any schema, only your PHP class definitions.

Type detection works by parsing @var docblock annotations of class properties,
as well as type hints in setter methods.

You do not have to modify your model classes by adding JSON specific code;
it works automatically by parsing already-existing docblocks.

Autoloader: %{php_home}/%{pk_vendor}/%{pk_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
phpab --template fedora --output src/autoload.php src

%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{pk_vendor}
cp -pr src %{buildroot}%{php_home}/%{pk_vendor}/%{pk_project}

%check
%if %{with tests}
mkdir vendor
phpab --template fedora --output vendor/autoload.php tests
cat << 'EOF' | tee -a vendor/autoload.php
require_once "%{buildroot}%{php_home}/%{pk_vendor}/%{pk_project}/autoload.php";
EOF

: Run upstream test suite
ret=0
for cmd in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit10} \
      --no-coverage \
      . || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc ChangeLog README.rst
%dir %{php_home}/%{pk_vendor}
     %{php_home}/%{pk_vendor}/%{pk_project}

%changelog
%autochangelog
