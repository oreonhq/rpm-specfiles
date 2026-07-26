%global source0_hash dfedc2572cf44d0491eb6d639ad9665d65aeaeaaa1d1a7a38605186ac2229c05

%global commit0 c98f06d942970cdf35dd66ab46840f7d6d567b60
%global date0   20190728
%global scommit %(c=%{commit0}; echo ${c:0:7} )

Name:           ocproxy
Version:        1.60
Release:        16.%{date0}git%{scommit}%{?dist}
Summary:        OpenConnect Proxy

# BSD for both ocproxy and bundled lwip
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/cernekee/%{name}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{scommit}.tar.gz
# PR#11 rebased:
# use latest lwip sources, fix gcc warnings
# drop useless files copied accidently from lwip project
Patch0:         %{name}-1.60-with-lwip-2.1.2.patch

BuildRequires:  automake make gcc
BuildRequires:  libevent-devel

Provides:       bundled(lwip) = 2.1.2
Requires:       openconnect

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

%files
%license LICENSE
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/vpnns
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/vpnns.1*

%changelog
%autochangelog
