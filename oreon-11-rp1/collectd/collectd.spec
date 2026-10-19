%global source0_hash 5bae043042c19c31f77eb8464e56a01a5454e0b39fa07cf7ad0f1bfc9c3a09d6
%global __provides_exclude_from ^%{_libdir}/collectd/.*\\.so$
%undefine _strict_symbol_defs_build
Summary:        Statistics collection daemon for filling RRD files
Name: collectd
Version: 5.12.0
Release:        1%{?dist}
License: GPL-2.0-only
URL: https://collectd.org/
Source0:        https://github.com/collectd/collectd/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1: collectd-httpd.conf
Source2: collectd.service
Source91: apache.conf
Source92: email.conf
Source93: mysql.conf
Source94: nginx.conf
Source95: sensors.conf
Source96: snmp.conf
Source97: rrdtool.conf
Patch0: %{name}-include-collectd.d.patch
Patch1: %{name}-gcc11.patch
Patch2: %{name}-remove-des-support-from-snmp-plugin.patch
Patch3: %{name}-py311-dont-include-longintrepr.patch
Patch4: collectd-c99.patch
Patch5: collectd-c99-2.patch
Patch6: collectd-5.12.0-automake-1.18.patch
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  OpenIPMI-devel
BuildRequires:  curl-devel
BuildRequires:  gpsd-devel
BuildRequires:  hiredis-devel
BuildRequires:  iproute-static
BuildRequires:  iptables-devel
BuildRequires:  libatasmart-devel
BuildRequires:  libdbi-devel
BuildRequires:  libesmtp-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libmemcached-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libmnl-devel
BuildRequires:  libmodbus-devel
BuildRequires:  libnotify-devel
BuildRequires:  liboping-devel
BuildRequires:  libpcap-devel
BuildRequires:  libpq-devel
BuildRequires:  librabbitmq-devel
BuildRequires:  librdkafka-devel
BuildRequires:  libvirt-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  lua-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mongo-c-driver-devel
BuildRequires:  mosquitto-devel
BuildRequires:  net-snmp-devel
BuildRequires:  nut-devel
BuildRequires:  openldap-devel
BuildRequires:  owfs-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  protobuf-c-devel
BuildRequires:  python3-devel
BuildRequires:  qpid-proton-c-devel
BuildRequires:  riemann-c-client-devel
BuildRequires:  rrdtool-devel
BuildRequires:  systemd-devel
BuildRequires:  varnish-libs-devel
# /oreon:deps
%description
collectd is a daemon which collects system performance statistics periodically
and provides mechanisms to store the values in a variety of ways,
for example in RRD files.

%package amqp
Summary:       AMQP plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel
%description amqp
This plugin can be used to communicate with other instances of collectd
or third party applications using an AMQP message broker.

%package amqp1
Summary:       Sends JSON-encoded data to an AMQP1 message intermediary
BuildRequires: qpid-proton-c-devel
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description amqp1
Sends JSON-encoded data to an Advanced Message Queuing Protocol (AMQP)
1.0 server, such as Qpid Dispatch Router or Apache Artemis Broker.

%package apache
Summary:       Apache plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description apache
This plugin collects data provided by Apache's 'mod_status'.

%package ascent
Summary:       Ascent plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: libxml2-devel
%description ascent
This plugin collects data about an Ascent server,
a free server for the "World of Warcraft" game.

%package bind
Summary:       Bind plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: libxml2-devel
%description bind
This plugin retrieves statistics from the BIND dns server.

%package chrony
Summary:       Chrony plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description chrony
Chrony plugin for collectd

%package -n collectd-utils
Summary:       Collectd utilities
Requires:      libcollectdclient%{?_isa} = %{version}-%{release}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description -n collectd-utils
Collectd utilities

%package curl
Summary:       Curl plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
%description curl
This plugin reads webpages with curl

%package curl_xml
Summary:       Curl XML plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: libxml2-devel
%description curl_xml
This plugin retrieves XML data via curl.

%package dbi
Summary:       DBI plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libdbi-devel
%description dbi
This plugin uses the dbi library to connect to various databases,
execute SQL statements and read back the results.

%package disk
Summary:       Disk plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: systemd-devel
%description disk
This plugin collects statistics of harddisk and, where supported, partitions.

%package dns
Summary:       DNS traffic analysis plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libpcap-devel
%description dns
This plugin collects DNS traffic data.

%package drbd
Summary:       DRBD plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description drbd
This plugin collects data from DRBD.

