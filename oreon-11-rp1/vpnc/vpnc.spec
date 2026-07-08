%global source0_hash 6465a317ea197d1df8bf1c1721fd623e2e94ffb08c760e451bf81b1aea31d8c0

%global commit 7f1274662e26775f47b0bbf296210c2845415e54
%global shortcommit 7f12746

Summary:        Client for Cisco3000 VPN concentrators
Name:           vpnc
Version:        0.5.3.20260629git%{shortcommit}
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://davidepucci.it/doc/vpnc
# Upstream has not tagged a release since 0.5.3 (2008); this is the actively
# maintained streambinder/vpnc fork, pinned to a specific commit for
# reproducibility.
Source0:        https://github.com/streambinder/vpnc/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libgcrypt)

Requires:       iproute

%description
vpnc is a VPN client compatible with Cisco3000 VPN Concentrators, and
Cisco ASA and clones. It supports IPsec (ESP) with Mode Configuration and
Xauth, and is used by NetworkManager-vpnc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{commit}

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix} ETCDIR=%{_sysconfdir}/vpnc MANDIR=%{_mandir}
mkdir -p %{buildroot}%{_sysconfdir}/vpnc
install -m 0644 vpnc.conf %{buildroot}%{_sysconfdir}/vpnc/default.conf

%files
%license LICENSE LICENSE.BSD2
%doc README.md ChangeLog
%{_sbindir}/vpnc
%{_sbindir}/vpnc-disconnect
%{_bindir}/cisco-decrypt
%{_bindir}/pcf2vpnc
%dir %{_sysconfdir}/vpnc
%config(noreplace) %{_sysconfdir}/vpnc/default.conf
%{_mandir}/man1/cisco-decrypt.1*
%{_mandir}/man1/pcf2vpnc.1*

%changelog
%autochangelog
