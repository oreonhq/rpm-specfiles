%global source0_hash 5963f9383564c641eb81be41d3b6743339adb415a252bed1945ad0f9e53bdd52

Name:    smcroute
Version: 2.5.7
Release: 5%{?dist}

Summary: Static multicast routing for UNIX

#*No copyright* Public domain
#smcroute

#Apple Public Source License 2.0 and/or BSD-4-Clause (University of California-Specific)
#src/ip_mroute.h

#BSD 2-Clause License and/or BSD 2-clause NetBSD License
#src/pidfile.c

#BSD 3-Clause License
#src/queue.h

#GNU General Public License v2.0 or later
#src/cap.c
#src/iface.c
#src/inet.c
#src/inet.h
#ipc.c
#src/log.c
#src/mcgroup.c
#src/mrdisc.c
#src/mrdisc.h
#src/mroute.c
#src/msg.c
#src/notify.c
#src/smcroutectl.c
#src/smcrouted.c
#src/socket.c
#src/socket.h
#src/timer.c
#src/timer.h

#GNU General Public License, Version 2
#COPYING

#ISC License
#lib/strlcat.c
#lib/strlcpy.c
#lib/tempfile.c
#lib/utimensat.c
#src/conf.c
#src/kern.c
#src/kern.h
#src/script.c

License: GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain

URL:     https://github.com/troglobit/smcroute
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf, automake, libtool
BuildRequires: libpcap-devel
BuildRequires: libcap-devel
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: iproute
BuildRequires: lsb_release
BuildRequires: valgrind

%description
SMCRoute is a static multicast routing daemon providing
fine grained control over the multicast forwarding cache (MFC)
in the UNIX kernel. Both IPv4 and IPv6 are fully supported.

SMCRoute can be used as an alternative to dynamic multicast
routers like mrouted, pimd, or pim6sd in setups where static
multicast routes should be maintained and/or no proper IGMP
or MLD signaling exists.

Multicast routes exist in the UNIX kernel as long as a
multicast routing daemon runs. On Linux, multiple multicast
routers can run simultaneously using different multicast
routing tables.

The full documentation of SMCRoute is available in the manual
pages, see smcrouted(8), smcroutectl(8), and smcroute.conf(5).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
./autogen.sh
%configure --enable-mrdisc --enable-test
%make_build

%install
%make_install

%check
pushd test
for i in include.sh join.sh joinlen.sh mem.sh mrcache.sh reload.sh reload6.sh vrfy.sh; do
    unshare -mrun ./"$i"
done
popd

mkdir -p %{buildroot}%{_sysconfdir}
rm -rf %{buildroot}%{_datadir}/doc/smcroute/
mkdir -p %{buildroot}%{_sysconfdir}/smcroute.d

%post
%systemd_post smcroute.service

%preun
%systemd_preun smcroute.service

%postun
%systemd_postun_with_restart smcroute.service

%files
%license COPYING
%doc ChangeLog.md README.md smcroute.conf
%{_sysconfdir}/smcroute.d/
%{_sbindir}/smcroute
%{_sbindir}/smcroutectl
%{_sbindir}/smcrouted
%{_mandir}/man5/smcroute.conf.5*
%{_mandir}/man8/smcroute*
%{_unitdir}/smcroute.service

%changelog
%autochangelog
