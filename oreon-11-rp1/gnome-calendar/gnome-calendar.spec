%global source0_hash 4b75df071a52d98fb35e647d018030129d24d9007790d02457746c98617aeab0
%global libical_version 3.0.5
%global gsettings_desktop_schemas_version 3.21.2
%global edataserver_version 3.45.1
%global glib2_version 2.80.0
%global gtk4_version 4.15.2
%global libadwaita_version 1.8~alpha
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           gnome-calendar
Version:        51.0
Release:        1%{?dist}
Summary:        Simple and beautiful calendar application designed to fit GNOME 3
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Calendar
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Requires:       evolution-data-server%{?_isa} >= %{edataserver_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       libical%{?_isa} >= %{libical_version}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libsoup-3.0)
# /oreon:deps
%description
Calendar is a simple and beautiful calendar application designed to fit
GNOME 3.
Features:
* Week, month and year views
* Basic editing of events
* Evolution Data Server integration
* Search support

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%{find_lang} %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Calendar.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Calendar.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
