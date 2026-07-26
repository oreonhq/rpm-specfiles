%global source0_hash 31c0ad477dc4f22e3c4fa284b51a415faa2e807f91aa580798b07f90973b7271

%global uuid pomodoro@arun.codito.in
%global gittag %{version}

Epoch:          1
Name:           gnome-pomodoro
Version:        0.28.0
Release:        2%{?dist}
Summary:        A time management utility for GNOME

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://gnomepomodoro.org/
Source0:        https://github.com/gnome-pomodoro/gnome-pomodoro/archive/%{gittag}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(json-glib-1.0)

# For gnome shell extension part of gnome-pomodoro
Requires:       gnome-shell >= 40.0
Requires:       hicolor-icon-theme
# For /usr/share/dbus-1/services ownership
Requires:       dbus-common

# Provides/Obsoletes added in F35 due to package rename
Provides:       gnome-shell-extension-pomodoro = %{epoch}:%{version}-%{release}
Obsoletes:      gnome-shell-extension-pomodoro < 1:0.19.2-1

%description
This GNOME utility helps to manage time according to Pomodoro Technique.
It intends to improve productivity and focus by taking short breaks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gnome-pomodoro-%{gittag}

%build
%meson
%meson_build

%install
%meson_install

# Remove unneeded unversioned symlink
rm %{buildroot}%{_libdir}/lib%{name}.so

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Pomodoro.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/*/org.gnome.Pomodoro.appdata.xml

%files -f %{name}.lang
%doc README.md NEWS
%license COPYING
%{_bindir}/gnome-pomodoro
%{_libdir}/gnome-pomodoro
%{_libdir}/libgnome-pomodoro.so*
%{_datadir}/gnome-pomodoro
%{_datadir}/*/org.gnome.Pomodoro.appdata.xml
%{_datadir}/applications/org.gnome.Pomodoro.desktop
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/glib-2.0/schemas/org.gnome.pomodoro.*
%{_datadir}/dbus-1/services/org.gnome.Pomodoro.service

%changelog
%autochangelog
