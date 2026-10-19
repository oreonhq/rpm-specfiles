%global source0_hash e3d60c83405268c422f95feec740455a1cc4b911d00bd8424d5d1272bc509b1a
%global source5_hash 0acb39e92d947e30175de0969a5b2e479e2983bc3e3d69c835ee5174610e9636
%define rsyslog_statedir %{_sharedstatedir}/rsyslog
%define rsyslog_pkidir %{_sysconfdir}/pki/rsyslog
%define rsyslog_docdir %{_docdir}/rsyslog
%define qpid_proton_v 0.40.0
%bcond_without hiredis
%bcond_without libdbi
%bcond_without mongodb
%bcond_without rabbitmq
%bcond_without impstats_push
%bcond_without clickhouse
%bcond_without imdocker
%bcond_without improg
%bcond_without gnutls
%bcond_without openssl
%bcond_without gssapi
%bcond_without omamqp1
%bcond_without rdkafka
%bcond_without relp
%bcond_without mysql
%bcond_without pgsql
%bcond_without snmp
%bcond_without udpspoof
%bcond_without mmtaghostname
Summary:        Enhanced system logging and kernel message trapping daemon
Name: rsyslog
Version: 8.2608.0
Release:        1%{?dist}
License: GPL-3.0-or-later AND Apache-2.0
URL: http://www.rsyslog.com/
Source0:        http://www.rsyslog.com/files/download/rsyslog/%{name}-%{version}.tar.gz
Source1: rsyslog.conf
Source2: rsyslog.sysconfig
Source3: rsyslog.log
Source4: rsyslog.service
Source5:        https://archive.apache.org/dist/qpid/proton/0.40.0/qpid-proton-0.40.0.tar.gz
%if %{with impstats_push}
%endif
Recommends: logrotate
Obsoletes: rsyslog-logrotate < 8.2310.0-2
Provides: rsyslog-logrotate = %{version}-%{release}
Requires: bash >= 2.0
%{?systemd_ordering}
Provides: syslog
Obsoletes: sysklogd < 1.5-11
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dos2unix
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  hiredis-devel
BuildRequires:  krb5-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdbi-devel
BuildRequires:  libestr-devel
BuildRequires:  libfastjson-devel
BuildRequires:  liblognorm-devel
BuildRequires:  libnet-devel
BuildRequires:  libpq-devel
BuildRequires:  librabbitmq-devel
BuildRequires:  librdkafka-devel
BuildRequires:  librelp-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mongo-c-driver-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c-compiler
BuildRequires:  protobuf-c-devel
BuildRequires:  python3
BuildRequires:  python3-docutils
BuildRequires:  snappy-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%package crypto
Summary: Encryption support
Requires: %name = %version-%release
%package doc
Summary: HTML documentation for rsyslog
BuildArch: noarch
%package elasticsearch
Summary: ElasticSearch output module for rsyslog
Requires: %name = %version-%release
BuildRequires: libcurl-devel
%package mmjsonparse
Summary: JSON enhanced logging support
Requires: %name = %version-%release
%package mmnormalize
Summary: Log normalization support for rsyslog
Requires: %name = %version-%release
BuildRequires: libestr-devel liblognorm-devel >= 1.0.2
%package mmaudit
Summary: Message modification module supporting Linux audit format
Requires: %name = %version-%release
%package mmfields
Summary: Fields extraction module
Requires: %name = %version-%release
%if %{with mmtaghostname}
%package mmtaghostname
Summary: Message modification module supporting adding tags
Requires: %name = %version-%release
%endif
%if %{with snmp}
%package mmsnmptrapd
Summary: Message modification module for snmptrapd generated messages
Requires: %name = %version-%release
%endif
%if %{with mysql}
%package mysql
Summary: MySQL support for rsyslog
Requires: %name = %version-%release
BuildRequires: mariadb-connector-c-devel
%endif
%if %{with pgsql}
%package pgsql
Summary: PostgresSQL support for rsyslog
Requires: %name = %version-%release
BuildRequires: libpq-devel
%endif
%if %{with gssapi}
%package gssapi
Summary: GSSAPI authentication and encryption support for rsyslog
Requires: %name = %version-%release
BuildRequires: krb5-devel
%endif
%if %{with relp}
%package relp
Summary: RELP protocol support for rsyslog
Requires: %name = %version-%release
BuildRequires: librelp-devel >= 1.2.16
%endif
%if %{with gnutls}
%package gnutls
Summary: TLS protocol support for rsyslog via GnuTLS library
Requires: %name = %version-%release
BuildRequires: gnutls-devel
%endif
%if %{with openssl}
%package openssl
Summary: TLS protocol support for rsyslog via OpenSSL library
Group: System Environment/Daemons
Requires: %name = %version-%release
Requires: openssl-libs
BuildRequires: openssl-devel
%endif
%if %{with snmp}
%package snmp
Summary: SNMP protocol support for rsyslog
Requires: %name = %version-%release
BuildRequires: net-snmp-devel
%endif
%if %{with udpspoof}
%package udpspoof
Summary: Provides the omudpspoof module
Requires: %name = %version-%release
BuildRequires: libnet-devel
%endif
%if %{with omamqp1}
%package omamqp1
Summary: Provides the omamqp1 module
Requires: %name = %version-%release
Requires: cyrus-sasl-lib
Requires: openssl-libs
BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cyrus-sasl-devel
BuildRequires: openssl-devel
BuildRequires: python3
%endif
%if %{with rdkafka}
%package kafka
Summary: Provides the omkafka module
Requires: %name = %version-%release
BuildRequires: librdkafka-devel
%endif
%package mmkubernetes
Summary: Provides the mmkubernetes module
Requires: %name = %version-%release
BuildRequires: libcurl-devel
%if %{with hiredis}
%package hiredis
Summary: Redis support for rsyslog
Requires: %name = %version-%release
BuildRequires: hiredis-devel
%endif
%if %{with libdbi}
%package libdbi
Summary: Libdbi database support for rsyslog
Requires: %name = %version-%release
BuildRequires: libdbi-devel
%endif
%if %{with mongodb}
%package mongodb
Summary: MongoDB support for rsyslog
Requires: %name = %version-%release
BuildRequires: mongo-c-driver-devel snappy-devel cyrus-sasl-devel
%endif
%if %{with rabbitmq}
%package rabbitmq
Summary: RabbitMQ support for rsyslog
Requires: %name = %version-%release
BuildRequires: librabbitmq-devel
%endif
%description
Rsyslog is an enhanced, multi-threaded syslog daemon. It supports MySQL,
syslog/TCP, RFC 3195, permitted sender lists, filtering on any message part,
and fine grain output format control. It is compatible with stock sysklogd
and can be used as a drop-in replacement. Rsyslog is simple to set up, with
advanced features suitable for enterprise-class, encryption-protected syslog
relay chains.

