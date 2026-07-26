%global source0_hash c728e2b7d4425ae81b54e1e07a3d3c8a4bd6377a63cffa43006045bceaa92e90

%global tarname goocanvas
%global apiver  2.0

Name:           goocanvas2
Version:        2.0.4
Release:        22%{?dist}
Summary:        A new canvas widget for GTK+ that uses cairo for drawing
# COPYING:          LGPL-2.0 text
# po/cs.po:         "same license as the goocanvas package"
# po/de.po:         "same license as the goocanvas package"
# po/en_GB.po:      "same license as the GooCanvas package"
# po/es.po:         "same license as the GooCanvas package"
# po/goocanvas2.pot:    "same license as the PACKAGE package"
# po/id.po:         "same license as the goocanvas package"
# po/ja.po:         "same license as the GooCanvas package"
# po/pl.po:         "same license as the goocanvas package"
# po/pt_BR.po:      "same license as the goocanvas package"
# po/sr.po:         "same license as the goocanvas package"
# po/sv.po:         "same license as the goocanvas package"
# src/goocanvas.c:      "GNU LGPL license. See COPYING"
# src/goocanvas.h:      "GNU LGPL license. See COPYING"
# src/goocanvasatk.c:       "GNU LGPL license. See COPYING"
# src/goocanvasatk.h:       "GNU LGPL license. See COPYING"
# src/goocanvasellipse.c:   "GNU LGPL license. See COPYING"
# src/goocanvasellipse.h:   "GNU LGPL license. See COPYING"
# src/goocanvasgrid.c:      "GNU LGPL license. See COPYING"
# src/goocanvasgrid.h:      "GNU LGPL license. See COPYING"
# src/goocanvasgroup.c:     "GNU LGPL license. See COPYING"
# src/goocanvasgroup.h:     "GNU LGPL license. See COPYING"
# src/goocanvasimage.c:     "GNU LGPL license. See COPYING"
# src/goocanvasimage.h:     "GNU LGPL license. See COPYING"
# src/goocanvasitem.c:      "GNU LGPL license. See COPYING"
# src/goocanvasitem.h:      "GNU LGPL license. See COPYING"
# src/goocanvasitemmodel.c:     "GNU LGPL license. See COPYING"
# src/goocanvasitemmodel.h:     "GNU LGPL license. See COPYING"
# src/goocanvasitemsimple.c:    "GNU LGPL license. See COPYING"
# src/goocanvasitemsimple.h:    "GNU LGPL license. See COPYING"
# src/goocanvaspath.c:          "GNU LGPL license. See COPYING"
# src/goocanvaspath.h:          "GNU LGPL license. See COPYING"
# src/goocanvaspolyline.c:      "GNU LGPL license. See COPYING"
# src/goocanvaspolyline.h:      "GNU LGPL license. See COPYING"
# src/goocanvasprivate.h:   "GNU LGPL license. See COPYING"
# src/goocanvasrect.c:      "GNU LGPL license. See COPYING"
# src/goocanvasrect.h:      "GNU LGPL license. See COPYING"
# src/goocanvastable.c:     "GNU LGPL license. See COPYING"
# src/goocanvastable.h:     "GNU LGPL license. See COPYING"
# src/goocanvastext.c:      "GNU LGPL license. See COPYING"
# src/goocanvastext.h:      "GNU LGPL license. See COPYING"
# src/goocanvasstyle.c:     "GNU LGPL license. See COPYING"
# src/goocanvasstyle.h:     "GNU LGPL license. See COPYING"
# src/goocanvasutils.c:     "GNU LGPL license. See COPYING"
# src/goocanvasutils.h:     "GNU LGPL license. See COPYING"
# src/goocanvaswidget.c:    "GNU LGPL license. See COPYING"
# src/goocanvaswidget.h:    "GNU LGPL license. See COPYING"
## Used at build time but not in any binary package
# demo/demo.c:              "GNU LGPL license. See COPYING"
# demo/demo-item.c:         "GNU LGPL license. See COPYING"
# demo/demo-item.h:         "GNU LGPL license. See COPYING"
# demo/demo-large-line.c:   "GNU LGPL license. See COPYING"
# demo/demo-large-line.h:   "GNU LGPL license. See COPYING"
# demo/demo-large-rect.c:   "GNU LGPL license. See COPYING"
# demo/demo-large-rect.h:   "GNU LGPL license. See COPYING"
# demo/mv-demo.c:   "GNU LGPL license. See COPYING"
## Unbundled
# aclocal.m4:       FSFULLRWD AND FSFULLR AND GPL-2.0-or-later WITH Libtool-exception AND FSFUL AND GPL-2.0-or-later WITH Autoconf-exception-generic
# bindings/Makefile.in:         FSFULLRWD
# bindings/python/Makefile.in:  FSFULLRWD
# compile:          GPL-2.0-or-later WITH Autoconf-exception-generic
# config.guess:     GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config.rpath:     FSFULLR
# config.sub:       GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# configure:        FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# demo/Makefile.in:         FSFULLRWD
# depcomp:          GPL-2.0-or-later WITH Autoconf-exception-generic
# docs/Makefile.in:         FSFULLRWD
# install-sh:       X11
# ltmain.sh:        GPL-2.0-or-later WITH Libtool-exception
# Makefile.in:      FSFULLRWD
# missing:          GPL-2.0-or-later WITH Autoconf-exception-generic
# po/Makefile.in.in:    "This file can be copied and used freely without restrictions"
# src/Makefile.in:      FSFULLRWD
## Not in any binary package and not used at build time
# INSTALL:          FSFAP
# py-compile:       GPL-2.0-or-later WITH Autoconf-exception-generic
# test-driver:      GPL-2.0-or-later WITH Autoconf-exception-generic
License:        LGPL-2.0-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic AND X11 AND FSFULLRWD AND FSFULLR AND FSFUL AND FSFAP
URL:            https://wiki.gnome.org/Projects(2f)GooCanvas.html
Source0:        https://download.gnome.org/sources/goocanvas/2.0/goocanvas-%{version}.tar.xz
# Adapt to GCC 14, bug #2261209, proposed to the upstream,
# <https://gitlab.gnome.org/GNOME/goocanvas/-/merge_requests/15>
Patch0:         goocanvas-2.0.4-Fix-building-with-GCC-14.patch
# Use recent gettext version which does not expect autoconf to inline po/Makevars
# into po/Makefile. It does not work with contemporary autoconf and gettext.
Patch1:         goocanvas-2.0.4-Allow-contemporary-gettext-version.patch
BuildRequires:  autoconf >= 2.50
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
# diffutils for cmp tool
BuildRequires:  diffutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel >= 0.19.4
BuildRequires:  gobject-introspection-devel >= 0.6.7
BuildRequires:  gtk-doc >= 1.16
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n goocanvas-%{version}
# Remove bundled and pregenerated files
rm -r ABOUT-NLS aclocal.m4 bindings/Makefile.in bindings/python/Makefile.in \
    compile config.guess config.h.in config.rpath config.sub configure \
    demo/Makefile.in depcomp docs/html docs/Makefile.in gtk-doc.make INSTALL \
    install-sh ltmain.sh Makefile.in missing po/*.gmo po/boldquot.sed \
    po/en@boldquot.header po/en@quot.header po/insert-header.sin \
    po/Makefile.in.in po/quot.sed po/remove-potcdate.sin po/Rules-quot \
    po/stamp-po src/Makefile.in test-driver

%build
gtkdocize
autoreconf -I/usr/share/gettext/m4 -fi
# python GI wrapper is not enabled yet until i figure a proper way to package it
%configure \
    --enable-gtk-doc \
    --enable-gtk-doc-html \
    --disable-gtk-doc-pdf \
    --enable-introspection \
    --disable-maintainer-mode \
    --enable-nls \
    --enable-rebuilds \
    --disable-rpath \
    --enable-shared \
    --disable-silent-rules \
    --disable-static \
    --enable-python=no
%{make_build}

%install
%{make_install}
find %buildroot -name '*.la' -delete
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README ChangeLog AUTHORS NEWS TODO
%{_libdir}/libgoocanvas-2.0.so.9{,.*}
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GooCanvas-2.0.typelib

%files devel
%{_includedir}/goocanvas-2.0
%{_libdir}/libgoocanvas-2.0.so
%{_libdir}/pkgconfig/%{tarname}-%{apiver}.pc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GooCanvas-2.0.gir

%changelog
%autochangelog
