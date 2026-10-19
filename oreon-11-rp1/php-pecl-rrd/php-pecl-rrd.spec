%global source0_hash a42161e58cdc8a853b72cff298989dcbde82b0f76456dd59ce02854c92b730f7
%global php_base   php
%global pecl_name  rrd
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}
%global _configure ../%{sources}/configure
Summary:        PHP Bindings for rrdtool
Name:         %{php_base}-pecl-rrd
Version:      2.0.3
Release:        21%{?dist}
License:      BSD-2-Clause
URL:          https://pecl.php.net/package/rrd
Source0:        https://pecl.%{php_base}.net/get/%{sources}.tgz
Patch0:       %{pecl_name}-build.patch
Patch1:       %{pecl_name}-php85.patch
ExcludeArch:   %{ix86}
Requires:     php(zend-abi)
Requires:     php(api)
Conflicts:    rrdtool-php
Provides:     php-pecl(%{pecl_name})         = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:     php-%{pecl_name}               = %{version}%{?pre}
Provides:     php-%{pecl_name}%{?_isa}       = %{version}%{?pre}
%if "%{php_base}" != "php"
Requires:     %{php_base}-common%{?_isa}
Conflicts:    php-pecl-%{pecl_name}
Provides:     php-pecl-%{pecl_name} = %{version}-%{release}
Provides:     php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  pkgconfig(librrd)
BuildRequires:  rrdtool
# /oreon:deps
%description
Procedural and simple OO wrapper for rrdtool - data logging and graphing
system for time series data.

%prep 

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -c -q

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
%patch -P0 -p1
%patch -P1 -p1

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_RRD_VERSION/{s/.* "//;s/".*$//;p}' php_rrd.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%build

export CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
cd %{sources}
%{__phpize}
%configure --with-php-config=%{__phpconfig}
make %{?_smp_mflags}
%install
make install -C %{sources} INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 %{sources}/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%ifnarch %{arm} s390x
cd %{sources}
if pkg-config librrd --atleast-version=1.5.0
then
  : ignore test failed with rrdtool > 1.5
  rm tests/rrd_{016,017}.phpt
fi
if ! pkg-config librrd --atleast-version=1.4.0
then
  : ignore test failed with rrdtool < 1.4
  rm tests/rrd_{012,017}.phpt
fi
make -C tests/data clean
make -C tests/data all
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php -q --show-diff
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.3-21
- Import
