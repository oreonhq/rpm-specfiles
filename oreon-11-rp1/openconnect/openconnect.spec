%global source0_hash 5b32369467db6e5f317aa1ed12cfcbb81ed00bdbc765450b6bfcbdc300944a58
%global source1_hash f0c4d936a382f07711263242699b5e2d85d1ace37136bb78785d352997c17742

Summary:        Open client for Cisco AnyConnect, Juniper and other SSL VPNs
Name:           openconnect
Version:        9.21
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://www.infradead.org/openconnect/
Source0:        https://www.infradead.org/openconnect/download/%{name}-%{version}.tar.gz
# Companion helper script maintained at gitlab.com/openconnect/vpnc-scripts.
# openconnect refuses to build without a vpnc-script present at a known
# location (see its own packaging docs), so we vendor the canonical script.
Source1:        vpnc-script

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libp11)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  krb5-devel

Provides:       vpnc-script

%description
OpenConnect is an SSL VPN client initially created to support Cisco's
AnyConnect SSL VPN, and now also supporting Juniper/Pulse, GlobalProtect,
Fortinet, F5, and Array SSL VPNs. Used as the backend library for
NetworkManager-openconnect and plasma-nm.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and pkgconfig file for building against libopenconnect.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
# passing an explicit --with-vpnc-script path (as opposed to leaving it on
# "auto") skips openconnect's build-time existence/executable check, per
# its own configure.ac; the real script is installed below in %%install.
%configure \
        --disable-static \
        --with-vpnc-script=%{_sysconfdir}/vpnc/vpnc-script \
        --without-openssl-version-check \
        --disable-nls
%make_build

%install
%make_install
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/vpnc/vpnc-script
find %{buildroot} -name '*.la' -delete

%files
%license COPYING.LGPL COPYING.OpenSSL
%doc README NEWS
%{_bindir}/openconnect
%{_libdir}/libopenconnect.so.*
%{_mandir}/man8/openconnect.8*
%dir %{_sysconfdir}/vpnc
%config(noreplace) %{_sysconfdir}/vpnc/vpnc-script

%files devel
%{_includedir}/openconnect.h
%{_libdir}/libopenconnect.so
%{_libdir}/pkgconfig/openconnect.pc

%changelog
%autochangelog
