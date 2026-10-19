%global source0_hash c20141a382eee00b4af53697b318c785248f3df841af35a50ead25f217276d90
%bcond check 1
%global goipath         github.com/facebook/time
%global date            20260107
%global commit          dbb45295c8620a9de7800f5e2650e37ffbbd03dc
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%gometa -L -f
%undefine distprefix
%global common_description %{expand:
Meta's Time libraries.}
Name:           golang-github-facebook-time
Version:        0^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Meta's Time libraries
License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/time-%{commit}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  libpcap-devel
# /oreon:deps
%description %{common_description}

%package vendor-licenses
Summary:        License files for Meta Time tools' dependencies
BuildArch:      noarch
%description vendor-licenses %{common_description}

This package contains the license files that ship with the third-party
Go modules used to build Meta's Time utilities.

%package -n calnex
Summary:        CLI for a Calnex Sentinel device
Requires:       %{name}-vendor-licenses = %{version}-%{release}
%description -n calnex
- calnex CLI supports several basic commands such as:
- Firmware upgrade
- Configuration of the device
- Measurement data export
- Device reboot
- Device clear
- Device problem report export

%package -n ntpcheck
Summary:        CLI to perform various NTP-related tasks
Requires:       %{name}-vendor-licenses = %{version}-%{release}
%description -n ntpcheck
ntpcheck is a CLI to perform various NTP-related tasks:
- replacement for ntptime and ntpdate commands
- human-readable diagnostics for typical problems with NTP based on data
  from chrony/ntpd
- server stats and peer stats taken from chrony/ntpd with output in JSON
 
%package -n ntpresponder
Summary:        Simple NTP server implementation with kernel timestamps support
Requires:       %{name}-vendor-licenses = %{version}-%{release}
Provides:       responder = %{version}-%{release}
Obsoletes:      responder < 0-0.6
%description -n ntpresponder
ntpresponder is a simple NTP server implementation with kernel timestamps
support, designed for scale and security.

%package -n     pshark
Summary:        Simple tool to print PTP packets from pcap/pcapng captures
Requires:       %{name}-vendor-licenses = %{version}-%{release}
%description -n pshark
pshark is a simple tool to read pcap/pcapng captures and parse and print PTP
packets from there. Allows to test our protocol parser implementation against
arbitrary tcpdump capture. Also the code shows integration with GoPacket
library.

%package -n     ptpcheck
Summary:        CLI to perform various PTP-related tasks
Requires:       %{name}-vendor-licenses = %{version}-%{release}
%description -n ptpcheck
CLI and library to perform various PTP-related tasks, including:
- reporting stats taken from local PTP instance in JSON format
- running basic unicast client to showcase or debug PTP protocol internals
- running human-readable diagnostics for basic problems with PTP based on data
  from local PTP client (ptp4l)
- comparing system time with PHC time
- mapping PHC devices to network cards and vice versa
- sync 2 PHCs

%package -n     ptp4u
Summary:        Scalable unicast PTP server supporting PTP and SPTP
Requires:       %{name}-vendor-licenses = %{version}-%{release}
%description -n ptp4u
ptp4u is a scalable unicast PTP server supporting PTP and SPTP.

%package -n     sptp
Summary:        Scalable unicast SPTP client.
Requires:       %{name}-vendor-licenses = %{version}-%{release}
%description -n sptp
sptp is a scalable unicast SPTP client.

%package -n     ziffy
Summary:        CLI tool to triangulate switches that are not operating correctly as PTP Transparent Clocks.
Requires:       %{name}-vendor-licenses = %{version}-%{release}
%description -n ziffy
CLI tool to triangulate datacenter switches that are not operating correctly as PTP Transparent Clocks.
Ziffy sends PTP SYNC/DELAY_REQ packets between two hosts to get data about the topology.
It supports sending packets from a range of source ports to encourage hashing of
traffic over multiple paths. In case the hashing is done using only destination IP and source IP, Ziffy can
target multiple IPs in the same /64 prefix as the destination.

%package -n     fbclock
Summary:        Fbclock daemon to calculate and publish WOU values
Requires:       %{name}-vendor-licenses = %{version}-%{release}
%description -n fbclock
Fbclock is used to calculate and publish Window of Uncertainty values in shared memory
accessible via fbclock-bin or C API

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

cd cmd/fbclock-bin
%make_build
mv fbclock-bin %{gobuilddir}/bin/fbclock-bin
cd -
%global gomodulesmode GO111MODULE=on
for cmd in calnex c4u ntpcheck ntpresponder pshark ptpcheck ptp4u sptp ziffy fbclock-daemon; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/cmd/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles calnex usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ntpcheck usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ntpresponder usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pshark usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ptpcheck usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ptp4u usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles sptp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ziffy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles fbclock usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%ifarch s390x
rm -f timestamp/timestamp_linux_test.go
%endif
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list
%files -n golang-github-facebook-time-vendor-licenses -f %{oreon_filedir}/golang-github-facebook-time-vendor-licenses.list
%files -n calnex -f %{oreon_filedir}/calnex.list
%files -n ntpcheck -f %{oreon_filedir}/ntpcheck.list
%files -n ntpresponder -f %{oreon_filedir}/ntpresponder.list
%files -n pshark -f %{oreon_filedir}/pshark.list
%files -n ptpcheck -f %{oreon_filedir}/ptpcheck.list
%files -n ptp4u -f %{oreon_filedir}/ptp4u.list
%files -n sptp -f %{oreon_filedir}/sptp.list
%files -n ziffy -f %{oreon_filedir}/ziffy.list
%files -n fbclock -f %{oreon_filedir}/fbclock.list

%changelog

%autochangelog
