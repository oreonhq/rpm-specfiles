%global source0_hash d2e4637ae700f72e5196b8fbd749850ed2e5e1e09c5a5be8d06ff55aaccf3b01
Name:           SDL3_image
Version:        3.4.6
Release:        1%{?dist}
Summary:        Image loading library for SDL
License:        Zlib AND (HPND-Pbmplus AND Zlib) AND MIT AND (MIT OR Unlicense) AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/libsdl-org/SDL_image
Source0:        https://github.com/libsdl-org/SDL_image/releases/download/release-%{version}/%{name}-%{version}.tar.gz
Provides:       bundled(nanosvg)
# oreon:deps
BuildRequires:  SDL3-test
BuildRequires:  cmake
BuildRequires:  cmake(libavif)
BuildRequires:  cmake(libjpeg-turbo)
BuildRequires:  cmake(sdl3)
BuildRequires:  cmake(webp)
BuildRequires:  gcc
BuildRequires:  libjxl-devel
BuildRequires:  libpng-devel
BuildRequires:  libpng-static
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  zlib-static
# /oreon:deps
%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device.

This is a simple library to load images of various formats as SDL surfaces.
It can load BMP, GIF, JPEG, LBM, PCX, PNG, PNM (PPM/PGM/PBM), QOI, TGA, XCF,
XPM, and simple SVG format images. It can also load AVIF, JPEG-XL, TIFF, and
WebP images.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cmake-filesystem
%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify the
functionality of the installed %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DSDLIMAGE_ANI=ON \
  -DSDLIMAGE_ANI_SAVE=ON \
  -DSDLIMAGE_AVIF=ON \
  -DSDLIMAGE_AVIF_SAVE=ON \
  -DSDLIMAGE_AVIF_SHARED=ON \
  -DSDLIMAGE_BACKEND_STB=OFF \
  -DSDLIMAGE_BMP=ON \
  -DSDLIMAGE_BMP_SAVE=ON \
  -DSDLIMAGE_DEPS_SHARED=ON \
  -DSDLIMAGE_GIF=ON \
  -DSDLIMAGE_GIF_SAVE=ON \
  -DSDLIMAGE_INSTALL=ON \
  -DSDLIMAGE_INSTALL_CPACK=ON \
  -DSDLIMAGE_INSTALL_MAN=ON \
  -DSDLIMAGE_JPG=ON \
  -DSDLIMAGE_JPG_SAVE=ON \
  -DSDLIMAGE_JXL=ON \
  -DSDLIMAGE_LBM=ON \
  -DSDLIMAGE_PCX=ON \
  -DSDLIMAGE_PNG=ON \
  -DSDLIMAGE_PNG_LIBPNG=ON \
  -DSDLIMAGE_PNG_SAVE=ON \
  -DSDLIMAGE_PNG_SHARED=OFF \
  -DSDLIMAGE_PNM=ON \
  -DSDLIMAGE_QOI=ON \
  -DSDLIMAGE_RELOCATABLE=OFF \
  -DSDLIMAGE_SAMPLES=ON \
  -DSDLIMAGE_SAMPLES_INSTALL=ON \
  -DSDLIMAGE_STRICT=OFF \
  -DSDLIMAGE_SVG=ON \
  -DSDLIMAGE_TESTS=ON \
  -DSDLIMAGE_TESTS_INSTALL=ON \
  -DSDLIMAGE_TGA=ON \
  -DSDLIMAGE_TGA_SAVE=ON \
  -DSDLIMAGE_TIF=ON \
  -DSDLIMAGE_TIF_SHARED=ON \
  -DSDLIMAGE_VENDORED=OFF \
  -DSDLIMAGE_WEBP=ON \
  -DSDLIMAGE_WEBP_SAVE=ON \
  -DSDLIMAGE_WEBP_SHARED=ON \
  -DSDLIMAGE_WERROR=OFF \
  -DSDLIMAGE_XCF=ON \
  -DSDLIMAGE_XPM=ON \
  -DSDLIMAGE_XV=ON
%cmake_build
%install
%cmake_install
%ifnarch s390x
%oreon_autofiles SDL3_image-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles SDL3_image-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n SDL3_image-devel -f %{oreon_filedir}/SDL3_image-devel.list
%files -n SDL3_image-tests -f %{oreon_filedir}/SDL3_image-tests.list

%changelog

%autochangelog