%description crypto
This package contains a module providing log file encryption and a
command line tool to process encrypted logs.

%description doc
This subpackage contains documentation for rsyslog.

%description elasticsearch
This module provides the capability for rsyslog to feed logs directly into
Elasticsearch.

%description mmjsonparse
This module provides the capability to recognize and parse JSON enhanced
syslog messages.

%description mmnormalize
This module provides the capability to normalize log messages via liblognorm.

%description mmaudit
This module provides message modification supporting Linux audit format
in various settings.

%description mmfields
The mmfield module permits to extract fields. Using this module is of special
advantage if a field-based log format is to be processed, like for example CEF
and either a large number of fields is needed or a specific field is used multiple
times inside filters.

%description mmtaghostname
This module provides message modification for changing or adding the host name.

%if %{with snmp}
%description mmsnmptrapd
This message modification module takes messages generated from snmptrapd and
modifies them so that they look like they originated from the read originator.
%endif

%if %{with mysql}
%description mysql
The rsyslog-mysql package contains a dynamic shared object that will add
MySQL database support to rsyslog.
%endif

%if %{with pgsql}
%description pgsql
The rsyslog-pgsql package contains a dynamic shared object that will add
PostgreSQL database support to rsyslog.
%endif

%if %{with gssapi}
%description gssapi
The rsyslog-gssapi package contains the rsyslog plugins which support GSSAPI
authentication and secure connections. GSSAPI is commonly used for Kerberos
authentication.
%endif

%if %{with relp}
%description relp
The rsyslog-relp package contains the rsyslog plugins that provide
the ability to receive syslog messages via the reliable RELP
protocol.
%endif

%if %{with gnutls}
%description gnutls
The rsyslog-gnutls package contains the rsyslog plugins that provide the
ability to send and receive syslog messages via TCP or RELP using TLS
encryption via GnuTLS library. For details refer to rsyslog doc on imtcp
and omfwd modules.
%endif

%if %{with openssl}
%description openssl
The rsyslog-openssl package contains the rsyslog plugins that provide the
ability to send and receive syslog messages via TCP or RELP using TLS
encryption via OpenSSL library. For details refer to rsyslog doc on imtcp
and omfwd modules.
%endif

%if %{with snmp}
%description snmp
The rsyslog-snmp package contains the rsyslog plugin that provides the
ability to send syslog messages as SNMPv1 and SNMPv2c traps.
%endif

%if %{with udpspoof}
%description udpspoof
This module is similar to the regular UDP forwarder, but permits to
spoof the sender address. Also, it enables to circle through a number
of source ports.
%endif

%if %{with omamqp1}
%description omamqp1
The omamqp1 output module can be used to send log messages via an AMQP
1.0-compatible messaging bus.
%endif

