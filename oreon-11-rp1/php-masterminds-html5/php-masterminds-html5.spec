%global source0_hash 6e8290e88cb851439348c220dbea3ccab0101cc2613e03eecad612fc687d81c6

#
# Fedora spec file for php-masterminds-html5
#
# Copyright (c) 2015-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Masterminds
%global github_name      html5-php
%global github_version   2.7.6
%global github_commit    897eb517a343a2281f11bc5556d6548db7d93947

%global composer_vendor  masterminds
%global composer_project html5

# "php" : ">=5.3.0"
%global php_min_ver 5.3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       9%{?dist}
Summary:       An HTML5 parser and serializer

License:       MIT
URL:           http://masterminds.github.io/html5-php
# GitHub export does not include tests.
# Run php-league-container-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Autoload generation
BuildRequires: %{_bindir}/phpab
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit8
BuildRequires: php-ctype
BuildRequires: php-dom
## phpcompatinfo (computed from version 2.7.0)
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-ctype
Requires:      php-dom
# phpcompatinfo (computed from version 2.7.0)
Requires:      php-iconv
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# notice: xml only detected for utf8_decode

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The need for an HTML5 parser in PHP is clear. This project initially began with
the seemingly abandoned html5lib project original source. But after some initial
refactoring work, we began a new parser.

* An HTML5 serializer
* Support for PHP namespaces
* Composer support
* Event-based (SAX-like) parser
* DOM tree builder
* Interoperability with QueryPath

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

: Docs
mkdir -p docs/{Parser,Serializer}
mv composer.json *.md docs/
mv src/HTML5/Parser/*.md docs/Parser/
mv src/HTML5/Serializer/*.md docs/Serializer/

%build
: Generate autoloader
# Vendor-level autoloader to pick up "Masterminds/HTML5" class
%{_bindir}/phpab --nolower --output src/autoload-html5.php src

%install
mkdir -p  %{buildroot}%{phpdir}/Masterminds
cp -pr src/* %{buildroot}%{phpdir}/Masterminds/
# Project-level autoloader for consistency with other pkgs
ln -s ../autoload-html5.php %{buildroot}%{phpdir}/Masterminds/HTML5/autoload.php

%check
%if %{with_tests}
: Generate test autoloader
%{_bindir}/phpab --nolower --output test/autoload.php test

: Create mock Composer autoloader
mkdir vendor
cat > vendor/autoload.php <<'AUTOLOAD'
<?php

require '%{buildroot}%{phpdir}/Masterminds/HTML5/autoload.php';
require __DIR__ . '/../test/autoload.php';
AUTOLOAD

: fix for phpunit8
find test \
  -name \*.php \
  -exec sed \
    -e 's/function setUp()/function setUp():void/' \
    -i {} \;

sed -e 's/assertContains(/assertStringContainsString(/' \
    -i test/HTML5/Html5Test.php

grep -v blacklist < phpunit.xml.dist | \
  grep -v '<file' > phpunit.xml

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in "" php74 php80 php81 php82; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc docs/*
%{phpdir}/Masterminds

%changelog
%autochangelog
