%global source0_hash 65ce03491782f9d9d5e9bc70bfe684255e5afa8486a2960c7a7cab033882a282

# Fedora spec file for php-pecl-xmlrpc
# Without SCL compatibility, from
#
# remirepo spec file for php-pecl-xmlrpc
#
# SPDX-FileCopyrightText:  Copyright 2020-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without      tests

%global pecl_name   xmlrpc
%global upver       1.0.0
%global rcver       RC3
%global rclower     rc3
# After 20-xml
%global ini_name    30-%{pecl_name}.ini
%global sources     %{pecl_name}-%{upver}%{?rcver}

Summary:        Functions to write XML-RPC servers and clients
Name:           php-pecl-%{pecl_name}
Version:        %{upver}%{?rclower:~%{rclower}}
Release:        17%{?dist}

# Extension is PHP
# Library is MIT
License:        PHP-3.01 AND MIT
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

Patch0:         %{pecl_name}-tests.patch

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 8.0
BuildRequires:  php-pear
BuildRequires:  php-xml

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-xml%{?_isa}

# Set epoch so 1:1.0 > 0:8.0
Obsoletes:      php-%{pecl_name}               < 8.0.0
Provides:       php-%{pecl_name}               = 1:%{version}
Provides:       php-%{pecl_name}%{?_isa}       = 1:%{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}

%description
This extension provides functions to write XML-RPC servers and clients.

You can find more information about XML-RPC at http://www.xmlrpc.com/,
and more documentation on this extension and its functions at
https://www.php.net/xmlrpc.

The extension is unbundled from php-src as of PHP 8.0.0, because the underlying
libxmlrpc has obviously been abandoned. It is recommended to reevaluate using
this extension.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

sed -e 's/role="test"/role="src"/' \
    -e '/COPYING/s/role="doc"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
%patch -P0 -p1 -b .up

# Check version as upstream often forget to update this
extver=$(sed -n '/#define PHP_XMLRPC_VERSION/{s/.* "//;s/".*$//;p}' php_xmlrpc.h)
if test "x${extver}" != "x%{upver}%{?rcver}%{?gh_date:-dev}"; then
   : Error: Upstream RECODE version is ${extver}, expecting %{upver}%{?rcver}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable "%{pecl_name}" extension module
extension=%{pecl_name}
EOF

%build
peclconf() {
%configure \
    --with-xmlrpc \
    --with-php-config=$1
}

cd %{sources}
%{__phpize}

peclconf %{__phpconfig}
make %{?_smp_mflags}

%install
# Install the extension
make -C %{sources} install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Test & Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 %{sources}/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}

: Minimal load test
%{__php} --no-php-ini \
    --define extension=xml \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Run upstream test suite
TEST_PHP_ARGS="-n -d extension=xml -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif

%files
%license %{sources}/LICENSE
%license %{sources}/libxmlrpc/COPYING
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
