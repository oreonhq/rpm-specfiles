%global source0_hash f9594d8f18f6bcc3d72da4051636d7a8b4d3f6d29d6827309b262c9483644994

%define	glib2_version	2.13.6
%define	gtk2_version	2.12.0

%define po_package gtksourceview-2.0

Summary:	A library for viewing source files
Name:		gtksourceview2
Version:	2.11.2
Release:	46%{?dist}

# Overall		LGPL-2.0-or-later
# data/language-specs/php.lang		GPL-2.0-or-later
# data/language-specs/ruby.lang		GPL-2.0-or-later
# SPDX confirmed
License:	LGPL-2.0-or-later AND GPL-2.0-or-later

URL:		http://gtksourceview.sourceforge.net/
#VCS: git:git://git.gnome.org/gtksourceview
Source0:	http://download.gnome.org/sources/gtksourceview/2.11/gtksourceview-%{version}.tar.bz2
# https://bugzilla.redhat.com/show_bug.cgi?id=661068
Patch0:	gtksourceview-2.11.2-cflags.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=672823
Patch1:	gtksourceview-2.11-fix-GCONST-def.patch
Patch2:	gtksourceview-2.11-add-libs.patch
Patch3:	gtksourceview-2.11-glib-unicode-constant.patch
Patch4:	gtksourceview-2.11-c99.patch
# https://gitlab.gnome.org/GNOME/gtksourceview/-/commit/b25e71c57fc934a7ce36e51826af9fa7c2cf9a80
Patch5:	gtksourceview-b25e71c-c99-type-cast.patch
# test_get_language needs /language-specs/ source, currently it is searched only
# from installed path, set search path from source directory
Patch6:	gtksourceview-2.11.2-test-get-languate-set-search-path.patch

BuildRequires:	GConf2-devel
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gtk+-2.0) >= %{gtk2_version}
BuildRequires:	intltool >= 0.35
BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	make
# %%check
BuildRequires:	xorg-x11-server-Xvfb

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
# Add pkgconfig search path to find out generated pc file
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

# remove unwanted files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_datadir}/gtksourceview-2.0/language-specs/check.sh
rm -f $RPM_BUILD_ROOT%{_datadir}/gtksourceview-2.0/language-specs/convert.py

%find_lang %{po_package}

%check
xvfb-run \
	make check \
	%{nil}

%ldconfig_scriptlets

%files -f %{po_package}.lang
%doc	README
%doc	AUTHORS
%license	COPYING
%license	COPYING.lib
%doc	NEWS
%doc	MAINTAINERS

%dir %{_datadir}/gtksourceview-2.0
%{_datadir}/gtksourceview-2.0/language-specs/
%{_datadir}/gtksourceview-2.0/styles/

%{_libdir}/libgtksourceview-2.0.so.0{,.*}
%{_libdir}/girepository-1.0/GtkSource-2.0.typelib

%files devel
%{_includedir}/gtksourceview-2.0
%{_datadir}/gtk-doc/html/*
%{_libdir}/pkgconfig/gtksourceview-2.0.pc
%{_libdir}/libgtksourceview-2.0.so
%{_datadir}/gir-1.0/GtkSource-2.0.gir

%changelog
%autochangelog
