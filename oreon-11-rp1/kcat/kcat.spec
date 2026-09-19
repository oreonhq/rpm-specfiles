%global source0_hash a2daa5a14c43522153241a1d8a7ba3a51aa2a76f53a957907e18c79beec4a3a3

%global forgeurl https://github.com/edenhill/kcat
Version:         1.7.1
%global ref      %{version}
%forgemeta
Name:            kcat
Release:         9%{?dist}
Summary:         Generic command line non-JVM Apache Kafka producer and consumer

License:         BSD-2-Clause
URL:             %{forgeurl}
Source:          %{forgesource}

BuildRequires:   gcc
BuildRequires:   librdkafka-devel

Provides:        kafkacat = %{version}-%{release}

%description
kcat is a generic non-JVM producer and consumer for Apache Kafka >=0.8, like a
netcat for Kafka.

In producer mode kcat reads messages from stdin, delimited with a configurable
delimiter (-D, defaults to newline), and produces them to the provided Kafka
cluster (-b), topic (-t) and partition (-p).

In consumer mode kcat reads messages from a topic and partition and prints them
to stdout using the configured message delimiter.

There's also support for the Kafka >=0.9 high-level balanced consumer, use the
-G <group> switch and provide a list of topics to join the group.

kcat also features a Metadata list (-L) mode to display the current state of the
Kafka cluster and its topics and partitions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
sed -i -e 's/echo $(INSTALL)/$(INSTALL)/g' Makefile

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/kcat
%{_mandir}/man1/kcat.1.gz

%changelog
%autochangelog
