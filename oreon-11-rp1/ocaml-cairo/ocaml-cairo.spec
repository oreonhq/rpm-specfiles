%global source0_hash 25dc41c9436d9abcf56caad9a105944ff7346041b8cc6a2a654ab8848b657372
ExcludeArch: %{ix86}
Name:           ocaml-cairo
Epoch:          2
Version:        0.6.5
Release:        6%{?dist}
Summary:        OCaml library for accessing cairo graphics
License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/Chris00/%{name}
VCS:            git:%{url}.git
Source0:        https://github.com/Chris00/%{name}/releases/download/%{version}/cairo2-%{version}.tbz
Patch0:         https://github.com/Chris00/ocaml-cairo/pull/37.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
# /oreon:deps
%description

This package contains OCaml bindings for Cairo.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       cairo-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        gtk
Summary:        OCaml library to render cairo on a gtk2 canvas
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    gtk

This package contains OCaml bindings for rendering cairo on a gtk2 canvas.

%package        gtk-devel
Summary:        Development files for %{name}-gtk
Requires:       %{name}-gtk%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       ocaml-lablgtk-devel%{?_isa}
%description    gtk-devel
The %{name}-gtk-devel package contains libraries and signature files for
developing applications that use %{name}-gtk.

%package        pango
Summary:        OCaml library to use pango with cairo
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    pango

This package contains OCaml bindings to use pango with cairo.

%package        pango-devel
Summary:        Development files for %{name}-pango
Requires:       %{name}-pango%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       ocaml-lablgtk-devel%{?_isa}
Requires:       pango-devel%{?_isa}
%description    pango-devel
The %{name}-pango-devel package contains libraries and signature files
for developing applications that use %{name}-pango.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cairo2-%{version}
%oreon_prep
%build

cairo_cflags="$(pkgconf --cflags cairo)"
cairo_libs="$(pkgconf --libs cairo)"
gtk_cflags="$(pkgconf --cflags gtk+-2.0)"
gtk_libs="$(pkgconf --libs gtk+-2.0)"
export CAIRO_CFLAGS="%{build_cflags} $cairo_cflags"
export CAIRO_LIBS="%{build_ldflags} $cairo_libs"
export GTK_CFLAGS="%{build_cflags} $gtk_cflags"
export GTK_LIBS="%{build_ldflags} $gtk_libs"
%dune_build
%install
%dune_install -s
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-cairo-devel -f %{oreon_filedir}/ocaml-cairo-devel.list
%files -n ocaml-cairo-gtk -f %{oreon_filedir}/ocaml-cairo-gtk.list
%files -n ocaml-cairo-gtk-devel -f %{oreon_filedir}/ocaml-cairo-gtk-devel.list
%files -n ocaml-cairo-pango -f %{oreon_filedir}/ocaml-cairo-pango.list
%files -n ocaml-cairo-pango-devel -f %{oreon_filedir}/ocaml-cairo-pango-devel.list

%changelog

%autochangelog
