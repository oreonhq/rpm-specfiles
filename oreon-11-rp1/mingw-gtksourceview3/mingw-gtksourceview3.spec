%global source0_hash 691b074a37b2a307f7f48edc5b8c7afa7301709be56378ccf9cc9735909077fd

%{?mingw_package_header}

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%define po_package gtksourceview-3.0

Name:           mingw-gtksourceview3
Version:        3.24.11
Release:        19%{?dist}
Summary:        MinGW Windows library for viewing source files

# the library itself is LGPL, some .lang files are GPL
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtksourceview/%{release_version}/gtksourceview-%{version}.tar.xz
# Fix assignment to incompatible pointer type
Patch0:         gtksourceview-incompat-pointer-type.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarshal and glib-mkenums
BuildRequires:  glib2-devel
BuildRequires:  intltool

%description
GtkSourceView is a text widget that extends the standard GTK+
GtkTextView widget. It improves GtkTextView by implementing
syntax highlighting and other features typical of a source code editor.

This package contains the MinGW Windows cross compiled GtkSourceView library,
version 3.

%package -n     mingw32-gtksourceview3
Summary:        MinGW Windows library for viewing source files

%description -n mingw32-gtksourceview3
GtkSourceView is a text widget that extends the standard GTK+
GtkTextView widget. It improves GtkTextView by implementing
syntax highlighting and other features typical of a source code editor.

This package contains the MinGW Windows cross compiled GtkSourceView library,
version 3.

%package -n     mingw64-gtksourceview3
Summary:        MinGW Windows library for viewing source files

%description -n mingw64-gtksourceview3
GtkSourceView is a text widget that extends the standard GTK+
GtkTextView widget. It improves GtkTextView by implementing
syntax highlighting and other features typical of a source code editor.

This package contains the MinGW Windows cross compiled GtkSourceView library,
version 3.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gtksourceview-%{version}

%build
%mingw_configure \
  --disable-static \
  --disable-gtk-doc \
  --disable-introspection

%mingw_make_build

%install
%mingw_make_install

# Remove .la files
rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la

# Remove documentation that duplicates what's in the native package
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc

%mingw_find_lang %{po_package}

%files -n mingw32-gtksourceview3 -f mingw32-%{po_package}.lang
%license COPYING
%{mingw32_bindir}/libgtksourceview-3.0-1.dll
%{mingw32_includedir}/gtksourceview-3.0/
%{mingw32_libdir}/libgtksourceview-3.0.dll.a
%{mingw32_libdir}/pkgconfig/gtksourceview-3.0.pc
%{mingw32_datadir}/gtksourceview-3.0/

%files -n mingw64-gtksourceview3 -f mingw64-%{po_package}.lang
%license COPYING
%{mingw64_bindir}/libgtksourceview-3.0-1.dll
%{mingw64_includedir}/gtksourceview-3.0/
%{mingw64_libdir}/libgtksourceview-3.0.dll.a
%{mingw64_libdir}/pkgconfig/gtksourceview-3.0.pc
%{mingw64_datadir}/gtksourceview-3.0/

%changelog
%autochangelog
