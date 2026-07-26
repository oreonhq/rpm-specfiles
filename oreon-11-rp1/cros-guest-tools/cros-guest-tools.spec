%global source0_hash 887f97ed3360de8e328b46621831b7c21aee0501e4ef384a71bb3e9301cf3cac

%global hash 0c21bc336c59daac5bff257c8129140ee9d1da37
%global snapshotdate 20251023

Name: cros-guest-tools
Version: 143
Release: 3%{?dist}
Summary: Chromium OS integration meta package

License: BSD-3-Clause
URL: https://chromium.googlesource.com/chromiumos/containers/cros-container-guest-tools
Source0: %{url}/+archive/%{hash}.tar.gz#/%{name}-%{hash}.tar.gz
BuildArch: noarch

BuildRequires: systemd
Recommends: bash-completion
Recommends: bzip2
Recommends: curl
Recommends: dbus-x11
Recommends: file
Recommends: fuse
Recommends: git
Recommends: gnupg
Recommends: iptables
Recommends: iputils
Recommends: less
Recommends: libXScrnSaver
Recommends: mesa-dri-drivers
Recommends: udev
Recommends: usbutils
Recommends: vim-enhanced
Recommends: wget
Recommends: xdg-utils
Recommends: xz
%if 0%{?fedora}
Requires: cros-adapta = %{version}-%{release}
%endif
Requires: cros-logging = %{version}-%{release}
Requires: cros-garcon = %{version}-%{release}
Requires: cros-host-fonts = %{version}-%{release}
Requires: cros-notificationd = %{version}-%{release}
Requires: cros-pulse-config = %{version}-%{release}
Requires: cros-sommelier = %{version}-%{release}
Requires: cros-sommelier-config = %{version}-%{release}
Requires: cros-sudo-config = %{version}-%{release}
Requires: cros-systemd-overrides = %{version}-%{release}
Requires: cros-ui-config = %{version}-%{release}
Requires: cros-wayland = %{version}-%{release}

# Package is obsolete
Obsoletes: cros-sftp < %{version}-%{release}

%description
This package has dependencies on all other packages necessary for Chromium OS
integration.

%package -n cros-systemd-overrides
Summary: Systemd overrides for running under Chromium OS
Requires(post): systemd
Requires(postun): systemd
BuildArch: noarch

%description -n cros-systemd-overrides
This package overrides the default behavior of some core systemd units.

%post -n cros-systemd-overrides
systemctl mask systemd-journald-audit.socket

%postun -n cros-systemd-overrides
if [ $1 -eq 0 ] ; then
systemctl unmask systemd-journald-audit.socket
fi

%package -n cros-logging
Summary: Journald config for Chromium OS integration
Requires: systemd
BuildArch: noarch

%description -n cros-logging
This package installs configuration for logging integration
with Chrome OS so e.g. filing feedback reports can collect
error logs from within the container.

%if 0%{?fedora}
%package -n cros-adapta
Summary: Chromium OS GTK Theme
Requires: filesystem
Requires: gtk2
Requires: gtk3
Requires: gtk-murrine-engine
Requires: gtk2-engines
Requires: qt5-qtstyleplugins
BuildArch: noarch

%description -n cros-adapta
This package provides symlinks which link the bind-mounted theme into the
correct location in the container.
%endif

%package -n cros-garcon
Summary: Chromium OS Garcon Bridge
BuildRequires: desktop-file-utils
Requires: PackageKit
Requires: mailcap
Requires: systemd
BuildArch: noarch

%description -n cros-garcon
This package provides the systemd unit files for Garcon, the bridge to
Chromium OS.

%post -n cros-garcon
%systemd_user_post cros-garcon.service

%preun -n cros-garcon
%systemd_user_preun cros-garcon.service

%package -n cros-host-fonts
Requires: fontpackages-filesystem
Summary: Chromium OS Host Fonts Configuration

%description -n cros-host-fonts
Share fonts from Chromium OS. This package provides a config file to search
for the shared Chromium OS font directory.

%package -n cros-notificationd
Summary: Chromium OS Notification Bridge
Requires: dbus-common
BuildArch: noarch

%description -n cros-notificationd
This package installs D-Bus on-demand service specification for notificationd.

%post -n cros-notificationd
%systemd_user_post cros-notificationd.service

%preun -n cros-notificationd
%systemd_user_preun cros-notificationd.service

