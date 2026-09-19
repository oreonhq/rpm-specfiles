%global source0_hash 37ea0d4588533316de122df4e1b249867b0a0575f646c7478d0cc4d747462943

%global ivykis_ver 0.42.3

%global syslog_ng_major_ver 4
%global syslog_ng_minor_ver 11
%global syslog_ng_patch_ver 0
%global syslog_ng_major_minor_ver %{syslog_ng_major_ver}.%{syslog_ng_minor_ver}
%global syslog_ng_ver %{syslog_ng_major_ver}.%{syslog_ng_minor_ver}.%{syslog_ng_patch_ver}

Name:    syslog-ng
Version: %{syslog_ng_ver}
Release: 1%{?dist}
Summary: Next-generation syslog server

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://www.syslog-ng.com/products/open-source-log-management/
Source0: https://github.com/balabit/syslog-ng/releases/download/syslog-ng-%{version}/%{name}-%{version}.tar.gz
Source1: syslog-ng.conf
Source2: syslog-ng.logrotate
Source3: syslog-ng.service

BuildRequires: make
BuildRequires: bison
BuildRequires: cyrus-sasl-devel
BuildRequires: flex
BuildRequires: glib2-devel
BuildRequires: hiredis-devel
BuildRequires: ivykis-devel >= %{ivykis_ver}
BuildRequires: json-c-devel
BuildRequires: libcap-devel
BuildRequires: libcurl-devel
BuildRequires: libdbi-devel
BuildRequires: libesmtp-devel
BuildRequires: libmaxminddb-devel
BuildRequires: libnet-devel
BuildRequires: librabbitmq-devel
BuildRequires: libtool
BuildRequires: libuuid-devel
BuildRequires: libxslt
BuildRequires: mongo-c-driver-devel
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: perl-generators
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: riemann-c-client-devel
BuildRequires: snappy-devel
BuildRequires: systemd-devel
BuildRequires: systemd-units
BuildRequires: librdkafka-devel
BuildRequires: zlib-devel
BuildRequires: paho-c-devel

BuildRequires:  python3-pip
BuildRequires:  python3-cachetools
BuildRequires:  python3-certifi
BuildRequires:  python3-charset-normalizer
BuildRequires:  python3-google-auth
BuildRequires:  python3-idna
BuildRequires:  python3-kubernetes
BuildRequires:  python3-oauthlib
BuildRequires:  python3-pyasn1
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-dateutil
BuildRequires:  python3-PyYAML
BuildRequires:  python3-requests
BuildRequires:  python3-requests-oauthlib
BuildRequires:  python3-rsa
BuildRequires:  python3-six
BuildRequires:  python3-urllib3
BuildRequires:  python3-websocket-client
BuildRequires:  python3-boto3
BuildRequires:  python3-botocore
BuildRequires:  python3-tornado

%ifarch i686
%bcond_with bpf
%bcond_with grpc
%bcond_with examples
%else
%bcond_without bpf
%bcond_without grpc
%bcond_without examples
%endif

%bcond_without snmp

%if %{with bpf}
BuildRequires: libbpf-devel
BuildRequires: bpftool
BuildRequires: clang
%endif

%if %{with grpc}
BuildRequires:  grpc-devel
BuildRequires:  protobuf-devel
BuildRequires:  gcc-c++
%endif

%if %{with snmp}
BuildRequires: net-snmp-devel
%endif

Requires: logrotate
Requires: ivykis >= %{ivykis_ver}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

Provides: syslog

# Fedora 17’s unified filesystem (/usr-move)
Conflicts: filesystem < 3

Obsoletes: syslog-ng-json < 3.8

%description
syslog-ng is an enhanced log daemon, supporting a wide range of input and
output methods: syslog, unstructured text, message queues, databases (SQL
and NoSQL alike) and more.

Key features:

 * receive and send RFC3164 and RFC5424 style syslog messages
 * work with any kind of unstructured data
 * receive and send JSON formatted messages
 * classify and structure logs with builtin parsers (csv-parser(),
   db-parser(), ...)
 * normalize, crunch and process logs as they flow through the system
 * hand on messages for further processing using message queues (like
   AMQP), files or databases (like PostgreSQL or MongoDB).

%package slog
Summary: secure logging support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description slog
This module supports secure message transfer and storage (experimental).

