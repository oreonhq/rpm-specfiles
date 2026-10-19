%global source0_hash 61266ab1afc9d73dbc60a8b2af73e99d2fdff47d99544d085760e4fa667b5dd1
Name:           libgudev
Version:        238
Release:        1%{?dist}
Summary:        GObject-based wrapper library for libudev
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/libgudev
Source0:        https://download.gnome.org/sources/libgudev/%{version}/libgudev-%{version}.tar.xz
Provides:       libgudev1 = %{version}-%{release}
Obsoletes:      libgudev1 < 230
# oreon:deps
BuildRequires:  glib2-devel
BuildRequires:  glibc-langpack-fr
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libudev-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  umockdev-devel
# /oreon:deps
%description
This library makes it much simpler to use libudev from programs
already using GObject. It also makes it possible to easily use libudev
from other programming languages, such as Javascript, because of
GObject introspection support.

%package devel
Summary:   Header files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Provides:       libgudev1-devel = %{version}-%{release}
Obsoletes:      libgudev1-devel < 230
%description devel
This package is necessary to build programs using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dgtk_doc=true -Dtests=enabled -Dvapi=disabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libgudev-devel -f %{oreon_filedir}/libgudev-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 238-9
- Prepare for Oreon 11 (RP1)
