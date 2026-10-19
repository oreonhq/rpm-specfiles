%global source0_hash 074671a3ed6fbcd67cae2a40e539107f4f097ca8a4ab1a894c05e2524ff340ef
%{?mingw_package_header}
Name:           mingw-librsvg2
Version:        2.63.0
Release:        1%{?dist}
Summary:        SVG library based on cairo for MinGW
License:        LGPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/LibRsvg
BuildArch:      noarch
Source0:        https://download.gnome.org/sources/librsvg/2.57/librsvg-%{version}.tar.xz
Source1:        librsvg-%{version}-vendor.tar.xz
Patch0:         librsvg_libs.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  cargo
BuildRequires:  gdk-pixbuf2
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-libcroco
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-libcroco
BuildRequires:  mingw64-pango
BuildRequires:  perl-File-Temp
BuildRequires:  rust-std-static-i686-pc-windows-gnu
BuildRequires:  rust-std-static-x86_64-pc-windows-gnu
# /oreon:deps
%description
An SVG library based on cairo for MinGW.

%package -n mingw32-librsvg2
Summary:        MinGW SVG library based on cairo
Requires:       pkgconfig
%description -n mingw32-librsvg2
This package contains the header files and libraries needed to develop
applications that use librsvg2.

%package -n mingw32-librsvg2-static
Summary:        MinGW SVG static library based on cairo
Requires:       mingw32-librsvg2 = %{version}-%{release}
%description -n mingw32-librsvg2-static
This package contains the static libraries needed to develop
applications that use librsvg2.

%package -n mingw64-librsvg2
Summary:        MinGW SVG library based on cairo
Requires:       pkgconfig
%description -n mingw64-librsvg2
This package contains the header files and libraries needed to develop
applications that use librsvg2.

%package -n mingw64-librsvg2-static
Summary:        MinGW static color daemon
Requires:       mingw64-librsvg2 = %{version}-%{release}
%description -n mingw64-librsvg2-static
This package contains the static libraries needed to develop
applications that use librsvg2.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n librsvg-%{version} -a1

mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build

MINGW32_CONFIGURE_ARGS="RUST_TARGET=i686-pc-windows-gnu" \
MINGW64_CONFIGURE_ARGS="RUST_TARGET=x86_64-pc-windows-gnu" \
%mingw_configure \
        --disable-gtk-doc \
        --enable-introspection=no \
        --without-pic
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name "*.la" -delete
rm -rf %{buildroot}%{mingw32_datadir}/man
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw32_datadir}/doc/librsvg
rm -rf %{buildroot}%{mingw64_datadir}/man
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/doc/librsvg
%oreon_autofiles mingw32-librsvg2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-librsvg2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-librsvg2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-librsvg2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-librsvg2 -f %{oreon_filedir}/mingw32-librsvg2.list
%files -n mingw32-librsvg2-static -f %{oreon_filedir}/mingw32-librsvg2-static.list
%files -n mingw64-librsvg2 -f %{oreon_filedir}/mingw64-librsvg2.list
%files -n mingw64-librsvg2-static -f %{oreon_filedir}/mingw64-librsvg2-static.list

%changelog

%autochangelog
