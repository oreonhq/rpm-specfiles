%global source0_hash 4d7a5e268698c8e7e40603e36e9e3a2b76133931ce1b637c1136301491b54cc3
Name:           gom
Version:        0.5.6
Release:        1%{?dist}
Summary:        GObject to SQLite object mapper library
License:        LGPL-2.1-or-later AND GFDL-1.1-or-later
URL:            https://wiki.gnome.org/Projects/Gom
Source0:        https://download.gnome.org/sources/gom/0.5/gom-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
# /oreon:deps
%description
Gom provides an object mapper from GObjects to SQLite. It helps you write
applications that need to store structured data as well as make complex queries
upon that data.

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

%meson -Denable-gtk-doc=true
%meson_build
%install
%meson_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gom-devel -f %{oreon_filedir}/gom-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.6-1
- Prepare for Oreon 11 (RP1)
