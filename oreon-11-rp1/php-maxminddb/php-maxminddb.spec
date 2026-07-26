%global source0_hash 6cd05979a75defcd7049d3108e161421de5411b5d68d5fa52985dde55604aae9

# Fedora spec file for php-maxminddb
# Without SCL compatibility from:
#
# remirepo spec file for php-maxminddb
#
# SPDX-FileCopyrightText:  Copyright 2018-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit   2194f58d0f024ce923e685cdf92af3daf9951908
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner    maxmind
%global gh_project  MaxMind-DB-Reader-php
# Extension
%global pie_vend    maxmind-db
%global pie_proj    reader-ext
%global pecl_name   maxminddb
%global ini_name    40-%{pecl_name}.ini
# pure PHP library
%global pk_vendor    maxmind-db
%global pk_project   reader
%global _configure   ../ext/configure

%if 0%{?fedora}
%bcond_without       tests
%else
%bcond_with          tests
%endif

Summary:       MaxMind DB Reader extension
Name:          php-maxminddb
Version:       1.13.1
Release:       2%{?dist}
License:       Apache-2.0
URL:           https://github.com/%{gh_owner}/%{gh_project}

Source0:       %{name}-%{version}-%{gh_short}.tgz
Source1:       makesrc.sh

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 7.2
BuildRequires: php-pear  >= 1.10
BuildRequires: pkgconfig(libmaxminddb) >= 1.0.0

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

# Weak dependencies on databases
Recommends:    geolite2-country
Suggests:      geolite2-city

# PECL
Provides:       php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
# PIE
Provides:       %{?scl_prefix}php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       %{?scl_prefix}php-%{pie_vend}-%{pie_proj} = %{version}

%description
MaxMind DB is a binary file format that stores data indexed by
IP address subnets (IPv4 or IPv6).

This optional PHP C Extension is a drop-in replacement for
MaxMind\Db\Reader.

Databases are available in geolite2-country and geolite2-city packages.

%package -n php-%{pk_vendor}-%{pk_project}
Summary:       MaxMind DB Reader

BuildArch:     noarch
BuildRequires: php-fedora-autoloader-devel
%if %{with tests}
BuildRequires: php-bcmath
BuildRequires: php-gmp
# from composer.json "require-dev": {
#        "friendsofphp/php-cs-fixer": "*",
#        "phpunit/phpunit": ">=8.0.0,<10.0.0",
#        "php-coveralls/php-coveralls": "^2.1",
#        "phpunit/phpcov": ">=6.0.0",
#        "squizlabs/php_codesniffer": "3.*"
BuildRequires: phpunit8
%endif

# from composer.json "require": {
#        "php": ">=7.2"
Requires:      php(language) >= 7.2
# from composer.json "suggest": {
#        "ext-bcmath": "bcmath or gmp is required for decoding larger integers with the pure PHP decoder",
#        "ext-gmp": "bcmath or gmp is required for decoding larger integers with the pure PHP decoder",
#        "ext-maxminddb": "A C-based database decoder that provides significantly faster lookups"
Recommends:    php-bcmath
Recommends:    php-gmp
Recommends:    php-maxminddb
# from composer.json "conflict": {
#        "ext-maxminddb": "<1.11.1,>=2.0.0"
Conflicts:     php-maxminddb < %{version}
# Weak dependencies on databases
Recommends:    geolite2-country
Suggests:      geolite2-city
# From phpcompatifo report for 1.3.0
Requires:      php-filter
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

Provides:      php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description -n php-%{pk_vendor}-%{pk_project}
MaxMind DB Reader PHP API.

MaxMind DB is a binary file format that stores data indexed by
IP address subnets (IPv4 or IPv6).

Databases are available in geolite2-country and geolite2-city packages.

The extension available in php-maxminddb package allow better
performance.

Autoloader: %{_datadir}/php/MaxMind/Db/Reader/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%{_bindir}/phpab \
    --template fedora \
    --output src/MaxMind/Db/Reader/autoload.php \
    src/MaxMind/Db

cd ext
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_MAXMINDDB_VERSION/{s/.* "//;s/".*$//;p}'  php_maxminddb.h)
if test "x${extver}" != "x%{version}%{?gh_date:-dev}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat << 'EOF' | tee %{ini_name}
; Enable '%{pecl_name}' extension module
extension = %{pecl_name}.so
EOF

%build
cd ext
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-php-config=%{__phpconfig} \
    --with-libdir=%{_lib} \
    --with-maxminddb

%make_build

%install
: Install the extension
%make_install -C ext

: Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the extension
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the library
mkdir -p                %{buildroot}%{_datadir}/php/MaxMind
cp -pr src/MaxMind/Db   %{buildroot}%{_datadir}/php/MaxMind/Db

%check
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

ret=0

cd ext
: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff || ret=1

%if %{with tests}
cd ..
: Upstream test suite for the library
for cmd in php80 php81 php82 php83 php84; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 \
      --bootstrap %{buildroot}%{_datadir}/php/MaxMind/Db/Reader/autoload.php \
      --verbose || ret=1
  fi
done

: Upstream test suite for the library with the extension
php --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
  %{_bindir}/phpunit8 \
    --bootstrap %{buildroot}%{_datadir}/php/MaxMind/Db/Reader/autoload.php \
    --verbose || ret=1
%endif
exit $ret

%files
%license LICENSE
%doc *.md
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%files -n php-%{pk_vendor}-%{pk_project}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/MaxMind
     %{_datadir}/php/MaxMind/Db

%changelog
%autochangelog
