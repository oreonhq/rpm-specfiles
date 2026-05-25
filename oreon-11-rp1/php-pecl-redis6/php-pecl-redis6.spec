# RHEL/Fedora spec file for php-pecl-redis6
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-redis6
#
# SPDX-FileCopyrightText:  Copyright 2012-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global php_base     php

%bcond_without       tests
%if 0%{?fedora} || 0%{?oreon}
# optional compressors/serializers enabled by default
%bcond_without       igbinary
%bcond_without       msgpack
%bcond_without       liblzf
%else
# optional compressors/serializers disabled by default
%bcond_with          igbinary
%bcond_with          msgpack
%bcond_with          liblzf
%endif
%bcond_without       valkey

%global pie_vend     phpredis
%global pie_proj     phpredis
%global pecl_name    redis
# after 40-igbinary and 40-msgpack
%global ini_name     50-%{pecl_name}.ini

%global upstream_version 6.3.0
#global upstream_prever  RC2
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}

Summary:       PHP extension for interfacing with key-value stores
Name:          %{php_base}-pecl-redis6
Version:       %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:       2%{?dist}
License:       PHP-3.01
URL:           https://pecl.php.net/package/redis
Source0:       https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: %{php_base}-devel >= 8.0
BuildRequires: php-pear
%if %{with igbinary}
BuildRequires: %{php_base}-pecl-igbinary-devel
%endif
%if %{with msgpack}
BuildRequires: %{php_base}-pecl-msgpack-devel >= 2.0.3
%endif
%if %{with liblzf}
BuildRequires: pkgconfig(liblzf)
%endif
BuildRequires: pkgconfig(libzstd) >= 1.3.0
BuildRequires: pkgconfig(liblz4)
# to run Test suite
%if %{with tests}
%if %{with valkey}
BuildRequires: valkey
%else
BuildRequires: redis
%endif
%endif

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}
%if %{with igbinary}
Requires:      %{php_base}-pecl-igbinary%{?_isa}
%endif
%if %{with msgpack}
Requires:      %{php_base}-pecl-msgpack%{?_isa}
%endif

Provides:      php-%{pecl_name}                 = %{version}
Provides:      php-%{pecl_name}%{?_isa}         = %{version}
Provides:      php-pecl(%{pecl_name})           = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:      php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:      php-%{pie_vend}-%{pie_proj}      = %{version}

%if "%{php_base}" != "php"
Requires:      %{php_base}-common%{?_isa}
Conflicts:     php-pecl-%{pecl_name}6
Provides:      php-pecl-%{pecl_name}6 = %{version}-%{release}
Provides:      php-pecl-%{pecl_name}6%{?_isa} = %{version}-%{release}
Provides:      php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:      php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}

%elif 0%{?fedora} >= 42 || 0%{?rhel} >= 10 || "%{php_version}" > "8.4"
Obsoletes:     php-pecl-%{pecl_name}          < 6
Provides:      php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:      php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}
Obsoletes:     php-pecl-%{pecl_name}4         < 6
Provides:      php-pecl-%{pecl_name}4         = %{version}-%{release}
Provides:      php-pecl-%{pecl_name}4%{?_isa} = %{version}-%{release}
Obsoletes:     php-pecl-%{pecl_name}5         < 6
Provides:      php-pecl-%{pecl_name}5         = %{version}-%{release}
Provides:      php-pecl-%{pecl_name}5%{?_isa} = %{version}-%{release}

%else
# A single version can be installed
Conflicts:     php-pecl-%{pecl_name}  < 6
Conflicts:     php-pecl-%{pecl_name}4 < 6
Conflicts:     php-pecl-%{pecl_name}5 < 6
%endif


%description
This extension provides an API for communicating with RESP-based key-value
stores, such as Redis, Valkey, and KeyDB.

This client implements most of the latest API.
As method only works when also implemented on the server side,
some doesn't work with an old server version.


%prep
%setup -q -c

# Don't install/register tests, license, and bundled library
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -e '/liblzf/d' \
    -i package.xml