%package libdbi
Summary: Libdbi support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description libdbi
This module supports a large number of database systems via libdbi.

%package mongodb
Summary: MongoDB support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description mongodb
This module supports the mongodb database via libmongo-client.

%package kafka
Summary: Kafka support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description kafka
This module supports sending logs to Kafka through librdkafka.

%package smtp
Summary: SMTP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description smtp
This module supports sending e-mail alerts through an smtp server.

%package snmp
Summary: SNMP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description snmp
This module adds support for SNMP destination.

%package geoip
Summary: GeoIP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description geoip
This template function returns the 2-letter country code of
any IPv4 address or host.

%package redis
Summary: Redis support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description redis
This module supports the redis key-value store via hiredis.

%package riemann
Summary: Riemann support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description riemann
This module supports the riemann monitoring server.

%package http
Summary: HTTP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-curl < 3.10

%description http
This module supports the http destination.

%package grpc
Summary: GRPC support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description grpc
This module supports the GRPC, a common requirement
for OpenTelemetry and Loki support.

%package opentelemetry
Summary: OpenTelemetry support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-grpc

%description opentelemetry
This module adds OpenTelemetry support.

%package loki
Summary: Loki support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-grpc

%description loki
This module adds loki support.

%package bigquery
Summary: Google BigQuery support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-grpc

%description bigquery
This module adds Google BigQuery support.

%package pubsub
Summary: Google PubSub support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-grpc

%description pubsub
This module adds Google PubSub support.

%package clickhouse
Summary: ClickHouse support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-grpc

%description clickhouse
This module adds ClickHouse support.

%package bpf
Summary: Faster UDP log collection for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description bpf
This module provides faster UDP log collection using bpf.

%package amqp
Summary: AMQP support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description amqp
This module supports the AMQP destination.

%package mqtt
Summary: mqtt support for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description mqtt
This module supports sending logs to MQTT through paho-c.

%package python
Summary: Python support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: python3-syslog-ng < 3.22

%description python
This package provides python support for syslog-ng.

%package python-modules
Summary:        Python-based drivers for syslog-ng
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires:       %{name}-python
Requires:  python3-cachetools
Requires:  python3-certifi
Requires:  python3-charset-normalizer
Requires:  python3-google-auth
Requires:  python3-idna
Requires:  python3-kubernetes
Requires:  python3-oauthlib
Requires:  python3-pyasn1
Requires:  python3-pyasn1-modules
Requires:  python3-dateutil
Requires:  python3-PyYAML
Requires:  python3-requests
Requires:  python3-requests-oauthlib
Requires:  python3-rsa
Requires:  python3-six
Requires:  python3-urllib3
Requires:  python3-websocket-client
Requires:  python3-boto3
Requires:  python3-botocore
Requires:  python3-tornado

%description python-modules
This package provides Python-based (Kubernetes, Hypr) drivers for syslog-ng.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# Remove bundled libraries
rm -rf lib/ivykis
rm -rf modules/afamqp/rabbitmq-c
rm -rf modules/afmongodb/mongo-c-driver

# fix perl path
sed -i 's|^#!/usr/local/bin/perl|#!%{__perl}|' contrib/relogger.pl

# fix executable perms on contrib files
chmod -c a-x contrib/syslog2ng

# fix authors file
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && \
    mv -f AUTHORS.conv AUTHORS

# Fix python shebang
%py3_shebang_fix lib/merge-grammar.py
touch -r lib/cfg-grammar.y lib/merge-grammar.py

%build
%configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --localstatedir=%{_sharedstatedir}/%{name} \
    --datadir=%{_datadir} \
    --with-module-dir=%{_libdir}/%{name} \
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-ivykis=system \
    --with-mongoc=system \
    --with-embedded-crypto \
    --enable-manpages \
    --enable-ipv6 \
    --enable-spoof-source \
    --with-linux-caps=auto \
    --enable-sql \
    --enable-kafka \
    --enable-mqtt \
    --enable-json \
    --enable-ssl \
    --enable-smtp \
    --enable-geoip \
    --enable-shared \
    --disable-static \
    --enable-dynamic-linking \
    --enable-systemd \
    --enable-redis \
    --enable-amqp \
    --enable-python \
    --with-python=3 \
    --with-python-packages=system \
    --disable-java \
    --disable-java-modules \
%if %{with snmp}
    --enable-afsnmp \
