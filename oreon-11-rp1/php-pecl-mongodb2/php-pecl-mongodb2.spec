%global source0_hash fd0d34b4c530bad6dc4e0be61e23c118a3cc851ad879e088d6afca25b574916b

# Fedora spec file for php-pecl-mongodb2
# without SCL compatibility, from
#
# remirepo spec file for php-pecl-mongodb
#
# SPDX-FileCopyrightText:  Copyright 2015-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pecl_name         mongodb
%global pie_vend          mongodb
%global pie_proj          mongodb-extension
# After 40-smbclient.ini, see https://jira.mongodb.org/browse/PHPC-658
%global ini_name          50-%{pecl_name}.ini

%global upstream_version  2.1.8
#global upstream_prever   RC1
#global upstream_lower    ~rc1
%global sources           %{pecl_name}-%{upstream_version}%{?upstream_prever}

# Required versions from config.m4
%global minimal_libmongo  1.30.7
%global minimal_libcrypt  1.12.0

# Build dependencies
%global system_libmongo   1.30
%global system_libcrypt   1.12

Summary:        MongoDB driver for PHP version 2
Name:           php-pecl-%{pecl_name}2
Version:        %{upstream_version}%{?upstream_lower}
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{upstream_version}%{?upstream_prever}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  php-devel >= 8.1
BuildRequires:  php-pear
BuildRequires:  php-json
BuildRequires:  pkgconfig(libbson-1.0)    >= %{system_libmongo}
BuildRequires:  pkgconfig(libmongoc-1.0)  >= %{system_libmongo}
BuildRequires:  pkgconfig(libmongocrypt)  >= %{system_libcrypt}

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-json%{?_isa}

# Extension (php-mongodb was the pure PHP library)
Obsoletes:      php-%{pecl_name}                 < 2
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
# PECL and package rename (for new major version)
Obsoletes:      php-pecl-%{pecl_name}            < 2
Provides:       php-pecl-%{pecl_name}            = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa}    = %{version}-%{release}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
# PIE
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

%description
The purpose of this driver is to provide exceptionally thin glue between
MongoDB and PHP, implementing only fundemental and performance-critical
components necessary to build a fully-functional MongoDB driver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests and License
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

pushd %{sources}

# Check our macro values
grep CHECK_MODULES config.m4
grep -q %{minimal_libmongo} config.m4
grep -q %{minimal_libcrypt} config.m4

# temporary: lower minimal required versions
sed -e 's/%{minimal_libmongo}/%{system_libmongo}/;s/%{minimal_libcrypt}/%{system_libcrypt}/' -i config.m4

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_MONGODB_VERSION /{s/.* "//;s/".*$//;p}' phongo_version.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi

popd

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable %{summary} extension module
extension=%{pecl_name}.so

; Configuration
;mongodb.debug=''
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

# Ensure we use system library
# Need to be removed only after phpize because of m4_include
rm -r src/libmongoc*

%configure \
    --with-php-config=%{__phpconfig} \
    --with-mongodb-system-libs \
    --with-mongodb-client-side-encryption \
    --enable-mongodb

%make_build

%install
cd %{sources}

: Install the extension
%make_install

: Install config file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}
OPT="-n"

: Minimal load test for the extension
%{__php} $OPT \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
