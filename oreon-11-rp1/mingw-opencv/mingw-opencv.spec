%global source0_hash none

%{?mingw_package_header}

%global pkgname opencv

Name:          mingw-%{pkgname}
Version:       4.12.0
Release:       3%{?dist}
Summary:       MinGW Windows OpenCV library

BuildArch:     noarch
License:       BSD-3-Clause AND Apache-2.0 AND ISC
URL:           https://opencv.org
# RUN opencv-clean.sh TO PREPARE TARBALLS FOR FEDORA
#
# Need to remove copyrighted lena.jpg images from tarball (rhbz#1295173)
# and SIFT/SURF from tarball, due to legal concerns.
#
Source0:       %{pkgname}-clean-%{version}.tar.gz
Source1:       %{pkgname}_contrib-clean-%{version}.tar.gz
Source2:       %{pkgname}-clean.sh

# Don't build bundled libraries
Patch0:        opencv_unbundle.patch
# Pass -mbig-obj to linker when linking python module, to prevent "too many sections" failure
Patch1:        opencv_bigobj.patch
# Fix CV_CheckGlError calling undefined function checkError if _DEBUG is not defined
Patch2:        opencv-fix-build.patch

BuildRequires: make
BuildRequires: cmake
BuildRequires: swig
BuildRequires: protobuf-compiler

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-eigen3
# BuildRequires: mingw32-flatbuffers
BuildRequires: mingw32-freetype
BuildRequires: mingw32-gdal
BuildRequires: mingw32-gstreamer1
BuildRequires: mingw32-gstreamer1-plugins-base
BuildRequires: mingw32-harfbuzz
BuildRequires: mingw32-jasper
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libpng
BuildRequires: mingw32-libtheora
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libvorbis
BuildRequires: mingw32-libwebp
BuildRequires: mingw32-openexr
BuildRequires: mingw32-openjpeg2-tools
BuildRequires: mingw32-protobuf
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-numpy
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-tesseract
BuildRequires: mingw32-vulkan-headers
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-eigen3
# BuildRequires: mingw64-flatbuffers
BuildRequires: mingw64-freetype
BuildRequires: mingw64-gdal
BuildRequires: mingw64-gstreamer1
BuildRequires: mingw64-gstreamer1-plugins-base
BuildRequires: mingw64-harfbuzz
BuildRequires: mingw64-jasper
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libpng
BuildRequires: mingw64-libtheora
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libvorbis
BuildRequires: mingw64-libwebp
BuildRequires: mingw64-openexr
BuildRequires: mingw64-openjpeg2-tools
BuildRequires: mingw64-protobuf
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-numpy
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-tesseract
BuildRequires: mingw64-vulkan-headers
BuildRequires: mingw64-zlib

%description
MinGW Windows OpenCV library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows OpenCV library

%description -n mingw32-%{pkgname}
MinGW Windows OpenCV library.

%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 OpenCV bindings
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 OpenCV bindings.

%package -n mingw32-%{pkgname}-tools
Summary:       MinGW Windows OpenCV library tools
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
MinGW Windows OpenCV library tools.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows OpenCV library

%description -n mingw64-%{pkgname}
MinGW Windows OpenCV library.

%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 OpenCV bindings
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 OpenCV bindings.

%package -n mingw64-%{pkgname}-tools
Summary:       MinGW Windows OpenCV library tools
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
MinGW Windows OpenCV library tools.

%{?mingw_debug_package}

%prep
%autosetup -p1 -n %{pkgname}-%{version} -a1
# we don't use pre-built contribs except quirc and flatbuffers
mv 3rdparty/quirc/ .
mv 3rdparty/flatbuffers/ .
rm -r 3rdparty/
mkdir 3rdparty/
mv quirc/ 3rdparty/
mv flatbuffers/ 3rdparty/

%build

# rgbd module disabled
# https://github.com/opencv/opencv_contrib/pull/2161#issuecomment-560155630
MINGW32_CMAKE_ARGS="\
    -DOPENCV_CONFIG_INSTALL_PATH=%{mingw32_libdir}/cmake/OpenCV \
    -DVULKAN_INCLUDE_DIRS=%{mingw32_includedir}/vulkan \
    -DPYTHON3_INCLUDE_PATH=%{mingw32_includedir}/python%{mingw32_python3_version} \
    -DPYTHON3_NUMPY_INCLUDE_DIRS=%{mingw32_includedir}/numpy/ " \
MINGW64_CMAKE_ARGS="\
    -DOPENCV_CONFIG_INSTALL_PATH=%{mingw64_libdir}/cmake/OpenCV \
    -DVULKAN_INCLUDE_DIRS=%{mingw64_includedir}/vulkan \
    -DPYTHON3_INCLUDE_PATH=%{mingw64_includedir}/python%{mingw64_python3_version} \
    -DPYTHON3_NUMPY_INCLUDE_DIRS=%{mingw64_includedir}/numpy/ " \
%mingw_cmake \
 -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo \
 -DWITH_IPP=OFF \
 -DWITH_ITT=OFF \
 -DWITH_QT=ON \
 -DWITH_OPENGL=ON \
 -DWITH_GDAL=ON \
 -DWITH_UNICAP=ON \
 -DWITH_CAROTENE=OFF \
 -DENABLE_PRECOMPILED_HEADERS=OFF \
 -DBUILD_opencv_java=OFF \
 -DWITH_FFMPEG=OFF \
 -DWITH_XINE=OFF \
 -DPYTHON2_EXECUTABLE=false \
 -DWITH_OPENCL=OFF \
 -DOPENCV_SKIP_PYTHON_LOADER=ON \
 -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-%{version}/modules \
 -DWITH_OPENMP=ON \
 -DBUILD_PERF_TESTS=OFF \
 -DBUILD_TESTS=OFF \
 -DBUILD_PROTOBUF=OFF \
 -DPROTOBUF_UPDATE_FILES=ON \
 -DBUILD_opencv_rgbd=OFF \
 -DWITH_OBSENSOR=OFF

%mingw_make_build

%install
%mingw_make_install

# Install licenses through %%license
mkdir install_licenses
mv %{buildroot}%{mingw32_datadir}/licenses/opencv4/* install_licenses/
rm -rf %{buildroot}%{mingw32_datadir}/licenses
rm -rf %{buildroot}%{mingw64_datadir}/licenses

# Remove stray files
rm -f %{buildroot}%{mingw32_prefix}/{LICENSE,setup_vars_opencv4.cmd}
rm -f %{buildroot}%{mingw64_prefix}/{LICENSE,setup_vars_opencv4.cmd}

%files -n mingw32-%{pkgname}
%license install_licenses/*
%{mingw32_bindir}/libopencv_*4120.dll
%{mingw32_includedir}/opencv4/
%{mingw32_libdir}/libopencv_*4120.dll.a
%{mingw32_libdir}/cmake/OpenCV/
%{mingw32_datadir}/opencv4

%files -n mingw32-python3-%{pkgname}
%{mingw32_python3_sitearch}/cv2.cpython-%{mingw32_python3_version_nodots}.dll

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license install_licenses/*
%{mingw64_bindir}/libopencv_*4120.dll
%{mingw64_includedir}/opencv4/
%{mingw64_libdir}/libopencv_*4120.dll.a
%{mingw64_libdir}/cmake/OpenCV/
%{mingw64_datadir}/opencv4

%files -n mingw64-python3-%{pkgname}
%{mingw64_python3_sitearch}/cv2.cpython-%{mingw64_python3_version_nodots}.dll

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe

%changelog
%autochangelog