%package email
Summary:       Email plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description email
This plugin collects data provided by spamassassin.

%ifarch %{java_arches}
%package generic-jmx
Summary:       Generic JMX plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description generic-jmx
This plugin collects data provided by JMX.
%endif

%package gps
Summary:       GPS plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: gpsd-devel
%description gps
This plugin monitor gps related data through gpsd.

%package hugepages
Summary:       Hugepages plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description hugepages
This plugin collects statistics about hugepage usage.

%package infiniband
Summary:       Collect metrics about infiniband ports
%description infiniband
Collect metrics about infiniband ports

%package ipmi
Summary:       IPMI plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: OpenIPMI-devel
%description ipmi
This plugin for collectd provides IPMI support.

%package iptables
Summary:       Iptables plugin for collectd
Requires:      collectd = %{version}-%{release}
BuildRequires: iptables-devel
%description iptables
This plugin collects data from iptables counters.

%package ipvs
Summary:       IPVS plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description ipvs
This plugin collects data from IPVS.

%ifarch %{java_arches}
%package java
Summary:       Java bindings for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: java-devel
BuildRequires: jpackage-utils
%description java
These are the Java bindings for collectd.
%endif

%package -n libcollectdclient
Summary:       Collectd client library
%description -n libcollectdclient
Collectd client library.

%package -n libcollectdclient-devel
Summary:       Development files for libcollectdclient
Requires:      libcollectdclient%{?_isa} = %{version}-%{release}
%description -n libcollectdclient-devel
Development files for libcollectdclient.

%package lua
Summary:       Lua plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lua-devel
%description lua
The Lua plugin embeds a Lua interpreter into collectd and exposes the
application programming interface (API) to Lua scripts.

%package mcelog
Summary:       Mcelog plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description mcelog
This plugin monitors machine check exceptions reported by mcelog and generates
appropriate notifications when machine check exceptions are detected.

%package mdevents
Summary:       Get events from RAID arrays in syslog
%description mdevents
This plugin, named mdevents, is responsible for gathering the events
from RAID arrays that were written to syslog by mdadm utility (which
is a user-space software for managing the RAIDs). Then, based on
configuration provided by user, plugin will decide whether to send the
collectd notification or not.

Mdevents needs the syslog and mdadm to be present on a platform that
collectd is launched.

%package memcachec
Summary:       Memcachec plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmemcached-devel
%description memcachec
This plugin connects to a memcached server, queries one or more
given pages and parses the returned data according to user specification.

%package modbus
Summary:       Modbus plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmodbus-devel
%description modbus
This plugin connects to a Modbus "slave" via Modbus/TCP
and reads register values.

%package mqtt
Summary:       MQTT plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: mosquitto-devel
%description mqtt
The MQTT plugin publishes and subscribes to MQTT topics.

%package mysql
Summary:       MySQL plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: mariadb-connector-c-devel
%description mysql
MySQL querying plugin. This plugin provides data of issued commands,
called handlers and database traffic.

%package netlink
Summary:       Netlink plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: iproute-static, libmnl-devel
%description netlink
This plugin uses a netlink socket to query the Linux kernel
about statistics of various interface and routing aspects.

%package nginx
Summary:       Nginx plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description nginx
This plugin collects data provided by Nginx.

%package notify_desktop
Summary:       Notify desktop plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libnotify-devel
%description notify_desktop
This plugin sends a desktop notification to a notification daemon,
as defined in the Desktop Notification Specification.

%package notify_email
Summary:       Notify email plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libesmtp-devel
%description notify_email
This plugin uses the ESMTP library to send
notifications to a configured email address.

%ifnarch s390 s390x
%package nut
Summary:       Network UPS Tools plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: nut-devel
%description nut
This plugin for collectd provides Network UPS Tools support.
%endif

%package openldap
Summary:       OpenLDAP plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: openldap-devel
%description openldap
This plugin for collectd reads monitoring information
from OpenLDAP's cn=Monitor subtree.

%package -n perl-Collectd
Summary:       Perl bindings for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description -n perl-Collectd
This package contains the Perl bindings and plugin for collectd.

%package pinba
Summary:       Pinba plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: protobuf-c-devel
%description pinba
This plugin receives profiling information from Pinba,
an extension for the PHP interpreter.

%package ping
Summary:       Ping plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: liboping-devel
%description ping
This plugin for collectd provides network latency statistics.