%if %{with rdkafka}
%description kafka
The rsyslog-kafka package provides module for Apache Kafka output.
%endif

%description mmkubernetes
The rsyslog-mmkubernetes package provides module for adding kubernetes
container metadata.

%if %{with hiredis}
%description hiredis
This module provides output to Redis.
%endif

%if %{with libdbi}
%description libdbi
This module supports a large number of database systems via
libdbi. Libdbi abstracts the database layer and provides drivers for
many systems. Drivers are available via the libdbi-drivers project.
%endif

%if %{with mongodb}
%description mongodb
The rsyslog-mongodb package contains a dynamic shared object that will add
MongoDB database support to rsyslog.
%endif

%if %{with rabbitmq}
%description rabbitmq
This module allows rsyslog to send messages to a RabbitMQ server.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; }
# set up rsyslog sources
%setup -q -D

%if %{with omamqp1}
# Unpack qpid-proton
%setup -q -D -T -b 5
%endif

%build

%ifarch sparc64
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpic"
%endif
%if %{with omamqp1}
(
	cd %{_builddir}/qpid-proton-%{qpid_proton_v}
	mkdir bld
	cd bld
	cmake .. \
		-DBUILD_BINDINGS="" \
		-DBUILD_STATIC_LIBS=YES \
		-DENABLE_FUZZ_TESTING=NO \
		-DPython_FIND_STRATEGY=LOCATION \
		-DPython_ROOT_DIR=/usr \
		-DCMAKE_AR="/usr/bin/gcc-ar" -DCMAKE_NM="/usr/bin/gcc-nm" -DCMAKE_RANLIB="/usr/bin/gcc-ranlib"
	make -j8
)
%endif
%ifarch sparc64
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpie"
%endif
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"
%if %{with hiredis}
export HIREDIS_CFLAGS=-I/usr/include/hiredis
export HIREDIS_LIBS="-L%{_libdir} -lhiredis"
%endif
sed -i 's/%{version}/%{version}-%{release}/g' configure.ac
autoreconf -if
%configure \
	--prefix=/usr \
	--disable-static \
	--disable-testbench \
%if %{with clickhouse}
	--enable-clickhouse \
%endif
%if %{with imdocker}
	--enable-imdocker \
%endif
%if %{with improg}
	--enable-improg \
%endif
  --enable-libcap-ng \
%if %{with libdbi}
	--enable-libdbi \
%endif
%if %{with hiredis}
	--enable-omhiredis \
%endif
%if %{with mongodb}
	--enable-ommongodb \
%endif
%if %{with rabbitmq}
	--enable-omrabbitmq \
%endif
%if %{with omamqp1}
	--enable-omamqp1 PROTON_PROACTOR_LIBS="%{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-core-static.a %{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-proactor-static.a %{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-static.a -lssl -lsasl2 -lcrypto" PROTON_PROACTOR_CFLAGS="-I%{_builddir}/qpid-proton-%{qpid_proton_v}/c/include -I%{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/include" PROTON_LIBS="%{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-core-static.a %{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-proactor-static.a %{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/libqpid-proton-static.a -lssl -lsasl2 -lcrypto" PROTON_CFLAGS="-I%{_builddir}/qpid-proton-%{qpid_proton_v}/c/include -I%{_builddir}/qpid-proton-%{qpid_proton_v}/bld/c/include" \
%endif
	--enable-elasticsearch \
	--enable-generate-man-pages \
%if %{with gnutls}
	--enable-gnutls \
%endif
%if %{with openssl}
	--enable-openssl \
%endif
%if %{with gssapi}
	--enable-gssapi-krb5 \
%endif
	--enable-imfile \
	--enable-imjournal \
%if %{with rdkafka}
	--enable-imkafka \
	--enable-omkafka \
%endif
	--enable-impstats \
%if %{with impstats_push}
	--enable-impstats-push \
%else
	--disable-impstats-push \
%endif
	--enable-imptcp \
	--enable-mail \
	--enable-mmanon \
	--enable-mmaudit \
	--enable-mmcount \
	--enable-mmfields \
	--enable-mmkubernetes \
	--enable-mmjsonparse \
	--enable-mmnormalize \
%if %{with mmtaghostname}
	--enable-mmtaghostname \
%endif
%if %{with snmp}
	--enable-mmsnmptrapd \
%endif
	--enable-mmutf8fix \
%if %{with mysql}
	--enable-mysql \
%endif
	--enable-omhttp \
	--enable-omjournal \
	--enable-omprog \
	--enable-omstdout \
%if %{with udpspoof}
	--enable-omudpspoof \
%endif
	--enable-omuxsock \
%if %{with pgsql}
	--enable-pgsql \
