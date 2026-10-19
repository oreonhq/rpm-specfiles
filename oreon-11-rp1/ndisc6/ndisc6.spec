%global source1_hash 4ed9ec505aaefba569ef8b5f0ba50f787d820cc7a58a65b111aaf52a81fcc1e5
%global source0_hash 1f2fb2dc1172770aa5a09d39738a44d8b753cc5e2e25e306ca78682f9fea0b4f
Name:		ndisc6
Version:	1.0.8
Release:        1%{?dist}
Summary:        IPv6 diagnostic tools
License:	GPL-2.0-only OR GPL-3.0-only
URL:		https://www.remlab.net/ndisc6/
Source0:        https://www.remlab.net/files/ndisc6/ndisc6-%{version}.tar.bz2
Source1:	https://www.remlab.net/files/ndisc6/ndisc6-%{version}.tar.bz2.asc
Source2:	772D56C80CA8ABF9C475FCA34E3557690BEE0224.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
This package gathers a few diagnostic tools for IPv6 networks:
- ndisc6, which performs ICMPv6 Neighbor Discovery in user-land,
- rdisc6, which performs ICMPv6 Router Discovery in user-land,
- rltraceroute6, yet another IPv6 implementation of traceroute,
- tcptraceroute6, a TCP/IPv6-based traceroute implementation,
- tracert6, a ICMPv6 Echo Request based traceroute,
- tcpspray6, a TCP/IP Discard/Echo bandwidth meter.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

%build

%configure --disable-suid-install
%make_build
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
