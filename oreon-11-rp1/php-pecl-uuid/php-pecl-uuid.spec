%global source0_hash b7af055e2c409622f8c5e6242d1c526c00e011a93c39b10ca28040b908da3f37

# Fedora spec file for php-pecl-uuid
#
# SPDX-FileCopyrightText:  Copyright 2012-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pie_vend    pecl
%global pie_proj    uuid
%global pecl_name   uuid
%global ini_name    40-%{pecl_name}.ini
%global sources     %{pecl_name}-%{version}

Summary:       Universally Unique Identifier extension for PHP
Name:          php-pecl-uuid
Version:       1.3.0
Release:       4%{?dist}
License:       LGPL-2.1-or-later
URL:           https://pecl.php.net/package/%{pecl_name}
Source:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel
BuildRequires: php-pear
BuildRequires: libuuid-devel

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}
# both provides same extension, with different API
Conflicts:     uuid-php

Provides:      php-%{pecl_name}                 = %{version}
Provides:      php-%{pecl_name}%{?_isa}         = %{version}
Provides:      php-pecl(%{pecl_name})           = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:      php-pie(%{pie_vend}/%{pie_proj}) = %{version}

%description
A wrapper around Universally Unique Identifier library (libuuid).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c 

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_UUID_VERSION/{s/.* "//;s/".*$//;p}' php_uuid.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat > %{ini_name} << 'EOF'
; Enable UUID extension module
extension = %{pecl_name}.so
EOF

%build
export PHP_RPATH=no

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-php-config=%{__phpconfig} \
    --with-libdir=%{_lib} \
    --with-uuid

%make_build

%install
: Install the configuration file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the package XML file
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

cd %{sources}
: Install the extension
%make_install

: Install the documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}

: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=mbstring.so \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

: Upstream test suite for the extension
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
