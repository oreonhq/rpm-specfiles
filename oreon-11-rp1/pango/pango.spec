%global source0_hash f138f964a8390c8aecc6c79dc18756989cc2d4db624b12f94a01a92ec57111ff
%global glib2_version 2.80
%global fribidi_version 1.0.6
%global libthai_version 0.1.9
%global harfbuzz_version 8.4.0
%global fontconfig_version 2.15.0
%global libXft_version 2.0.0
%global cairo_version 1.18
%global freetype_version 2.1.5
Name:    pango
Version: 1.90.0
Release:        1%{?dist}
Summary:        System for layout and rendering of internationalized text
License: LGPL-2.0-or-later
URL:     https://pango.gnome.org/
Source0:        https://download.gnome.org/sources/%{name}/1.90/%{name}-%{version}.tar.xz
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: freetype%{?_isa} >= %{freetype_version}
Requires: fontconfig%{?_isa} >= %{fontconfig_version}
Requires: cairo%{?_isa} >= %{cairo_version}
Requires: harfbuzz%{?_isa} >= %{harfbuzz_version}
Requires: libthai%{?_isa} >= %{libthai_version}
Requires: libXft%{?_isa} >= %{libXft_version}
Requires: fribidi%{?_isa} >= %{fribidi_version}
Provides: pango-tests = %{version}-%{release}
Obsoletes: pango-tests < 1.54.0-1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gi-docgen
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libthai)
BuildRequires:  pkgconfig(xft)
BuildRequires:  python3-docutils
# /oreon:deps
%description
Pango is a library for laying out and rendering of text, with an emphasis
on internationalization. Pango can be used anywhere that text layout is needed,
though most of the work on Pango so far has been done in the context of the
GTK+ widget toolkit. Pango forms the core of text and font handling for GTK+.

Pango is designed to be modular; the core Pango layout engine can be used
with different font backends.

The integration of Pango with Cairo provides a complete solution with high
quality text handling and graphics rendering.

%package devel
Summary: Development files for pango
Requires: pango%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa} >= %{glib2_version}
Requires: freetype-devel%{?_isa} >= %{freetype_version}
Requires: fontconfig-devel%{?_isa} >= %{fontconfig_version}
Requires: cairo-devel%{?_isa} >= %{cairo_version}
%description devel
The pango-devel package includes the header files for the pango package.

%package doc
Summary: Developer documentation for pango
Requires: pango%{?_isa} = %{version}-%{release}
Recommends: gi-docgen-fonts
%description doc
The pango-doc package contains developer documentation for the pango package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pango-%{version}
%oreon_prep
%build

export CFLAGS='-std=c11 %optflags'
%meson \
  -Dbuild-examples=true \
  -Ddocumentation=true
%meson_build
%install
%meson_install
PANGOXFT_SO=$RPM_BUILD_ROOT%{_libdir}/libpangoxft-1.0.so
if ! test -e $PANGOXFT_SO; then
        echo "$PANGOXFT_SO not found; did not build with Xft support?"
        ls $RPM_BUILD_ROOT%{_libdir}
        exit 1
fi
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pango-devel -f %{oreon_filedir}/pango-devel.list
%files -n pango-doc -f %{oreon_filedir}/pango-doc.list

%changelog

%autochangelog
