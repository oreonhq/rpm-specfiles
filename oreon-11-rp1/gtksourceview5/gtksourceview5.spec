%global source0_hash none

%global glib_version 2.72
%global gtk_version 4.17

%global api_ver 5

%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)

Name:           gtksourceview5
Version:        5.20.0
Release:        %autorelease
Summary:        Source code editing widget

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0: https://download.gnome.org/sources/gtksourceview/%{major_minor_version}/gtksourceview-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk_version}
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  vala

Requires: glib2%{?_isa} >= %{glib_version}
Requires: gtk4%{?_isa} >= %{gtk_version}
Requires: hicolor-icon-theme

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
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
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
%autosetup -n gtksourceview-%{version} -p1

%build
%meson -Ddocumentation=true -Dsysprof=true -Dinstall-tests=true
%meson_build

%install
%meson_install

%find_lang gtksourceview-%{api_ver}

%files -f gtksourceview-%{api_ver}.lang
%license COPYING
%doc NEWS README.md
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GtkSource-%{api_ver}.typelib
%{_libdir}/libgtksourceview-%{api_ver}.so.0*
%{_datadir}/gtksourceview-%{api_ver}/
%{_datadir}/icons/hicolor/scalable/actions/*

%files devel
%{_includedir}/gtksourceview-%{api_ver}/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgtksourceview-%{api_ver}.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GtkSource-%{api_ver}.gir
%{_datadir}/doc/gtksourceview5
%{_datadir}/vala

%files tests
%{_bindir}/gtksourceview%{api_ver}-widget
%{_libexecdir}/installed-tests
%{_datadir}/installed-tests

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.20.0-1
- Prepare for Oreon 11 (RP1)
