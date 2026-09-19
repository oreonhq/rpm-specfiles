%global source0_hash 90e737df93f1e8a9e4a584be701a4254e7cb2e1a741566b7c9c8a89ed3449096

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/garrigue/lablgtk

Name:           ocaml-lablgtk3
Version:        3.1.5
Release:        9%{?dist}
Summary:        OCaml interface to gtk3

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://garrigue.github.io/lablgtk/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/lablgtk3-%{version}.tar.gz

BuildRequires:  help2man
BuildRequires:  ocaml >= 4.12.0
BuildRequires:  ocaml-cairo-devel >= 0.6
BuildRequires:  ocaml-camlp-streams-devel >= 5.0
BuildRequires:  ocaml-dune >= 1.8.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(goocanvas-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)

%global _description %{expand:LablGTK3 is an Objective Caml interface to gtk3.  It uses the rich type system
of Objective Caml to provide a strongly typed, yet very comfortable,
object-oriented interface to gtk3.}

%description
%_description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel%{?_isa}
Requires:       ocaml-cairo-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        goocanvas2
Summary:        OCaml interface to GooCanvas
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    goocanvas2
%_description

This package contains OCaml bindings for the GTK3 GooCanvas library.

%package        goocanvas2-devel
Summary:        Development files for %{name}-goocanvas2
Requires:       %{name}-goocanvas2%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       goocanvas2-devel%{?_isa}

%description    goocanvas2-devel
The %{name}-goocanvas2-devel package contains libraries and signature
files for developing applications that use %{name}-goocanvas2.

%package        gtkspell3
Summary:        OCaml interface to gtkspell3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtkspell3
%_description

This package contains OCaml bindings for gtkspell3.

%package        gtkspell3-devel
Summary:        Development files for %{name}-gtkspell3
Requires:       %{name}-gtkspell3%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       gtkspell3-devel%{?_isa}

%description    gtkspell3-devel
The %{name}-gtkspell3-devel package contains libraries and signature
files for developing applications that use %{name}-gtkspell3.

%package        rsvg2
Summary:        OCaml interface to librsvg2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    rsvg2
%_description

This package contains OCaml bindings for librsvg2.

%package        rsvg2-devel
Summary:        Development files for %{name}-rsvg2
Requires:       %{name}-rsvg2%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       librsvg2-devel%{?_isa}

%description    rsvg2-devel
The %{name}-rsvg2-devel package contains libraries and signature
files for developing applications that use %{name}-rsvg2.

%package        sourceview3
Summary:        OCaml interface to gtksourceview3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    sourceview3
%_description

This package contains OCaml bindings for gtksourceview3.

%package        sourceview3-devel
Summary:        Development files for %{name}-sourceview3
Requires:       %{name}-sourceview3%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       gtksourceview3-devel%{?_isa}

%description    sourceview3-devel
The %{name}-sourceview3-devel package contains libraries and signature
files for developing applications that use %{name}-sourceview3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lablgtk-%{version} -p1

%conf
# This file is empty, so drop it before we make assemble the docs
rm doc/FAQ.text

# Make sure we do not use the bundled copy of xml-light
rm -fr tools/instrospection/xml-light

%build
export LABLGTK_EXTRA_FLAGS=-g
%dune_build

# Make the man pages
HELP2MAN="-N --version-string=%{version}"
cd _build/install/default/bin
help2man $HELP2MAN -N -o ../../../../gdk_pixbuf_mlsource3.1 \
  -n 'Generate pixel data' ./gdk_pixbuf_mlsource3
help2man $HELP2MAN -N -o ../../../../lablgladecc3.1 \
  -n 'GTK interface compiler' ./lablgladecc3
cd -

%install
%dune_install -s

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p gdk_pixbuf_mlsource3.1 lablgladecc3.1 %{buildroot}%{_mandir}/man1

%check
%dune_check

%files -f .ofiles-lablgtk3
%doc CHANGES.md CHANGELOG.API README.md doc
%license LGPL LICENSE
%{_mandir}/man1/gdk_pixbuf_mlsource3.1*
%{_mandir}/man1/lablgladecc3.1*

%files devel -f .ofiles-lablgtk3-devel

%files goocanvas2 -f .ofiles-lablgtk3-goocanvas2

%files goocanvas2-devel -f .ofiles-lablgtk3-goocanvas2-devel

%files gtkspell3 -f .ofiles-lablgtk3-gtkspell3

%files gtkspell3-devel -f .ofiles-lablgtk3-gtkspell3-devel

%files rsvg2 -f .ofiles-lablgtk3-rsvg2

%files rsvg2-devel -f .ofiles-lablgtk3-rsvg2-devel

%files sourceview3 -f .ofiles-lablgtk3-sourceview3

%files sourceview3-devel -f .ofiles-lablgtk3-sourceview3-devel

%changelog
%autochangelog
