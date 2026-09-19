%global source0_hash 1f2fb2dc1172770aa5a09d39738a44d8b753cc5e2e25e306ca78682f9fea0b4f

Name:		ndisc6
Version:	1.0.8
Release:	5%{?dist}
Summary:	IPv6 diagnostic tools

License:	GPL-2.0-only OR GPL-3.0-only
URL:		https://www.remlab.net/ndisc6/
Source0:	https://www.remlab.net/files/ndisc6/ndisc6-%{version}.tar.bz2
Source1:	https://www.remlab.net/files/ndisc6/ndisc6-%{version}.tar.bz2.asc
# gpg2 --recv-key 0x772D56C80CA8ABF9C475FCA34E3557690BEE0224
# gpg2 --export --export-options export-minimal 0x772D56C80CA8ABF9C475FCA34E3557690BEE0224 > 772D56C80CA8ABF9C475FCA34E3557690BEE0224.gpg
Source2:	772D56C80CA8ABF9C475FCA34E3557690BEE0224.gpg
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	gnupg2
BuildRequires:	perl-generators

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

%files -f %{name}.lang
%license COPYING 
%doc README
%{_sysconfdir}/rdnssd
%{_bindir}/addr2name
%{_bindir}/dnssort
%{_bindir}/name2addr
%{_bindir}/tcpspray
%{_bindir}/tcpspray6
%{_sbindir}/ndisc6
%{_sbindir}/rdisc6
%{_sbindir}/rdnssd
%{_sbindir}/rltraceroute6
%{_sbindir}/tcptraceroute6
%{_sbindir}/tracert6
%doc %{_mandir}/man1/addr2name.1.gz
%doc %{_mandir}/man1/dnssort.1.gz
%doc %{_mandir}/man1/name2addr.1.gz
%doc %{_mandir}/man1/tcpspray.1.gz
%doc %{_mandir}/man1/tcpspray6.1.gz
%doc %{_mandir}/man8/ndisc6.8.gz
%doc %{_mandir}/man8/rdisc6.8.gz
%doc %{_mandir}/man8/rdnssd.8.gz
%doc %{_mandir}/man8/rltraceroute6.8.gz
%doc %{_mandir}/man8/tcptraceroute6.8.gz
%doc %{_mandir}/man8/tracert6.8.gz

%changelog
%autochangelog
