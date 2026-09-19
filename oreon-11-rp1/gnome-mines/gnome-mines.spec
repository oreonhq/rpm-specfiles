%global source0_hash 9d3a44122d04af787c64a869ef90dd54ea7500e5b48be457c6d64d9b2773fb9f

%global tarball_version %%(echo %{version} | tr '~' '.')
%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)

Name:           gnome-mines
Version:        50.0
Release:        %autorelease
Summary:        GNOME Mines Sweeper game

License:        GPL-3.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Mines
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala

%description
The popular logic puzzle minesweeper. Find mines on a grid
using hints from squares you have already cleared.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gnome-mines-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome
%find_lang %{name}_libgnome-games-support --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Mines.desktop

%files -f %{name}.lang -f %{name}_libgnome-games-support.lang
%license COPYING
%{_bindir}/gnome-mines
%{_datadir}/applications/org.gnome.Mines.desktop
%{_datadir}/dbus-1/services/org.gnome.Mines.service
%{_datadir}/glib-2.0/schemas/org.gnome.Mines.gschema.xml
%{_datadir}/gnome-mines/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Mines*svg
%{_datadir}/metainfo/org.gnome.Mines.metainfo.xml
%{_mandir}/man6/gnome-mines.6*

%changelog
%autochangelog
