%global source0_hash f04e143da881cd63c299125b592cfb85e4812abbd146f419a1894c00f2ae6208

%global _hardened_build 1

Name:		addrwatch
Version:	1.0.2
Release:	16%{?dist}
Summary:	Monitoring IPv4/IPv6 and Ethernet address pairings

License:	GPL-3.0-only
URL:		https://github.com/fln/addrwatch
Source0:	%{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.service
Source2:	%{name}.sysconfig

%{?systemd_requires}
BuildRequires:	libpcap-devel, libevent-devel, systemd, mariadb-connector-c-devel, sqlite-devel, gcc
BuildRequires:	autoconf automake
BuildRequires: make

%description
It main purpose is to monitor network and log discovered Ethernet/IP pairings.

Main features of addrwatch:

 * IPv4 and IPv6 address monitoring
 * Monitoring multiple network interfaces with one daemon
 * Monitoring of VLAN tagged (802.1Q) packets.
 * Output to std-out, plain text file, syslog, sqlite3 db, MySQL db
 * IP address usage history preserving output/logging

Addrwatch is extremely useful in networks with IPv6 auto configuration (RFC4862)
enabled. It allows to track IPv6 addresses of hosts using IPv6 privacy
extensions (RFC4941).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Create a sysusers.d config file
cat >addrwatch.sysusers.conf <<EOF
u addrwatch - 'network neighborhoud watch' /var/lib/%{name} -
EOF

%build
autoreconf -fiv
%configure --enable-sqlite3 --enable-mysql LDFLAGS="-I/usr/include/mysql -L/usr/lib64/mysql"
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_unitdir}/
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/addrwatch
mkdir -p %{buildroot}/var/lib/addrwatch

install -m0644 -D addrwatch.sysusers.conf %{buildroot}%{_sysusersdir}/addrwatch.conf

%files
%{_bindir}/addrwatch
%{_bindir}/addrwatch_stdout
%{_bindir}/addrwatch_mysql
%{_bindir}/addrwatch_syslog
%{_mandir}/man8/addrwatch.8*
%{_unitdir}/addrwatch.service
%config(noreplace) %{_sysconfdir}/sysconfig/addrwatch
%license COPYING
%attr(-, addrwatch, addrwatch) /var/lib/addrwatch
%{_sysusersdir}/addrwatch.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
%autochangelog