%package -n cros-pulse-config
Summary: PulseAudio helper for Chromium OS integration.
Requires: alsa-plugins-pulseaudio
Requires: pulseaudio-utils
BuildArch: noarch

%description -n cros-pulse-config
This package installs customized pulseaudio configurations to /etc/skel.
"default.pa" is required as a workaround for the lack of udev in
unprivileged containers.
"daemon.conf" contains low latency configuration.

%package -n cros-sommelier
Summary: This package installs unit-files and support scripts for sommelier
Requires: gtk2
Requires: xorg-x11-fonts-100dpi
Requires: xorg-x11-fonts-75dpi
Requires: xorg-x11-fonts-cyrillic
Requires: xorg-x11-fonts-ISO8859-1-100dpi
Requires: xorg-x11-fonts-ISO8859-14-100dpi
Requires: xorg-x11-fonts-ISO8859-14-75dpi
Requires: xorg-x11-fonts-ISO8859-15-100dpi
Requires: xorg-x11-fonts-ISO8859-15-75dpi
Requires: xorg-x11-fonts-ISO8859-1-75dpi
Requires: xorg-x11-fonts-ISO8859-2-100dpi
Requires: xorg-x11-fonts-ISO8859-2-75dpi
Requires: xorg-x11-fonts-ISO8859-9-100dpi
Requires: xorg-x11-fonts-ISO8859-9-75dpi
Requires: xorg-x11-fonts-misc
Requires: xorg-x11-fonts-Type1
# xorg-x11-utils: Obsoleted by individual packages
Requires: xdpyinfo
Requires: xwininfo
Requires: xvinfo
Requires: xprop
Requires: xlsfonts
Requires: xlsclients
Requires: xlsatoms
Requires: xev
Requires: xorg-x11-xauth
Requires: vim-common
BuildArch: noarch

%description -n cros-sommelier
%{summary}

%post -n cros-sommelier
%systemd_user_post sommelier@.service
%systemd_user_post sommelier-x@.service

%preun -n cros-sommelier
%systemd_user_preun sommelier@.service
%systemd_user_preun sommelier-x@.service

%package -n cros-sommelier-config
Summary: Sommelier config for Chromium OS integration
Requires: cros-sommelier
BuildArch: noarch

%description -n cros-sommelier-config
This package installs default configuration for sommelier that is ideal for
integration with Chromium OS.

%package -n cros-sudo-config
Summary: sudo config for Chromium OS integration.
Requires: sudo
BuildArch: noarch

%description -n cros-sudo-config
sudo config for Chromium OS integration. This package installs default
configuration for sudo to allow passwordless sudo access for the sudo group,
and passwordless pkexec for the sudo group.

%package -n cros-ui-config
Summary: UI integration for Chromium OS
Requires: dconf
Requires: gtk2
Requires: gtk3
BuildArch: noarch

%description -n cros-ui-config
This package installs default configuration for GTK+ that is ideal for
integration with Chromium OS.

%package -n cros-wayland
Summary: Wayland extras for virtwl in Chromium OS
Requires: systemd-udev
BuildArch: noarch

%description -n cros-wayland
This package provides config files and udev rules to improve the Wayland
experience under CrOS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/dconf/db/local.d
mkdir -p %{buildroot}%{_sysconfdir}/gtk-2.0
mkdir -p %{buildroot}%{_sysconfdir}/gtk-3.0
mkdir -p %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d
mkdir -p %{buildroot}%{_sysconfdir}/xdg
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config/pulse
mkdir -p %{buildroot}%{_sysconfdir}/tmpfiles.d
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_userunitdir}
mkdir -p %{buildroot}%{_datarootdir}/applications
mkdir -p %{buildroot}%{_datarootdir}/dbus-1/services
mkdir -p %{buildroot}%{_datarootdir}/themes
mkdir -p %{buildroot}%{_userunitdir}/cros-garcon.service.d
mkdir -p %{buildroot}%{_userunitdir}/sommelier@0.service.d
mkdir -p %{buildroot}%{_userunitdir}/sommelier@1.service.d
mkdir -p %{buildroot}%{_userunitdir}/sommelier-x@0.service.d
mkdir -p %{buildroot}%{_userunitdir}/sommelier-x@1.service.d
mkdir -p %{buildroot}%{_userunitdir}/pulseaudio.service.wants
mkdir -p %{buildroot}%{_userunitdir}/default.target.wants
mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
mkdir -p %{buildroot}/var/lib/polkit-1/localauthority/10-vendor.d
mkdir -p %{buildroot}/usr/share/ansible/plugins/callback

