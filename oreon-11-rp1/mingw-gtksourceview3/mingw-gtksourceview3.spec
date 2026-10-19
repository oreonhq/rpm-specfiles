%global source0_hash 65f7ce9d2ec683c6ff9b27a50d909f3abef65f742d11011e1b8f8b848cadf0f7
%{?mingw_package_header}
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%define po_package gtksourceview-3.0
Name:           mingw-gtksourceview3
Version:        5.21.0
Release:        1%{?dist}
Summary:        MinGW Windows library for viewing source files
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtksourceview/%{release_version}/gtksourceview-%{version}.tar.xz
Patch0:         gtksourceview-incompat-pointer-type.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-libxml2
# /oreon:deps
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
%global oreon_srcdir gtksourceview-%{version}
%oreon_prep
%build

%mingw_configure \
  --disable-static \
  --disable-gtk-doc \
  --disable-introspection
%mingw_make_build
%install
%mingw_make_install
rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc
%mingw_find_lang %{po_package}
%oreon_autofiles mingw32-gtksourceview3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gtksourceview3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gtksourceview3 -f %{oreon_filedir}/mingw32-gtksourceview3.list
%files -n mingw64-gtksourceview3 -f %{oreon_filedir}/mingw64-gtksourceview3.list

%changelog

%autochangelog
