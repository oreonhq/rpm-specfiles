%global source0_hash 691b074a37b2a307f7f48edc5b8c7afa7301709be56378ccf9cc9735909077fd
%global glib_version 2.48
%global gtk_version 3.20
%global po_package gtksourceview-3.0
Name: gtksourceview3
Version: 3.24.11
Release:        1%{?dist}
Summary:        Source code editing widget
License: LicenseRef-Callaway-LGPLv2+
URL: https://wiki.gnome.org/Projects/GtkSourceView
Source0:        https://download.gnome.org/sources/gtksourceview/3.24/gtksourceview-%{version}.tar.xz
Patch0:  0001-gcc14.patch
Requires: glib2%{?_isa} >= %{glib_version}
Requires: gtk3%{?_isa} >= %{gtk_version}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  make
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  vala
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gtksourceview-%{version}
%oreon_prep
%build

%configure --disable-gtk-doc --disable-static --enable-installed-tests
make %{?_smp_mflags}
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%find_lang %{po_package}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtksourceview3-devel -f %{oreon_filedir}/gtksourceview3-devel.list
%files -n gtksourceview3-tests -f %{oreon_filedir}/gtksourceview3-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.24.11-17
- Prepare for Oreon 11 (RP1)
