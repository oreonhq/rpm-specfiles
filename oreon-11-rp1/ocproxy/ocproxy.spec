%global source0_hash dfedc2572cf44d0491eb6d639ad9665d65aeaeaaa1d1a7a38605186ac2229c05
%global commit0 c98f06d942970cdf35dd66ab46840f7d6d567b60
%global date0   20190728
%global scommit %(c=%{commit0}; echo ${c:0:7} )
Name:           ocproxy
Version:        1.60
Release:        1%{?dist}
Summary:        OpenConnect Proxy
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/cernekee/%{name}
Source0:        https://github.com/cernekee/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{scommit}.tar.gz
Patch0:         %{name}-1.60-with-lwip-2.1.2.patch
Provides:       bundled(lwip) = 2.1.2
Requires:       openconnect
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  make
# /oreon:deps
%description
OCProxy is a user-level SOCKS and port forwarding proxy for OpenConnect based
on lwIP. When using ocproxy, OpenConnect only handles network activity that 
the user specifically asks to proxy, so the VPN interface no longer "hijacks" 
all network traffic on the host.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n%{name}-%{commit0}
./autogen.sh

%build

%configure --enable-vpnns
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