ln -sf /opt/google/cros-containers/bin/sommelier %{buildroot}%{_bindir}/sommelier

%if 0%{?fedora}
ln -sf /opt/google/cros-containers/cros-adapta %{buildroot}%{_datarootdir}/themes/CrosAdapta
%endif

install -m 644 cros-host-fonts/usr-share-fonts-chromeos.mount %{buildroot}%{_unitdir}
install -m 440 cros-sudo-config/10-cros-nopasswd %{buildroot}%{_sysconfdir}/sudoers.d/10-cros-nopasswd
install -m 440 cros-sudo-config/10-cros-nopasswd.pkla %{buildroot}/var/lib/polkit-1/localauthority/10-vendor.d/10-cros-nopasswd.pkla
install -m 644 cros-sommelier/sommelierrc  %{buildroot}%{_sysconfdir}/sommelierrc
install -m 644 cros-sommelier/sommelier.sh %{buildroot}%{_sysconfdir}/profile.d/sommelier.sh
install -m 644 cros-sommelier/skel.sommelierrc %{buildroot}%{_sysconfdir}/skel/.sommelierrc
install -m 644 cros-garcon/skel.cros-garcon.conf %{buildroot}%{_sysconfdir}/skel/.config/cros-garcon.conf
install -m 644 cros-wayland/skel.weston.ini %{buildroot}%{_sysconfdir}/skel/.config/weston.ini
install -m 644 cros-wayland/10-cros-virtwl.rules %{buildroot}%{_udevrulesdir}/10-cros-virtwl.rules
install -m 644 cros-pulse-config/default.pa %{buildroot}%{_sysconfdir}/skel/.config/pulse/default.pa
install -m 644 cros-pulse-config/daemon.conf %{buildroot}%{_sysconfdir}/skel/.config/pulse/daemon.conf
install -m 755 cros-garcon/garcon-terminal-handler %{buildroot}%{_bindir}/garcon-terminal-handler
install -m 755 cros-garcon/garcon-url-handler %{buildroot}%{_bindir}/garcon-url-handler
install -m 644 cros-notificationd/org.freedesktop.Notifications.service %{buildroot}%{_datarootdir}/dbus-1/services/org.freedesktop.Notifications.service
install -m 644 cros-ui-config/gtkrc %{buildroot}%{_sysconfdir}/gtk-2.0/gtkrc
install -m 644 cros-ui-config/settings.ini %{buildroot}%{_sysconfdir}/gtk-3.0/settings.ini
install -m 644 cros-ui-config/Trolltech.conf %{buildroot}%{_sysconfdir}/xdg/Trolltech.conf
install -m 644 cros-ui-config/01-cros-ui %{buildroot}%{_sysconfdir}/dconf/db/local.d/01-cros-ui

install -m 644 cros-garcon/cros-garcon.service %{buildroot}%{_userunitdir}/cros-garcon.service
install -m 644 cros-sommelier/sommelier@.service %{buildroot}%{_userunitdir}/sommelier@.service
install -m 644 cros-sommelier/sommelier-x@.service %{buildroot}%{_userunitdir}/sommelier-x@.service
install -m 644 cros-garcon/cros-garcon-override.conf %{buildroot}%{_userunitdir}/cros-garcon.service.d/cros-garcon-override.conf
install -m 644 cros-sommelier-config/cros-sommelier-override.conf %{buildroot}%{_userunitdir}/sommelier@0.service.d/cros-sommelier-override.conf
install -m 644 cros-sommelier-config/cros-sommelier-x-override.conf %{buildroot}%{_userunitdir}/sommelier-x@0.service.d/cros-sommelier-x-override.conf
install -m 644 cros-sommelier-config/cros-sommelier-low-density-override.conf %{buildroot}%{_userunitdir}/sommelier@1.service.d/cros-sommelier-low-density-override.conf
install -m 644 cros-sommelier-config/cros-sommelier-low-density-override.conf %{buildroot}%{_userunitdir}/sommelier-x@1.service.d/cros-sommelier-low-density-override.conf
install -m 644 cros-notificationd/cros-notificationd.service %{buildroot}%{_userunitdir}/cros-notificationd.service
install -m 644 cros-logging/00-create-logs-dir.conf %{buildroot}%{_sysconfdir}/tmpfiles.d/00-create-logs-dir.conf
sed -i 's/OnlyShowIn=Never/OnlyShowIn=X-Never/g' cros-garcon/garcon_host_browser.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications cros-garcon/garcon_host_browser.desktop

