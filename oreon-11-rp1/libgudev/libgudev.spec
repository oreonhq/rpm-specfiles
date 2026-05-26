Name:           libgudev
Version:        238
Release:        9%{?dist}
Summary:        GObject-based wrapper library for libudev

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/libgudev
Source0:        https://download.gnome.org/sources/libgudev/%{version}/libgudev-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 61266ab1afc9d73dbc60a8b2af73e99d2fdff47d99544d085760e4fa667b5dd1
%global source0_file libgudev-238.tar.xz
# oreon url source checksums end

BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig
BuildRequires:  libudev-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
# For tests
BuildRequires:  umockdev-devel
BuildRequires:  glibc-langpack-fr

# Upstream promises to remove libgudev from systemd before this version
Provides:       libgudev1 = %{version}-%{release}
Obsoletes:      libgudev1 < 230

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libgudev-238.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "61266ab1afc9d73dbc60a8b2af73e99d2fdff47d99544d085760e4fa667b5dd1" || { echo "oreon: Source0 SHA256 mismatch for libgudev-238.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%meson -Dgtk_doc=true -Dtests=enabled -Dvapi=disabled
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_libdir}/libgudev-1.0.so.*
%{_libdir}/girepository-1.0/GUdev-1.0.typelib

%files devel
%{_libdir}/libgudev-1.0.so
%dir %{_includedir}/gudev-1.0
%dir %{_includedir}/gudev-1.0/gudev
%{_includedir}/gudev-1.0/gudev/*.h
%{_datadir}/gir-1.0/GUdev-1.0.gir
%dir %{_datadir}/gtk-doc/html/gudev
%{_datadir}/gtk-doc/html/gudev/*
%{_libdir}/pkgconfig/gudev-1.0*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 238-9
- Prepare for Oreon 11 (RP1)
