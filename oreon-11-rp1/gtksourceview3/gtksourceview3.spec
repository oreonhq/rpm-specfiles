%global source0_hash 691b074a37b2a307f7f48edc5b8c7afa7301709be56378ccf9cc9735909077fd

%global glib_version 2.48
%global gtk_version 3.20

%global po_package gtksourceview-3.0

Name: gtksourceview3
Version: 3.24.11
Release: 17%{?dist}
Summary: Source code editing widget

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: https://wiki.gnome.org/Projects/GtkSourceView
Source0: https://download.gnome.org/sources/gtksourceview/3.24/gtksourceview-%{version}.tar.xz
# fix build with GCC 14 -Wincompatible-pointer-types
Patch0:  0001-gcc14.patch

BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk_version}
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: vala
BuildRequires: make

Requires: glib2%{?_isa} >= %{glib_version}
Requires: gtk3%{?_isa} >= %{gtk_version}

%description
GtkSourceView is a GNOME library that extends GtkTextView, the standard GTK+
widget for multiline text editing. GtkSourceView adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features
typical of a source code editor.

This package contains version 3 of GtkSourceView.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n gtksourceview-%{version} -p1

%build
%configure --disable-gtk-doc --disable-static --enable-installed-tests

make %{?_smp_mflags}

%install
%make_install

# remove unwanted files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{po_package}

%ldconfig_scriptlets

%files -f %{po_package}.lang
%doc README AUTHORS NEWS MAINTAINERS
%license COPYING
%{_datadir}/gtksourceview-3.0
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/GtkSource-3.0.typelib

%files devel
%{_includedir}/gtksourceview-3.0
%{_datadir}/gtk-doc/html/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/GtkSource-3.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtksourceview-3.0.deps
%{_datadir}/vala/vapi/gtksourceview-3.0.vapi

%files tests
%{_libexecdir}/installed-tests/gtksourceview-3.0/
%{_datadir}/installed-tests/gtksourceview-3.0/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.24.11-17
- Prepare for Oreon 11 (RP1)
