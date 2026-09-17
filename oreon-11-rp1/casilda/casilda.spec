%global source0_hash c9d916c61cc71e947061be1cd99b889720b3cb1d6c2ba53e7c23f58bb8ada9d5

Name:           casilda
Version:        1.0.0
Release:        %autorelease
Summary:        Wayland compositor for GTK4

# The entire source is LGPL-2.1-only, except src/casilda.h and
# src/casilda-version.h.in, which are LGPL-2.1-or-later.
License:        LGPL-2.1-only AND LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/jpu/casilda
Source:         %{url}/-/archive/%{version}/casilda-%{version}.tar.gz

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

%autosetup -p 1

%build
%meson
%meson_build

%install
%meson_install

%check
# Nothing yet

%files
%license COPYING
%doc README.md
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Casilda-1.0.typelib
%{_libdir}/libcasilda-1.0.so.1
%{_libdir}/libcasilda-1.0.so.1.0

%files devel
%dir %{_includedir}/casilda
%{_includedir}/casilda/*.h
%{_libdir}/libcasilda-1.0.so
%{_libdir}/pkgconfig/casilda-1.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Casilda-1.0.gir

%changelog
%autochangelog
