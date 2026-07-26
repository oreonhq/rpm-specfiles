%global source0_hash 25dc41c9436d9abcf56caad9a105944ff7346041b8cc6a2a654ab8848b657372

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Important note!
# There are at least two quite separate OCaml cairo projects.
#
# This is (packaged in Fedora >= 23):
#   http://forge.ocamlcore.org/projects/cairo/
#   https://github.com/Chris00/ocaml-cairo
#
# The other one (which used to be packaged in Fedora <= 22) is:
#   http://cairographics.org/cairo-ocaml/

Name:           ocaml-cairo
Epoch:          2
Version:        0.6.5
Release:        6%{?dist}
Summary:        OCaml library for accessing cairo graphics

License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/Chris00/%{name}
VCS:            git:%{url}.git

Source0:        %{url}/releases/download/%{version}/cairo2-%{version}.tbz
# Fix a segfault when a Cairo error occurs
# See https://github.com/Chris00/ocaml-cairo/issues/36
Patch0:         https://github.com/Chris00/ocaml-cairo/pull/37.patch

BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 2.7.0
BuildRequires:  ocaml-dune-configurator-devel >= 2.7.0
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  pkgconfig(cairo) >= 1.2.0
BuildRequires:  pkgconfig(freetype2)

%global _description %{expand:
Cairo is a multi-platform library providing anti-aliased vector-based
rendering for multiple target backends. Paths consist of line segments
and cubic splines and can be rendered at any width with various join
and cap styles. All colors may be specified with optional translucence
(opacity/alpha) and combined using the extended Porter/Duff
compositing algebra as found in the X Render Extension.

Cairo exports a stateful rendering API similar in spirit to the path
construction, text, and painting operators of PostScript, (with the
significant addition of translucence in the imaging model). When
complete, the API is intended to support the complete imaging model of
PDF 1.4.}

%description %_description

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

%description    gtk %_description

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

%description    pango %_description

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

%autosetup -n cairo2-%{version} -p1

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

%check
%dune_check

%files -f .ofiles-cairo2
%doc CHANGES.md README.md
%license GPL3.md LICENSE.md

%files devel -f .ofiles-cairo2-devel
# XXX The tutorial doesn't build.
%doc examples

%files gtk -f .ofiles-cairo2-gtk

%files gtk-devel -f .ofiles-cairo2-gtk-devel

%files pango -f .ofiles-cairo2-pango

%files pango-devel -f .ofiles-cairo2-pango-devel

%changelog
%autochangelog
