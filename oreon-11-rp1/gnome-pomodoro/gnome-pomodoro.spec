%global source0_hash 5ffc950f0f710a249d5e6659e55c62092568e3688b76c644b0f5afa77e32c4b8
%global uuid pomodoro@arun.codito.in
%global gittag %{version}
Epoch:          1
Name:           gnome-pomodoro
Version:        1.1.5
Release:        1%{?dist}
Summary:        A time management utility for GNOME
License:        GPL-3.0-or-later
URL:            https://gnomepomodoro.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}.tar.gz
Requires:       gnome-shell >= 40.0
Requires:       hicolor-icon-theme
Requires:       dbus-common
Provides:       gnome-shell-extension-pomodoro = %{epoch}:%{version}-%{release}
Obsoletes:      gnome-shell-extension-pomodoro < 1:0.19.2-1
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  vala
# /oreon:deps
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
rm %{buildroot}%{_libdir}/lib%{name}.so
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Pomodoro.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/*/org.gnome.Pomodoro.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
