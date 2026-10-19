%global source0_hash 3ebce33c781e65590a450ecd3ffade480d8e3135b52ee996f1620d6c7dffbbff
%global glib_version 2.72
%global gtk_version 4.17
%global api_ver 5
%define major_minor_version %(echo %{version} | cut -d. -f1-2)
Name:           gtksourceview5
Version:        5.22.0
Release:        1%{?dist}
Summary:        Source code editing widget
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        https://download.gnome.org/sources/gtksourceview/%{major_minor_version}/gtksourceview-%{version}.tar.xz
Requires: glib2%{?_isa} >= %{glib_version}
Requires: gtk4%{?_isa} >= %{gtk_version}
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  vala
# /oreon:deps
%description
GtkSourceView is a GNOME library that extends GtkTextView, the standard GTK+
widget for multiline text editing. GtkSourceView adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features
typical of a source code editor.

This package contains version %{api_ver} of GtkSourceView.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gtksourceview-%{version}
%oreon_prep
%build

%meson -Ddocumentation=true -Dsysprof=true -Dinstall-tests=true
%meson_build
%install
%meson_install
%find_lang gtksourceview-%{api_ver}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtksourceview5-devel -f %{oreon_filedir}/gtksourceview5-devel.list
%files -n gtksourceview5-tests -f %{oreon_filedir}/gtksourceview5-tests.list

%changelog

%autochangelog
