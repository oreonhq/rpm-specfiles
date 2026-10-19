%global source0_hash c40d33acd97b89c2e943bfd839c19b69e5a7a5997052e2fc9a595602745c0465
Name:           openfortivpn
Version:        1.24.1
Release:        1%{?dist}
Summary:        Client for PPP+SSL VPN tunnel services
License:        GPL-3.0-or-later
URL:            https://github.com/adrienverge/openfortivpn
Source0:        https://github.com/adrienverge/openfortivpn/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       ppp
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
