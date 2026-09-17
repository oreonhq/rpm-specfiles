%global source0_hash none

%undefine __cmake_in_source_build
%global sover 3.1

Name:           OpenImageIO
Version:        3.1.12.0
Release:        2%{?dist}
Epoch:          1
Summary:        Library for reading and writing images

License:        BSD-3-Clause AND MIT
# The included fmtlib is MIT licensed
# src/include/OpenImageIO/fmt
URL:            https://openimageio.org/
Source0:        https://github.com/AcademySoftwareFoundation/OpenImageIO/archive/v%{version}/%{name}-%{version}.tar.gz
# Images for test suite
#Source1:        https://github.com/OpenImageIO/oiio-images/archive/master/oiio-images.tar.gz

# LifHeif modifies the headers to make things work for multilib systems.
Patch0:         oiio-libheif_version.patch

# OpenVDB no longer builds for i686
ExcludeArch:    i686

# LibRaw on RHEL is only available on s390x and aarch64. As of RHEL 10 it looks
# like the package has moved back to EPEL and build for all architectures.
%if 0%{?rhel} >= 8 && 0%{?rhel} < 10
ExclusiveArch:  x86_64 ppc64le
%endif

# Utilities
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  txt2man
# Libraries
BuildRequires:  bzip2-devel
# Not currently in RHEL/EPEL
%if ! 0%{?rhel}
BuildRequires:  dcmtk-devel
%endif
BuildRequires:  fmt-devel
BuildRequires:  freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  glew-devel
BuildRequires:  imath-devel
# Only available on RPM Fusion
BuildRequires:  libheif-devel
BuildRequires:  libultrahdr-devel
BuildRequires:  turbojpeg-devel
BuildRequires:  libjxl-devel
BuildRequires:  libpng-devel
BuildRequires:  LibRaw-devel
BuildRequires:  libsquish-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  opencv-devel
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(OpenColorIO)
BuildRequires:  cmake(openjph)
BuildRequires:  openjpeg2-devel
BuildRequires:  openssl-devel
BuildRequires:  openvdb-devel
BuildRequires:  pugixml-devel
BuildRequires:  ptex-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  robin-map-devel
# OpenVDB is locked to tbb 2020.3
BuildRequires:  cmake(tbb) = 2020.3
BuildRequires:  zlib-devel

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
# The next two are required due to the binaries having cmake targets exported, see:
# https://bugzilla.redhat.com/show_bug.cgi?id=1959632
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
# CMAKE_SKIP_RPATH is OK here because it is set to FALSE internally and causes
# CMAKE_INSTALL_RPATH to be cleared, which is the desiered result.
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

# Move man pages to the right directory
pushd %{_vpath_builddir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -a src/doc/*.1 %{buildroot}%{_mandir}/man1

%check
# Not all tests pass on linux
#pushd build/linux && make test

%files
%doc CHANGES.md CREDITS.md README.md
%license LICENSE.md THIRD-PARTY.md
%{_libdir}/libOpenImageIO.so.%{sover}*
%{_libdir}/libOpenImageIO_Util.so.%{sover}*

%files -n python3-openimageio
%{python3_sitearch}/%{name}/

%files utils
%exclude %{_bindir}/iv
%{_bindir}/*
%exclude %{_mandir}/man1/iv.1.gz
%{_mandir}/man1/*.1.gz

%files iv
%{_bindir}/iv
%{_mandir}/man1/iv.1.gz

%files devel
%{_libdir}/libOpenImageIO.so
%{_libdir}/libOpenImageIO_Util.so
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%changelog
%autochangelog
