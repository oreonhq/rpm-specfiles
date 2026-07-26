%global source0_hash 2463773c7d3090052f54ade075998475f88b4615bddc0c0c9f22cc2e6decf248

%global glib2_version 2.64
%global gnome_desktop_version 44.4
%global gnome_settings_daemon_version 49
%global gsettings_desktop_schemas_version 49
%global gtk3_version 3.24
%global polkit_version 0.105
%global vala_version 0.56.18

Name:           budgie-desktop
Version:        10.10.2
Release:        1%{?dist}
Summary:        A feature-rich, modern desktop designed to keep out the way of the user

# GPL-2.0-or-later:
# - /usr/bin/*
# - /usr/share/icons/hicolor/scalable/actions/notification-disabled-symbolic.svg
# GPL-2.0-only:
# - /usr/share/icons/hicolor/scalable/actions/pane-hide-symbolic.svg
# - /usr/share/icons/hicolor/scalable/actions/pane-show-symbolic.svg
# LGPL-2.1-or-later: all libraries
# CC-1.0:
# - /usr/share/backgrounds/budgie/default.jpg
# - /usr/share/icons/hicolor/scalable/actions/budgie-menu-symbolic.svg
# - /usr/share/icons/hicolor/scalable/actions/notification-alert-symbolic.svg
# CC-BY-SA-4.0: All icons except those noted above
License:        GPL-2.0-or-later AND GPL-2.0-only AND LGPL-2.1-or-later AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://github.com/BuddiesOfBudgie/budgie-desktop
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        https://forge.moderndesktop.dev/BuddiesOfBudgie/keyrings/raw/branch/main/JoshuaStrobl.gpg

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  pkgconfig(accountsservice) >= 0.6.55
BuildRequires:  pkgconfig(alsa) >= 1.2.6
BuildRequires:  pkgconfig(gee-0.8) >= 0.20.0
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_desktop_version}
BuildRequires:  pkgconfig(gnome-settings-daemon) >= %{gnome_settings_daemon_version}
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.20.0
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.10
BuildRequires:  pkgconfig(libcanberra) >= 0.30
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libpeas-2) >= 2.2.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(libxfce4windowing-0)
BuildRequires:  pkgconfig(polkit-agent-1) >= %{polkit_version}
BuildRequires:  pkgconfig(upower-glib) >= 0.99.13
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen) >= %{vala_version}
BuildRequires:  budgie-desktop-view
BuildRequires:  desktop-file-utils
BuildRequires:  egl-utils
BuildRequires:  gammastep
BuildRequires:  grim
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  gsettings-desktop-schemas >= %{gsettings_desktop_schemas_version}
BuildRequires:  gtk-doc >= 1.33.0
BuildRequires:  gtklock
BuildRequires:  intltool
BuildRequires:  magpie-devel
BuildRequires:  meson
BuildRequires:  sassc
BuildRequires:  slurp
BuildRequires:  swaybg
BuildRequires:  swayidle
BuildRequires:  wlopm
Requires:       budgie-desktop-services
Requires:       budgie-session
Requires:       egl-utils
Requires:       gammastep
Requires:       grim
Requires:       gnome-settings-daemon
Requires:       gsettings-desktop-schemas
Requires:       gnome-keyring-pam
Requires:       hicolor-icon-theme
Requires:       labwc
# mutter-common is required for gschemas that the labwc bridge uses
Requires:       mutter-common
Requires:       network-manager-applet
Requires:       python3-psutil
Requires:       slurp
Requires:       swaybg
Requires:       swayidle
Requires:       switcheroo-control
Requires:       xdg-desktop-portal-gtk
Requires:       xdg-desktop-portal-wlr
Requires:       wlopm

Suggests:       budgie-control-center
Suggests:       budgie-display-configurator
Suggests:       papirus-icon-theme

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}

# Deal with fixing the gir file installation
Conflicts:      %{name} < 10.6.4-2
Conflicts:      %{name}-devel < 10.6.4-2

Obsoletes:      budgie-screensaver < 5.1.0-9

%description
A feature-rich, modern desktop designed to keep out the way of the user.

%package devel
Summary:        Development package for budgie-desktop
Requires:       %{name}%{?_isa} = %{version}-%{release}

# Deal with fixing the gir file installation
Conflicts:      %{name} < 10.6.4-2
Conflicts:      %{name}-devel < 10.6.4-2

