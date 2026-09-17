%global source0_hash 2213b56fdaff2220d0e38c8e420cbe1a83c87374190cba8c70af2156097ce30a

%{?mingw_package_header}

Name:           mingw-SDL2_image
Version:        2.8.8
Release:        4%{?dist}
Summary:        MinGW Windows port of the Image loading library for SDL2

License:        LGPL-2.0-or-later
URL:            https://github.com/libsdl-org/SDL_image
Source0:        https://github.com/libsdl-org/SDL_image/releases/download/release-%{version}/SDL2_image-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp

%description
Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL2 surfaces.

# Win32
%package -n mingw32-SDL2_image
Summary:        MinGW Windows port of the Image loading library for SDL2

%description -n mingw32-SDL2_image
Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL2 surfaces.

# Win64
%package -n mingw64-SDL2_image
Summary:        MinGW Windows port of the Image loading library for SDL2

%description -n mingw64-SDL2_image
Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL2 surfaces.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n SDL2_image-%{version}

%build
# the --disabled-*-shared lines below stops SDL2_image from loading those
# libraries at link time. Instead they are loaded when needed.
%mingw_configure \
    --disable-jpg-shared \
    --disable-png-shared \
    --disable-tif-shared \
    --disable-webp-shared \
    --disable-static
#    --disable-dependency-tracking \
%mingw_make_build

%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Win32
%files -n mingw32-SDL2_image
%license LICENSE.txt
%{mingw32_bindir}/SDL2_image.dll
%{mingw32_libdir}/libSDL2_image.dll.a
%{mingw32_libdir}/cmake/SDL2_image/
%{mingw32_libdir}/pkgconfig/SDL2_image.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_image
%license LICENSE.txt
%{mingw64_bindir}/SDL2_image.dll
%{mingw64_libdir}/libSDL2_image.dll.a
%{mingw64_libdir}/cmake/SDL2_image/
%{mingw64_libdir}/pkgconfig/SDL2_image.pc
%{mingw64_includedir}/SDL2

%changelog
%autochangelog