%else
    --disable-afsnmp \
%endif
%if %{with examples}
    --enable-example-modules \
%else
    --disable-example-modules \
%endif
%if %{with grpc}
    --enable-cpp --enable-grpc \
%endif
%if %{with bpf}
    --enable-ebpf \
%endif
    --enable-riemann

%make_build

%install
%make_install

install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/conf.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/syslog-ng.conf

install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/syslog

install -d -m 755 %{buildroot}%{_prefix}/lib/systemd/system
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service

# create the local state dir
install -d -m 755 %{buildroot}/%{_sharedstatedir}/%{name}

# install the main library header files
install -d -m 755 %{buildroot}%{_includedir}/%{name}
install -p -m 644 config.h %{buildroot}%{_includedir}/%{name}
install -p -m 644 lib/*.h %{buildroot}%{_includedir}/%{name}

find %{buildroot} -name "*.la" -exec rm -f {} \;

# remove some extra testing related files
rm %{buildroot}%{_unitdir}/%{name}@.service

%post
ldconfig
%systemd_post syslog-ng.service

%preun
%systemd_preun syslog-ng.service

%postun
ldconfig
%systemd_postun_with_restart syslog-ng.service

%triggerun -- syslog-ng < 3.2.3
if /sbin/chkconfig --level 3 %{name} ; then
    /bin/systemctl enable %{name}.service >/dev/null 2>&1 || :
fi

%files
%doc AUTHORS COPYING NEWS.md
%doc contrib/{relogger.pl,syslog2ng,syslog-ng.conf.doc}

%dir %{_sysconfdir}/syslog-ng
%dir %{_sysconfdir}/syslog-ng/conf.d
%dir %{_sysconfdir}/syslog-ng/patterndb.d
%config(noreplace) %{_sysconfdir}/logrotate.d/syslog
%config(noreplace) %{_sysconfdir}/syslog-ng/syslog-ng.conf

%{_unitdir}/syslog-ng.service

%dir %{_sharedstatedir}/syslog-ng

%{_sbindir}/syslog-ng
%{_sbindir}/syslog-ng-ctl
%{_sbindir}/syslog-ng-debun

%{_bindir}/dqtool
%{_bindir}/loggen
%{_bindir}/pdbtool
%{_bindir}/persist-tool
%{_bindir}/update-patterndb
%{_bindir}/syslog-ng-update-virtualenv

%{_libdir}/libevtlog-%{syslog_ng_major_minor_ver}.so.0
%{_libdir}/libevtlog-%{syslog_ng_major_minor_ver}.so.0.0.0
%{_libdir}/libloggen_helper-%{syslog_ng_major_minor_ver}.so.0
%{_libdir}/libloggen_helper-%{syslog_ng_major_minor_ver}.so.0.0.0
%{_libdir}/libloggen_plugin-%{syslog_ng_major_minor_ver}.so.0
%{_libdir}/libloggen_plugin-%{syslog_ng_major_minor_ver}.so.0.0.0
%{_libdir}/libsecret-storage.so.0
%{_libdir}/libsecret-storage.so.0.0.0
%{_libdir}/libsyslog-ng-%{syslog_ng_major_minor_ver}.so.0
%{_libdir}/libsyslog-ng-%{syslog_ng_major_minor_ver}.so.0.0.0

%dir %{_libdir}/syslog-ng
%{_libdir}/syslog-ng/*.so

%dir %{_libdir}/syslog-ng/loggen
%{_libdir}/syslog-ng/loggen/libloggen_socket_plugin.so
%{_libdir}/syslog-ng/loggen/libloggen_ssl_plugin.so

%exclude %{_libdir}/syslog-ng/libafamqp.so
%exclude %{_libdir}/syslog-ng/libafmongodb.so
%exclude %{_libdir}/syslog-ng/libafsmtp.so
%exclude %{_libdir}/syslog-ng/libafsql.so
%exclude %{_libdir}/syslog-ng/libgeoip2-plugin.so
%exclude %{_libdir}/syslog-ng/libhttp.so
%exclude %{_libdir}/syslog-ng/libmod-python.so
%exclude %{_libdir}/syslog-ng/libredis.so
%exclude %{_libdir}/syslog-ng/libriemann.so
%exclude %{_libdir}/syslog-ng/libafsnmp.so
%exclude %{_libdir}/syslog-ng/libkafka.so
%exclude %{_libdir}/syslog-ng/libotel.so
%exclude %{_libdir}/syslog-ng/libmqtt.so
%exclude %{_libdir}/syslog-ng/libebpf.so
%exclude %{_libdir}/syslog-ng/libotel.so
%exclude %{_libdir}/syslog-ng/libloki.so
%exclude %{_libdir}/syslog-ng/libbigquery.so
%exclude %{_libdir}/syslog-ng/libcloud_auth.so
%exclude %{_libdir}/syslog-ng/libclickhouse.so
%exclude %{_libdir}/syslog-ng/libpubsub.so

%dir %{_datadir}/%{name}

# scl files
%{_datadir}/syslog-ng/include/

# uhm, some better places for those?
%{_datadir}/syslog-ng/xsd/

%{_datadir}/syslog-ng/smart-multi-line.fsm

%{_mandir}/man1/loggen.1*
%{_mandir}/man1/pdbtool.1*
%{_mandir}/man1/syslog-ng-ctl.1*
%{_mandir}/man1/syslog-ng-debun.1*
%{_mandir}/man1/dqtool.1*
%{_mandir}/man5/syslog-ng.conf.5*
%{_mandir}/man8/syslog-ng.8*
%{_mandir}/man1/persist-tool.1*

%files slog
%{_bindir}/slogkey
%{_bindir}/slogencrypt
%{_bindir}/slogverify
%{_libdir}/syslog-ng/libsecure-logging.so
%{_mandir}/man1/slogkey.1*
%{_mandir}/man1/slogencrypt.1*
%{_mandir}/man1/slogverify.1*
%{_mandir}/man7/secure-logging.7*

%if %{with grpc}

%files grpc
%{_libdir}/libgrpc-protos.*

%files opentelemetry
%{_libdir}/%{name}/libotel.so

%files loki
%{_libdir}/%{name}/libloki.so

%files bigquery
%{_libdir}/%{name}/libbigquery.so

%files clickhouse
%{_libdir}/%{name}/libclickhouse.so

%files pubsub
%{_libdir}/%{name}/libpubsub.so

%endif

%if %{with cloudauth}
%files cloudauth
%{_libdir}/%{name}/libcloud_auth.so

%endif

%files libdbi
%{_libdir}/syslog-ng/libafsql.so

%files kafka
%{_libdir}/%{name}/libkafka.so

%files mongodb
%{_libdir}/syslog-ng/libafmongodb.so

%files redis
%{_libdir}/syslog-ng/libredis.so

%files mqtt
%{_libdir}/%{name}/libmqtt.so

%files smtp
%{_libdir}/syslog-ng/libafsmtp.so

%if %{with snmp}
%files snmp
%{_libdir}/%{name}/libafsnmp.so
%endif

%files geoip
%{_libdir}/syslog-ng/libgeoip2-plugin.so

%files riemann
%{_libdir}/syslog-ng/libriemann.so

%files http
%{_libdir}/syslog-ng/libhttp.so

%files amqp
%{_libdir}/syslog-ng/libafamqp.so

%if %{with bpf}
%files bpf
%{_libdir}/%{name}/libebpf.so
%endif

%files python
%{_libdir}/%{name}/libmod-python.so
%dir %{_sysconfdir}/%{name}/python
%{_sysconfdir}/%{name}/python/README.md
%{_libdir}/%{name}/python/syslogng-1.0-py%{python3_version}.egg-info
%{_libdir}/%{name}/python/syslogng/*
%{_libdir}/%{name}/python/requirements.txt
%exclude %{_libdir}/syslog-ng/python/syslogng/modules/

%files python-modules
%dir %{_libdir}/syslog-ng/python/syslogng/modules/
%{_libdir}/syslog-ng/python/syslogng/modules/*

%files devel
%{_datadir}/syslog-ng/tools/
%{_includedir}/syslog-ng/
%{_libdir}/libevtlog.so
%{_libdir}/libloggen_helper.so
%{_libdir}/libloggen_plugin.so
%{_libdir}/libsecret-storage.so
%{_libdir}/libsyslog-ng-native-connector.a
%{_libdir}/libsyslog-ng.so
%{_libdir}/pkgconfig/syslog-ng-native-connector.pc
%{_libdir}/pkgconfig/syslog-ng.pc

%changelog
%autochangelog
