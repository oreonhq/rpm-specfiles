%global source0_hash 0b90722984561004de84847744d566809dbb9daf732a9e503b91a1b5a84e5699
%{?mingw_package_header}
Name:           mingw-SDL_image
Version:        1.2.12
Release:        1%{?dist}
Summary:        MinGW Windows port of the Image loading library for SDL
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.libsdl.org/projects/SDL_image/
Source0:        http://www.libsdl.org/projects/SDL_image/release/SDL_image-%{version}.tar.gz
Patch0:         sdl-image-incompatible-pointer-types.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-SDL
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-SDL
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-win-iconv
# /oreon:deps
%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, TIF, JPEG, PNG) as SDL surfaces.

# Win32
%package -n mingw32-SDL_image
Summary:        MinGW Windows port of the Image loading library for SDL
Requires:       pkgconfig
%description -n mingw32-SDL_image
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, TIF, JPEG, PNG) as SDL surfaces.

# Win64
%package -n mingw64-SDL_image
Summary:        MinGW Windows port of the Image loading library for SDL
Requires:       pkgconfig
%description -n mingw64-SDL_image
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, TIF, JPEG, PNG) as SDL surfaces.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir SDL_image-%{version}
%oreon_prep
%build

%mingw_configure \
    --disable-jpg-shared \
    --disable-png-shared \
    --disable-tif-shared \
    --disable-static
%mingw_make_build
%install
%mingw_make_install
iconv --from=ISO-8859-1 --to=UTF-8 CHANGES > CHANGES.new && \
touch -r CHANGES CHANGES.new && \
mv CHANGES.new CHANGES
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-SDL_image usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-SDL_image usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-SDL_image -f %{oreon_filedir}/mingw32-SDL_image.list
%files -n mingw64-SDL_image -f %{oreon_filedir}/mingw64-SDL_image.list

%changelog

%autochangelog
