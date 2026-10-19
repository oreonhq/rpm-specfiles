%global source0_hash 337a9f167b05a0202c230b72fcb0aac637deae6c8ff70420b49b4aa7670dc59d
Name:           pantheon-wayland
Version:        1.1.0
Release:        1%{?dist}
Summary:        Wayland integration library to the Pantheon Desktop
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/elementary/pantheon-wayland
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  vala
BuildRequires:  wayland-devel
# /oreon:deps
%description
Pantheon Wayland is an utility library made exclusively for the Pantheon
Desktop utilities.

%package        devel
Summary:        Wayland integration library to the Pantheon Desktop (development files)
Requires:       pantheon-wayland%{?_isa} = %{version}-%{release}
%description    devel
Pantheon Wayland is an utility library made exclusively for the Pantheon
Desktop utilities.

This package contains files useful for developing against the
pantheon-wayland library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pantheon-wayland-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pantheon-wayland-devel -f %{oreon_filedir}/pantheon-wayland-devel.list

%changelog

%autochangelog
