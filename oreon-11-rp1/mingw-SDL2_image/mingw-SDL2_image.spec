%global source0_hash 393f5efb50536ec13ca4f4affb69cc9966d3c3f969e6c5e701faddf9f9785381
%{?mingw_package_header}
Name:           mingw-SDL2_image
Version:        2.8.12
Release:        1%{?dist}
Summary:        MinGW Windows port of the Image loading library for SDL2
License:        LGPL-2.0-or-later
URL:            https://github.com/libsdl-org/SDL_image
Source0:        https://github.com/libsdl-org/SDL_image/releases/download/release-%{version}/SDL2_image-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp
# /oreon:deps
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
%global oreon_srcdir SDL2_image-%{version}
%oreon_prep
%build

%mingw_configure \
    --disable-jpg-shared \
    --disable-png-shared \
    --disable-tif-shared \
    --disable-webp-shared \
    --disable-static
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name "*.la" -delete
%oreon_autofiles mingw32-SDL2_image usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-SDL2_image usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-SDL2_image -f %{oreon_filedir}/mingw32-SDL2_image.list
%files -n mingw64-SDL2_image -f %{oreon_filedir}/mingw64-SDL2_image.list

%changelog

%autochangelog