%description devel
Header files, libraries, and other files for developing Budgie Desktop.

%package docs
Summary:        Documentation for budgie-desktop
BuildArch:      noarch
Requires:       gtk-doc
Requires:       %{name} = %{version}-%{release}

%description docs
Documentation for budgie-desktop

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson -Dwith-hibernate=false
%meson_build

%install
%meson_install
chmod +x %{buildroot}/%{_libexecdir}/%{name}/labwc_bridge.py
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSE
%dir %{_datadir}/backgrounds/budgie
%dir %{_datadir}/budgie
%dir %{_datadir}/xdg-desktop-portal
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins/
%dir %{_libdir}/%{name}/plugins/*
%{_bindir}/budgie-*
%{_bindir}/org.buddiesofbudgie.*
%{_bindir}/startbudgielabwc
%{_datadir}/applications/org.buddiesofbudgie*.desktop
%{_datadir}/backgrounds/budgie/default.jpg
%{_datadir}/budgie/budgie-version.xml
%{_datadir}/%{name}/gammastep.config
%{_datadir}/%{name}/labwc/*
%{_datadir}/glib-2.0/schemas/20_buddiesofbudgie.%{name}.notifications.gschema.override
%{_datadir}/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.%{name}.raven.widget.*.gschema.xml
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.%{name}.screenshot.gschema.xml
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.settings-daemon.plugins.media-keys.gschema.xml
%{_datadir}/gnome-session/sessions/org.buddiesofbudgie.BudgieDesktop.session
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/icons/hicolor/symbolic/emblems/*.svg
%{_datadir}/xdg-desktop-portal/budgie-portals.conf
%{_datadir}/wayland-sessions/%{name}.desktop
%{_libdir}/libbudgie-windowing.so.0{,.*}
%{_libdir}/girepository-1.0/Budgie-3.0.typelib
%{_libdir}/girepository-1.0/BudgieRaven-3.0.typelib
%{_libdir}/%{name}/libgvc.so
%{_libdir}/%{name}/plugins/*/*.plugin
%{_libdir}/%{name}/plugins/*/*.so*
%{_libdir}/%{name}/raven-plugins/*/*.plugin
%{_libdir}/%{name}/raven-plugins/*/*.so*
%{_libexecdir}/%{name}/budgie-polkit-dialog
%{_libexecdir}/%{name}/budgie-power-dialog
%{_libexecdir}/%{name}/budgie-screenshot-dialog
%{_libexecdir}/%{name}/labwc_bridge.py
%{_libdir}/libbudgie-appindexer.so.0{,.*}
%{_libdir}/libbudgie-plugin.so.0{,.*}
%{_libdir}/libbudgie-private.so.0{,.*}
%{_libdir}/libbudgie-raven-plugin.so.0{,.*}
%{_libdir}/libbudgietheme.so.0{,.*}
%{_libdir}/libraven.so.0{,.*}
%{_mandir}/man1/budgie-*
%{_mandir}/man1/org.buddiesofbudgie.BudgieScreenshot.*
%{_mandir}/man1/org.buddiesofbudgie.sendto.*
%{_mandir}/man1/startbudgielabwc.*
%{_sysconfdir}/xdg/autostart/*.desktop

%files devel
%dir %{_datadir}/gir-1.0
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%dir %{_includedir}/%{name}
%{_datadir}/gir-1.0/Budgie-3.0.gir
%{_datadir}/gir-1.0/BudgieRaven-3.0.gir
%{_datadir}/vala/vapi/budgie-*.deps
%{_datadir}/vala/vapi/budgie-*.vapi
%{_includedir}/%{name}/*.h
%{_libdir}/libbudgie-appindexer.so
%{_libdir}/libbudgie-plugin.so
%{_libdir}/libbudgie-private.so
%{_libdir}/libbudgie-raven-plugin.so
%{_libdir}/libbudgie-windowing.so
%{_libdir}/libbudgietheme.so
%{_libdir}/libraven.so
%{_libdir}/pkgconfig/budgie-3.0.pc
%{_libdir}/pkgconfig/budgie-raven-plugin-3.0.pc
%{_libdir}/pkgconfig/budgie-theme-1.0.pc
%{_libdir}/pkgconfig/budgie-windowing-1.0.pc

%files docs
%dir %{_datadir}/gtk-doc/html/
%dir %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gtk-doc/html/%{name}/*

%changelog
%autochangelog
