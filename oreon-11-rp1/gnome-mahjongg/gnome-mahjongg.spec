%global source0_hash e9edd31ac2698b8d9a5be1d11c60d43450a889f8769cca0bef3395a11a5d5fd1

%global tarball_version %%(echo %{version} | tr '~' '.')
%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)

Name:           gnome-mahjongg
Version:        49.1.1
Release:        %autorelease
Summary:        GNOME Mahjongg game

License:        GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Mahjongg
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)

%description
Mahjongg is a simple pattern recognition game. You score points by
matching identical tiles.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%{_bindir}/gnome-mahjongg
%{_datadir}/applications/org.gnome.Mahjongg.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Mahjongg.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Mahjongg.*
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Mahjongg-symbolic.svg
%{_metainfodir}/org.gnome.Mahjongg.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.Mahjongg.service
%{_mandir}/man6/gnome-mahjongg.6*

%changelog
%autochangelog
