%global source0_hash 5bae043042c19c31f77eb8464e56a01a5454e0b39fa07cf7ad0f1bfc9c3a09d6

%global __provides_exclude_from ^%{_libdir}/collectd/.*\\.so$
%undefine _strict_symbol_defs_build

Summary: Statistics collection daemon for filling RRD files
Name: collectd
Version: 5.12.0
Release: 61%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://collectd.org/

Source: https://github.com/collectd/collectd/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1: collectd-httpd.conf
Source2: collectd.service
Source91: apache.conf
Source92: email.conf
Source93: mysql.conf
Source94: nginx.conf
Source95: sensors.conf
Source96: snmp.conf
Source97: rrdtool.conf
%if 0%{?fedora}
Source98: onewire.conf
%endif

Patch0: %{name}-include-collectd.d.patch
Patch1: %{name}-gcc11.patch
Patch2: %{name}-remove-des-support-from-snmp-plugin.patch
Patch3: %{name}-py311-dont-include-longintrepr.patch
Patch4: collectd-c99.patch
Patch5: collectd-c99-2.patch
Patch6: collectd-5.12.0-automake-1.18.patch

BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: libgcrypt-devel
BuildRequires: libxcrypt-devel
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

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

%if 0%{?fedora}
%package onewire
Summary:       OneWire bus plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: owfs-devel
%description onewire
The experimental OneWire plugin collects temperature information
from sensors connected to the computer over the OneWire bus.
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

%if 0%{?fedora}
%ifarch x86_64
%package xencpu
Summary:       xencpu plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: xen-devel
%description xencpu
The xencpu plugin collects CPU statistics from Xen.
%endif
%endif

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

# Remove Perl hidden .packlist files.
find %{buildroot} -name .packlist -delete
# Remove Perl temporary file perllocal.pod
find %{buildroot} -name perllocal.pod -delete

