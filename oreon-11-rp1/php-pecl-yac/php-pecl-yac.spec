%global source0_hash 6225f526a2c68ebe30b528eebbcb42d2e4d42bb971ab9b13829ac47c36401494
%bcond_without      tests
%global pecl_name   yac
%global ini_name    50-%{pecl_name}.ini
%global sources     %{pecl_name}-%{version}
Summary:        Lockless user data cache
Name:           php-pecl-%{pecl_name}
Version:        2.3.1
Release:        1%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz
ExcludeArch:    %{ix86}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-igbinary%{?_isa}
Requires:       php-msgpack%{?_isa}
Obsoletes:      php-%{pecl_name} < %{version}
Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
# oreon:deps
BuildRequires:  fastlz-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  php-pecl-igbinary-devel
BuildRequires:  php-pecl-msgpack-devel
# /oreon:deps
%description
Yac (Yet Another Cache) is a shared memory user data cache for PHP.

It can be used to replace APC or local memcached.

Yac is lockless, that means, it is very fast, but there could be a
chance you will get a wrong data(depends on how many key slots are
allocated and how many keys are stored), so you'd better make sure
that your product is not very sensitive to that.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

# Don't install (register) the tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# drop bundled fastlz to ensure it is not used
sed -e '\:name="compressor/fastlz:d' -i ../package.xml
rm -r compressor/fastlz

# Check version as upstream often forget to update this
extver=$(sed -n '/#define PHP_YAC_VERSION/{s/.* "//;s/".*$//;p}' php_yac.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream YAC version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat > %{ini_name} << 'EOF'
; Enable Yet Another Cache extension module
extension = %{pecl_name}.so

;yac.enable=1
;yac.enable_cli=0
;yac.debug=0
;yac.keys_memory_size=4M
;yac.values_memory_size=64M
;yac.compress_threshold=-1
;yac.serializer=php
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure \
    --enable-json \
    --enable-msgpack \
    --enable-igbinary \
    --with-system-fastlz \
    --with-php-config=%{__phpconfig}
%make_build
%install
cd %{sources}
: Install the extension
%make_install
: Install the configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
: Install Test and Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

cd %{sources}
OPTS="-n"
[ -f %{php_extdir}/igbinary.so ] && OPTS="$OPTS -d extension=igbinary.so"
[ -f %{php_extdir}/msgpack.so  ] && OPTS="$OPTS -d extension=msgpack.so"
: Minimal load test for the extension
%{__php} $OPTS  \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
: Upstream test suite for the extension
TEST_PHP_ARGS="$OPTS -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%else
: Upstream test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
