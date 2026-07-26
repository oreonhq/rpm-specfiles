%global source0_hash 074671a3ed6fbcd67cae2a40e539107f4f097ca8a4ab1a894c05e2524ff340ef

%{?mingw_package_header}

Name:           mingw-librsvg2
Version:        2.57.1
Release:        7%{?dist}
Summary:        SVG library based on cairo for MinGW

License:        LGPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/LibRsvg
BuildArch:      noarch
Source0:        https://download.gnome.org/sources/librsvg/2.57/librsvg-%{version}.tar.xz
# tar xf librsvg-${version}.tar.xz
# cd librsvg-${version}
# cargo vendor
# tar cfJ ../librsvg-${version}-vendor.tar.xz vendor
Source1:        librsvg-%{version}-vendor.tar.xz
# Add missing link libs
Patch0:         librsvg_libs.patch

BuildRequires:  cargo
BuildRequires:  make
BuildRequires:  automake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-libcroco
BuildRequires:  mingw32-pango
BuildRequires:  rust-std-static-i686-pc-windows-gnu

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-libcroco
BuildRequires:  mingw64-pango
BuildRequires:  rust-std-static-x86_64-pc-windows-gnu

# we need to call the host gdk-pixbuf-query-loaders executable
BuildRequires:  gdk-pixbuf2
BuildRequires:  perl-File-Temp

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

# Delete docs already part of native package
rm -rf %{buildroot}%{mingw32_datadir}/man
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw32_datadir}/doc/librsvg
rm -rf %{buildroot}%{mingw64_datadir}/man
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/doc/librsvg

%files -n mingw32-librsvg2
%license COPYING.LIB
%{mingw32_bindir}/librsvg-2-2.dll
%{mingw32_bindir}/rsvg-convert.exe
%{mingw32_includedir}/librsvg-2.0
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll.a
%{mingw32_libdir}/librsvg-2.dll.a
%{mingw32_libdir}/pkgconfig/*.pc
%dir %{mingw32_datadir}/thumbnailers
%{mingw32_datadir}/thumbnailers/librsvg.thumbnailer

%files -n mingw32-librsvg2-static
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.a
%{mingw32_libdir}/librsvg-2.a

%files -n mingw64-librsvg2
%license COPYING.LIB
%{mingw64_bindir}/librsvg-2-2.dll
%{mingw64_bindir}/rsvg-convert.exe
%{mingw64_includedir}/librsvg-2.0
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll.a
%{mingw64_libdir}/librsvg-2.dll.a
%{mingw64_libdir}/pkgconfig/*.pc
%dir %{mingw64_datadir}/thumbnailers
%{mingw64_datadir}/thumbnailers/librsvg.thumbnailer

%files -n mingw64-librsvg2-static
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.a
%{mingw64_libdir}/librsvg-2.a

%changelog
%autochangelog
