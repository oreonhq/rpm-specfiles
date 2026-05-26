# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 75fd653745ea0705995c25e6c07b34252ecc2563c6a91b007a3a8c26f29cc252
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary:        A console-based network monitoring utility
Name:           iptraf-ng
Version:        1.2.2
Release:        20%{?dist}
Source0:        https://github.com/iptraf-ng/iptraf-ng/archive/v%{version}.tar.gz
Source1:        %{name}-logrotate.conf
Source2:        %{name}-tmpfiles.conf
URL:            https://github.com/iptraf-ng/iptraf-ng/
License:        GPL-2.0-or-later
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  make
Obsoletes:      iptraf < 3.1
Provides:       iptraf = 3.1

%description
IPTraf-ng is a console-based network monitoring utility.  IPTraf gathers
data like TCP connection packet and byte counts, interface statistics
and activity indicators, TCP/UDP traffic breakdowns, and LAN station
packet and byte counts.  IPTraf-ng features include an IP traffic monitor
which shows TCP flag information, packet and byte counts, ICMP
details, OSPF packet types, and oversize IP packet warnings;
interface statistics showing IP, TCP, UDP, ICMP, non-IP and other IP
packet counts, IP check sum errors, interface activity and packet size
counts; a TCP and UDP service monitor showing counts of incoming and
outgoing packets for common TCP and UDP application ports, a LAN
statistics module that discovers active hosts and displays statistics
about their activity; TCP, UDP and other protocol display filters so
you can view just the traffic you want; logging; support for Ethernet,
FDDI, ISDN, SLIP, PPP, and loop back interfaces; and utilization of the
built-in raw socket interface of the Linux kernel, so it can be used
on a wide variety of supported network cards.

%prep
%oreon_verify_sources
%setup -q

%build
make %{?_smp_mflags} V=1 \
  CFLAGS="-g -O2 -Wall -W -std=gnu99 -Werror=format-security %{optflags}" \
  LDFLAGS="$RPM_LD_FLAGS"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} prefix=%{_prefix} sbindir=%{_sbindir}

# remove everything besides the html and pictures in Documentation
find Documentation -type f | grep -v '\.html$\|\.png$\|/stylesheet' | \
     xargs rm -f

install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/iptraf-ng

install -d -m 0755 %{buildroot}%{_localstatedir}/{log,lib}/iptraf-ng

mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf

mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/

%files
%doc CHANGES FAQ LICENSE README*
%doc Documentation
%{_sbindir}/iptraf-ng
%{_mandir}/man8/iptraf-ng.8*
%{_localstatedir}/log/iptraf-ng
%{_localstatedir}/lib/iptraf-ng
%config(noreplace) %{_sysconfdir}/logrotate.d/iptraf-ng
%dir /run/%{name}/
%{_prefix}/lib/tmpfiles.d/%{name}.conf

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.2-20
- Import
