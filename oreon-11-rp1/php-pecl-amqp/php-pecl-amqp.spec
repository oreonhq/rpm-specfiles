%global source0_hash 5ae624bd785e299523f6132c204bd562cc73066dd33a10a12aa96389f55a4de7

# Fedora spec file for php-pecl-amqp
#
# SPDX-FileCopyrightText:  Copyright 2012-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_with         tests

%global pie_vend         php-amqp
%global pie_proj         php-amqp
%global pecl_name        amqp
%global ini_name         40-%{pecl_name}.ini

%global upstream_version 2.2.0
#global upstream_prever  RC1
#global upstream_lower   rc1
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
%global _configure       ../%{sources}/configure

Summary:       Communicate with any AMQP compliant server
Name:          php-pecl-amqp
Version:       %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:       2%{?dist}
License:       PHP-3.01
URL:           https://pecl.php.net/package/amqp
Source0:       https://pecl.php.net/get/%{pecl_name}-%{upstream_version}%{?upstream_prever}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 7.4
BuildRequires: php-pear
BuildRequires: pkgconfig(librabbitmq) >= 0.8.0
%if %{with tests}
BuildRequires: rabbitmq-server
BuildRequires: hostname
%endif

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

Provides:      php-%{pecl_name}                 = %{version}
Provides:      php-%{pecl_name}%{?_isa}         = %{version}
Provides:      php-pecl(%{pecl_name})           = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:      php-pie(%{pie_vend}/%{pie_proj}) = %{version}

%description
This extension can communicate with any AMQP spec 0-9-1 compatible server,
such as RabbitMQ, OpenAMQP and Qpid, giving you the ability to create and
delete exchanges and queues, as well as publish to any exchange and consume
from any queue.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Upstream often forget to change this
extver=$(sed -n '/#define PHP_AMQP_VERSION /{s/.* "//;s/".*$//;p}' php_amqp_version.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension = %{pecl_name}.so

; Whether calls to AMQPQueue::get() and AMQPQueue::consume()
; should require that the client explicitly acknowledge messages.
; Setting this value to 1 will pass in the AMQP_AUTOACK flag to
; the above method calls if the flags field is omitted.
;amqp.auto_ack = 0

; The host to which to connect.
;amqp.host = localhost

; The login to use while connecting to the broker.
;amqp.login = guest

; The password to use while connecting to the broker.
;amqp.password = guest

; The port on which to connect.
;amqp.port = 5672

; The number of messages to prefect from the server during a
; call to AMQPQueue::get() or AMQPQueue::consume() during which
; the AMQP_AUTOACK flag is not set.
;amqp.prefetch_count = 3
;amqp.prefetch_size = 0
;amqp.global_prefetch_count =0
;amqp.global_prefetch_size =0

; The virtual host on the broker to which to connect.
;amqp.vhost = /

; Timeout
;amqp.timeout =
;amqp.read_timeout = 0
;amqp.write_timeout = 0
;amqp.connect_timeout = 0
;amqp.rpc_timeout = 0

;amqp.channel_max = 256
;amqp.frame_max = 131072
;amqp.heartbeat = 0

;amqp.cacert = ''
;amqp.cert = ''
;amqp.key = ''
;amqp.verify = 1
;amqp.sasl_method = 'AMQP_SASL_METHOD_PLAIN'
;amqp.serialization_depth = 128
;amqp.deserialization_depth = 128
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
install -Dpm 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -Dpm 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{sources}/modules/%{pecl_name}.so \
    -m | grep '^%{pecl_name}$'

%if %{with tests}
mkdir log run base
: Launch the RabbitMQ service
export LANG=C.UTF-8
export RABBITMQ_PID_FILE=$PWD/run/pid
export RABBITMQ_LOG_BASE=$PWD/log
export RABBITMQ_MNESIA_BASE=$PWD/base
export PHP_AMQP_HOST=localhost
/usr/lib/rabbitmq/bin/rabbitmq-server &>log/output &
/usr/lib/rabbitmq/bin/rabbitmqctl wait $RABBITMQ_PID_FILE

ret=0
pushd %{sources}
: Run the upstream test Suite for the extension
TEST_PHP_ARGS="-n -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff || ret=1
popd

: Cleanup
if [ -s $RABBITMQ_PID_FILE ]; then
   kill $(cat $RABBITMQ_PID_FILE)
fi
rm -rf log run base

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
