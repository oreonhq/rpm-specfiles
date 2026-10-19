%global source0_hash 32333754230e96d41d70080cac0e26da8a5122d33eaf1d51fb474153ac2da090
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           gnome-todo
Version:        43.0
Release:        4%{?dist}
Summary:        Personal task manager for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/Endeavour/
Source0:        https://gitlab.gnome.org/World/Endeavour/-/archive/%{version}/Endeavour-%{version}.tar.bz2
Patch0:         endeavour-girepository.patch
Patch1:         endeavour-fix-tests-build.patch
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui4-1.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(rest-0.7)
# /oreon:deps
%description
GNOME To Do is a small application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%package devel
Summary:        Development files needed to write plugins for GNOME To Do
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Endeavour-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang endeavour --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Todo.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Todo.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n gnome-todo-devel -f %{oreon_filedir}/gnome-todo-devel.list

%changelog

%autochangelog
