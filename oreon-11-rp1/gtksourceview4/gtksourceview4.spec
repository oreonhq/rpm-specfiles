# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7ec9d18fb283d1f84a3a3eff3b7a72b09a10c9c006597b3fbabbb5958420a87d
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond glade %[!(0%{?rhel} >= 10)]

%global glib_version 2.48
%global gtk_version 3.22

Name:           gtksourceview4
Version:        4.8.4
Release:        11%{?dist}
Summary:        Source code editing widget

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        https://download.gnome.org/sources/gtksourceview/4.8/gtksourceview-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/gtksourceview/-/commit/2538a4daf1aba9c42c3dcfe2ff394874ac157c67
# https://gitlab.gnome.org/GNOME/gtksourceview/-/issues/278
# Fix some regexes to work with pcre2
Patch0:         0001-language-specs-use-N-U-escape-sequences.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
%if %{with glade}
BuildRequires:  pkgconfig(gladeui-2.0)
%endif
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk_version}
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  vala

Requires: glib2%{?_isa} >= %{glib_version}
Requires: gtk3%{?_isa} >= %{gtk_version}

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
%oreon_verify_sources
%autosetup -n gtksourceview-%{version} -p1

%build
%meson -Dgtk_doc=true %{?with_glade:-Dglade_catalog=true} -Dinstall_tests=true
%meson_build

%install
%meson_install

%find_lang gtksourceview-4

%files -f gtksourceview-4.lang
%license COPYING
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GtkSource-4.typelib
%{_libdir}/libgtksourceview-4.so.0*
%{_datadir}/gtksourceview-4/

%files devel
%{_includedir}/gtksourceview-4/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgtksourceview-4.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GtkSource-4.gir
%if %{with glade}
%dir %{_datadir}/glade
%dir %{_datadir}/glade/catalogs
%{_datadir}/glade/catalogs/gtksourceview.xml
%endif
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/*
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtksourceview-4.deps
%{_datadir}/vala/vapi/gtksourceview-4.vapi

%files tests
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/gtksourceview-4/
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/gtksourceview-4/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.8.4-11
- Prepare for Oreon 11 (RP1)
