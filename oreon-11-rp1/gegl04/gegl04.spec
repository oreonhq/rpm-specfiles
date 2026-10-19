%global source0_hash ccbb8cdd1db56ecd4ece5dbabae0118ab2c46b5b3439c94f3cec467798ce956d
%global apiver 0.4
%bcond use_system_libnsgif 0
%bcond lensfun 1
%bcond docs 1
Name:           gegl04
Version:        0.4.72
Release:        1%{?dist}
Summary:        Graph based image processing framework
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.gegl.org/
Source0:        http://download.gimp.org/pub/gegl/%{apiver}/gegl-%{version}.tar.xz
%if %{with lensfun}
%endif
%if %{with use_system_libnsgif}
%endif
Provides:       bundled(poly2tri-c)
%if %{without use_system_libnsgif}
Provides:       bundled(libnsgif) = 1.0.0
%endif
Recommends: %{name}-matting-levin%{?_isa}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  chrpath
BuildRequires:  enscript
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libspiro-devel
BuildRequires:  meson
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(babl-0.1)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jasper)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  ruby
BuildRequires:  suitesparse-devel
BuildRequires:  vala
# /oreon:deps
%description
GEGL (Generic Graphics Library) is a graph based image processing framework.
GEGLs original design was made to scratch GIMP's itches for a new
compositing and processing core. This core is being designed to have
minimal dependencies and a simple well defined API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use GEGL API version %{apiver}.

%package        matting-levin
Summary:        Matting Levin foreground select plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    matting-levin
The Matting Levin foreground select plugin for %{name}.

%if %{with docs}
%package        devel-docs
Summary:        Documentation files for developing with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel-docs
The %{name}-devel-docs package contains documentation files for developing
applications that use GEGL API version %{apiver}.
%endif

%package        tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
The %{name}-tools package contains tools for the command line that use the
GEGL library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n gegl-%{version}
%if %{with use_system_libnsgif}
rm -rf subprojects/libnsgif
%endif

%build

%meson --auto-features=auto %{!?with_docs:-Ddocs=false -Dgtk-doc=false}%{?with_docs:-Ddocs=true -Dgtk-doc=true}
%meson_build
%install
%meson_install
chrpath --delete %{buildroot}%{_bindir}/*
chrpath --delete %{buildroot}%{_libdir}/*.so*
chrpath --delete %{buildroot}%{_libdir}/gegl-%{apiver}/*.so
%find_lang gegl-%{apiver}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gegl04-devel -f %{oreon_filedir}/gegl04-devel.list
%files -n gegl04-matting-levin -f %{oreon_filedir}/gegl04-matting-levin.list
%files -n gegl04-devel-docs -f %{oreon_filedir}/gegl04-devel-docs.list
%files -n gegl04-tools -f %{oreon_filedir}/gegl04-tools.list

%changelog

%autochangelog