sed -i -e '13,20d' %{buildroot}%{_userunitdir}/sommelier-x@.service
sed -i '13iEnvironment="SOMMELIER_XFONT_PATH=/usr/share/X11/fonts/misc,/usr/share/X11/fonts/cyrillic,/usr/share/X11/fonts/100dpi/:unscaled,/usr/share/X11/fonts/75dpi/:unscaled,/usr/share/X11/fonts/Type1,/usr/share/X11/fonts/100dpi,/usr/share/X11/fonts/75dpi,built-ins"\nEnvironment="LIBGL_DRIVERS_PATH=/opt/google/cros-containers/lib/"' %{buildroot}%{_userunitdir}/sommelier-x@.service
sed -i 's/false/true/g' %{buildroot}%{_sysconfdir}/skel/.config/cros-garcon.conf
sed -i '1i if [ "$UID" -ne "0" ]; then' %{buildroot}%{_sysconfdir}/profile.d/sommelier.sh
sed -i '1i export XDG_RUNTIME_DIR=/run/user/$UID' %{buildroot}%{_sysconfdir}/profile.d/sommelier.sh
echo "fi" >> %{buildroot}%{_sysconfdir}/profile.d/sommelier.sh

%files
%dir %{_sysconfdir}/skel/.config
%license LICENSE
%doc README.md

%if 0%{?fedora}
%files -n cros-adapta
%{_datarootdir}/themes/CrosAdapta
%license LICENSE
%doc README.md
%endif

%files -n cros-logging
%license LICENSE
%doc README.md
%{_sysconfdir}/tmpfiles.d/00-create-logs-dir.conf

%files -n cros-garcon
%{_bindir}/garcon-terminal-handler
%{_bindir}/garcon-url-handler
%{_datarootdir}/applications/garcon_host_browser.desktop
%{_sysconfdir}/skel/.config/cros-garcon.conf
%{_userunitdir}/cros-garcon.service
%{_userunitdir}/cros-garcon.service.d
%license LICENSE
%doc README.md

%files -n cros-host-fonts
%{_unitdir}/usr-share-fonts-chromeos.mount
%license LICENSE
%doc README.md

%files -n cros-notificationd
%{_datarootdir}/dbus-1/services/org.freedesktop.Notifications.service
%{_userunitdir}/cros-notificationd.service
%license LICENSE
%doc README.md

%files -n cros-sudo-config
%config(noreplace) %{_sysconfdir}/sudoers.d/10-cros-nopasswd
/var/lib/polkit-1/localauthority/10-vendor.d/10-cros-nopasswd.pkla
%license LICENSE
%doc README.md

%files -n cros-systemd-overrides
%license LICENSE
%doc README.md

%files -n cros-pulse-config
%{_sysconfdir}/skel/.config/pulse/daemon.conf
%{_sysconfdir}/skel/.config/pulse/default.pa
%license LICENSE
%doc README.md

%files -n cros-sommelier
%{_bindir}/sommelier
%{_sysconfdir}/skel/.sommelierrc
%config(noreplace) %{_sysconfdir}/sommelierrc
%config(noreplace) %{_sysconfdir}/profile.d/sommelier.sh
%{_userunitdir}/sommelier@.service
%{_userunitdir}/sommelier-x@.service
%license LICENSE
%doc README.md

%files -n cros-sommelier-config
%{_userunitdir}/sommelier@0.service.d
%{_userunitdir}/sommelier@1.service.d
%{_userunitdir}/sommelier-x@0.service.d
%{_userunitdir}/sommelier-x@1.service.d
%license LICENSE
%doc README.md

%files -n cros-ui-config
%config(noreplace) %{_sysconfdir}/gtk-2.0/gtkrc
%dir %{_sysconfdir}/gtk-3.0
%config(noreplace) %{_sysconfdir}/gtk-3.0/settings.ini
%config(noreplace) %{_sysconfdir}/xdg/Trolltech.conf
%config(noreplace) %{_sysconfdir}/dconf/db/local.d/01-cros-ui
%license LICENSE
%doc README.md

%files -n cros-wayland
%config(noreplace) %{_sysconfdir}/skel/.config/weston.ini
%{_udevrulesdir}/10-cros-virtwl.rules
%license LICENSE
%doc README.md

%changelog
%autochangelog
