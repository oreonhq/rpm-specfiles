%global source0_hash 92a26c0af4ffc6676d72d9dfe0e991eb45fdf3192abee3d0855a24d6c721b013
%undefine __cmake_in_source_build
%global sover 3.1
Name:           OpenImageIO
Version:        3.1.17.0
Release:        1%{?dist}
Epoch:          1
Summary:        Library for reading and writing images
License:        BSD-3-Clause AND MIT
URL:            https://openimageio.org/
Source0:        https://github.com/AcademySoftwareFoundation/OpenImageIO/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         oiio-libheif_version.patch
ExcludeArch:    i686
# oreon:deps
BuildRequires:  LibRaw-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  cmake(OpenColorIO)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(openjph)
BuildRequires:  cmake(tbb)
BuildRequires:  dcmtk-devel
BuildRequires:  fmt-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  glew-devel
BuildRequires:  imath-devel
BuildRequires:  libheif-devel
BuildRequires:  libjxl-devel
BuildRequires:  libpng-devel
BuildRequires:  libsquish-devel
BuildRequires:  libtiff-devel
BuildRequires:  libultrahdr-devel
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

%package -n python3-openimageio
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-openimageio}
%description -n python3-openimageio
Python bindings for %{name}.

%package utils
Summary:        Command line utilities for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description utils
Command-line tools to manipulate and get information on images using the
%{name} library.

%package iv
Summary:        %{name} based image viewer
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description iv
A really nice image viewer, iv, based on %{name} classes (and so will work
with any formats for which plugins are available).

%package devel
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-iv%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-utils%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       opencv-devel
Requires:       cmake(OpenEXR)
%description devel
Development files for package %{name}

%prep

%autosetup -p1

# Remove bundled pugixml
rm -f src/include/OpenImageIO/pugixml.hpp \
      src/include/OpenImageIO/pugiconfig.hpp \
      src/libutil/OpenImageIO/pugixml.cpp 

# Remove bundled tbb
rm -rf src/include/tbb

# Install test images
#mkdir ../oiio-images && pushd ../oiio-images
#tar --strip-components=1 -xzf %{SOURCE1}
#popd

%build

mkdir build/linux && pushd build/linux
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_CXX_STANDARD=17 \
       -DCMAKE_SKIP_RPATH:BOOL=TRUE \
       -DPYTHON_VERSION=%{python3_version} \
       -DBUILD_DOCS:BOOL=TRUE \
	   -DOIIO_BUILD_TESTS:BOOL=FALSE \
       -DINSTALL_DOCS:BOOL=FALSE \
       -DINSTALL_FONTS:BOOL=FALSE \
       -DUSE_EXTERNAL_PUGIXML:BOOL=TRUE \
       -DSTOP_ON_WARNING:BOOL=FALSE \
       -DJPEG_INCLUDE_DIR=$(pkgconf --variable=includedir libjpeg) \
       -DOPENJPEG_INCLUDE_DIR=$(pkgconf --variable=includedir libopenjp2) \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DVERBOSE=TRUE
%cmake_build
%install
%cmake_install
pushd %{_vpath_builddir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -a src/doc/*.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles python3-openimageio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles OpenImageIO-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles OpenImageIO-iv usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles OpenImageIO-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n python3-openimageio -f %{oreon_filedir}/python3-openimageio.list
%files -n OpenImageIO-utils -f %{oreon_filedir}/OpenImageIO-utils.list
%files -n OpenImageIO-iv -f %{oreon_filedir}/OpenImageIO-iv.list
%files -n OpenImageIO-devel -f %{oreon_filedir}/OpenImageIO-devel.list

%changelog

%autochangelog
