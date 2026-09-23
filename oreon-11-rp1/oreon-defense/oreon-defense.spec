Name:           oreon-defense
Version:        1.0.2
Release:        1%{?dist}
Summary:        Oreon security system with real-time protection
License:        GPL-3.0-or-later
URL:            https://oreonhq.com
Source0:        https://tarballs.oreonhq.com/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-devel
BuildRequires:  openssl-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  json-devel
BuildRequires:  systemd-rpm-macros

Requires:       qt6-qtbase
Requires:       qt6-qtbase-gui
Requires:       openssl-libs
Requires:       yaml-cpp
Requires:       systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Straightforward protection and visibility with real-time alerts.

%prep
%autosetup

%build
%cmake -DOREON_BUILD_TESTS=OFF
%cmake_build

%install
%cmake_install
install -D -m 0755 scripts/trigger-scan.sh %{buildroot}%{_libexecdir}/oreon-defense/trigger-scan.sh
mkdir -p %{buildroot}%{_localstatedir}/lib/oreon-defense/quarantine
mkdir -p %{buildroot}%{_sysconfdir}/oreon-defense

%post
%systemd_post oreon-defense.service
%systemd_post oreon-defense-scan.timer
if [ -x /usr/bin/systemctl ]; then
  systemctl daemon-reload >/dev/null 2>&1 || :
  systemctl enable --now oreon-defense.service >/dev/null 2>&1 || :
  systemctl enable --now oreon-defense-scan.timer >/dev/null 2>&1 || :
fi
if [ -x /usr/bin/dbus-send ]; then
  dbus-send --system --type=method_call --dest=org.freedesktop.DBus \
    /org/freedesktop/DBus org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :
fi
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -f %{_datadir}/icons/hicolor >/dev/null 2>&1 || :
fi

%preun
%systemd_preun oreon-defense.service
%systemd_preun oreon-defense-scan.timer

%postun
%systemd_postun_with_restart oreon-defense.service
%systemd_postun oreon-defense-scan.timer

%files
%license LICENSE
%doc README.md
%{_bindir}/oreon-defense
%{_bindir}/oreon-defense-daemon
%{_libexecdir}/oreon-defense/trigger-scan.sh
%{_datadir}/applications/oreon-defense.desktop
%{_datadir}/oreon-defense/
%{_datadir}/icons/hicolor/*/apps/oreon-defense.*
%{_datadir}/polkit-1/actions/org.oreon.defense.policy
%{_datadir}/dbus-1/system.d/org.oreon.Defense1.conf
%{_unitdir}/oreon-defense.service
%{_unitdir}/oreon-defense-scan.service
%{_unitdir}/oreon-defense-scan.timer
%config(noreplace) %{_sysconfdir}/oreon-defense/config.json
%dir %{_localstatedir}/lib/oreon-defense
%dir %{_localstatedir}/lib/oreon-defense/quarantine

%changelog
%autochangelog