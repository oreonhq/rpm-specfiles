%global source0_hash 5f3885b764fe20ecf8f577c12747545ba21fef5f9af09b4c8447d39d7fd7f7c8
%bcond_without tests
%global pecl_name  geos
%global ini_name   40-%{pecl_name}.ini
%global sources    %{name}
%global _configure ../%{sources}/configure
Name:           php-%{pecl_name}
Version:        1.0.0
Release:        38%{?dist}
Summary:        PHP module for GEOS
License:        LGPL-2.1-or-later AND MIT
URL:            http://trac.osgeo.org/geos
Source0:        https://git.osgeo.org/gogs/%{pecl_name}/%{name}/archive/%{version}.tar.gz
Patch0:         0001-fix-test-for-7.3-int-vs-integer.patch
Patch1:         0002-fix-error-message-with-php-7-Wformat-warnings-raised.patch
Patch2:         0003-add-all-arginfo-and-fix-build-with-PHP-8.patch
Patch4:         0005-fix-for-8.0.0RC1.patch
Patch3:         0004-fix-all-zend_parse_parameters-call-to-use-zend_long.patch
Patch5:         0006-fix-__toString-with-8.2.patch
Patch6:         0001-Fix-incompatible-pointer-types.patch
Patch7:         0001-use-zend_ce_exception-instead-of-zend_exception_get_.patch
ExcludeArch:    %{ix86}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Obsoletes:      geos-php        <= 3.5.0
Provides:       geos-php         = 1:%{version}-%{release}
Provides:       geos-php%{?_isa} = 1:%{version}-%{release}
# oreon:deps
BuildRequires:  geos-devel
BuildRequires:  php-devel
BuildRequires:  php-pear
# /oreon:deps
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
install -Dpm 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
%oreon_autofiles main

%check

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
cd %{sources}
if pkg-config geos --atleast-version 3.12; then
rm tests/002_WKTWriter.phpt
rm tests/004_WKBWriter.phpt
rm tests/005_WKBReader.phpt
fi
if pkg-config geos --atleast-version 3.8; then
rm tests/001_Geometry.phpt
fi
%ifarch ppc64 ppc64le aarch64 armv7hl s390 s390x
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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
