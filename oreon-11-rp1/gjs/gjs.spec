%global source0_hash 47e9f22b1d4aca841c6c492b449b6de32ff680972183e26fe7b98a45c5c3fee1
%global glib2_version 2.68.0
%global gobject_introspection_version 1.72.0
%global mozjs140_version 140.1.0
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name:           gjs
Version:        1.90.0
Release:        1%{?dist}
Summary:        Javascript Bindings for GNOME
License:        MIT AND BSD-3-Clause AND (MIT OR LGPL-2.0-or-later) AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
URL:            https://wiki.gnome.org/Projects/Gjs
Source0:        https://download.gnome.org/sources/%{name}/1.90/%{name}-%{version}.tar.xz
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gobject-introspection%{?_isa} >= %{gobject_introspection_version}
Requires: mozjs140%{?_isa} >= %{mozjs140_version}
# oreon:deps
BuildRequires:  /usr/bin/dbus-run-session
BuildRequires:  dbus-x11
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3
BuildRequires:  mesa-dri-drivers
BuildRequires:  meson
BuildRequires:  mutter
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(mozjs-140)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  readline-devel
BuildRequires:  xwayland-run
# /oreon:deps
%description
Gjs allows using GNOME libraries from Javascript. It's based on the
Spidermonkey Javascript engine from Mozilla and the GObject introspection
framework.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package tests
Summary: Tests for the gjs package
License: MIT AND (MIT OR LGPL-2.0-or-later) AND BSD-3-Clause
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tests
The gjs-tests package contains tests that can be used to verify
the functionality of the installed gjs package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{shrink:xwfb-run -c mutter -- %meson_test --timeout-multiplier=5}
%files -f %{oreon_filedir}/main.list
%files -n gjs-devel -f %{oreon_filedir}/gjs-devel.list
%files -n gjs-tests -f %{oreon_filedir}/gjs-tests.list

%changelog

%autochangelog
