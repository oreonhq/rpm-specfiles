%global source0_hash 7ec9d18fb283d1f84a3a3eff3b7a72b09a10c9c006597b3fbabbb5958420a87d
%bcond glade %[!(0%{?rhel} >= 10)]
%global glib_version 2.48
%global gtk_version 3.22
Name:           gtksourceview4
Version:        4.8.4
Release:        1%{?dist}
Summary:        Source code editing widget
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        https://download.gnome.org/sources/gtksourceview/4.8/gtksourceview-%{version}.tar.xz
Patch0:         0001-language-specs-use-N-U-escape-sequences.patch
%if %{with glade}
%endif
Requires: glib2%{?_isa} >= %{glib_version}
Requires: gtk3%{?_isa} >= %{gtk_version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gladeui-2.0)
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

This package contains version 4 of GtkSourceView.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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

%meson -Dgtk_doc=true %{?with_glade:-Dglade_catalog=true} -Dinstall_tests=true
%meson_build
%install
%meson_install
%find_lang gtksourceview-4
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtksourceview4-devel -f %{oreon_filedir}/gtksourceview4-devel.list
%files -n gtksourceview4-tests -f %{oreon_filedir}/gtksourceview4-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.8.4-11
- Prepare for Oreon 11 (RP1)
