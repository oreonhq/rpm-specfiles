%global source0_hash c55cd5037adeb05a25c21fd4a9c03bd147e2917727c189a58e79c9dbfcaf489c

%global cinnamon_desktop_version 6.6.0

Name:           cinnamon-settings-daemon
Version:        6.6.3
Release:        1%{?dist}
Summary:        The daemon sharing settings from CINNAMON to GTK+/KDE applications

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:   %{ix86}

# add hard cinnamon-desktop required version due logind schema
Requires:       cinnamon-desktop%{?_isa} >= %{cinnamon_desktop_version}
Requires:       colord%{?_isa}
Requires:       iio-sensor-proxy%{?_isa}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  intltool
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires:  pkgconfig(colord) >= 0.1.27
BuildRequires:  pkgconfig(cups) >= 1.4
BuildRequires:  pkgconfig(cvc) >= %{cinnamon_desktop_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(pango) >= 1.20.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(libpulse) >= 0.9.16
BuildRequires:  pkgconfig(upower-glib) >= 0.9.11
%ifnarch s390 s390x %{?rhel:ppc ppc64}
BuildRequires:  pkgconfig(libwacom) >= 0.7
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(lcms2) >= 2.2
BuildRequires:  pkgconfig(libsystemd)

%description
A daemon to share settings from CINNAMON to other applications. It also
handles global keybindings, and many of desktop-wide settings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson \
 -Duse_smartcard=disabled \
%ifarch s390 s390x %{?rhel:ppc ppc64}
 -Duse_wacom=disabled
%endif

%meson_build

%install
%meson_install

desktop-file-install --delete-original           \
  --dir %{buildroot}%{_sysconfdir}/xdg/autostart/  \
  %{buildroot}%{_sysconfdir}/xdg/autostart/*

desktop-file-install --delete-original           \
  --dir %{buildroot}%{_datadir}/applications/  \
  %{buildroot}%{_datadir}/applications/csd-automount.desktop
  
# Remove script
rm -rf %{buildroot}%{_datadir}/cinnamon-settings-daemon-3.0/

# Delete csd symlinks
rm -rf %{buildroot}%{_libdir}/cinnamon-settings-daemon/

%files
%doc AUTHORS
%license COPYING COPYING.LIB
%{_bindir}/csd-*
%config %{_sysconfdir}/xdg/autostart/*
%{_libdir}/cinnamon-settings-daemon-3.0/
%{_libexecdir}/csd-a11y-settings
%{_libexecdir}/csd-automount
%{_libexecdir}/csd-background
%{_libexecdir}/csd-backlight-helper
%{_libexecdir}/csd-clipboard
%{_libexecdir}/csd-color
%{_libexecdir}/csd-datetime-mechanism
%{_libexecdir}/csd-housekeeping
%{_libexecdir}/csd-input-helper
%{_libexecdir}/csd-keyboard
%{_libexecdir}/csd-media-keys
%{_libexecdir}/csd-power
%{_libexecdir}/csd-printer
%{_libexecdir}/csd-print-notifications
%{_libexecdir}/csd-screensaver-proxy
%{_libexecdir}/csd-settings-remap
%{_libexecdir}/csd-xsettings
%ifnarch s390 s390x %{?rhel:ppc ppc64}
%{_libexecdir}/csd-wacom-oled-helper
%{_libexecdir}/csd-wacom-led-helper
%{_libexecdir}/csd-wacom
%endif
%{_datadir}/applications/csd-automount.desktop
%{_datadir}/dbus-1/system.d/org.cinnamon.SettingsDaemon.DateTimeMechanism.conf
%{_datadir}/dbus-1/system-services/org.cinnamon.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon*.xml
%{_datadir}/icons/hicolor/*/apps/csd-*
%{_datadir}/polkit-1/actions/org.cinnamon.settings*.policy

%changelog
%autochangelog
