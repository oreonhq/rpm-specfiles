%global source0_hash 6c84b6cdcc21ebea6daeb8c5356dcdfd8681f4981a734f8485ed0b31fc30aadd

Summary:        Client for Secure Socket Tunneling Protocol (SSTP) VPNs
Name:           sstp-client
Version:        1.0.20
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://gitlab.com/sstp-project/sstp-client
Source0:        https://gitlab.com/sstp-project/sstp-client/-/releases/%{version}/downloads/dist-gzip/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  ppp-devel

Requires:       ppp

%description
sstp-client is a client implementation of the Microsoft Secure Socket
Tunneling Protocol (SSTP) for Linux, used to establish PPP over SSL VPN
connections to Windows Server RRAS gateways. Consumed by
NetworkManager-sstp.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and pkgconfig file for building the sstp-client pppd plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files
%license COPYING
%doc AUTHORS README
%{_sbindir}/sstpc
%{_libdir}/pppd/*/sstp-pppd-plugin.so
%{_mandir}/man8/sstpc.8*

%files devel
%{_includedir}/sstp-client/
%{_libdir}/pkgconfig/sstp-client-1.0.pc

%changelog
%autochangelog
