%global source0_hash 3db95450c5e1efaeea7547af344b5621f4453af3c227f26ec43bcbc79087b045
%global unitdir /usr/lib/systemd/system
Summary:        Layer 2 Tunneling Protocol (L2TP) daemon
Name:           xl2tpd
Version:        1.3.20
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            https://github.com/xelerance/xl2tpd
Source0:        https://github.com/xelerance/xl2tpd/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       ppp
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  systemd-devel
# /oreon:deps
%description
xl2tpd is an implementation of the Layer 2 Tunneling Protocol as defined
by RFC 2661, used to tunnel PPP over UDP. It is commonly paired with an
IPsec stack (such as strongSwan or Libreswan) to provide L2TP/IPsec VPN
connections, and is consumed by NetworkManager-l2tp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%make_build PREFIX=%{_prefix}
%install
make install PREFIX=%{_prefix} \
    SBINDIR=%{buildroot}%{_sbindir} \
    BINDIR=%{buildroot}%{_bindir} \
    MANDIR=%{buildroot}%{_mandir}
install -D -p -m 0644 debian/xl2tpd.service %{buildroot}%{unitdir}/xl2tpd.service
install -D -p -m 0644 examples/xl2tpd.conf %{buildroot}%{_sysconfdir}/xl2tpd/xl2tpd.conf
install -D -p -m 0600 doc/l2tp-secrets.sample %{buildroot}%{_sysconfdir}/xl2tpd/l2tp-secrets
%oreon_autofiles main

%post

%systemd_post xl2tpd.service
%preun

%systemd_preun xl2tpd.service
%postun

%systemd_postun_with_restart xl2tpd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
