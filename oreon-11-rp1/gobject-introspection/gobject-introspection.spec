%global source0_hash 920d1a3fcedeadc32acff95c2e203b319039dd4b4a08dd1a2dfd283d19c0b9ae
%global glib2_version 2.80.0
Name:           gobject-introspection
Version:        1.86.0
Release:        1%{?dist}
Summary:        Introspection system for GObject-based libraries
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause
URL:            https://wiki.gnome.org/Projects/GObjectIntrospection
Source0:        https://download.gnome.org/sources/%{name}/1.86/%{name}-%{version}.tar.xz
Patch:          workaround.patch
Requires:       glib2%{?_isa} >= %{glib2_version}
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-markdown
BuildRequires:  python3-setuptools
# /oreon:deps
%description
GObject Introspection can scan C header and source files in order to
generate introspection "typelib" files.  It also provides an API to examine
typelib files, useful for creating language bindings among other
things.

%package devel
Summary:        Libraries and headers for gobject-introspection
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libtool
Requires:       python3-mako
Requires:       python3-markdown
Requires:       python3-devel
Requires:       python3-setuptools
%description devel
Libraries and headers for gobject-introspection

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
mv giscanner/ast.py giscanner/gio_ast.py

%build

%meson -Ddoctool=enabled -Dgtk_doc=true -Dpython=%{__python3}
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gobject-introspection-devel -f %{oreon_filedir}/gobject-introspection-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.86.0-1
- Prepare for Oreon 11 (RP1)
