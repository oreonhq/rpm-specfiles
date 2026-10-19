%global source0_hash 48b010e7bcdf93e4e4b6e43c53c7f60aa6873d574cbd45a8d86fa7aaeebaff9c
%global       gitname     IPMITOOL
%global       gitversion  1_8_19
Name:         ipmitool
Summary:        Utility for IPMI control
Version:      1_8_19
Release:        1%{?dist}
License:      BSD-3-Clause-Sun
URL:          http://ipmitool.sourceforge.net/
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{gitname}_%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:      openipmi-ipmievd.sysconf
Source2:      ipmievd.service
Source3:      exchange-bmc-os-info.service
Source4:      exchange-bmc-os-info.sysconf
Source5:      set-bmc-url.sh
Source6:      exchange-bmc-os-info
Source7:      enterprise-numbers
Patch3:       ipmitool-1.8.19-set-kg-key.patch
Patch4:       0004-slowswid.patch
Patch5:       0005-sensor-id-length.patch
Patch7:       0007-check-input.patch
Patch14:      0014-lanplus-cipher-retry.patch
Patch100:     0100-fix_buf_overflow.patch
Patch105:     0105-sensor_reading.patch
%{?systemd_requires}
Obsoletes: OpenIPMI-tools < 2.0.14-3
Provides: OpenIPMI-tools = 2.0.14-3
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
BuildRequires:  systemd
# /oreon:deps
%description
This package contains a utility for interfacing with devices that support
the Intelligent Platform Management Interface specification.  IPMI is
an open standard for machine health, inventory, and remote power control.

This utility can communicate with IPMI-enabled devices through either a
kernel driver such as OpenIPMI or over the RMCP LAN protocol defined in
the IPMI specification.  IPMIv2 adds support for encrypted LAN
communications and remote Serial-over-LAN functionality.

It provides commands for reading the Sensor Data Repository (SDR) and
displaying sensor values, displaying the contents of the System Event
Log (SEL), printing Field Replaceable Unit (FRU) information, reading and
setting LAN configuration, and chassis power control.

%package -n ipmievd
Requires: ipmitool
%{?systemd_requires}
BuildRequires: systemd
Summary: IPMI event daemon for sending events to syslog
%description -n ipmievd
ipmievd is a daemon which will listen for events from the BMC that are
being  sent to the SEL and also log those messages to syslog.

%package -n bmc-snmp-proxy
Requires: net-snmp
Requires: exchange-bmc-os-info
BuildArch: noarch
Summary: Reconfigure SNMP to include host SNMP agent within BMC
%description -n bmc-snmp-proxy
Given a host with BMC, this package would extend system configuration
of net-snmp to include redirections to BMC based SNMP.

%package -n exchange-bmc-os-info
Requires: hostname
Requires: ipmitool
BuildArch: noarch
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: make
Summary: Let OS and BMC exchange info
%description -n exchange-bmc-os-info
Given a host with BMC, this package would pass the hostname &
OS information to the BMC and also capture the BMC ip info
for the host OS to use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{gitname}_%{gitversion} -p1

for f in AUTHORS ChangeLog; do
    iconv -f iso-8859-1 -t utf8 < ${f} > ${f}.utf8
    mv ${f}.utf8 ${f}
done

%build

aclocal
libtoolize --automake --copy
autoheader
automake --foreign --add-missing --copy
aclocal
autoconf
automake --foreign
install -Dm 644 %{SOURCE7} .
%configure --disable-dependency-tracking --enable-file-security --disable-intf-free --enable-intf-usb
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/ipmievd.service
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/ipmievd
install -Dm 644 %{SOURCE3} %{buildroot}%{_unitdir}/exchange-bmc-os-info.service
install -Dm 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/exchange-bmc-os-info
install -Dm 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/profile.d/set-bmc-url.sh
install -Dm 755 %{SOURCE6} %{buildroot}%{_libexecdir}/exchange-bmc-os-info
install -Dm 644 contrib/bmc-snmp-proxy.sysconf %{buildroot}%{_sysconfdir}/sysconfig/bmc-snmp-proxy
install -Dm 644 contrib/bmc-snmp-proxy.service %{buildroot}%{_unitdir}/bmc-snmp-proxy.service
install -Dm 755 contrib/bmc-snmp-proxy         %{buildroot}%{_libexecdir}/bmc-snmp-proxy
%oreon_autofiles ipmievd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bmc-snmp-proxy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles exchange-bmc-os-info usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post -n ipmievd

%systemd_post ipmievd.service
%preun -n ipmievd

%systemd_preun ipmievd.service
%postun -n ipmievd

%systemd_postun_with_restart ipmievd.service
%post -n exchange-bmc-os-info

%systemd_post exchange-bmc-os-info.service
%preun -n exchange-bmc-os-info

%systemd_preun exchange-bmc-os-info.service
%postun -n exchange-bmc-os-info

%systemd_postun_with_restart exchange-bmc-os-info.service
%triggerun -- ipmievd < 1.8.11-7

/usr/bin/systemd-sysv-convert --save ipmievd >/dev/null 2>&1 ||:
/sbin/chkconfig --del ipmievd >/dev/null 2>&1 || :
/bin/systemctl try-restart ipmievd.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n ipmievd -f %{oreon_filedir}/ipmievd.list
%files -n bmc-snmp-proxy -f %{oreon_filedir}/bmc-snmp-proxy.list
%files -n exchange-bmc-os-info -f %{oreon_filedir}/exchange-bmc-os-info.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.19-12
- Import
