%global source0_hash fff28052d0d93d136fe8d66fadf134c037156c0196933bf9c0a798276e0c3344
Name:           aprsdigi
Version:        3.10.0
Release:        1%{?dist}
Summary:        AX.25 Automatic Position Reporting System
License:        GPL-2.0-only
URL:            https://github.com/n2ygk/aprsdigi/releases
Source0:        https://github.com/n2ygk/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         aprsdigi-c99.patch
Requires:       kernel-modules-extra
Requires:       ax25-tools
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libax25-devel
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
Aprsdigi is a specialized Amateur Packet Radio (AX.25) UI-frame digipeater for
the Automatic Position Reporting Systems, APRS(tm). It uses the Linux kernel
AX.25 network stack as well as the SOCK_PACKET facility to listen for packets
on one or more radio interfaces (ports) and repeat those packets -- with
several possible modifications -- on the same or other interfaces. Aprsdigi can
also use the Internet to tunnel connections among other APRS digipeaters and
nodes using IPv4 or IPv6 UDP unicast or multicast.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
install -D -m 644 aprsdigi.service %{buildroot}%{_unitdir}/aprsdigi.service
install -D -m 644 aprsbeacon.service %{buildroot}%{_unitdir}/aprsbeacon.service
install -D -m 644 aprsdigi.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/aprsdigi
mkdir -p %{buildroot}%{_sysconfdir}/ax25
echo > %{buildroot}%{_sysconfdir}/ax25/%{name}.conf << EOL
EOL
%oreon_autofiles main

%post

%systemd_post aprsdigi.service
%systemd_post aprsbeacon.service
%preun

%systemd_preun aprsdigi.service
%systemd_preun aprsbeacon.service
%postun

%systemd_postun_with_restart aprsdigi.service 
%systemd_postun_with_restart aprsbeacon.service 
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
