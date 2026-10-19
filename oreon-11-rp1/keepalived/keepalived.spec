%global source0_hash 6afd95ddb7d3e0d3b8b8e5b3a489144131b61a01b06d29e883d0c44acc8a36bf
%bcond_without snmp
%bcond_without vrrp
%bcond_without sha1
%bcond_without json
%bcond_without nftables
%bcond_with profile
%bcond_with debug
%global _hardened_build 1
Name: keepalived
Summary:        High Availability monitor built upon LVS, VRRP and service pollers
Version: 2.3.4
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://www.keepalived.org/
Source0:        http://www.keepalived.org/software/keepalived-%{version}.tar.gz
Source1: keepalived.service
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%if %{with snmp}
%endif
%if %{with nftables}
%else
%endif
# oreon:deps
BuildRequires:  file-devel
BuildRequires:  gcc
BuildRequires:  libmnl-devel
BuildRequires:  libnfnetlink-devel
BuildRequires:  libnftnl-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
# /oreon:deps
%description
Keepalived provides simple and robust facilities for load balancing
and high availability to Linux system and Linux based infrastructures.
The load balancing framework relies on well-known and widely used
Linux Virtual Server (IPVS) kernel module providing Layer4 load
balancing. Keepalived implements a set of checkers to dynamically and
adaptively maintain and manage load-balanced server pool according
their health. High availability is achieved by VRRP protocol. VRRP is
a fundamental brick for router failover. In addition, keepalived
implements a set of hooks to the VRRP finite state machine providing
low-level and high-speed protocol interactions. Keepalived frameworks
can be used independently or all together to provide resilient
infrastructures.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Prevent re-running autotools.
touch aclocal.m4 Makefile.in lib/config.h.in configure

%build

%configure \
    %{?with_debug:--enable-debug} \
    %{?with_profile:--enable-profile} \
    %{!?with_vrrp:--disable-vrrp} \
    %{?with_snmp:--enable-snmp --enable-snmp-rfc} \
    %{?with_nftables:--enable-nftables --disable-iptables} \
    %{?with_json:--enable-json} \
    %{?with_sha1:--enable-sha1} \
    --with-init=systemd
%{__make} %{?_smp_mflags} STRIP=/bin/true
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_initrddir}/
rm -rf %{buildroot}%{_sysconfdir}/keepalived/samples/
mv %{buildroot}%{_sysconfdir}/keepalived/keepalived.conf.sample \
   %{buildroot}%{_sysconfdir}/keepalived/keepalived.conf
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/keepalived.service
mkdir -p %{buildroot}%{_libexecdir}/keepalived
%oreon_autofiles main

%post

%systemd_post keepalived.service
%preun

%systemd_preun keepalived.service
%postun

%systemd_postun_with_restart keepalived.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
