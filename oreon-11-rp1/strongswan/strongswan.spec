%global source0_hash e518e34e159514f4c6ba80d1f926cb151e0dd4e3a1d94213171234b8b9ae6f55

Summary:        Open source IPsec-based VPN solution
Name:           strongswan
Version:        6.0.7
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            https://www.strongswan.org/
Source0:        https://download.strongswan.org/strongswan-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  openssl-devel
BuildRequires:  gmp-devel
BuildRequires:  systemd-devel
BuildRequires:  pam-devel
BuildRequires:  curl-devel
BuildRequires:  libgcrypt-devel

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
strongSwan is an OpenSource IPsec-based VPN solution for Linux, licensed
under the GPLv2. It supports both the IKEv1 and IKEv2 protocols, and can be
used to secure the IPsec/L2TP and IPsec/IKEv2 connections offered by
NetworkManager-l2tp and other IPsec based VPN plugins.

This build enables the "charon-nm" NetworkManager backend so plasma-nm can
drive strongSwan directly for native IKEv2 VPN connections, in addition to
being the userland IPsec stack consumed by NetworkManager-l2tp.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers for building software against libstrongswan.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%configure \
        --disable-static \
        --enable-nm \
        --enable-openssl \
        --disable-gmp \
        --enable-systemd \
        --enable-swanctl \
        --enable-pki \
        --with-systemdsystemunitdir=%{_unitdir}
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
rm -rf %{buildroot}%{_localstatedir}/run

%post
%systemd_post strongswan.service

%preun
%systemd_preun strongswan.service

%postun
%systemd_postun_with_restart strongswan.service

%files
%license COPYING
%doc NEWS README
%{_sbindir}/ipsec
%{_sbindir}/swanctl
%{_sbindir}/pki
%{_libdir}/libstrongswan.so.*
%{_libdir}/libcharon.so.*
%{_libdir}/libtnccs.so.*
%{_libexecdir}/ipsec/
%{_libdir}/ipsec/
%{_sysconfdir}/strongswan.conf
%{_sysconfdir}/strongswan.d/
%{_sysconfdir}/swanctl/
%{_datadir}/strongswan/
%{_unitdir}/strongswan.service
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%{_includedir}/strongswan/
%{_libdir}/libstrongswan.so
%{_libdir}/libcharon.so
%{_libdir}/libtnccs.so
%{_libdir}/pkgconfig/strongswan.pc

%changelog
%autochangelog
