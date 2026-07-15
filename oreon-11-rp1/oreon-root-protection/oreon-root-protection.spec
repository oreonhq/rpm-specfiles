%global source0_hash 78046571027e42ac14776dcbe2e53ad4679ac49c677251a13523b3dc92afc85c

Name:           oreon-root-protection
Version:        1.0.7
Release:        1%{?dist}
Summary:        Production system snapshots and GRUB rollback for ext4 on LVM thin

License:        GPL-3.0-only
URL:            https://github.com/oreonhq/root-protection
Source0:        https://tarballs.oreonhq.com/root-protection-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

Requires:       python3 >= 3.9
Requires:       snapper
Requires:       lvm2
Requires:       boom-boot
Requires:       util-linux
Requires:       grub2-tools
Requires:       systemd
Recommends:     dnf
Recommends:      python3-dnf
Recommends:      libdnf5-plugin-actions

Provides:       root-protection = %{version}-%{release}

%description
Adds CoW snapshots for an ext4 root on LVM thin, keeps a recoverable timeline
(daily and package transactions), syncs boom/GRUB rollback entries, watches
thin pool pressure, and soft-guards catastrophic interactive root commands.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n root-protection-%{version}
rm -rf .git .github tests/__pycache__ src/rpctl/__pycache__

%install
%make_install PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir} UNITDIR=%{_unitdir} \
  LIBEXECDIR=%{_libexecdir} PYTHON=%{__python3}
printf '%s\n' '%{version}' > %{buildroot}%{_prefix}/lib/root-protection/VERSION

%check
make check PYTHON=%{__python3}

%files
%license LICENSE
%{_bindir}/root-protection
%dir %{_prefix}/lib/root-protection
%dir %{_prefix}/lib/root-protection/rpctl
%{_prefix}/lib/root-protection/root-protection.py
%{_prefix}/lib/root-protection/rpctl/*.py
%{_prefix}/lib/root-protection/VERSION
%{_libexecdir}/root-protection/dnf-hook
%{_libexecdir}/root-protection/ensure-boom-profile
%{_libexecdir}/root-protection/boom-create-entry
%{_libexecdir}/root-protection/restore-grub-default
%{_libexecdir}/root-protection/fix-grub-layout
%{_libexecdir}/root-protection/emergency-fix-grub.sh
%{_libexecdir}/root-protection/rp-conf-get.awk
%{_libexecdir}/root-protection/guard-lib.sh
%{_unitdir}/root-protection-snapshot.service
%{_unitdir}/root-protection-snapshot.timer
%{_unitdir}/root-protection-health.service
%{_unitdir}/root-protection-health.timer
%{_datadir}/root-protection/config.toml
%{_datadir}/doc/root-protection/
%config(noreplace) %{_sysconfdir}/root-protection/config.toml
%config(noreplace) %{_sysconfdir}/root-protection/patterns.toml
%config(noreplace) %{_sysconfdir}/profile.d/root-protection-guard.sh
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/actions.d/root-protection.actions
%config(noreplace) %{_sysconfdir}/dnf/plugins/root_protection.conf
%config(noreplace) %{_sysconfdir}/grub.d/42_root-protection
%{python3_sitelib}/dnf-plugins/root_protection.py
/usr/local/bin/sudo
%dir %{_localstatedir}/lib/root-protection
%dir %{_localstatedir}/log/root-protection
%dir /boot/root-protection
%dir /boot/root-protection/bls

%post
%systemd_post root-protection-snapshot.timer root-protection-health.timer

%preun
%systemd_preun root-protection-snapshot.timer root-protection-health.timer

%postun
%systemd_postun_with_restart root-protection-snapshot.timer root-protection-health.timer

%changelog
%autochangelog
