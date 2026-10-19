%global source0_hash 6c20bd16c87aba15869e56444424481f632ac302989a203e8ce4dcc73dea33a5
Name:           gnome-autoar
Version:        0.5.2
Release:        1%{?dist}
Summary:        Archive library
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-autoar
Source0:        https://download.gnome.org/sources/%{name}/0.5/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  vala
# /oreon:deps
%description
gnome-autoar is a GObject based library for handling archives.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dvapi=true \
       -Dgtk_doc=true \
       -Dtests=true \
        %{nil}
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gnome-autoar-devel -f %{oreon_filedir}/gnome-autoar-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.5-4
- Prepare for Oreon 11 (RP1)
