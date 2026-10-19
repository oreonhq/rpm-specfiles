%global source0_hash 0a66e01abd2cf048a793b0f83ab2a4156006075f27e1b2896fd8288694d1366e
%global gjs_version 1.69.2
%global libadwaita_version 1.8~alpha
%global libshumate_version 1.5~alpha
%global tarball_version %%(echo %{version} | tr '~' '.')
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$
Name:           gnome-maps
Version:        51.0
Release:        1%{?dist}
Summary:        Map application for GNOME
License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Maps
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Requires:       dbus
Requires:       gdk-pixbuf2%{?_isa}
Requires:       geoclue2-libs%{?_isa}
Requires:       geocode-glib2%{?_isa}
Requires:       gjs%{?_isa} >= %{gjs_version}
Requires:       gobject-introspection%{?_isa}
Requires:       gsettings-desktop-schemas%{?_isa}
Requires:       gtk4%{?_isa}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       libgweather4%{?_isa}
Requires:       libportal%{?_isa}
Requires:       libshumate%{?_isa} >= %{libshumate_version}
Requires:       libsoup3%{?_isa}
Requires:       rest%{?_isa}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  blueprint-compiler
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  libsecret
BuildRequires:  meson
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-1.0)
BuildRequires:  pkgconfig(shumate-1.0)
# /oreon:deps
%description
GNOME Maps is a simple map application for the GNOME desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
rm %{buildroot}%{_libdir}/gnome-maps/libgnome-maps.so
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Maps.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Maps.desktop
%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
