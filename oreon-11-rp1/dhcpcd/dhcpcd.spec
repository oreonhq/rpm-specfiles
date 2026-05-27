%global source0_hash 06e4c1aaf958523f3fd1c57258c613c6c7ae56b8f1d678fa7943495d5ea6aeb5

%global forgeurl0 https://github.com/NetworkConfiguration/dhcpcd

Name: dhcpcd
Version: 10.3.0
Release: %autorelease
Summary: A minimalistic network configuration daemon with DHCPv4, rdisc and DHCPv6 support
License: BSD-2-Clause AND ISC AND MIT
URL: http://roy.marples.name/projects/%{name}/
# Moved to github
VCS: git:%{forgeurl0}
Source0:        https://github.com/NetworkConfiguration/dhcpcd/releases/download/v10.3.0/dhcpcd-10.3.0.tar.xz
Source1:        https://github.com/NetworkConfiguration/dhcpcd/releases/download/v10.3.0/dhcpcd-10.3.0.tar.xz.asc
Source2: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xa785ed2755955d9e93ea59f6597f97ea9ad45549#/roy-marples.name.asc
Source3: %{name}.service
Source4: %{name}@.service
Source5: systemd-sysusers.conf
Source6: systemd-tmpfiles.conf

BuildRequires: gcc
BuildRequires: systemd-rpm-macros
BuildRequires: chrony
BuildRequires: systemd-devel
%if 0%{?fedora}
# Not in RHEL
BuildRequires: ypbind
%endif
BuildRequires: make
%if 0%{?fedora} || 0%{?rhel} > 8
BuildRequires: gnupg2
%endif
%{?systemd_requires}
%description
The dhcpcd package provides a minimalistic network configuration daemon
that supports IPv4 and IPv6 configuration including configuration discovery
through NDP, DHCPv4 and DHCPv6 protocols.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%if 0%{?fedora} || 0%{?rhel} > 8
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1

%build
%configure \
    --dbdir=/var/lib/%{name} --runstatedir=%{_rundir}
%make_build

%check
%make_build test

%install
export BINMODE=755
%make_install
find %{buildroot} -name '*.la' -delete -print
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}@.service
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d %{buildroot}%{_sharedstatedir}/%{_name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/hooks
%{_datadir}/%{name}/hooks/10-wpa_supplicant
%{_datadir}/%{name}/hooks/15-timezone
%{_datadir}/%{name}/hooks/29-lookup-hostname
%{_datadir}/%{name}/hooks/50-yp.conf
%{_libdir}/%{name}
%{_libexecdir}/%{name}-hooks
%{_libexecdir}/%{name}-run-hooks
%{_mandir}/man5/%{name}.conf.5.gz
%{_mandir}/man8/%{name}-run-hooks.8.gz
%{_mandir}/man8/%{name}.8.gz
%{_sbindir}/%{name}
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%defattr(0644,root,dhcpcd,0755)
%{_sharedstatedir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.3.0-1
- Prepare for Oreon 11 (RP1)