%package postgresql
Summary:       PostgreSQL plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libpq-devel
%description postgresql
PostgreSQL querying plugin. This plugins provides data of issued commands,
called handlers and database traffic.

%package python
Summary:       Python plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: python3-devel
%description python
The Python plugin embeds a Python interpreter into Collectd and exposes the
application programming interface (API) to Python-scripts.

%package redis
Summary:       Redis plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: hiredis-devel
%description redis
The Redis plugin connects to one or more instances of Redis, a key-value store,
and collects usage information using the hiredis library.

%package rrdcached
Summary:       RRDCacheD plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: rrdtool-devel
%description rrdcached
This plugin uses the RRDtool accelerator daemon, rrdcached(1),
to store values to RRD files in an efficient manner.

%package rrdtool
Summary:       RRDTool plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: rrdtool-devel
%description rrdtool
This plugin for collectd provides rrdtool support.

%ifnarch ppc sparc sparc64
%package sensors
Summary:       Libsensors module for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lm_sensors-devel
%description sensors
This plugin for collectd provides querying of sensors supported by
lm_sensors.
%endif

%package smart
Summary:       SMART plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libatasmart-devel
%description smart
This plugin for collectd collects SMART statistics,
notably load cycle count, temperature and bad sectors.

%package snmp
Summary:       SNMP module for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: net-snmp-devel
%description snmp
This plugin for collectd provides querying of net-snmp.

%package snmp_agent
Summary:       SNMP AgentX plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: net-snmp-devel
%description snmp_agent
This plugin is an AgentX subagent that receives and handles queries
from a SNMP master agent and returns the data collected by read plugins.

%package synproxy
Summary:       Synproxy plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description synproxy
This plugin provides statistics for Linux SYNPROXY available since 3.12

%package varnish
Summary:       Varnish plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: varnish-libs-devel
%description varnish
This plugin collects information about Varnish, an HTTP accelerator.

%ifnarch ppc sparc sparc64
%package virt
Summary:       Libvirt plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libvirt-devel
BuildRequires: libxml2-devel
%description virt
This plugin collects information from virtualized guests.
%endif

%package web
Summary:       Contrib web interface to viewing rrd files
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      collectd-rrdtool = %{version}-%{release}
Requires:      perl-HTML-Parser, perl-Regexp-Common, rrdtool-perl, httpd
%description web
This package will allow for a simple web interface to view rrd files created by
collectd.

%package write_http
Summary:       HTTP output plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
%description write_http
This plugin can send data to Redis.

%package write_kafka
Summary:       Kafka output plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librdkafka-devel
%description write_kafka
This sends values to Kafka, a distributed messaging system.

%package write_mongodb
Summary:       MongoDB output plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: mongo-c-driver-devel
%description write_mongodb
This plugin sends values to MongoDB.

%package write_prometheus
Summary:       Prometheus output plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmicrohttpd-devel
%description write_prometheus
This plugin exposes collected values using an embedded HTTP
server, turning the collectd daemon into a Prometheus exporter.

%package write_redis
Summary:       Redis output plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: hiredis-devel
%description write_redis
This plugin can send data to Redis.

%package write_riemann
Summary:       Riemann output plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: riemann-c-client-devel
%description write_riemann
This plugin can send data to Riemann.

%package write_sensu
Summary:       Sensu output plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description write_sensu
This plugin can send data to Sensu.

%package write_syslog
Summary:       syslog output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-write-syslog = %{version}-%{release}
%description write_syslog
This plugin can send data to syslog.

%package write_tsdb
Summary:       OpenTSDB output plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description write_tsdb
This plugin can send data to OpenTSDB.


%package zookeeper
Summary:       Zookeeper plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description zookeeper
This is a collectd plugin that reads data from Zookeeper's MNTR command.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -v -p1

# recompile generated files
touch src/pinba.proto

%build

%configure \
    --disable-dependency-tracking \
    --enable-all-plugins \
    --disable-static \
    --disable-apple_sensors \
    --disable-aquaero \
    --disable-barometer \
    --disable-buddyinfo \
    --disable-capabilities \
    --disable-ceph \
    --disable-check_uptime \
    --disable-connectivity \
    --disable-curl_json \
    --disable-dcpmm \
    --disable-dpdk_telemetry \
    --disable-dpdkevents \
    --disable-dpdkstat \
    --disable-gmond \
    --disable-gpu_nvidia \
    --disable-grpc \
    --disable-intel_pmu \
    --disable-intel_rdt \
    --disable-ipstats \
    --disable-logparser \
    --disable-log_logstash \
    --disable-lpar \
    --disable-lvm \
    --disable-mic \
    --disable-netapp \
    --disable-netstat_udp \
    --disable-ovs_events \
    --disable-ovs_stats \
