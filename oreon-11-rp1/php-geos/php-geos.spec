%global source0_hash 09cd4e7a3b026f65d86320b1250d6d6ceb8d78179cbfd480f622011d52f92035

# Fedora spec file for php-geos
# Without SCL compatibility stuff, from:
#
# remirepo spec file for php-geos
#
# SPDX-FileCopyrightText:  Copyright 2016-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without tests

%global pecl_name  geos
%global ini_name   40-%{pecl_name}.ini
%global sources    %{name}
%global _configure ../%{sources}/configure

Name:           php-%{pecl_name}
Version:        1.0.0
Release:        38%{?dist}

Summary:        PHP module for GEOS

# See COPYING
License:        LGPL-2.1-or-later AND MIT
URL:            http://trac.osgeo.org/geos
Source0:        https://git.osgeo.org/gogs/geos/php-geos/archive/%{version}%{?prever}.tar.gz

# https://git.osgeo.org/gitea/geos/php-geos/issues/20
Patch0:         0001-fix-test-for-7.3-int-vs-integer.patch
Patch1:         0002-fix-error-message-with-php-7-Wformat-warnings-raised.patch
# https://git.osgeo.org/gitea/geos/php-geos/issues/24
Patch2:         0003-add-all-arginfo-and-fix-build-with-PHP-8.patch
Patch4:         0005-fix-for-8.0.0RC1.patch
# https://git.osgeo.org/gitea/geos/php-geos/issues/25
Patch3:         0004-fix-all-zend_parse_parameters-call-to-use-zend_long.patch
# https://git.osgeo.org/gitea/geos/php-geos/issues/27
Patch5:         0006-fix-__toString-with-8.2.patch
# https://git.osgeo.org/gitea/geos/php-geos/issues/32
Patch6:         0001-Fix-incompatible-pointer-types.patch
# https://git.osgeo.org/gitea/geos/php-geos/issues/35
Patch7:         0001-use-zend_ce_exception-instead-of-zend_exception_get_.patch

ExcludeArch:    %{ix86}

BuildRequires:  php-devel
BuildRequires:  php-pear
# Test failures with 3.3 (EL-6)
BuildRequires:  geos-devel >= 3.4

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Dropped from geos
Obsoletes:      geos-php        <= 3.5.0
Provides:       geos-php         = 1:%{version}-%{release}
Provides:       geos-php%{?_isa} = 1:%{version}-%{release}

%description
PHP module for GEOS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

cd %{sources}
%patch -P0 -p1 -b .test
%patch -P1 -p1 -b .wformat
%patch -P2 -p1 -b .arginfo
%patch -P3 -p1 -b .zendlong
%patch -P4 -p1 -b .arg
%patch -P5 -p1 -b .php82
%patch -P6 -p1 -b .pointers
%patch -P7 -p1 -b .php85

sed -e '/PHP_GEOS_VERSION/s/"0.0"/"%{version}%{?prever}"/' -i php_geos.h

# Check extension version
ver=$(sed -n '/define PHP_GEOS_VERSION/{s/.* "//;s/".*$//;p}' php_geos.h)
if test "$ver" != "%{version}%{?prever}%{?gh_date:-dev}"; then
   : Error: Upstream VERSION version is ${ver}, expecting %{version}%{?prever}%{?gh_date:-dev}.
   exit 1
fi
cd ..

cat  << 'EOF' | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%build
cd %{sources}
%{__phpize}

%configure --with-php-config=%{__phpconfig}
make %{?_smp_mflags}

%install
make -C %{sources} install INSTALL_ROOT=%{buildroot}

# install configuration
install -Dpm 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

%check
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
cd %{sources}
if pkg-config geos --atleast-version 3.12; then
# See https://git.osgeo.org/gitea/geos/php-geos/issues/31
# ignore failing test with geos 3.12
rm tests/002_WKTWriter.phpt
rm tests/004_WKBWriter.phpt
rm tests/005_WKBReader.phpt
fi
if pkg-config geos --atleast-version 3.8; then
# See https://git.osgeo.org/gitea/geos/php-geos/issues/23
# ignore failing test with geos 3.8
rm tests/001_Geometry.phpt
fi
%ifarch ppc64 ppc64le aarch64 armv7hl s390 s390x
# see https://git.osgeo.org/gogs/geos/php-geos/issues/17
# ignore failing tests
rm -f tests/001_Geometry.phpt
rm -f tests/005_WKBReader.phpt
%endif

: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php -q --show-diff || ret=1

exit $ret
%endif

%files
%license %{sources}/{COPYING,LGPL-2,MIT-LICENSE}
%doc %{sources}/{CREDITS,NEWS,README.md,TODO}

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
