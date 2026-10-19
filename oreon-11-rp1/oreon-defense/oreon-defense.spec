%global source0_hash 64d756bf4f17df3a316315d4fe27d9abc7a3c7e80394faa2a6b77ee681e72010
Name:           oreon-defense
Version:        1.0.15
Release:        1%{?dist}
Summary:        Oreon security system with real-time protection
License:        GPL-3.0-or-later
URL:            https://oreonhq.com
Source0:        https://tarballs.oreonhq.com/%{name}-%{version}.tar.gz
Requires:       qt6-qtbase
Requires:       qt6-qtbase-gui
Requires:       openssl-libs
Requires:       yaml-cpp
Requires:       clamav-lib
Requires:       (clamav-update or clamav-data)
Requires:       libcurl
Requires:       nftables
Requires:       polkit
Requires:       systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  clamav-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  yaml-cpp-devel
# /oreon:deps
%description
Straightforward protection and visibility with real-time alerts.

%prep
%oreon_prep
%build

%cmake -DOREON_BUILD_TESTS=OFF -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build
%install
%cmake_install
install -D -m 0755 scripts/trigger-scan.sh %{buildroot}%{_libexecdir}/oreon-defense/trigger-scan.sh
install -D -m 0755 scripts/test_installed_detection.sh %{buildroot}%{_libexecdir}/oreon-defense/test_installed_detection.sh
install -D -m 0755 scripts/verify_detection.sh %{buildroot}%{_libexecdir}/oreon-defense/verify_detection.sh
install -D -m 0644 data/keys/od-rules-ed25519.pub %{buildroot}%{_datadir}/oreon-defense/keys/od-rules-ed25519.pub
install -D -m 0644 config/config.json.example %{buildroot}%{_sysconfdir}/oreon-defense/config.json
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
cat > %{buildroot}%{_sysconfdir}/xdg/autostart/oreon-defense-autostart.desktop <<'EOF'
[Desktop Entry]
Type=Application
Name=Oreon Defense
Comment=Start Oreon Defense tray at login
Exec=oreon-defense --tray
Icon=oreon-defense
Terminal=false
Categories=System;Security;Qt;
X-GNOME-Autostart-enabled=true
Hidden=false
NoDisplay=true
EOF
mkdir -p %{buildroot}%{_localstatedir}/lib/oreon-defense/quarantine
%oreon_autofiles main

%post

%systemd_post oreon-defense.service
%systemd_post oreon-defense-scan.timer
if [ -x /usr/bin/systemctl ]; then
  systemctl daemon-reload >/dev/null 2>&1 || :
  if systemctl cat clamav-freshclam.service >/dev/null 2>&1; then
    systemctl enable --now clamav-freshclam.service >/dev/null 2>&1 || :
  fi
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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
