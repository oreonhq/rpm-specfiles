%global source0_hash 0b90722984561004de84847744d566809dbb9daf732a9e503b91a1b5a84e5699

%{?mingw_package_header}

Name:           mingw-SDL_image
Version:        1.2.12
Release:        36%{?dist}
Summary:        MinGW Windows port of the Image loading library for SDL

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.libsdl.org/projects/SDL_image/
Source0:        http://www.libsdl.org/projects/SDL_image/release/SDL_image-%{version}.tar.gz
# Fix incompatible pointer types
Patch0:         sdl-image-incompatible-pointer-types.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-SDL
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libtiff

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-SDL
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libtiff

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

%autosetup -p1 -n SDL_image-%{version}

%build
# the --disabled-*-shared lines below stops SDL_image from loading those
# libraries at link time. Instead they are loaded when needed.
%mingw_configure \
    --disable-jpg-shared \
    --disable-png-shared \
    --disable-tif-shared \
    --disable-static
#    --disable-dependency-tracking \

%mingw_make_build

%install
%mingw_make_install

# silence rpmlint:
iconv --from=ISO-8859-1 --to=UTF-8 CHANGES > CHANGES.new && \
touch -r CHANGES CHANGES.new && \
mv CHANGES.new CHANGES

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Win32
%files -n mingw32-SDL_image
%doc README CHANGES COPYING
%{mingw32_bindir}/SDL_image.dll
%{mingw32_libdir}/libSDL_image.dll.a
%{mingw32_libdir}/pkgconfig/SDL_image.pc
%{mingw32_includedir}/SDL

# Win64
%files -n mingw64-SDL_image
%doc README CHANGES COPYING
%{mingw64_bindir}/SDL_image.dll
%{mingw64_libdir}/libSDL_image.dll.a
%{mingw64_libdir}/pkgconfig/SDL_image.pc
%{mingw64_includedir}/SDL

%changelog
%autochangelog
