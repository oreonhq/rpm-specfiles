%global source0_hash 393f5efb50536ec13ca4f4affb69cc9966d3c3f969e6c5e701faddf9f9785381
Name:           SDL2_image
Version:        2.8.12
Release:        1%{?dist}
Summary:        Image loading library for SDL
License:        LicenseRef-Callaway-LGPLv2+ AND Zlib
URL:            https://github.com/libsdl-org/SDL_image
Source0:        https://github.com/libsdl-org/SDL_image/releases/download/release-%{version}/SDL2_image-%{version}.tar.gz
Provides:       bundled(miniz) = 1.15
Provides:       bundled(nanosvg)
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  libavif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libjxl-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  make
# /oreon:deps
%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL surfaces.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i -e 's/\r//g' README.txt CHANGES.txt

%build

./autogen.sh
%configure --disable-dependency-tracking \
           --disable-jpg-shared \
           --disable-png-shared \
           --disable-tif-shared \
           --disable-webp-shared \
           --disable-jxl-shared \
           --disable-avif-shared \
           --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_bindir}
./libtool --mode=install /usr/bin/install showimage %{buildroot}%{_bindir}/showimage2
chrpath -d %{buildroot}%{_bindir}/showimage2
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles SDL2_image-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SDL2_image-devel -f %{oreon_filedir}/SDL2_image-devel.list

%changelog

%autochangelog
