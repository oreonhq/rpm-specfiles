%global source0_hash daeb3e0473120541ebfa0d16b9cf4829d797d04cf30348d6c02b9b9a37fc9f05
%global date 20241209
%global commit b2e3ba3c5a593abf203e65a407c3a9de0f998d4a
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
Name:           ngrep
Version:        1.47^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Network layer grep tool
License:        ngrep
URL:            https://github.com/jpr5/ngrep
Source0:        https://github.com/jpr5/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          %{url}/pull/27.patch
Patch:          %{url}/pull/28.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  pcre2-devel
# /oreon:deps
%description
ngrep strives to provide most of GNU grep's common features, applying them
to the network layer. ngrep is a pcap-aware tool that will allow you to
specify extended regular or hexadecimal expressions to match against data
payloads of packets. It currently recognizes TCP, UDP, ICMP, IGMP and Raw
protocols across Ethernet, PPP, SLIP, FDDI, Token Ring, 802.11 and null
interfaces, and understands bpf filter logic in the same fashion as more
common packet sniffing tools, such as tcpdump and snoop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}
# Make sure not to be using bundled libs
rm -r regex-0.12

%build

autoreconf -fiv
%configure \
  --enable-pcre2 \
  --enable-ipv6 \
  --with-pcap-includes=%{_includedir}/pcap \
  --enable-tcpkill
%make_build STRIPFLAG=
%install
install -Ddpm0755 %{buildroot}%{_sbindir} %{buildroot}%{_mandir}/man8
%make_install BINDIR_INSTALL="%{_sbindir}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
