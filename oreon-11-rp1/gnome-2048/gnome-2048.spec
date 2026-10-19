%global source0_hash 6d15df68a6128cf0c99e598908af8c667b733dc4003ef4d21d4b4c4a42bd2da9
Name:           gnome-2048
Version:        50.2
Release:        1%{?dist}
Summary:        A 2048 clone for GNOME
License:        GPL-3.0-or-later
URL:            https://wiki.gnome.org/Apps/2048
Source0:        https://download.gnome.org/sources/gnome-2048/50/gnome-2048-%{version}.tar.xz
Provides:       bundled(libgnome-games-support)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  vala
# /oreon:deps
%description
A GNOME clone of the popular game 2048
http://en.wikipedia.org/wiki/2048_(video_game)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%find_lang gnome-2048_libgnome-games-support --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
