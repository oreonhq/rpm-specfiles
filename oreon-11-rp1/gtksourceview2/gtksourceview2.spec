%global source0_hash f9594d8f18f6bcc3d72da4051636d7a8b4d3f6d29d6827309b262c9483644994
%define	glib2_version	2.13.6
%define	gtk2_version	2.12.0
%define po_package gtksourceview-2.0
Summary:        A library for viewing source files
Name:		gtksourceview2
Version:	5.21.0
Release:        1%{?dist}
License:	LGPL-2.0-or-later AND GPL-2.0-or-later
URL:		http://gtksourceview.sourceforge.net/
Source0:        http://download.gnome.org/sources/gtksourceview/2.11/gtksourceview-%{version}.tar.bz2
Patch0:	gtksourceview-2.11.2-cflags.patch
Patch1:	gtksourceview-2.11-fix-GCONST-def.patch
Patch2:	gtksourceview-2.11-add-libs.patch
Patch3:	gtksourceview-2.11-glib-unicode-constant.patch
Patch4:	gtksourceview-2.11-c99.patch
Patch5:	gtksourceview-b25e71c-c99-type-cast.patch
Patch6:	gtksourceview-2.11.2-test-get-languate-set-search-path.patch
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
GtkSourceView is a text widget that extends the standard GTK+
GtkTextView widget. It improves GtkTextView by implementing
syntax highlighting and other features typical of a source code editor.

This package contains version 2 of GtkSourceView. The older version
1 is contains in the gtksourceview package.

%package devel
Summary: Files to compile applications that use gtksourceview2
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
gtksourceview2-devel contains the files required to compile
applications which use GtkSourceView 2.x.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gtksourceview-%{version}
%patch -P0 -p1 -b .cflags
%patch -P1 -p1 -b .gconst
#%%patch2 -p1 -b .addlibs
%patch -P3 -p1 -b .glib-deprecated
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1 -b .search_path

# Explictly use gtk+-2.0
sed -i.gtk configure -e '\@gtk+-3.0@s|2.90|9999|'

%build

export PKG_CONFIG_PATH=%{_datadir}/pkgconfig:%{_libdir}/pkgconfig:$(pwd)
%configure \
	--disable-gtk-doc \
	--disable-static \
	--disable-deprecations \
	--disable-silent-rules \
	%{nil}
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_datadir}/gtksourceview-2.0/language-specs/check.sh
rm -f $RPM_BUILD_ROOT%{_datadir}/gtksourceview-2.0/language-specs/convert.py
%find_lang %{po_package}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

xvfb-run \
	make check \
	%{nil}
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n gtksourceview2-devel -f %{oreon_filedir}/gtksourceview2-devel.list

%changelog

%autochangelog
