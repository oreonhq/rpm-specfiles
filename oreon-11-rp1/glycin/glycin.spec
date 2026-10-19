%global source0_hash 937ae571d76c0de5e59db944d1194981360be37ee97875729781bc3816ddeafe
%bcond check    1
%bcond heif     %{undefined rhel}
%bcond jpegxl   %{undefined rhel}
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_without bundled_rust_deps
%else
%bcond_with bundled_rust_deps
%endif
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           glycin
Version:        2.2.1
Release:        1%{?dist}
Summary:        Sandboxed image rendering
SourceLicense:  MPL-2.0 OR LGPL-2.1-or-later
License:        %{shrink:
    (MPL-2.0 OR LGPL-2.1-or-later) AND
    BSD-3-Clause AND
    GPL-3.0-or-later AND
    IJG AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (BSD-3-Clause OR Apache-2.0) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
URL:            https://gitlab.gnome.org/GNOME/glycin
Source0:        https://download.gnome.org/sources/%{name}/2.2/%{name}-%{version}.tar.xz
Patch:        0001-fix-invalid-crate-manifest-for-tests-workspace-membe.patch
Patch:        0002-Replace-serde_yaml_ng-with-equivalent-serde_yaml-dep.patch
%if %{with heif}
%endif
%if %{with jpegxl}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  rustc
BuildRequires:  vala
# /oreon:deps
%description
Sandboxed and extendable image decoding.

%package        loaders
Summary:        Sandboxed image rendering (image loading backends)
Requires:       bubblewrap
%description    loaders
Sandboxed and extendable image decoding.

This package contains the different image loading backends.

%package        thumbnailer
Summary:        Sandboxed image rendering (thumbnailer)
Requires:       glycin-loaders%{_isa} = %{version}-%{release}
Obsoletes:      gdk-pixbuf2 < 2.43.5-1
%description    thumbnailer
Sandboxed and extendable image decoding.

This package contains the thumbnailer implementation.

%package        libs
Summary:        Sandboxed image rendering (C library)
Requires:       glycin-loaders%{_isa} = %{version}-%{release}
%description    libs
Sandboxed and extendable image decoding.

This package contains a shared library interface for glycin.

%package        gtk4-libs
Summary:        Sandboxed image rendering (GTK4 integration)
Requires:       glycin-libs%{_isa} = %{version}-%{release}
%description    gtk4-libs
Sandboxed and extendable image decoding.

This package contains a shared library interface for glycin
which provides integration with GDK / GTK4.

%package        devel
Summary:        Sandboxed image rendering (development files)
Requires:       glycin-libs%{_isa} = %{version}-%{release}
%description    devel
Sandboxed and extendable image decoding.

This package contains files for developing against libglycin.

%package        gtk4-devel
Summary:        Sandboxed image rendering (GTK4 development files)
Requires:       glycin-devel%{_isa} = %{version}-%{release}
Requires:       glycin-gtk4-libs%{_isa} = %{version}-%{release}
%description    gtk4-devel
Sandboxed and extendable image decoding.

This package contains files for developing against libglycin-gtk4.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if %{with bundled_rust_deps}
%autosetup -n glycin-%{tarball_version} -N
%autopatch -p1 -M 0
cargo vendor --versioned-dirs
%else
%autosetup -n glycin-%{tarball_version} -N
%autopatch -p1
rm -rf vendor
%endif
rm -r glycin-loaders/glycin-raw
%if %{without bundled_rust_deps}
%oreon_vendor_cargo
%build

%meson \
    -Dloaders=%{?with_heif:glycin-heif,}glycin-image-rs,%{?with_jpegxl:glycin-jxl,}glycin-svg \
    -Dtest_skip_install=true \
    %{nil}
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%if %{with bundled_rust_deps}
%cargo_vendor_manifest
%endif
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%meson_test || :
%endif
%files -f %{oreon_filedir}/main.list
%files -n glycin-loaders -f %{oreon_filedir}/glycin-loaders.list
%files -n glycin-thumbnailer -f %{oreon_filedir}/glycin-thumbnailer.list
%files -n glycin-libs -f %{oreon_filedir}/glycin-libs.list
%files -n glycin-gtk4-libs -f %{oreon_filedir}/glycin-gtk4-libs.list
%files -n glycin-devel -f %{oreon_filedir}/glycin-devel.list
%files -n glycin-gtk4-devel -f %{oreon_filedir}/glycin-gtk4-devel.list

%changelog

%autochangelog
%endif
