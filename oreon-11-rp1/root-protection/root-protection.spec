Name:           root-protection
Version:        2.0.0
Release:        1%{?dist}
Summary:        Universal backup, restore, and root protection for Oreon Linux
License:        GPL-3.0-only
URL:            https://oreonhq.com
Source0:        https://tarballs.oreonhq.com/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-devel
Requires:       rsync
Requires:       grub2-tools
Requires:       tar
Requires:       zstd
Requires:       polkit
Requires:       util-linux
Recommends:     python3-dnf
Recommends:      breeze

%description
Oreon Root Protection takes space-efficient hardlink snapshots of / on any
filesystem that supports hardlinks (ext4, xfs, btrfs), optional native btrfs
subvolume snapshots, external tar+zstd backups, GRUB overlay rollback,
permanent merge restore, soft interactive root guard, and dnf transaction
snapshots. Protect root without making it immutable.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DORP_BUILD_GUI=ON -DORP_BUILD_TESTS=OFF
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE
install -d %{buildroot}%{_sysconfdir}/root-protection
install -d %{buildroot}%{_localstatedir}/lib/root-protection/snaps
install -d %{buildroot}%{_localstatedir}/lib/root-protection/backups
install -d %{buildroot}%{_localstatedir}/log/root-protection
install -d %{buildroot}%{_libexecdir}/root-protection
install -d %{buildroot}/boot/root-protection/bls
# dnf4 plugin path varies; also drop a copy under libexec for the hook
install -D -m 0644 hooks/dnf/root_protection.conf %{buildroot}%{_sysconfdir}/dnf/plugins/root_protection.conf
install -D -m 0644 hooks/dnf/root_protection.py %{buildroot}%{python3_sitelib}/dnf-plugins/root_protection.py
install -D -m 0755 hooks/dnf5/dnf-hook %{buildroot}%{_libexecdir}/root-protection/dnf-hook
install -D -m 0644 hooks/dnf5/rp-conf-get.awk %{buildroot}%{_libexecdir}/root-protection/rp-conf-get.awk
if [ -f hooks/dnf5/root-protection.actions ]; then
  install -D -m 0644 hooks/dnf5/root-protection.actions %{buildroot}%{_datadir}/dnf5/libdnf5-plugins/actions.d/root-protection.actions
fi
install -D -m 0755 grub/overlay-init %{buildroot}%{_libexecdir}/root-protection/overlay-init
install -D -m 0755 scripts/fix-grub-layout %{buildroot}%{_libexecdir}/root-protection/fix-grub-layout
install -D -m 0755 grub/42_root-protection %{buildroot}%{_sysconfdir}/grub.d/42_root-protection
install -D -m 0755 guard/guard-lib.sh %{buildroot}%{_libexecdir}/root-protection/guard-lib.sh
install -D -m 0644 guard/patterns.toml %{buildroot}%{_datadir}/root-protection/patterns.toml
install -D -m 0644 guard/patterns.toml %{buildroot}%{_sysconfdir}/root-protection/patterns.toml
install -D -m 0644 guard/root-protection-guard.sh %{buildroot}%{_sysconfdir}/profile.d/root-protection-guard.sh
install -D -m 0644 config/config.toml %{buildroot}%{_sysconfdir}/root-protection/config.toml
install -D -m 0644 packaging/org.oreon.RootProtection.desktop %{buildroot}%{_datadir}/applications/org.oreon.RootProtection.desktop
install -D -m 0644 polkit/org.oreon.RootProtection.policy %{buildroot}%{_datadir}/polkit-1/actions/org.oreon.RootProtection.policy
install -D -m 0644 systemd/root-protection-snapshot.service %{buildroot}%{_unitdir}/root-protection-snapshot.service
install -D -m 0644 systemd/root-protection-snapshot.timer %{buildroot}%{_unitdir}/root-protection-snapshot.timer
install -D -m 0644 systemd/root-protection-health.service %{buildroot}%{_unitdir}/root-protection-health.service
install -D -m 0644 systemd/root-protection-health.timer %{buildroot}%{_unitdir}/root-protection-health.timer
install -D -m 0644 systemd/root-protection-weekly.service %{buildroot}%{_unitdir}/root-protection-weekly.service
install -D -m 0644 systemd/root-protection-weekly.timer %{buildroot}%{_unitdir}/root-protection-weekly.timer
install -D -m 0644 systemd/orpd.service %{buildroot}%{_unitdir}/orpd.service

