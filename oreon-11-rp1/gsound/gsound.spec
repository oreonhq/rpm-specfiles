%global source0_hash ca2d039e1ebd148647017a7f548862350bc9af01986d39f10cfdc8e95f07881a
Name:           gsound
Version:        1.0.3
Release:        1%{?dist}
Summary:        Small gobject library for playing system sounds
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GSound
Source0:        http://download.gnome.org/sources/gsound/1.0/gsound-%{version}.tar.xz
# oreon:deps
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  vala
# /oreon:deps
%description
GSound is a small library for playing system sounds. 
It's designed to be used via GObject Introspection, 
and is a thin wrapper around the libcanberra C library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gsound-devel -f %{oreon_filedir}/gsound-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.3-12
- Prepare for Oreon 11 (RP1)
