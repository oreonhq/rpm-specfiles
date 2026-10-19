%global source0_hash 55306a84797d399c6b269181ec484634f18bea1330bbd9d7405043c597de69cd
%bcond_with              msgpack
%bcond_without           tests
%global upstream_version 3.0.0
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
%global _configure       ../%{sources}/configure
%global pie_vend         msgpack
%global pie_proj         msgpack-php
%global pecl_name        msgpack
%global ini_name         40-%{pecl_name}.ini
Summary:        API for communicating with MessagePack serialization
Name:          php-pecl-msgpack
Version:       %{upstream_version}%{?upstream_lower:~%{upstream_lower}}
Release:        6%{?dist}
Source0:        https://pecl.php.net/get/%{pie_vend}-%{version}.tgz
License:       BSD-3-Clause
URL:           https://pecl.php.net/package/msgpack
ExcludeArch:   %{ix86}
%if %{with msgpack}
%else
Provides:      bundled(msgpack) = 3.2.0
%endif
Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}
Provides:      php-%{pecl_name}                 = %{version}
Provides:      php-%{pecl_name}%{?_isa}         = %{version}
Provides:      php-pecl(%{pecl_name})           = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:      php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:      php-%{pie_vend}-%{pie_proj}      = %{version}
# oreon:deps
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  php-pecl-apcu-devel
# /oreon:deps
%description
This extension provide API for communicating with MessagePack serialization.

MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON but it's faster and smaller.
For example, small integers (like flags or error code) are encoded into a
single byte, and typical short strings only require an extra byte in addition
to the strings themselves.

If you ever wished to use JSON for convenience (storing an image with metadata)
but could not for technical reasons (encoding, size, speed...), MessagePack is
a perfect replacement.

%package devel
Summary:       MessagePack developer files (header)
Requires:      php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}
%description devel
These are the files needed to compile programs using MessagePack serializer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml

cd %{sources}
%if %{with msgpack}
# use system library
rm -rf msgpack
%endif

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_MSGPACK_VERSION/{s/.* "//;s/".*$//;p}' php_msgpack.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}%{?gh_date:-dev}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat > %{ini_name} << 'EOF'
; Enable MessagePack extension module
extension = %{pecl_name}.so

; Configuration options

;msgpack.error_display = On
;msgpack.php_only = On
;msgpack.assoc = On
;msgpack.illegal_key_insert = Off
;msgpack.use_str8_serialization = On
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure --with-php-config=%{__phpconfig}
%make_build
%install
: Install the configuration file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
: Install the package XML file
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
cd %{sources}
: Install the extension
%make_install
: Install Test and Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do [ -f tests/$i ] && install -Dpm 644 tests/$i %{buildroot}%{pecl_testdir}/%{pecl_name}/tests/$i
   [ -f $i ]       && install -Dpm 644 $i       %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd %{sources}
rm tests/034.phpt
rm tests/035.phpt
: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
: Upstream test suite
TEST_PHP_ARGS="-n -d extension=apcu.so -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}
%endif
%files -f %{oreon_filedir}/main.list
%files -n php-pecl-msgpack-devel -f %{oreon_filedir}/php-pecl-msgpack-devel.list

%changelog

%autochangelog
