%global source0_hash 92a26c0af4ffc6676d72d9dfe0e991eb45fdf3192abee3d0855a24d6c721b013
%undefine __cmake_in_source_build
%global sover 3.1
Name:           OpenImageIO2.5
Version:        3.1.17.0
Release:        1%{?dist}
Summary:        Library for reading and writing images
License:        BSD-3-Clause AND MIT
URL:            https://openimageio.org/
Source0:        https://github.com/AcademySoftwareFoundation/OpenImageIO/archive/v%{version}/OpenImageIO-%{version}.tar.gz
Patch0:         oiio-libheif_version.patch
ExcludeArch:    i686
# oreon:deps
BuildRequires:  LibRaw-devel
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  cmake(OpenColorIO)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(tbb)
BuildRequires:  dcmtk-devel
BuildRequires:  fmt-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  glew-devel
BuildRequires:  hdf5-devel
BuildRequires:  imath-devel
BuildRequires:  jasper-devel
BuildRequires:  libheif-devel
BuildRequires:  libpng-devel
BuildRequires:  libsquish-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  opencv-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  openssl-devel
BuildRequires:  openvdb-devel
BuildRequires:  ptex-devel
BuildRequires:  pugixml-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  robin-map-devel
BuildRequires:  turbojpeg-devel
BuildRequires:  txt2man
BuildRequires:  zlib-devel
# /oreon:deps
%description
OpenImageIO is a library for reading and writing images, and a bunch of related
classes, utilities, and applications. Main features include:
- Extremely simple but powerful ImageInput and ImageOutput APIs for reading and
  writing 2D images that is format agnostic.
- Format plugins for TIFF, JPEG/JFIF, OpenEXR, PNG, HDR/RGBE, Targa, JPEG-2000,
  DPX, Cineon, FITS, BMP, ICO, RMan Zfile, Softimage PIC, DDS, SGI,
  PNM/PPM/PGM/PBM.
- An ImageCache class that transparently manages a cache so that it can access
  truly vast amounts of image data.

%package devel
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opencv-devel
Requires:       cmake(OpenEXR)
Requires:       OpenEXR-devel ilmbase-devel
Conflicts:      OpenImageIO-devel
%description devel
Development files for package %{name}

%prep

%autosetup -p1 -n OpenImageIO-%{version}

# Remove bundled pugixml
rm -f src/include/OpenImageIO/pugixml.hpp \
      src/include/OpenImageIO/pugiconfig.hpp \
      src/libutil/OpenImageIO/pugixml.cpp 

# Remove bundled tbb
rm -rf src/include/tbb

%build

mkdir build/linux && pushd build/linux
%cmake  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_CXX_STANDARD=17 \
       -DCMAKE_SKIP_RPATH:BOOL=TRUE \
       -DBUILD_DOCS:BOOL=FALSE \
	   -DOIIO_BUILD_TESTS:BOOL=FALSE \
       -DINSTALL_DOCS:BOOL=FALSE \
       -DINSTALL_FONTS:BOOL=FALSE \
       -DUSE_EXTERNAL_PUGIXML:BOOL=TRUE \
       -DSTOP_ON_WARNING:BOOL=FALSE \
       -DJPEG_INCLUDE_DIR=$(pkgconf --variable=includedir libjpeg) \
       -DOPENJPEG_INCLUDE_DIR=$(pkgconf --variable=includedir libopenjp2) \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DVERBOSE=TRUE \
	   -USE_PYTHON=FALSE
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{python3_sitearch}
%oreon_autofiles OpenImageIO2.5-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n OpenImageIO2.5-devel -f %{oreon_filedir}/OpenImageIO2.5-devel.list

%changelog

%autochangelog
