%global source0_hash ecacfc7f18d87f4ff503198177e51a83316b59b4646f31caa8140fdbfaa40389

Name:           openfortivpn
Version:        1.23.1
Release:        3%{?dist}
Summary:        Client for PPP+SSL VPN tunnel services

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/adrienverge/openfortivpn
Source0:        https://github.com/adrienverge/openfortivpn/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc autoconf automake
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
Requires:       ppp

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a pppd
process and operates the communication between the gateway and this process.

It is compatible with Fortinet VPNs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
autoreconf -fi
%configure --enable-resolvconf --with-resolvconf=/usr/sbin/resolvconf
make %{?_smp_mflags} V=1

%install
%make_install

%files
%{_bindir}/openfortivpn
%{_mandir}/man1/openfortivpn.1*
%{_datadir}/openfortivpn
%{_unitdir}/openfortivpn@.service
%dir %{_sysconfdir}/openfortivpn
%config(noreplace) %{_sysconfdir}/openfortivpn/config
%doc README.md
%license LICENSE LICENSE.OpenSSL

%changelog
%autochangelog
