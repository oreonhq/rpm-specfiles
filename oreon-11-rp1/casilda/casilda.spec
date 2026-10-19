%global source0_hash 2dcc9b8b73f92ac6149a991d458dd22a5384bb0396d20af6feda6b66a39f9096
Name:           casilda
Version:        1.6.0
Release:        1%{?dist}
Summary:        Wayland compositor for GTK4
License:        LGPL-2.1-only AND LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/jpu/casilda
Source0:        https://gitlab.gnome.org/jpu/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.18)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
# /oreon:deps
%description
A simple Wayland compositor widget for Gtk 4 which can be used to embed other
processes windows in your Gtk 4 application.
It was originally created for Cambalache's workspace using wlroots,
a modular library to create Wayland compositors.
Following Wayland tradition, this library is named after my hometown in
Santa Fe, Argentina.

%package devel
Summary: Wayland compositor for GTK4
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for Casilda.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles casilda-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n casilda-devel -f %{oreon_filedir}/casilda-devel.list

%changelog

%autochangelog