%endif
	--enable-pmaixforwardedfrom \
	--enable-pmcisconames \
	--enable-pmlastmsg \
	--enable-pmsnare \
%if %{with relp}
	--enable-relp \
%endif
%if %{with snmp}
	--enable-snmp \
%endif
	--enable-unlimited-select \
	--enable-usertools \
	--disable-libgcrypt \
	--enable-openssl_crypto_provider
make V=1
%check

make V=1 check
%install
make V=1 DESTDIR=%{buildroot} install
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_sysconfdir}/rsyslog.d
install -d -m 700 %{buildroot}%{rsyslog_statedir}
install -d -m 700 %{buildroot}%{rsyslog_pkidir}
install -d -m 755 %{buildroot}%{rsyslog_docdir}/html
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rsyslog.conf
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/rsyslog
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/rsyslog
install -p -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/rsyslog.service
%if %{with mysql}
install -p -m 644 plugins/ommysql/createDB.sql %{buildroot}%{rsyslog_docdir}/mysql-createDB.sql
%endif
%if %{with pgsql}
install -p -m 644 plugins/ompgsql/createDB.sql %{buildroot}%{rsyslog_docdir}/pgsql-createDB.sql
%endif
dos2unix tools/recover_qi.pl
install -p -m 644 tools/recover_qi.pl %{buildroot}%{rsyslog_docdir}/recover_qi.pl
install -p -m 644 contrib/mmkubernetes/*.rulebase %{buildroot}%{rsyslog_docdir}
cp -r doc/* %{buildroot}%{rsyslog_docdir}/html
rm -f %{buildroot}%{_libdir}/rsyslog/*.la
rm -f %{buildroot}%{_libdir}/rsyslog/imdiag.so
rm -f %{buildroot}%{_libdir}/rsyslog/liboverride_gethostname.so
rm -f %{buildroot}%{_libdir}/rsyslog/liboverride_getaddrinfo.so
rm -f %{buildroot}%{_libdir}/rsyslog/liboverride_gethostname_nonfqdn.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

for n in /var/log/{messages,secure,maillog,spooler}
do
	[ -f $n ] && continue
	umask 066 && touch $n
done
%systemd_post rsyslog.service
%preun

%systemd_preun rsyslog.service
%postun

%systemd_postun_with_restart rsyslog.service
%files -f %{oreon_filedir}/main.list
%files -n rsyslog-crypto -f %{oreon_filedir}/rsyslog-crypto.list
%files -n rsyslog-doc -f %{oreon_filedir}/rsyslog-doc.list
%files -n rsyslog-elasticsearch -f %{oreon_filedir}/rsyslog-elasticsearch.list
%files -n rsyslog-mmjsonparse -f %{oreon_filedir}/rsyslog-mmjsonparse.list
%files -n rsyslog-mmnormalize -f %{oreon_filedir}/rsyslog-mmnormalize.list
%files -n rsyslog-mmaudit -f %{oreon_filedir}/rsyslog-mmaudit.list
%files -n rsyslog-mmfields -f %{oreon_filedir}/rsyslog-mmfields.list
%files -n rsyslog-mmtaghostname -f %{oreon_filedir}/rsyslog-mmtaghostname.list
%files -n rsyslog-mmsnmptrapd -f %{oreon_filedir}/rsyslog-mmsnmptrapd.list
%files -n rsyslog-mysql -f %{oreon_filedir}/rsyslog-mysql.list
%files -n rsyslog-pgsql -f %{oreon_filedir}/rsyslog-pgsql.list
%files -n rsyslog-gssapi -f %{oreon_filedir}/rsyslog-gssapi.list
%files -n rsyslog-relp -f %{oreon_filedir}/rsyslog-relp.list
%files -n rsyslog-gnutls -f %{oreon_filedir}/rsyslog-gnutls.list
%files -n rsyslog-openssl -f %{oreon_filedir}/rsyslog-openssl.list
%files -n rsyslog-snmp -f %{oreon_filedir}/rsyslog-snmp.list
%files -n rsyslog-udpspoof -f %{oreon_filedir}/rsyslog-udpspoof.list
%files -n rsyslog-omamqp1 -f %{oreon_filedir}/rsyslog-omamqp1.list
%files -n rsyslog-kafka -f %{oreon_filedir}/rsyslog-kafka.list
%files -n rsyslog-mmkubernetes -f %{oreon_filedir}/rsyslog-mmkubernetes.list
%files -n rsyslog-hiredis -f %{oreon_filedir}/rsyslog-hiredis.list
%files -n rsyslog-libdbi -f %{oreon_filedir}/rsyslog-libdbi.list
%files -n rsyslog-mongodb -f %{oreon_filedir}/rsyslog-mongodb.list
%files -n rsyslog-rabbitmq -f %{oreon_filedir}/rsyslog-rabbitmq.list

%changelog

%autochangelog