%ifarch s390 s390x
    --disable-nut \
%endif
    --disable-oracle \
%ifarch s390 s390x
    --disable-pcie_errors \
%endif
    --disable-pf \
    --disable-procevent \
    --disable-redfish \
    --disable-routeros \
%ifarch ppc sparc sparc64
    --disable-sensors \
%endif
    --disable-sigrok \
    --disable-slurm \
    --disable-sysevent \
    --disable-tape \
    --disable-tokyotyrant \
    --disable-turbostat \
    --disable-ubi \
    --disable-write_influxdb_udp \
%ifnarch x86_64
    --disable-xencpu \
%endif
    --disable-xmms \
    --disable-zone \
%ifarch %{java_arches}
    --with-java \
%else
    --disable-java \
%endif
    --disable-write_stackdriver \
    --with-python=%{_bindir}/python3 \
    --with-perl-bindings=INSTALLDIRS=vendor \
    --disable-werror \
    AR_FLAGS="-cr"
make %{?_smp_mflags}
%install
rm -rf contrib/SpamAssassin
make install DESTDIR="%{buildroot}"
install -Dp -m0644 src/collectd.conf %{buildroot}%{_sysconfdir}/collectd.conf
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/collectd.service
install -d -m0755 %{buildroot}%{_localstatedir}/lib/collectd/rrd
install -d -m0755 %{buildroot}%{_datadir}/collectd/collection3/
install -d -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d/
find contrib/ -type f -exec chmod a-x {} \;
find %{buildroot} -name .packlist -delete
find %{buildroot} -name perllocal.pod -delete
cp -ad contrib/collection3/* %{buildroot}%{_datadir}/collectd/collection3/
cp -pv %{buildroot}%{_datadir}/collectd/collection3/etc/collection.conf %{buildroot}%{_sysconfdir}/collection.conf
ln -rsf %{_sysconfdir}/collection.conf %{buildroot}%{_datadir}/collectd/collection3/etc/collection.conf
cp -pv %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/collectd.conf
chmod +x %{buildroot}%{_datadir}/collectd/collection3/bin/*.cgi
mkdir perl-examples
find contrib -name '*.p[lm]' -exec mv {} perl-examples/ \;
mkdir -p %{buildroot}%{_sysconfdir}/collectd.d/
cp %{SOURCE91} %{buildroot}%{_sysconfdir}/collectd.d/apache.conf
cp %{SOURCE92} %{buildroot}%{_sysconfdir}/collectd.d/email.conf
cp %{SOURCE93} %{buildroot}%{_sysconfdir}/collectd.d/mysql.conf
cp %{SOURCE94} %{buildroot}%{_sysconfdir}/collectd.d/nginx.conf
cp %{SOURCE95} %{buildroot}%{_sysconfdir}/collectd.d/sensors.conf
cp %{SOURCE96} %{buildroot}%{_sysconfdir}/collectd.d/snmp.conf
cp %{SOURCE97} %{buildroot}%{_sysconfdir}/collectd.d/rrdtool.conf
%ifnarch %{java_arches}
rm -f %{buildroot}%{_mandir}/man5/collectd-java.5*
%endif
%ifnarch s390 s390x
for p in dns ipmi libvirt nut perl ping postgresql
%else
for p in dns ipmi libvirt perl ping postgresql
%endif
do
cat > %{buildroot}%{_sysconfdir}/collectd.d/$p.conf <<EOF
LoadPlugin $p
EOF
done
rm -f %{buildroot}/%{_libdir}/{collectd/,}*.la
%ifnarch s390 s390x
%oreon_autofiles collectd-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libcollectdclient usr/*/lib*.so.*
%oreon_autofiles libcollectdclient-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles perl-Collectd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%endif
%post

%systemd_post collectd.service
%preun

%systemd_preun collectd.service
%postun

%systemd_postun_with_restart collectd.service
%files -f %{oreon_filedir}/main.list
%files -n collectd-utils -f %{oreon_filedir}/collectd-utils.list
%files -n libcollectdclient -f %{oreon_filedir}/libcollectdclient.list
%files -n libcollectdclient-devel -f %{oreon_filedir}/libcollectdclient-devel.list
%files -n perl-Collectd -f %{oreon_filedir}/perl-Collectd.list

%changelog

%autochangelog
