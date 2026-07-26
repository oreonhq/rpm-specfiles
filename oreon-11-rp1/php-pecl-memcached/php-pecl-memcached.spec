%global source0_hash c163434eb0da97c8f45c7ad41d979d381f8b81c49402b1b90b063987fb37972e

# Fedora spec file for php-pecl-memcached
#
# SPDX-FileCopyrightText:  Copyright 2009-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without      tests

%global pie_vend    php-memcached
%global pie_proj    php-memcached
%global pecl_name   memcached
# After 40-igbinary, 40-json, 40-msgpack
%global ini_name    50-%{pecl_name}.ini

%global upstream_version 3.4.0
#global upstream_prever  RC1
# upstream use    dev => alpha => beta => RC
# make RPM happy  DEV => alpha => beta => rc
#global upstream_lower   rc1
%global sources    %{pecl_name}-%{upstream_version}%{?upstream_prever}

Summary:      Extension to work with the Memcached caching daemon
Name:         php-pecl-memcached
Version:      %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:      2%{?dist}
License:      PHP-3.01
URL:          https://pecl.php.net/package/%{pecl_name}

Source0:      https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 7
BuildRequires: php-pear
BuildRequires: php-json
BuildRequires: php-pecl-igbinary-devel
%ifnarch ppc64
BuildRequires: php-pecl-msgpack-devel
%endif
BuildRequires: libevent-devel  > 2
BuildRequires: libmemcached-devel >= 1.0.18
BuildRequires: zlib-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: fastlz-devel
BuildRequires: libzstd-devel
%if %{with tests}
BuildRequires: memcached
%endif

Requires:     php-json%{?_isa}
Requires:     php-igbinary%{?_isa}
Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}
%ifnarch ppc64
Requires:     php-msgpack%{?_isa}
%endif

Provides:     php-%{pecl_name}                 = %{version}
Provides:     php-%{pecl_name}%{?_isa}         = %{version}
Provides:     php-pecl(%{pecl_name})           = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:     php-pie(%{pie_vend}/%{pie_proj}) = %{version}

%description
This extension uses libmemcached library to provide API for communicating
with memcached servers.

memcached is a high-performance, distributed memory object caching system,
generic in nature, but intended for use in speeding up dynamic web 
applications by alleviating database load.

It also provides a session handler (memcached). 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q
# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -e '/name=.fastlz/d' \
    -i package.xml

cd %{sources}
rm -r fastlz

# Chech version as upstream often forget to update this
extver=$(sed -n '/#define PHP_MEMCACHED_VERSION/{s/.* "//;s/".*$//;p}' php_memcached.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever:%{upstream_prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever:%{upstream_prever}}.
   : Update the macro and rebuild.
   exit 1
fi
cd ..

cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; ----- Options to use the memcached session handler

; RPM note : save_handler and save_path are defined
; for mod_php, in /etc/httpd/conf.d/php.conf
; for php-fpm, in /etc/php-fpm.d/*conf

;  Use memcache as a session handler
;session.save_handler=memcached
;  Defines a comma separated list of server urls to use for session storage
;session.save_path="localhost:11211"

; ----- Configuration options
; http://php.net/manual/en/memcached.configuration.php

EOF

# default options with description from upstream
cat %{sources}/memcached.ini >>%{ini_name}

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --enable-memcached-igbinary \
           --enable-memcached-json \
           --enable-memcached-sasl \
%ifnarch ppc64
           --enable-memcached-msgpack \
%endif
           --enable-memcached-protocol \
           --with-system-fastlz \
           --with-zstd \
           --with-php-config=%{__phpconfig}

%make_build

%install
cd %{sources}

: Install the extension
%make_install

: Drop in the bit of configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
OPT="-n"
[ -f %{php_extdir}/igbinary.so ] && OPT="$OPT -d extension=igbinary.so"
[ -f %{php_extdir}/json.so ]     && OPT="$OPT -d extension=json.so"
[ -f %{php_extdir}/msgpack.so ]  && OPT="$OPT -d extension=msgpack.so"

: Minimal load test for NTS extension
%{__php} $OPT \
    -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
cd %{sources}
# XFAIL and very slow so no value
rm tests/expire.phpt
rm tests/flush_buffers.phpt
rm tests/touch_binary.phpt

ret=0

: Launch the Memcached service
port=$(%{__php} -r 'echo 10000 + PHP_MAJOR_VERSION*100 + PHP_MINOR_VERSION*10 + PHP_INT_SIZE;')
memcached -p $port -U $port      -d -P $PWD/memcached.pid
sed -e "s/11211/$port/" -i tests/*

: Port for MemcachedServer
port=$(%{__php} -r 'echo 11000 + PHP_MAJOR_VERSION*100 + PHP_MINOR_VERSION*10 + PHP_INT_SIZE;')
sed -e "s/3434/$port/" -i tests/*

: Run the upstream test Suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="$OPT -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php -q -x --show-diff || ret=1

# Cleanup
if [ -f memcached.pid ]; then
   kill $(cat memcached.pid)
   sleep 1
fi

exit $ret
%endif

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
