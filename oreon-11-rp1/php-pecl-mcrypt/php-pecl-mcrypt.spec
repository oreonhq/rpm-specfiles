%global source0_hash 2a9ef0817d3bf677f6d7baf8e325629a2758974735d8abad6566384788d424a5

# Fedora spec file for php-pecl-mcrypt
# without SCL compatibility, from
#
# remirepo spec file for php-pecl-mcrypt
#
# SPDX-FileCopyrightText:  Copyright 2017-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pie_vend       pecl
%global pie_proj       mcrypt
%global pecl_name      mcrypt
%global ini_name       30-%{pecl_name}.ini
%global sources        %{pecl_name}-%{version}

Summary:      Bindings for the libmcrypt library
Name:         php-pecl-mcrypt
Version:      1.0.9
Release:      3%{?dist}
License:      PHP-3.01
URL:          https://pecl.php.net/package/mcrypt
Source0:      https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: php-devel >= 7.2
BuildRequires: libmcrypt-devel
BuildRequires: php-pear

Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}

Provides:     php-pecl(%{pecl_name}) = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}
Obsoletes:    php-%{pecl_name} < 7.2.0
Provides:     php-%{pecl_name} = 1:%{version}-%{release}
Provides:     php-%{pecl_name}%{?_isa} = 1:%{version}-%{release}
Provides:     php-pie(%{pie_vend}/%{pie_proj}) = %{version}

%description
Provides bindings for the unmaintained libmcrypt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_MCRYPT_VERSION/{s/.* "//;s/".*$//;p}' php_mcrypt.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi

cd ..
: Create the configuration file
cat >%{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
  --with-mcrypt \
  --with-php-config=%{__phpconfig}

%make_build

%install
cd %{sources}
%make_install

# Configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}
: minimal load test of the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

: upstream test suite
make test TESTS='-q --show-diff'

%files
%license %{sources}/LICENSE
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
