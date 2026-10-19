%global source0_hash c176b889b75630a17f4e3d7ef24c09a3e12368e633496087459c8b53ac3a122d
Summary:        GTK+ 3 support library for colord
Name:      colord-gtk
Version:   0.3.1
Release:        1%{?dist}
License:   LGPL-2.1-or-later
URL:       http://www.freedesktop.org/software/colord/
Source0:        http://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  colord-devel
BuildRequires:  docbook5-style-xsl
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  gtk4-devel
BuildRequires:  lcms2-devel
BuildRequires:  meson
BuildRequires:  vala
# /oreon:deps
%description
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package -n colord-gtk4
Summary:  GTK 4 support library for colord
%description -n colord-gtk4
colord-gtk is a support library for colord and provides additional
functionality that requires GTK. This package contains the GTK 4
build of colord-gtk.

%package -n colord-gtk4-devel
Summary:  Development package for colord-gtk4
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description -n colord-gtk4-devel
Files for GTK 4 development with %{name}4.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Ddocs=true -Dgtk2=false -Dman=true -Dtests=false -Dvapi=true
%meson_build
%install
%meson_install
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles colord-gtk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles colord-gtk4 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles colord-gtk4-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n colord-gtk-devel -f %{oreon_filedir}/colord-gtk-devel.list
%files -n colord-gtk4 -f %{oreon_filedir}/colord-gtk4.list
%files -n colord-gtk4-devel -f %{oreon_filedir}/colord-gtk4-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.1-1
- Prepare for Oreon 11 (RP1)
