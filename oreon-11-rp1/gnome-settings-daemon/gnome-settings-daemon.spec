%global source0_hash 7c6249118ddfffc4bb34d6b3edaa86b3ea02a1ad2b7711d79480749906767665
%global glib2_version 2.70
%global colord_version 1.4.5
%global geocode_glib_version 3.26.3
%global gnome_desktop_version 4.0
%global gsettings_desktop_schemas_version 46~beta
%global gtk4_version 4.0
%global geoclue_version 2.3.1
%global xfixes_version 6.0
%global systemd_units org.gnome.SettingsDaemon.A11ySettings.service org.gnome.SettingsDaemon.Color.service org.gnome.SettingsDaemon.Datetime.service org.gnome.SettingsDaemon.Housekeeping.service org.gnome.SettingsDaemon.Keyboard.service org.gnome.SettingsDaemon.MediaKeys.service org.gnome.SettingsDaemon.Power.service org.gnome.SettingsDaemon.PrintNotifications.service org.gnome.SettingsDaemon.Rfkill.service org.gnome.SettingsDaemon.ScreensaverProxy.service org.gnome.SettingsDaemon.Sharing.service org.gnome.SettingsDaemon.Smartcard.service org.gnome.SettingsDaemon.Sound.service org.gnome.SettingsDaemon.UsbProtection.service org.gnome.SettingsDaemon.Wwan.service org.gnome.SettingsDaemon.XSettings.service
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           gnome-settings-daemon
Version:        51.0
Release:        1%{?dist}
Summary:        The daemon sharing settings from GNOME to GTK+/KDE applications
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-settings-daemon
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Source1:    	org.gnome.settings-daemon.plugins.housekeeping.gschema.override
Source100:    	org.gnome.settings-daemon.plugins.power.gschema.override
Requires: colord >= %{colord_version}
Requires: iio-sensor-proxy
Requires: geoclue2 >= %{geoclue_version}
Requires: geocode-glib2%{?_isa} >= %{geocode_glib_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-desktop4%{?_isa} >= %{gnome_desktop_version}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk4%{?_isa} >= %{gtk4_version}
Requires: libgweather4%{?_isa}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gck-2)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A daemon to share settings from GNOME to other applications. It also
handles global keybindings, as well as a number of desktop-wide settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_user_post %{systemd_units}
%preun

%systemd_user_preun %{systemd_units}
%files -f %{oreon_filedir}/main.list
%files -n gnome-settings-daemon-devel -f %{oreon_filedir}/gnome-settings-daemon-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
