%global source0_hash 88c3a3e0a5300532f3d368d5df64838a87f1fb85273f22d41df0a6b8d0ec59c6
%global apiver  0
Name:           gtk-layer-shell
Version:        0.10.1
Release:        1%{?dist}
Summary:        Library to create components for Wayland using the Layer Shell
License:        LGPL-3.0-or-later and MIT
URL:            https://github.com/wmww/gtk-layer-shell
Source0:        https://github.com/wmww/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  vala
# /oreon:deps
%description
A library to write GTK applications that use Layer Shell. Layer Shell is a
Wayland protocol for desktop shell components, such as panels, notifications and
wallpapers. You can use it to anchor your windows to a corner or edge of the
output, or stretch them across the entire output. It supports all Layer Shell
features including popups and popovers (GTK popups Just Work™). This Library is
compatible with C, C++ and any language that supports GObject introspection
files (Python, Vala, etc, see using the library below).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson           \
    -Dtests=true \
    %{nil}
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gtk-layer-shell-devel -f %{oreon_filedir}/gtk-layer-shell-devel.list

%changelog

%autochangelog
