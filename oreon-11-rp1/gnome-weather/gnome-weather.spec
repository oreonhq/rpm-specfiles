%global source0_hash 57de7578605f91f9ab400551ce7738db7505bc88f42a33c70ce7a70167fdb513
%global gobject_introspection_version 1.35.9
%global gtk4_version 4.5
%global gjs_version 1.71.0
%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %%(cut -d '.' -f 1 <<<%{tarball_version})
Name:		gnome-weather
Version:	50.0
Release:        1%{?dist}
Summary:        A weather application for GNOME
License:	GPL-2.0-or-later AND BSD-3-Clause and CC-BY-3.0 and CC-BY-SA-3.0
URL:		https://wiki.gnome.org/Apps/Weather
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Patch:          no-absolute-symlinks.patch
BuildArch:	noarch
Requires:	gdk-pixbuf2
Requires:	geoclue2-libs
Requires:	gjs >= %{gjs_version}
Requires:	glib2
Requires:	gobject-introspection >= %{gobject_introspection_version}
Requires:	gsettings-desktop-schemas
Requires:	gtk4 >= %{gtk4_version}
Requires:	libadwaita
Requires:	libgweather4
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  python3-devel
BuildRequires:  typescript
# /oreon:deps
%description
gnome-weather is a weather application for GNOME

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} .

%build

%meson
%meson_build
%install
%meson_install
%find_lang org.gnome.Weather
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Weather.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
