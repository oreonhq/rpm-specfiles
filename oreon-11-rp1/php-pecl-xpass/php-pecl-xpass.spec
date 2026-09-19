%global source0_hash 9a1d713b69cb44e8f46c764daf2d87763944396d255a942d8b857e01f90dc3df

# Fedora spec file for php-pecl-xpass
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-xpass
#
# SPDX-FileCopyrightText:  Copyright 2024-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global php_base         php

%bcond_without           tests

%global pie_vend         remi
%global pie_proj         xpass
%global pecl_name        xpass
%global ini_name         40-%{pecl_name}.ini
%global upstream_version 1.2.0
#global upstream_prever  RC2
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}

Summary:        Extended password extension
Name:           %{php_base}-pecl-%{pecl_name}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        2%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libxcrypt) >= 4.4
BuildRequires:  libxcrypt-devel
BuildRequires:  %{php_base}-devel >= 8.0
BuildRequires:  php-pear

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Extension
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
# PECL
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
# PIE
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

%if "%{php_base}" != "php"
Requires:       %{php_base}-common%{?_isa}
Conflicts:      php-pecl-%{pecl_name}
Provides:       php-pecl-%{pecl_name} = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
%endif

%description
This extension provides password hashing algorithms used by Linux
distributions, using extended crypt library (libxcrypt):

* sha512 provided for legacy as used on some old distributions
* yescrypt used on modern distributions
* sm3crypt
* sm3yescrypt

It also provides additional functions from libxcrypt missing in core PHP:

* crypt_preferred_method
* crypt_gensalt
* crypt_checksalt

See PHP documentation on https://www.php.net/xpass

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_XPASS_VERSION/{s/.* "//;s/".*$//;p}' php_xpass.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' extension module
extension=%{pecl_name}.so
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --enable-xpass \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build

%install
%make_install -C %{sources}

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 %{sources}/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}
# Minimal load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
# Upstream test suite
TEST_PHP_ARGS="-n -d extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}
%endif

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
