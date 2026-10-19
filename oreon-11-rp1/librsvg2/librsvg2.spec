%global source0_hash 852b18e1a00b8605528825a27dc7748bff2a5dd254028f59dc22a34ea57e81b6
%bcond check 1
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global bundled_rust_deps 1
%else
%global bundled_rust_deps 0
%endif
%global cairo_version 1.18.0
Name:           librsvg2
Summary:        An SVG library based on cairo
Version:        2.63.2
Release:        1%{?dist}
SourceLicense:  LGPL-2.1-or-later
License:        %{shrink:
    LGPL-2.1-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (BSD-3-Clause OR Apache-2.0) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
    }
URL:            https://wiki.gnome.org/Projects/LibRsvg
Source0:        https://download.gnome.org/sources/librsvg/2.63/librsvg-%{version}.tar.xz
Patch:          0001-Fedora-Drop-dependencies-required-for-benchmarking.patch
Patch:          0002-Fedora-Drop-dependencies-and-references-to-mutation-.patch
Patch:          0003-Fedora-Drop-windows-specific-dependencies.patch
%if 0%{?oreon} >= 11
%elif 0%{?bundled_rust_deps}
%else
%endif
Requires:       cairo%{?_isa} >= %{cairo_version}
Requires:       cairo-gobject%{?_isa} >= %{cairo_version}
Obsoletes:      rsvg-pixbuf-loader < %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/rst2man
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  rustc
BuildRequires:  vala
# /oreon:deps
%description
An SVG library based on cairo.

%package devel
Summary:        Libraries and include files for developing with librsvg
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%package tools
Summary:        Extra tools for librsvg
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
This package provides extra utilities based on the librsvg library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if ! 0%{?bundled_rust_deps}
%autosetup -p1 -n librsvg-%{version}
%else
%autosetup -N -n librsvg-%{version}
cargo vendor --versioned-dirs
%endif
sed -i 's/, "--locked"//g' meson/cargo_wrapper.py
%if ! 0%{?bundled_rust_deps}
%oreon_vendor_cargo
%build

%meson %{?rhel:-Davif=disabled}
%meson_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*
%if %{with check}
%check

%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n librsvg2-devel -f %{oreon_filedir}/librsvg2-devel.list
%files -n librsvg2-tools -f %{oreon_filedir}/librsvg2-tools.list

%changelog

%autochangelog
%endif
