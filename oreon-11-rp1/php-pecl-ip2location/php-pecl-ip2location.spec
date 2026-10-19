%global source0_hash 4ef4260cf13319911952f202a2a06fd75f9c3e09c6fe9cc0f975715fb2c2ddcc
%global pecl_name  ip2location
%global pie_vend   ip2location
%global pie_proj   ip2location-pie
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{upstream_version}%{?upstream_prever}
%global upstream_version 8.3.0
%global libversion       8.7
Summary:        Get geo location information of an IP address
Name:           php-pecl-%{pecl_name}
License:        PHP-3.01
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{upstream_version}.tgz
Patch0:         https://patch-diff.githubusercontent.com/raw/chrislim2888/IP2Location-PECL-Extension/pull/25.patch
ExcludeArch:    %{ix86}
Requires:       IP2Location-libs%{?_isa} >= %{libversion}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}
# oreon:deps
BuildRequires:  IP2Location-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
# /oreon:deps
%description
This PHP extension enables you to get the geo location information of
an IP address, such as country, region or state, city, latitude and
longitude, US ZIP code, time zone, Internet Service Provider (ISP) or
company name, domain name, net speed, area code, weather station code,
weather station name, mobile country code (MCC), mobile network code
(MNC) and carrier brand, elevation, and usage type.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -e '/README.TXT/s/role="doc"/role="test"/' \
    -i package.xml

cd %{sources}
%patch -P0 -p1 -b .pr25

sed -e "s/\r//" -i LICENSE CREDITS *.md *.c *.h

# Check version
extver=$(sed -n '/#define PHP_IP2LOCATION_VERSION/{s/.* "//;s/".*$//;p}' php_ip2location.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

cat <<EOF | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure --with-php-config=%{__phpconfig}
%make_build
%install
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
cd %{sources}
%make_install
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

: simple module load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
: upstream test suite
cd %{sources}
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