cd %{sources}
# Use system library
rm -r liblzf

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_REDIS_VERSION/{s/.* "//;s/".*$//;p}' php_redis.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension = %{pecl_name}.so

; phpredis can be used to store PHP sessions. 
; To do this, uncomment and configure below

; RPM note : save_handler and save_path are defined
; for mod_php, in /etc/httpd/conf.d/php.conf
; for php-fpm, in %{_sysconfdir}/php-fpm.d/*conf

;session.save_handler = %{pecl_name}
;session.save_path = "tcp://host1:6379?weight=1, tcp://host2:6379?weight=2&timeout=2.5, tcp://host3:6379?weight=2"

; Configuration
;redis.arrays.algorithm = ''
;redis.arrays.auth = ''
;redis.arrays.autorehash = 0
;redis.arrays.connecttimeout = 0
;redis.arrays.consistent = 0
;redis.arrays.distributor = ''
;redis.arrays.functions = ''
;redis.arrays.hosts = ''
;redis.arrays.index = 0
;redis.arrays.lazyconnect = 0
;redis.arrays.names = ''
;redis.arrays.pconnect = 0
;redis.arrays.previous = ''
;redis.arrays.readtimeout = 0
;redis.arrays.retryinterval = 0
;redis.clusters.auth = 0
;redis.clusters.cache_slots = 0
;redis.clusters.persistent = 0
;redis.clusters.read_timeout = 0
;redis.clusters.seeds = ''
;redis.clusters.timeout = 0
;redis.pconnect.pooling_enabled = 1
;redis.pconnect.connection_limit = 0
;redis.pconnect.echo_check_liveness = 1
;redis.pconnect.pool_detect_dirty = 0
;redis.pconnect.pool_poll_timeout = 0
;redis.pconnect.pool_pattern => ''
;redis.session.locking_enabled = 0
;redis.session.lock_expire = 0
;redis.session.lock_retries = 100
;redis.session.lock_wait_time = 20000
;redis.session.early_refresh = 0
;redis.session.compression = none
;redis.session.compression_level = 3
EOF


%build
peclconf() {
%configure \
    --enable-redis \
    --enable-redis-session \
%if %{with igbinary}
    --enable-redis-igbinary \
%endif
%if %{with msgpack}
    --enable-redis-msgpack \
%endif
%if %{with liblzf}
    --enable-redis-lzf \
    --with-liblzf \
%else
    --disable-redis-lzf \
%endif
    --enable-redis-zstd \
    --with-libzstd \
    --enable-redis-lz4 \
    --with-liblz4 \
    --with-php-config=$1
}

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

peclconf %{__phpconfig}
%make_build


%install
# Install the configuration file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install the package XML file
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

cd %{sources}
%make_install

# Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
# simple module load test
DEPS="--no-php-ini"
for i in igbinary msgpack
do  [ -f %{php_extdir}/${i}.so ] && DEPS="$DEPS --define extension=${i}.so"
done

%{__php} $DEPS \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
cd %{sources}/tests
: Ignore ONLINE test
sed -e 's/testConnectException/skipConnectException/' -i RedisTest.php

: Launch redis server
%if %{with valkey}
SRV=%{_bindir}/valkey-server
CLI=%{_bindir}/valkey-cli
%else
SRV=%{_bindir}/redis-server
CLI=%{_bindir}/redis-cli
%endif

mkdir -p data
pidfile=$PWD/server.pid
port=$(%{__php} -r 'echo 9000 + PHP_MAJOR_VERSION*100 + PHP_MINOR_VERSION*10 + PHP_INT_SIZE;')
$SRV   \
    --bind      127.0.0.1      \
    --port      $port          \
    --daemonize yes            \
    --logfile   $PWD/server.log \
    --dir       $PWD/data      \
    --pidfile   $pidfile


: Run the test Suite
sed -e "s/6379/$port/" -i *.php

ret=0
export TEST_PHP_EXECUTABLE=%{__php}
export TEST_PHP_ARGS="$DEPS \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so"
$TEST_PHP_EXECUTABLE $TEST_PHP_ARGS TestRedis.php || ret=1

: Cleanup
if [ -f $pidfile ]; then
   $CLI -p $port shutdown nosave
   sleep 2
fi
cat $PWD/server.log

exit $ret
%else
: Upstream test suite disabled
%endif

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%{php_extdir}/%{pecl_name}.so
%config(noreplace) %{php_inidir}/%{ini_name}


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.3.0-2
- Import