%pre
getent group root-protection >/dev/null || groupadd -r root-protection 2>/dev/null || true

%post
# dirs + first-boot defaults so install = ready to protect
mkdir -p /var/lib/root-protection/snaps /var/lib/root-protection/backups /var/log/root-protection /boot/root-protection/bls
chmod 700 /var/lib/root-protection/snaps /var/lib/root-protection/backups 2>/dev/null || true
if [ ! -f /etc/root-protection/config.toml ]; then
  cp -n /usr/share/doc/root-protection/config.toml /etc/root-protection/config.toml 2>/dev/null || true
fi
%systemd_post root-protection-snapshot.timer root-protection-weekly.timer root-protection-health.timer orpd.service
systemctl enable --now root-protection-snapshot.timer root-protection-weekly.timer root-protection-health.timer >/dev/null 2>&1 || true
systemctl enable --now orpd.service >/dev/null 2>&1 || true
# mark enabled and take baseline when possible
if [ -x /usr/bin/root-protection ]; then
  /usr/bin/root-protection set general.enabled=true >/dev/null 2>&1 || true
  /usr/bin/root-protection enable >/dev/null 2>&1 || true
fi
# refresh grub submenu if tools present
if [ -x /usr/libexec/root-protection/fix-grub-layout ]; then
  /usr/libexec/root-protection/fix-grub-layout >/dev/null 2>&1 || true
fi

%preun
%systemd_preun root-protection-snapshot.timer root-protection-weekly.timer root-protection-health.timer orpd.service
if [ $1 -eq 0 ] && [ -x /usr/bin/root-protection ]; then
  /usr/bin/root-protection disable >/dev/null 2>&1 || true
fi

%postun
%systemd_postun_with_restart orpd.service
if [ $1 -eq 0 ]; then
  systemctl disable --now root-protection-snapshot.timer root-protection-weekly.timer root-protection-health.timer orpd.service >/dev/null 2>&1 || true
fi

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/root-protection/config.toml
%config(noreplace) %{_sysconfdir}/root-protection/patterns.toml
%config(noreplace) %{_sysconfdir}/dnf/plugins/root_protection.conf
%config(noreplace) %{_sysconfdir}/profile.d/root-protection-guard.sh
%{_sysconfdir}/grub.d/42_root-protection
%{_bindir}/root-protection
%{_bindir}/orpd
%{_bindir}/oreon-root-protection
%{_libexecdir}/root-protection/
%{_unitdir}/root-protection-snapshot.service
%{_unitdir}/root-protection-snapshot.timer
%{_unitdir}/root-protection-health.service
%{_unitdir}/root-protection-health.timer
%{_unitdir}/root-protection-weekly.service
%{_unitdir}/root-protection-weekly.timer
%{_unitdir}/orpd.service
%{_datadir}/applications/org.oreon.RootProtection.desktop
%{_datadir}/polkit-1/actions/org.oreon.RootProtection.policy
%{_datadir}/root-protection/
%pycached %{python3_sitelib}/dnf-plugins/root_protection.py
%{_datadir}/dnf5/libdnf5-plugins/actions.d/root-protection.actions
%dir %{_localstatedir}/lib/root-protection
%dir %{_localstatedir}/lib/root-protection/snaps
%dir %{_localstatedir}/lib/root-protection/backups
%dir %{_localstatedir}/log/root-protection

%changelog
%autochangelog
