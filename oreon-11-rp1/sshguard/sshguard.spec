%global source0_hash 997a1e0ec2b2165b4757c42f8948162eb534183946af52efc406885d97cb89fc
Name: sshguard
Version: 2.5.1
Release:        1%{?dist}
License: BSD-3-Clause AND GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
Summary:        Protects hosts from brute-force attacks against SSH and other services
Url: http://www.sshguard.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.conf.in
Source2: %{name}.whitelist
Patch1: 0001-fix-backend-path-in-example.patch
Provides: bundled(fnv) = 5.0.2
Provides: bundled(simclist) = 1.4.4
%if 0%{?use_subpackages}
Requires: %{name}-config = %{version}-%{release}
Recommends: (%{name}-firewalld if firewalld)
Recommends: (%{name}-iptables if iptables-services)
Recommends: (%{name}-nftables if nftables)
%endif
Requires: coreutils
Requires: grep
Requires: systemd
# oreon:deps
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
Sshguard protects hosts from brute-force attacks against SSH and other
services. It aggregates system logs and blocks repeat offenders using one of
several firewall backends.

Sshguard can read log messages from standard input or monitor one or more log
files. Log messages are parsed, line-by-line, for recognized patterns. If an
attack, such as several login failures within a few seconds, is detected, the
offending IP is blocked. Offenders are unblocked after a set interval, but can
be semi-permanently banned using the blacklist option.

%if 0%{?use_subpackages}
%package iptables
Requires: iptables-services
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-config = %{version}-%{release}
Conflicts: %{name}-firewalld %{name}-nftables
Summary: Configuration for iptables backend of SSHGuard
RemovePathPostfixes: .iptables
%description iptables
Sshguard-iptables provides a configuration file for SSHGuard to use iptables
as the firewall backend.

%package firewalld
Requires: firewalld ipset
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-config = %{version}-%{release}
Conflicts: %{name}-iptables %{name}-nftables
Summary: Configuration for firewalld backend of SSHGuard
RemovePathPostfixes: .firewalld
%description firewalld
Sshguard-firewalld provides a configuration file for SSHGuard to use firewalld
as the firewall backend.

%package nftables
Requires: nftables
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-config = %{version}-%{release}
Conflicts: %{name}-firewalld %{name}-iptables
Summary: Configuration for nftables backend of SSHGuard
RemovePathPostfixes: .nftables
%description nftables
Sshguard-nftables provides a configuration file for SSHGuard to use nftables
as the firewall backend.
%endif

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i -e "s|%%{_bindir}|%{_bindir}|g" \
       -e "s|%%{_sbindir}|%{_sbindir}|g" \
       -e "s|%%{_libexecdir}|%{_libexecdir}|g" \
       -e "s|%%{_sysconfdir}|%{_sysconfdir}|g" \
       -e "s|%%{_initddir}|%{_initddir}|g" \
       -e "s|%%{_localstatedir}|%{_localstatedir}|g" \
       -e "s|%%{_sharedstatedir}|%{_sharedstatedir}|g" \
       -e "s|%%{_rundir}|%{_rundir}|g" \
       -e "s|%%{_pkgdocdir}|%{_pkgdocdir}|g" \
       -e "s|%%{name}|%{name}|g" \
       %{SOURCE1} %{SOURCE2}

%build

%{configure} --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --sbindir=%{_sbindir} --libexecdir=%{_libexecdir}/%{name}
%{make_build}
%install
%{make_install}
install -p -d -m 0755 %{buildroot}%{_pkgdocdir}/
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/
install -p -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}/
%if 0%{?use_subpackages}
sed -e "s|__BACKEND__|sshg-fw-firewalld|g" %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf.firewalld
sed -e "s|__BACKEND__|sshg-fw-nft-sets|g" %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf.nftables
sed -e "s|__BACKEND__|sshg-fw-iptables|g" %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf.iptables
chmod 0644 %{buildroot}%{_sysconfdir}/%{name}.conf.*
%endif
install -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.whitelist
install -p -d -m 0755 %{buildroot}%{_unitdir}
sed -i -e "/ExecStartPre=/d" examples/%{name}.service
sed -i -e "s|ExecStart=/usr/local/sbin/sshguard|ExecStart=%{_sbindir}/%{name}|g" examples/%{name}.service
install -p -m 0644 examples/%{name}.service %{buildroot}%{_unitdir}/
rm examples/net.sshguard.plist
rm examples/sshguard.service
%oreon_autofiles main

%check

make check
%post

%systemd_post %{name}.service
%if 0%{?use_subpackages}
%post iptables

if [[ $1 -eq 1 ]]; then
  iptables -N sshguard
  iptables -A INPUT -j sshguard
  iptables-save > /etc/sysconfig/iptables
  ip6tables -N sshguard
  ip6tables -A INPUT -j sshguard
  ip6tables-save > /etc/sysconfig/ip6tables
fi
exit 0
%endif
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
