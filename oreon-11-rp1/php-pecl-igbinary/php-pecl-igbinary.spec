%global source0_hash 8bf25d465abc7973d9e2c9a3039a5f8eea635b23bc1477017ff3999ff95836da

# Fedora spec file for php-pecl-igbinary
#
# SPDX-FileCopyrightText:  Copyright 2010-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pecl_name  igbinary
%global ini_name   40-%{pecl_name}.ini

%global upstream_version 3.2.16
#global upstream_prever  RC1
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}

Summary:        Replacement for the standard PHP serializer
Name:           php-pecl-igbinary
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        7%{?dist}
Source0:        https://pecl.php.net/get/%{sources}.tgz
License:        BSD-3-Clause

URL:            https://pecl.php.net/package/igbinary

Patch0:         393.patch
Patch1:         398.patch
Patch2:         399.patch

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  php-pear
BuildRequires:  php-devel >= 7.0
BuildRequires:  php-pecl-apcu-devel
BuildRequires:  php-json
# used by tests
BuildRequires:  tzdata

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}

%description
Igbinary is a drop in replacement for the standard PHP serializer.

Instead of time and space consuming textual representation, 
igbinary stores PHP data structures in a compact binary form. 
Savings are significant when using memcached or similar memory
based storages for serialized data.

%package devel
Summary:       Igbinary developer files (header)
Requires:      php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}

%description devel
These are the files needed to compile programs using Igbinary

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

sed -e '/COPYING/s/role="doc"/role="src"/' -i package.xml

cd %{sources}
%patch -P0 -p1 -b .pr393
%patch -P1 -p1 -b .pr398
%patch -P2 -p1 -b .pr399

# Check version
subdir="php$(%{__php} -r 'echo (PHP_MAJOR_VERSION < 7 ? 5 : 7);')"
extver=$(sed -n '/#define PHP_IGBINARY_VERSION/{s/.* "//;s/".*$//;p}' src/$subdir/igbinary.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

cat <<EOF | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; Enable or disable compacting of duplicate strings
; The default is On.
;igbinary.compact_strings=On

; Use igbinary as session serializer
;session.serialize_handler=igbinary

; Use igbinary as APC serializer
;apc.serializer=igbinary
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --with-php-config=%{__phpconfig}

%make_build

%install
: Install package.xml
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the configuration file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the extension
cd %{sources}
%make_install

: Install Test and Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do [ -f $i       ] && install -Dpm 644 $i       %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
   [ -f tests/$i ] && install -Dpm 644 tests/$i %{buildroot}%{pecl_testdir}/%{pecl_name}/tests/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}
MOD=""
# drop extension load from phpt
sed -e '/^extension=/d' -i tests/*phpt

: simple module load test, without APC, as optional
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

# APC required for test 045
if [ -f %{php_extdir}/apcu.so ]; then
  MOD="-d extension=apcu.so"
fi
# Json used in tests
if [ -f %{php_extdir}/json.so ]; then
  MOD="$MOD -d extension=json.so"
fi

: upstream test suite
TEST_PHP_ARGS="-n $MOD -d extension=modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -x -q --show-diff %{?_smp_mflags}

%files
%license %{sources}/COPYING
%doc %{pecl_docdir}/%{pecl_name}
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so
%{pecl_xmldir}/%{name}.xml

%files devel
%doc %{pecl_testdir}/%{pecl_name}
%{php_incldir}/ext/%{pecl_name}

%changelog
%autochangelog
