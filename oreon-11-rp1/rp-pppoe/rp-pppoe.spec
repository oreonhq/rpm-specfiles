%global source0_hash 41ac34e5db4482f7a558780d3b897bdbb21fae3fef4645d2852c3c0c19d81cea
Name: rp-pppoe
Version: 4.0
Release:        1%{?dist}
Summary:        A PPP over Ethernet client (for xDSL support).
License: GPL-2.0-or-later
Url: https://dianne.skoll.ca/projects/rp-pppoe/
Source0:        https://dianne.skoll.ca/projects/rp-pppoe/download/rp-pppoe-%{version}.tar.gz
Requires: ppp >= 2.4.6
Requires: iproute >= 2.6
Requires: coreutils
Requires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ppp-devel
BuildRequires:  systemd
# /oreon:deps
%description
PPPoE (Point-to-Point Protocol over Ethernet) is a protocol used by
many ADSL Internet Service Providers. This package contains the
Roaring Penguin PPPoE client, a user-mode program that does not
require any kernel modifications. It is fully compliant with RFC 2516,
the official PPPoE specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

cd src
%configure #--docdir=%{_pkgdocdir}
make
%install
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_unitdir}
make -C src install DESTDIR=%{buildroot}
rm -rf %{buildroot}/etc/ppp/plugins
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
