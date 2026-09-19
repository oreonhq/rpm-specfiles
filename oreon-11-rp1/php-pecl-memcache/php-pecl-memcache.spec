%global source0_hash b3f0640eacdeb9046c6c86a1546d7fb8a4e9f219e5d9a36a287e59b2dd8208e5

# Fedora spec file for php-pecl-memcache
#
# SPDX-FileCopyrightText:  Copyright 2007-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without     tests

%global pecl_name  memcache
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Summary:      Extension to work with the Memcached caching daemon
Name:         php-pecl-memcache
Version:      8.2
Release:      13%{?dist}
Source0:      https://pecl.php.net/get/%{sources}.tgz
License:      PHP-3.01
Group:        Development/Languages
URL:          https://pecl.php.net/package/%{pecl_name}

Patch0:       118.patch
Patch1:       120.patch

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 8.0
BuildRequires: php-pear
BuildRequires: zlib-devel
%if %{with tests}
BuildRequires: memcached
%endif

Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}

Provides:     php-pecl(%{pecl_name}) = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:     php-%{pecl_name} = %{version}
Provides:     php-%{pecl_name}%{?_isa} = %{version}

%description
Memcached is a caching daemon designed especially for
dynamic web applications to decrease database load by
storing objects in memory.

This extension allows you to work with memcached through
handy OO and procedural interfaces.

Memcache can be used as a PHP session handler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

pushd %{sources}
%patch -P0 -p1 -b .pr118
%patch -P1 -p1 -b .pr120

extver=$(sed -n '/#define PHP_MEMCACHE_VERSION/{s/.* "//;s/".*$//;p}' src/php_memcache.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream version is now ${extver}, expecting %{version}%{?prever:-%{prever}}
   : Update the pdover macro and rebuild.
   exit 1
fi
popd

cat >%{ini_name} << 'EOF'
; ----- Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; ----- Options for the %{pecl_name} module
; see http://www.php.net/manual/en/memcache.ini.php

;  Whether to transparently failover to other servers on errors
;memcache.allow_failover=1
;  Data will be transferred in chunks of this size
;memcache.chunk_size=32768
;  Autocompress large data
;memcache.compress_threshold=20000
;  The default TCP port number to use when connecting to the memcached server 
;memcache.default_port=11211
;  Hash function {crc32, fnv}
;memcache.hash_function=crc32
;  Hash strategy {standard, consistent}
;memcache.hash_strategy=consistent
;  Defines how many servers to try when setting and getting data.
;memcache.max_failover_attempts=20
;  The protocol {ascii, binary} : You need a memcached >= 1.3.0 to use the binary protocol
;  The binary protocol results in less traffic and is more efficient
;memcache.protocol=ascii
;  Redundancy : When enabled the client sends requests to N servers in parallel
;memcache.redundancy=1
;memcache.session_redundancy=2
;  Lock Timeout
;memcache.lock_timeout = 15

;memcache.prefix_host_key = Off
;memcache.prefix_host_key_remove_www = On
;memcache.prefix_host_key_remove_subdomain = Off
;memcache.prefix_static_key = ''

; ----- Options to use the memcache session handler

; RPM note : save_handler and save_path are defined
; for mod_php, in /etc/httpd/conf.d/php.conf
; for php-fpm, in /etc/php-fpm.d/*conf

;  Use memcache as a session handler
;session.save_handler=memcache
;  Defines a comma separated of server urls to use for session storage
;  Only used when memcache.session_save_path is not set
;session.save_path="tcp://localhost:11211?persistent=1&weight=1&timeout=1&retry_interval=15"
;memcache.session_prefix_host_key = Off
;memcache.session_prefix_host_key_remove_www = On
;memcache.session_prefix_host_key_remove_subdomain = Off
;memcache.session_prefix_static_key = ''
;memcache.session_save_path = ''
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

: Drop in the bit of configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -Dpm 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep '<file .* role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    -m | grep %{pecl_name}

%if %{with tests}
cd %{sources}
: ignore test with erratic results
rm tests/040.phpt
rm tests/056.phpt
rm tests/100c.phpt

: Configuration for tests
sed -e "s:/var/run/memcached/memcached.sock:$PWD/memcached.sock:" \
    -i tests/connect.inc

: Launch the daemons
memcached -p 11211 -U 11211      -d -P $PWD/memcached1.pid
memcached -p 11212 -U 11212      -d -P $PWD/memcached2.pid
memcached -s $PWD/memcached.sock -d -P $PWD/memcached3.pid

: Upstream test suite for the extension
ret=0
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension_dir=$PWD/modules -d extension=%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php --show-diff || ret=1

: Cleanup
if [ -f memcached2.pid ]; then
   kill $(cat memcached?.pid)
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
