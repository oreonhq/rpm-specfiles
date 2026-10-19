%global source0_hash a4245c6930580c15ed263b9a7bb7e39f47693baec78be1026b4e0e28b233cb4e
Name: gtk-session-lock
Version: 0.2.0
Release:        1%{?dist}
Summary:        Library to use GTK 3 to build screen lockers
License: GPL-3.0-or-later AND MIT
URL: https://github.com/Cu3PO42/gtk-session-lock
Source0:        https://github.com/Cu3PO42/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
# /oreon:deps
%description
A library to use GTK 3 to build screen lockers using the secure 
ext-session-lock-v1 protocol.

This library is compatible with C, C++, and any language that 
supports GObject introspection files (Python, Vala, etc.).

This library only works on Wayland, and only on Wayland compositors 
that support the ext-session-lock-v1 protocol. Session lock is supported on:

- wlroots based compositors
- Mir-based compositors

%package devel
Summary: Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files, libraries, and other files used for developing 
with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gtk-session-lock-devel -f %{oreon_filedir}/gtk-session-lock-devel.list

%changelog

%autochangelog
