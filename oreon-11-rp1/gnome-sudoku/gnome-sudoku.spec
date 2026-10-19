%global source0_hash 525fedff287c83e3fa73c5a474e1a49f0d0b8b588e3deb08ca341770c781425d
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           gnome-sudoku
Epoch:          1
Version:        51.0.1
Release:        1%{?dist}
Summary:        GNOME Sudoku game
License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Sudoku
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(qqwing)
BuildRequires:  vala
# /oreon:deps
%description
GNOME version of the popular Sudoku Japanese logic game.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Sudoku.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