# copy web interface
cp -ad contrib/collection3/* %{buildroot}%{_datadir}/collectd/collection3/
cp -pv %{buildroot}%{_datadir}/collectd/collection3/etc/collection.conf %{buildroot}%{_sysconfdir}/collection.conf
ln -rsf %{_sysconfdir}/collection.conf %{buildroot}%{_datadir}/collectd/collection3/etc/collection.conf
cp -pv %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/collectd.conf
chmod +x %{buildroot}%{_datadir}/collectd/collection3/bin/*.cgi

# Move the Perl examples to a separate directory.
mkdir perl-examples
find contrib -name '*.p[lm]' -exec mv {} perl-examples/ \;

# Move config contribs
mkdir -p %{buildroot}%{_sysconfdir}/collectd.d/
cp %{SOURCE91} %{buildroot}%{_sysconfdir}/collectd.d/apache.conf
cp %{SOURCE92} %{buildroot}%{_sysconfdir}/collectd.d/email.conf
cp %{SOURCE93} %{buildroot}%{_sysconfdir}/collectd.d/mysql.conf
cp %{SOURCE94} %{buildroot}%{_sysconfdir}/collectd.d/nginx.conf
cp %{SOURCE95} %{buildroot}%{_sysconfdir}/collectd.d/sensors.conf
cp %{SOURCE96} %{buildroot}%{_sysconfdir}/collectd.d/snmp.conf
cp %{SOURCE97} %{buildroot}%{_sysconfdir}/collectd.d/rrdtool.conf
%if 0%{?fedora}
cp %{SOURCE98} %{buildroot}%{_sysconfdir}/collectd.d/onewire.conf
%endif

%ifnarch %{java_arches}
# remove collectd-java.5 man page on non-java arches
rm -f %{buildroot}%{_mandir}/man5/collectd-java.5*
%endif

# configs for subpackaged plugins
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

# *.la files shouldn't be distributed.
rm -f %{buildroot}/%{_libdir}/{collectd/,}*.la

%ifnarch s390 s390x
# checks fails in test_plugin_smart on s390
%check
make check
%endif

%post
%systemd_post collectd.service

%preun
%systemd_preun collectd.service

%postun
%systemd_postun_with_restart collectd.service

%files
%license COPYING
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/collectd.conf
%config(noreplace) %{_sysconfdir}/collectd.d/
%exclude %{_sysconfdir}/collectd.d/apache.conf
%exclude %{_sysconfdir}/collectd.d/dns.conf
%exclude %{_sysconfdir}/collectd.d/email.conf
%exclude %{_sysconfdir}/collectd.d/ipmi.conf
%exclude %{_sysconfdir}/collectd.d/libvirt.conf
%exclude %{_sysconfdir}/collectd.d/mysql.conf
%exclude %{_sysconfdir}/collectd.d/nginx.conf
%ifnarch s390 s390x
%exclude %{_sysconfdir}/collectd.d/nut.conf
%endif
%if 0%{?fedora}
%exclude %{_sysconfdir}/collectd.d/onewire.conf
%endif
%exclude %{_sysconfdir}/collectd.d/perl.conf
%exclude %{_sysconfdir}/collectd.d/ping.conf
%exclude %{_sysconfdir}/collectd.d/postgresql.conf
%exclude %{_datadir}/collectd/postgresql_default.conf
%exclude %{_sysconfdir}/collectd.d/rrdtool.conf
%exclude %{_sysconfdir}/collectd.d/sensors.conf
%exclude %{_sysconfdir}/collectd.d/snmp.conf

%{_unitdir}/collectd.service
%{_sbindir}/collectd
%{_sbindir}/collectdmon
%dir %{_localstatedir}/lib/collectd/

%dir %{_libdir}/collectd

%{_libdir}/collectd/aggregation.so
%{_libdir}/collectd/apcups.so
%{_libdir}/collectd/battery.so
%{_libdir}/collectd/cgroups.so
%{_libdir}/collectd/conntrack.so
%{_libdir}/collectd/contextswitch.so
%{_libdir}/collectd/cpu.so
%{_libdir}/collectd/cpufreq.so
%{_libdir}/collectd/cpusleep.so
%{_libdir}/collectd/csv.so
%{_libdir}/collectd/df.so
%{_libdir}/collectd/entropy.so
%{_libdir}/collectd/ethstat.so
%{_libdir}/collectd/exec.so
%{_libdir}/collectd/fhcount.so
%{_libdir}/collectd/filecount.so
%{_libdir}/collectd/fscache.so
%{_libdir}/collectd/hddtemp.so
%{_libdir}/collectd/interface.so
%{_libdir}/collectd/ipc.so
%{_libdir}/collectd/irq.so
%{_libdir}/collectd/load.so
%{_libdir}/collectd/logfile.so
%{_libdir}/collectd/madwifi.so
%{_libdir}/collectd/match_empty_counter.so
%{_libdir}/collectd/match_hashed.so
%{_libdir}/collectd/match_regex.so
%{_libdir}/collectd/match_timediff.so
%{_libdir}/collectd/match_value.so
%{_libdir}/collectd/mbmon.so
%{_libdir}/collectd/md.so
%{_libdir}/collectd/memcached.so
%{_libdir}/collectd/memory.so
%{_libdir}/collectd/multimeter.so
%{_libdir}/collectd/network.so
%{_libdir}/collectd/nfs.so
%{_libdir}/collectd/notify_nagios.so
%{_libdir}/collectd/ntpd.so
%{_libdir}/collectd/numa.so
%{_libdir}/collectd/olsrd.so
%{_libdir}/collectd/openvpn.so
%{_libdir}/collectd/powerdns.so
%ifnarch s390 s390x
%{_libdir}/collectd/pcie_errors.so
%endif
%{_libdir}/collectd/processes.so
%{_libdir}/collectd/protocols.so
%{_libdir}/collectd/serial.so
%{_libdir}/collectd/statsd.so
%{_libdir}/collectd/swap.so
%{_libdir}/collectd/syslog.so
%{_libdir}/collectd/table.so
%{_libdir}/collectd/tail.so
%{_libdir}/collectd/tail_csv.so
%{_libdir}/collectd/target_notification.so
%{_libdir}/collectd/target_replace.so
%{_libdir}/collectd/target_scale.so
%{_libdir}/collectd/target_set.so
%{_libdir}/collectd/target_v5upgrade.so
%{_libdir}/collectd/tcpconns.so
%{_libdir}/collectd/teamspeak2.so
%{_libdir}/collectd/ted.so
%{_libdir}/collectd/thermal.so
%{_libdir}/collectd/threshold.so
%{_libdir}/collectd/unixsock.so
%{_libdir}/collectd/uptime.so
%{_libdir}/collectd/users.so
%{_libdir}/collectd/uuid.so
%{_libdir}/collectd/vmem.so
%{_libdir}/collectd/vserver.so
%{_libdir}/collectd/wireless.so
%{_libdir}/collectd/write_graphite.so
%{_libdir}/collectd/write_log.so
%{_libdir}/collectd/zfs_arc.so

%dir %{_datadir}/collectd/
%{_datadir}/collectd/types.db

%doc %{_mandir}/man1/collectd.1*
%doc %{_mandir}/man1/collectdmon.1*
%doc %{_mandir}/man5/collectd.conf.5*
%doc %{_mandir}/man5/collectd-exec.5*
%doc %{_mandir}/man5/collectd-threshold.5*
%doc %{_mandir}/man5/collectd-unixsock.5*
%doc %{_mandir}/man5/types.db.5*

%files -n libcollectdclient-devel
%dir %{_includedir}/collectd/
%{_includedir}/collectd/client.h
%{_includedir}/collectd/lcc_features.h
%{_includedir}/collectd/network.h
%{_includedir}/collectd/network_buffer.h
%{_includedir}/collectd/network_parse.h
%{_includedir}/collectd/server.h
%{_includedir}/collectd/types.h
%{_libdir}/pkgconfig/libcollectdclient.pc
%{_libdir}/libcollectdclient.so

%files -n libcollectdclient
%{_libdir}/libcollectdclient.so.1
%{_libdir}/libcollectdclient.so.1.1.0

%files -n collectd-utils
%{_bindir}/collectd-nagios
%{_bindir}/collectd-tg
%{_bindir}/collectdctl
%{_mandir}/man1/collectdctl.1*
%{_mandir}/man1/collectd-nagios.1*
%{_mandir}/man1/collectd-tg.1*

%files amqp
%{_libdir}/collectd/amqp.so

%files amqp1
%{_libdir}/collectd/amqp1.so

%files apache
%{_libdir}/collectd/apache.so
%config(noreplace) %{_sysconfdir}/collectd.d/apache.conf

%files ascent
%{_libdir}/collectd/ascent.so

%files bind
%{_libdir}/collectd/bind.so

%files chrony
%{_libdir}/collectd/chrony.so

%files curl
%{_libdir}/collectd/curl.so

%files curl_xml
%{_libdir}/collectd/curl_xml.so

%files disk
%{_libdir}/collectd/disk.so

%files dbi
%{_libdir}/collectd/dbi.so

%files dns
%{_libdir}/collectd/dns.so
%config(noreplace) %{_sysconfdir}/collectd.d/dns.conf

%files drbd
%{_libdir}/collectd/drbd.so

%files email
%{_libdir}/collectd/email.so
%config(noreplace) %{_sysconfdir}/collectd.d/email.conf
%doc %{_mandir}/man5/collectd-email.5*

%ifarch %{java_arches}
%files generic-jmx
%{_datadir}/collectd/java/generic-jmx.jar
%endif

%files gps
%{_libdir}/collectd/gps.so

%files hugepages
%{_libdir}/collectd/hugepages.so

%files infiniband
%{_libdir}/collectd/infiniband.so

%files ipmi
%{_libdir}/collectd/ipmi.so
%config(noreplace) %{_sysconfdir}/collectd.d/ipmi.conf

%files iptables
%{_libdir}/collectd/iptables.so

%files ipvs
%{_libdir}/collectd/ipvs.so

%ifarch %{java_arches}
%files java
%{_libdir}/collectd/java.so
%dir %{_datadir}/collectd/java/
%{_datadir}/collectd/java/collectd-api.jar
%doc %{_mandir}/man5/collectd-java.5*
%endif

%files lua
%{_mandir}/man5/collectd-lua*
%{_libdir}/collectd/lua.so

%files mcelog
%{_libdir}/collectd/mcelog.so

%files mdevents
%{_libdir}/collectd/mdevents.so

%files memcachec
%{_libdir}/collectd/memcachec.so

%files modbus
%{_libdir}/collectd/modbus.so

%files mqtt
%{_libdir}/collectd/mqtt.so

%files mysql
%{_libdir}/collectd/mysql.so
%config(noreplace) %{_sysconfdir}/collectd.d/mysql.conf

%files netlink
%{_libdir}/collectd/netlink.so

%files nginx
%{_libdir}/collectd/nginx.so
%config(noreplace) %{_sysconfdir}/collectd.d/nginx.conf

%files notify_desktop
%{_libdir}/collectd/notify_desktop.so

%files notify_email
%{_libdir}/collectd/notify_email.so

%ifnarch s390 s390x
%files nut
%{_libdir}/collectd/nut.so
%config(noreplace) %{_sysconfdir}/collectd.d/nut.conf
%endif

%if 0%{?fedora}
%files onewire
%{_libdir}/collectd/onewire.so
%config(noreplace) %{_sysconfdir}/collectd.d/onewire.conf
%endif

%files openldap
%{_libdir}/collectd/openldap.so

%files -n perl-Collectd
%doc perl-examples/*
%{_libdir}/collectd/perl.so
%{perl_vendorlib}/Collectd.pm
%{perl_vendorlib}/Collectd/
%config(noreplace) %{_sysconfdir}/collectd.d/perl.conf
%doc %{_mandir}/man5/collectd-perl.5*
%doc %{_mandir}/man3/Collectd::Unixsock.3pm*

%files pinba
%{_libdir}/collectd/pinba.so

%files ping
%{_libdir}/collectd/ping.so
%config(noreplace) %{_sysconfdir}/collectd.d/ping.conf

%files postgresql
%{_libdir}/collectd/postgresql.so
%config(noreplace) %{_sysconfdir}/collectd.d/postgresql.conf
%{_datadir}/collectd/postgresql_default.conf

%files python
%{_libdir}/collectd/python.so
%doc %{_mandir}/man5/collectd-python.5*

%files redis
%{_libdir}/collectd/redis.so

%files rrdcached
%{_libdir}/collectd/rrdcached.so

%files rrdtool
%{_libdir}/collectd/rrdtool.so
%config(noreplace) %{_sysconfdir}/collectd.d/rrdtool.conf

%ifnarch ppc sparc sparc64
%files sensors
%{_libdir}/collectd/sensors.so
%config(noreplace) %{_sysconfdir}/collectd.d/sensors.conf
%endif

%files smart
%{_libdir}/collectd/smart.so

%files snmp
%{_libdir}/collectd/snmp.so
%config(noreplace) %{_sysconfdir}/collectd.d/snmp.conf
%doc %{_mandir}/man5/collectd-snmp.5*

%files snmp_agent
%{_libdir}/collectd/snmp_agent.so

%files synproxy
%{_libdir}/collectd/synproxy.so

%files varnish
%{_libdir}/collectd/varnish.so

%ifnarch ppc sparc sparc64
%files virt
%{_libdir}/collectd/virt.so
%config(noreplace) %{_sysconfdir}/collectd.d/libvirt.conf
%endif

%files web
%{_datadir}/collectd/collection3/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/collectd.conf
%config(noreplace) %{_sysconfdir}/collection.conf

%files write_http
%{_libdir}/collectd/write_http.so

%files write_kafka
%{_libdir}/%{name}/write_kafka.so

%files write_mongodb
%{_libdir}/%{name}/write_mongodb.so

%files write_prometheus
%{_libdir}/collectd/write_prometheus.so

%files write_redis
%{_libdir}/collectd/write_redis.so

%files write_riemann
%{_libdir}/collectd/write_riemann.so

%files write_sensu
%{_libdir}/collectd/write_sensu.so

%files write_syslog
%{_libdir}/collectd/write_syslog.so

%files write_tsdb
%{_libdir}/collectd/write_tsdb.so

%if 0%{?fedora}
%ifarch x86_64
%files xencpu
%{_libdir}/collectd/xencpu.so
%endif
%endif

%files zookeeper
%{_libdir}/collectd/zookeeper.so

%changelog
%autochangelog
