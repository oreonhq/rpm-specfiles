%global source0_hash fd8d3fbf7344854feb169cf3f1e6698ed22825d35a3a5229fe320c8053306eaf

# Fedora spec file for php-zstd
# without SCL compatibility from:
#
# remirepo spec file for php-zstd
#
# SPDX-FileCopyrightText:  Copyright 2018-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pie_vend    kjdev
%global pie_proj    zstd
%global pecl_name   zstd
%global ini_name    40-%{pecl_name}.ini
%global sources     %{pecl_name}-%{version}

Summary:       Zstandard extension
Name:          php-%{pecl_name}
Version:       0.15.2
Release:       3%{?dist}
License:       MIT
URL:           https://pecl.php.net/package/%{pecl_name}
Source0:       https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 7.0
BuildRequires: php-pecl-apcu-devel
BuildRequires: php-pear
BuildRequires: pkgconfig(libzstd)

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

Provides:       php-pecl-%{pecl_name}            = %{version}
Provides:       php-pecl-%{pecl_name}%{?_isa}    = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

%description
PHP extension for compression and decompression with Zstandard library.

%package devel
Summary:       %{name} developer files (header)
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}

%description devel
These are the files needed to compile programs using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml
sed -e '\:"zstd/:d' -i package.xml

cd %{sources}
# Use the system library
rm -r zstd

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_ZSTD_VERSION/{s/.* "//;s/".*$//;p}' php_zstd.h)
if test "x${extver}" != "x%{version}%{?gh_date:-dev}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' extension module
extension = %{pecl_name}.so

; Configuration
;zstd.output_compression = Off
;zstd.output_compression_level = 3
;zstd.output_compression_dict =
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-php-config=%{__phpconfig} \
    --with-libzstd \
    --with-libdir=%{_lib} \
    --enable-zstd

%make_build

%install
cd %{sources}

: Install the extension
%make_install

: Install Configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install Test and Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}

export REPORT_EXIT_STATUS=1
%ifarch s390x
: ignore test with erratic results
rm tests/streams_*phpt
%endif

: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Check that apcu is aware of zstd serializer
%{__php} --no-php-ini \
    --define extension=apcu.so \
    --define apc.enabled=1 \
    --define apc.enable_cli=1 \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --ri apcu | grep '%{pecl_name}'

: Upstream test suite for the extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --offline --show-diff

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%files devel
%doc %{pecl_testdir}/%{pecl_name}
%{php_incldir}/ext/%{pecl_name}

%changelog
%autochangelog
