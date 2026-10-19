%global source0_hash 11c15f8fce63f3251e1de40a488c6857cdd549c5f2835177a972d7c92f14eb47
Name:    smcroute
Version: 2.6.0
Release:        1%{?dist}
Summary:        Static multicast routing for UNIX
License: GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain
URL:     https://github.com/troglobit/smcroute
Source0:        https://github.com/troglobit/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  iproute
BuildRequires:  libcap-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  lsb_release
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  valgrind
# /oreon:deps
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
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
