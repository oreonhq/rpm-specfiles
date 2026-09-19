%global source0_hash 7567187df63adb1d008cb2d2405a47efe5959f9c691f8e974f156174109c6fab

# Fedora spec file for php-pecl-xattr
# with SCL compatibility removed, from
#
# remirepo spec file for php-pecl-xattr
#
# SPDX-FileCopyrightText:  Copyright 2013-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pecl_name xattr
%global pie_vend  pecl
%global pie_proj  xattr
%global ini_name  40-%{pecl_name}.ini
%global sources   %{pecl_name}-%{version}

Summary:        Extended attributes
Name:           php-pecl-%{pecl_name}
Version:        1.4.1
Release:        2%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 7.2
BuildRequires:  php-pear  >= 1.10

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Extension
Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
# PECL
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
# PIE
Provides:       %{?scl_prefix}php-pie(%{pie_vend}/%{pie_proj}) = %{version}

%description
This package allows to manipulate extended attributes on filesystems
that support them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_XATTR_VERSION/{s/.* "//;s/".*$//;p}' php_xattr.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever:-%{prever}}.
   exit 1
fi
cd ..

# Create configuration file
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%build
cd %{sources}

%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build

%install
cd %{sources}

: Install the extension
%make_install

: Install the config file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}

: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite for the extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=$PWD/modules/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php --show-diff

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
