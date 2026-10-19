%global source0_hash c72890ca7e5809cefeb876b01199f8b197146b5c25e9d5745301a284c0f3cdaa
%global gobject_introspection_version 1.35.9
%global grilo_version 0.3.13
%global gtk4_version 4.10.0
%global libadwaita_version 1.5~beta
%global pygobject_version 3.47.0
%global tracker_sparql_version 2.99.3
%global tarball_version %%(echo %{version} | tr '~' '.')
%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)
Name:          gnome-music
Summary:        Music player and management application for GNOME
Version:       50.0
Release:        1%{?dist}
License:       (LicenseRef-Callaway-GPLv2+-with-exceptions) AND CC-BY-SA-3.0
URL:           https://wiki.gnome.org/Apps/Music
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
BuildArch:     noarch
Requires:      gdk-pixbuf2
Requires:      gobject-introspection >= %{gobject_introspection_version}
Requires:      grilo >= %{grilo_version}
Requires:      grilo-plugins
Requires:      gstreamer1
Requires:      gstreamer1-plugins-base
Requires:      gtk4 >= %{gtk4_version}
Requires:      libadwaita >= %{libadwaita_version}
Requires:      libmediaart
Requires:      libnotify >= 0.7.6
Requires:      libsoup3
Requires:      libtinysparql
Requires:      pango
Requires:      python3-cairo
Requires:      python3-gobject >= %{pygobject_version}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(grilo-plugins-0.3)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libmediaart-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
Music player and management application for GNOME.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Music.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Music.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
