%global source0_hash 510b3caf454ddcbd21234ccc0703829d4973fa7e4818cb32189a8c06d9e64d22

# Fedora spec file for php-pecl-zip
#
# SPDX-FileCopyrightText:  Copyright 2013-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global php_base         php

%global pecl_name        zip
%global pie_vend         pecl
%global pie_proj         zip
%global ini_name         40-%{pecl_name}.ini
%global upstream_version 1.22.8
#global upstream_prever  RC6

# Github forge
%global gh_vend     pierrejoye
%global gh_proj     php_zip
%global forgeurl    https://github.com/%{gh_vend}/%{gh_proj}
%global tag         %{upstream_version}%{?upstream_prever}

Summary:      A ZIP archive management extension
Name:         %{php_base}-pecl-zip
License:      PHP-3.01
Version:      %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:      3%{?dist}
%forgemeta
URL:          %{forgeurl}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: %{php_base}-devel
BuildRequires: pkgconfig(libzip) >= 1.0.0
BuildRequires: zlib-devel

Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}

# Extension
Provides:     php-%{pecl_name} = %{version}-%{release}
Provides:     php-%{pecl_name}%{?_isa} = %{version}-%{release}
# PECL
Provides:     php-pecl(%{pecl_name}) = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}
# PIE
Provides:     php-pie(%{pie_vend}/%{pie_proj}) = %{version}

%if "%{php_base}" != "php"
Requires:     %{php_base}-common%{?_isa}
Conflicts:    php-pecl-%{pecl_name}
Provides:     php-pecl-%{pecl_name} = %{version}-%{release}
Provides:     php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
%endif


%description
Zip is an extension to create and read zip files.


%prep 
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%forgesetup

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_ZIP_VERSION/{s/.* "//;s/".*$//;p}' php8/php_zip.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi

: Create the configuration file
cat >%{ini_name} << 'EOF'
; Enable ZIP extension module
extension=%{pecl_name}.so
EOF


%build
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
  --with-libzip \
  --with-libdir=%{_lib} \
  --with-php-config=%{__phpconfig}

%make_build


%install
: Install the configuration file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the extension
%make_install


%check
: minimal load test of the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

: upstream test suite
TEST_PHP_ARGS="-n -d extension=$PWD/modules/%{pecl_name}.so" \
TEST_PHP_EXECUTABLE=%{__php} \
%{__php} -n run-tests.php -q --show-diff


%files
%license LICENSE
%doc composer.json
%doc CREDITS
%doc examples

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{upstream_version}%{?upstream_prever:~%{upstream_prever}}-3
- Prepare for Oreon 11 (RP1)
