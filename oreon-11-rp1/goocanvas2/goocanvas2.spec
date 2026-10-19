%global source0_hash c728e2b7d4425ae81b54e1e07a3d3c8a4bd6377a63cffa43006045bceaa92e90
%global tarname goocanvas
%global apiver  3.0
Name:           goocanvas2
Version:        3.0.0
Release:        1%{?dist}
Summary:        A new canvas widget for GTK+ that uses cairo for drawing
License:        LGPL-2.0-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic AND X11 AND FSFULLRWD AND FSFULLR AND FSFUL AND FSFAP
URL:            https://wiki.gnome.org/Projects(2f)GooCanvas.html
Source0:        https://download.gnome.org/sources/goocanvas/2.0/goocanvas-%{version}.tar.xz
Patch0:         goocanvas-2.0.4-Fix-building-with-GCC-14.patch
Patch1:         goocanvas-2.0.4-Allow-contemporary-gettext-version.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  diffutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n goocanvas2-devel -f %{oreon_filedir}/goocanvas2-devel.list

%changelog

%autochangelog
