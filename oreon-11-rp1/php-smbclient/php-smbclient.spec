%global source0_hash 1e6a744563aac700815e571ad98b1135a84e840d44e6ac67997494c780a9cde7

# Fedora spec file for php-smbclient
# with SCL compatibility removed, from
#
# remirepo spec file for php-smbclient
#
# SPDX-FileCopyrightText:  Copyright 2015-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pecl_name  smbclient
%global ini_name   40-%{pecl_name}.ini
# Test suite requires a Samba server and configuration file
%bcond_with        tests
%global sources    %{pecl_name}-%{version}%{?prever}

Name:           php-smbclient
Version:        1.1.2
Release:        5%{?dist}
Summary:        PHP wrapper for libsmbclient

License:        BSD-2-Clause
URL:            https://github.com/eduardok/libsmbclient-php
Source0:        https://pecl.php.net/get/%{sources}.tgz
%if %{with tests}
Source2:        %{pecl_name}-phpunit.xml
%endif

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  libsmbclient-devel > 3.6
%if %{with tests}
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires:  samba
%endif

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Renamed (and "php -m" reports both smbclient and libsmbclient)
Obsoletes:      php-libsmbclient         < 0.8.0-0.2
Provides:       php-libsmbclient         = %{version}-%{release}
Provides:       php-libsmbclient%{?_isa} = %{version}-%{release}
# PECL
Provides:       php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}

%description
%{pecl_name} is a PHP extension that uses Samba's libsmbclient
library to provide Samba related functions and 'smb' streams
to PHP programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Check extension version
ver=$(sed -n '/define PHP_SMBCLIENT_VERSION/{s/.* "//;s/".*$//;p}' php_smbclient.h)
if test "$ver" != "%{version}%{?prever}"; then
   : Error: Upstream VERSION version is ${ver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

cat  << 'EOF' | tee %{ini_name}
; Enable %{summary} extension module
extension=%{pecl_name}.so
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --with-php-config=%{__phpconfig}

%make_build

%install
cd %{sources}

: Install the extension
%make_install

: Install configuration
install -Dpm 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with tests}
: Upstream test suite for the extension
cp %{SOURCE2} phpunit.xml

%{__php} \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    %{_bindir}/phpunit --verbose
%endif

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
