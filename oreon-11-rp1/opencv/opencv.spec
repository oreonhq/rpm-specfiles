%global source0_hash 1d40ca017ea51c533cf9fd5cbde5b5fe7ae248291ddf2af99d4c17cf8e13017d
%global source1_hash 1e0077a4fd2960a7d2f4c9e49d6ba7bb891cac2d1be36d7e8e47aa97a9d1039b
%global source2_hash 73eda44b867b898c3266db6b0c31c1641a7b6ca6e46914c43508e780a7d56d66
%global source3_hash eeab592db2861a6c94d592a48456cf59945d31483ce94a6bc4d3a4e318049ba3
%global face_landmark_commit 8afa57abc8229d611c4937165d20e2a2d9fc5a12
%global source4_hash 3be62c864dcdd8b925e92f6a5b15a7a039819e04a6b3cf088827f08cf2cc07bf

%bcond_with  tests
%bcond_without  compat_openvc_pc
%if %{without tests}
%bcond_with     extras_tests
%else
%bcond_without  extras_tests
%endif
# linters are enabled by default if BUILD_DOCS OR BUILD_EXAMPLES
%bcond_with     linters
%bcond_without  ffmpeg
%bcond_without  gstreamer
%bcond_without  eigen3
%bcond_without  opencl
%ifarch x86_64 %{arm}
%bcond_without  openni
%else
# we dont have openni in other archs
%bcond_with     openni
%endif
%bcond_without  tbb
%bcond_with     cuda
%bcond_without  xine
# Atlas need (missing: Atlas_CLAPACK_INCLUDE_DIR Atlas_CBLAS_LIBRARY Atlas_BLAS_LIBRARY Atlas_LAPACK_LIBRARY)
# LAPACK may use atlas or openblas since now it detect openblas, atlas is not used anyway, more info please
# Now FlexiBLAS should be used instead: https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager
%bcond_with     atlas
%bcond_with     openblas
%bcond_without  flexiblas
%bcond_without  gdcm
%if 0%{?rhel} >= 8
%bcond_with     vtk
%else
%bcond_without  vtk
%endif

%ifarch x86_64
%bcond_without  libmfx
%else
%bcond_with     libmfx
%endif
%if 0%{?rhel} >= 8
%bcond_with  clp
%else
%bcond_without  clp
%endif
%ifarch %{java_arches}
%bcond_without  java
%else
%bcond_with  java
%endif

%if 0%{?fedora}
%bcond_without openexr
%else
%bcond_with openexr
%endif

%bcond_without  libva
%bcond_without  vulkan

# If _cuda_version is unset
%if 0%{!?_cuda_version:1} && 0%{?with_cuda:1}
%global _cuda_version 11.2
%global _cuda_rpm_version 11-2
%global _cuda_prefix /usr/local/cuda-%{_cuda_version}
%bcond_without dnn_cuda
%endif

Name:           opencv
Version:        4.13.0
%global javaver %(foo=%{version}; echo ${foo//./})
%global majorver %(foo=%{version}; a=(${foo//./ }); echo ${a[0]} )
%global minorver %(foo=%{version}; a=(${foo//./ }); echo ${a[1]} )
%global padding  %(digits=00; num=%{minorver}; echo ${digits:${#num}:${#digits}} )
%global abiver   %(echo %{majorver}%{padding}%{minorver} )
Release:        2%{?dist}
Summary:        Collection of algorithms for computer vision
# This is normal three clause BSD.
License:        BSD-3-Clause AND Apache-2.0 AND ISC
URL:            https://opencv.org
# strip lena/lenna and xfeatures2d in %%prep (rhbz#1295173)
Source0:        https://github.com/opencv/opencv/archive/refs/tags/%{version}.tar.gz#/opencv-%{version}.tar.gz
Source1:        https://github.com/opencv/opencv_contrib/archive/refs/tags/%{version}.tar.gz#/opencv_contrib-%{version}.tar.gz
%{?with_extras_tests:
Source2:        https://github.com/opencv/opencv_extra/archive/refs/tags/%{version}.tar.gz#/opencv_extra-%{version}.tar.gz
}
Source3:        https://raw.githubusercontent.com/opencv/opencv_3rdparty/%{face_landmark_commit}/face_landmark_model.dat#/face_landmark_model.dat
# SRC=v0.1.2d.zip ; wget https://github.com/opencv/ade/archive/$SRC; mv $SRC $(md5sum $SRC | cut -d' ' -f1)-$SRC
Source4:        https://github.com/opencv/ade/archive/v0.1.2e.zip#/962ce79e0b95591f226431f7b5f152cd-v0.1.2e.zip
Source5:        xorg.conf
%global wechat_commit 3487ef7cde71d93c6a01bb0b84aa0f22c6128f6b
%global wechat_shortcommit %(c=%{wechat_commit}; echo ${c:0:7})
%global wechat_gitdate 20230712
Source6:        https://github.com/WeChatCV/opencv_3rdparty/archive/%{wechat_commit}/wechat-%{wechat_gitdate}.git%{wechat_shortcommit}.tar.gz#/opencv-wechat-%{wechat_gitdate}.tar.gz

Patch0:        opencv-4.1.0-install_3rdparty_licenses.patch
# Fix build with vtk 9.6 - https://github.com/opencv/opencv_contrib/pull/4085
Patch1:        opencv-vtk.patch
Patch3:        opencv.python.patch
Patch4:        Fix-macro-definition-for-Power10-architecture.patch


BuildRequires:  gcc-c++
BuildRequires:  cmake >= 2.6.3
BuildRequires:  chrpath
%{?with_cuda:
BuildRequires:  cuda-minimal-build-%{?_cuda_rpm_version}
BuildRequires:  pkgconfig(cublas-%{?_cuda_version})
BuildRequires:  pkgconfig(cufft-%{?_cuda_version})
BuildRequires:  pkgconfig(nppc-%{?_cuda_version})
%{?with_dnn_cuda:BuildRequires: libcudnn8-devel}
}
%{?with_eigen3:BuildRequires:  eigen3-devel}
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
%if 0%{?fedora}
%ifnarch s390 s390x
BuildRequires:  libraw1394-devel
BuildRequires:  libdc1394-devel
%endif
%endif
BuildRequires:  jasper-devel
BuildRequires:  pkgconfig(libavif)
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libGL-devel
BuildRequires:  libv4l-devel
%{?with_openexr:
BuildRequires:  OpenEXR-devel
}
%{?with_openni:
BuildRequires:  openni-devel
%if 0%{?fedora} && 0%{?fedora} < 44
BuildRequires:  openni-primesense
%endif
}
%{?with_tbb:
BuildRequires:  tbb-devel
}
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
%{?with_linters:
BuildRequires:  pylint
BuildRequires:  python3-flake8
}
BuildRequires:  swig >= 1.3.24
%{?with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libavdevice)
}
%{?with_gstreamer:BuildRequires:  gstreamer1-devel gstreamer1-plugins-base-devel}
%{?with_xine:BuildRequires:  xine-lib-devel}
%{?with_opencl:BuildRequires:  opencl-headers}
BuildRequires:  libgphoto2-devel
BuildRequires:  libwebp-devel
BuildRequires:  tesseract-devel
BuildRequires:  protobuf-devel
BuildRequires:  gdal-devel
BuildRequires:  glog-devel
#BuildRequires:  doxygen
BuildRequires:  python3-beautifulsoup4
#for doc/doxygen/bib2xhtml.pl
#BuildRequires:  perl-open
BuildRequires:  gflags-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  hdf5-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
# Module opencv_ovis disabled because of incompatible OGRE3D version < 1.11.5
# BuildRequires:  ogre-devel
%{?with_vtk:BuildRequires: vtk-devel}
%{?with_vtk:
  %{?with_java:
BuildRequires:  vtk-java
   }
}
#ceres-solver-devel push eigen3-devel and tbb-devel
%{?with_tbb:
  %{?with_eigen3:
# CERES support is disabled. Ceres Solver for reconstruction API is required.
# seems that ceres-solver is only needed for SFM algorithms but SFM algorithms are disabled because needs xfeatures2d
# BuildRequires:  ceres-solver-devel
  }
}
%{?with_atlas:BuildRequires:  atlas-devel}
%{?with_openblas:BuildRequires:  openblas-devel}
%{?with_flexiblas:BuildRequires:  flexiblas-devel}
%{?with_gdcm:BuildRequires: gdcm-devel}
%{?with_libmfx:BuildRequires:  libvpl-devel}
%{?with_clp:BuildRequires:  coin-or-Clp-devel}
%{?with_libva:BuildRequires:   libva-devel}
%{?with_java:
BuildRequires:  ant
BuildRequires:  java-devel
}
%{?with_vulkan:BuildRequires:  vulkan-headers}
%ifnarch i686
BuildRequires: flatbuffers-devel
BuildRequires: flatbuffers-compiler
%endif
%if %{with tests}
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  mesa-dri-drivers
%endif

Requires:       opencv-core%{_isa} = %{version}-%{release}
Requires:       opencv-data = %{version}-%{release}

%description
OpenCV means Intel® Open Source Computer Vision Library. It is a collection of
C functions and a few C++ classes that implement some popular Image Processing
and Computer Vision algorithms.


%package        core
Summary:        OpenCV core libraries
Provides:       bundled(quirc) = 1.0
Obsoletes:      python2-%{name} < %{version}
# any removed modules should be listed here
Obsoletes:      %{name}-core < 4.8.0-2
Obsoletes:      %{name}-contrib < 4.8.0-2

%description    core
This package contains the OpenCV C/C++ core libraries.


%package        data
Summary:        OpenCV data
BuildArch:      noarch

%description    data
This package contains OpenCV data.


%global opencv_devel_requires %{name}-core%{_isa} = %{version}-%{release}

%define opencv_module_subpkg(m:d:) \
%global opencv_devel_requires %{opencv_devel_requires} %{name}-%{-m*}%{_isa} = %{version}-%{release}\
%define modulename %{-m:%{-m*}}%{!-m:%{error:Module name not defined}}\
%define moduledesc %{-d:%{-d*}}%{!-d:%{-m*}}\
%package %{modulename}\
Summary:  OpenCV module: %{moduledesc}\
Requires: %{name}-core%{_isa} = %{version}-%{release}\
\
%description %{modulename}\
This package contains the OpenCV %{moduledesc} module runtime.\
\
%files %{modulename}\
%{_libdir}/libopencv_%{modulename}.so.{%{abiver},%{version}}

# main modules
%opencv_module_subpkg -m calib3d -d %{quote:Camera Calibration and 3D Reconstruction}
%opencv_module_subpkg -m dnn -d %{quote:Deep Neural Network}
%opencv_module_subpkg -m features2d -d %{quote:2D Feature Detection}
%opencv_module_subpkg -m flann -d %{quote:Clustering and Search in Multi-dimensional Space}
%opencv_module_subpkg -m gapi -d %{quote:Graph API}
%opencv_module_subpkg -m highgui -d %{quote:High-level GUI}
%opencv_module_subpkg -m imgcodecs -d %{quote:Image Encoding/Decoding}
%opencv_module_subpkg -m imgproc -d %{quote:Image Processing}
%opencv_module_subpkg -m ml -d %{quote:Machine Learning}
%opencv_module_subpkg -m objdetect -d %{quote:Object Detection}
%opencv_module_subpkg -m photo -d %{quote:Computational Photography}
%opencv_module_subpkg -m stitching -d %{quote:Images stitching}
%opencv_module_subpkg -m video -d %{quote:Video Analysis}
%opencv_module_subpkg -m videoio -d %{quote:Video I/O}
# contrib/extra modules
%if %{with eigen3}
%opencv_module_subpkg -m alphamat -d %{quote:Alpha Matting}
%endif
%opencv_module_subpkg -m aruco -d %{quote:Aruco Markers}
%opencv_module_subpkg -m bgsegm -d %{quote:Background Segmentation}
%opencv_module_subpkg -m bioinspired -d %{quote:Biologically-inspired Vision Models}
%opencv_module_subpkg -m ccalib -d %{quote:Custom Calibration Pattern}
%if %{with cuda}
%opencv_module_subpkg -m cudaarithm -d %{quote:CUDA Matrix Arithmatic}
%opencv_module_subpkg -m cudabgsegm -d %{quote:CUDA Background Segmentation}
%opencv_module_subpkg -m cudacodec -d %{quote:CUDA Video Encoding/Decoding}
%opencv_module_subpkg -m cudafeatures2d -d %{quote:CUDA 2D Feature Detection}
%opencv_module_subpkg -m cudafilters -d %{quote:CUDA Image Filtering}
%opencv_module_subpkg -m cudaimgproc -d %{quote:CUDA Image Processing}
%opencv_module_subpkg -m cudalegacy -d %{quote:CUDA Legacy Support}
%opencv_module_subpkg -m cudaobjdetect -d %{quote:CUDA Object Detection}
%opencv_module_subpkg -m cudaoptflow -d %{quote:CUDA Optical Flow}
%opencv_module_subpkg -m cudastereo -d %{quote:CUDA Stereo Correspondance}
%opencv_module_subpkg -m cudawarping -d %{quote:CUDA Image Warping}
%opencv_module_subpkg -m cudev -d %{quote:CUDA Device Layer}
%endif
%opencv_module_subpkg -m cvv -d %{quote:Interactive Computer Vision Visual Debugging}
%opencv_module_subpkg -m datasets -d %{quote:Datasets Framework}
%opencv_module_subpkg -m dnn_objdetect -d %{quote:Deep Neural Network Object Detection}
%opencv_module_subpkg -m dnn_superres -d %{quote:Deep Neural Network Super Resolution}
%opencv_module_subpkg -m dpm -d %{quote:Deformable Part-based Models}
%opencv_module_subpkg -m face -d %{quote:Face Analysis}
%opencv_module_subpkg -m freetype -d %{quote:Freetype/Harfbuzz UTF-8 Strings}
%opencv_module_subpkg -m fuzzy -d %{quote:Fuzzy Math-based Image Processing}
%opencv_module_subpkg -m hdf -d %{quote:HDF Data Format I/O}
%opencv_module_subpkg -m hfs -d %{quote:Heirarchical Feature Selection}
%opencv_module_subpkg -m img_hash -d %{quote:Image Hashing}
%opencv_module_subpkg -m intensity_transform -d %{quote:Intensity Transformation}
%opencv_module_subpkg -m line_descriptor -d %{quote:Extracted Line Binary Descriptor}
%opencv_module_subpkg -m mcc -d %{quote:Macbeth Chart}
%opencv_module_subpkg -m optflow -d %{quote:Optical Flow Algorithms}
#opencv_module_subpkg -m ovis -d %%{quote:OGRE 3D Visualiser}
%opencv_module_subpkg -m phase_unwrapping -d %{quote:Phase Unwrapping}
%opencv_module_subpkg -m plot -d %{quote:2D Plotting}
%opencv_module_subpkg -m quality -d %{quote:Image Quality Analysis}
%opencv_module_subpkg -m rapid -d %{quote:Silhouette based 3D Object Tracking}
%opencv_module_subpkg -m reg -d %{quote:Image Registration}
%opencv_module_subpkg -m rgbd -d %{quote:RGB-Depth Processing}
%opencv_module_subpkg -m saliency -d %{quote:Saliency}
%opencv_module_subpkg -m shape -d %{quote:Shape Distance and Matching}
%opencv_module_subpkg -m signal -d %{quote:Signal processing algorithms}
%opencv_module_subpkg -m stereo -d %{quote:Stereo Correspondance}
%opencv_module_subpkg -m structured_light -d %{quote:Structed Light}
%opencv_module_subpkg -m superres -d %{quote:Super Resolution}
%opencv_module_subpkg -m surface_matching -d %{quote:Surface Matching}
%opencv_module_subpkg -m text -d %{quote:Text Detection and Recognition}
%opencv_module_subpkg -m tracking -d %{quote:Tracking}
%opencv_module_subpkg -m videostab -d %{quote:Video Stabilization}
%if %{with vtk}
%opencv_module_subpkg -m viz -d %{quote:3D Visualizer}
%endif
%opencv_module_subpkg -m wechat_qrcode -d %{quote:WeChat QR code detector}
%opencv_module_subpkg -m ximgproc -d %{quote:Extended Image Processing}
%opencv_module_subpkg -m xobjdetect -d %{quote:Extended Object Detection}
%opencv_module_subpkg -m xphoto -d %{quote:Extended Photo Processing}


%package        devel
Summary:        Development files for using the OpenCV library
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       %{name}-data = %{version}-%{release}
Requires:       %{opencv_devel_requires}

%description    devel
This package contains the OpenCV C/C++ library and header files, as well as
documentation. It should be installed if you want to develop programs that
will use the OpenCV library. You should consider installing opencv-doc
package.


%package        doc
Summary:        Documentation files
Requires:       opencv-devel = %{version}-%{release}
# Doc dependes on architecture, specifically whether the va_intel sample is installed depends on HAVE_VA
# BuildArch:      noarch
Provides:       %{name}-devel-docs = %{version}-%{release}
Obsoletes:      %{name}-devel-docs < %{version}-%{release}

%description    doc
This package contains the OpenCV documentation, samples and examples programs.


%package        -n python3-opencv
Summary:        Python3 bindings for apps which use OpenCV
Requires:       opencv%{_isa} = %{version}-%{release}
Requires:       python3-numpy
%{?%py_provides:%py_provides python3-%{name}}

%description    -n python3-opencv
This package contains Python3 bindings for the OpenCV library.


%package    java
Summary:    Java bindings for apps which use OpenCV
Requires:   java-headless
Requires:   javapackages-filesystem
Requires:   %{name}-core%{_isa} = %{version}-%{release}

%description java
This package contains Java bindings for the OpenCV library.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%if %{with extras_tests}
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%endif
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
# https://github.com/rpm-software-management/rpm/issues/1204
%setup -q -a1 %{?with_extras_tests:-a2} -a6

_opencv_legal_scrub() {
  find "$1" -iname '*lena*' -delete
  find "$1" -iname '*lenna*' -delete
  find "$1" -type d -name xfeatures2d -prune -exec rm -rf {} +
}
_opencv_extra_scrub() {
  find "$1" -iname '*lena*' -delete
  find "$1" -iname '*lenna*' -delete
  find "$1" \( -iname 'len*.*' -o -iname '*lena*.png' -o -iname '*lena*.jpg' \) -delete
}
_opencv_legal_scrub .
%{?with_extras_tests:_opencv_extra_scrub .}

# we don't use pre-built contribs except quirc
pushd 3rdparty
shopt -s extglob
rm -r !(dlpack|quirc|flatbuffers)
shopt -u extglob
popd &>/dev/null

%patch -P 0 -p1 -b .install_3rdparty_licenses
%patch -P 3 -p1 -b .python_install_binary
%patch -P 4 -p1 -b .ppc_macro

pushd %{name}_contrib-%{version}
%patch -P 1 -p1 -b .vtk
popd

# Install face_landmark_model
mkdir -p .cache/data
install -pm 0644 %{S:3} .cache/data/7505c44ca4eb54b4ab1e4777cb96ac05-face_landmark_model.dat
mkdir -p .cache/wechat_qrcode
mv opencv_3rdparty-%{wechat_commit}/detect.caffemodel .cache/wechat_qrcode/238e2b2d6f3c18d6c3a30de0c31e23cf-detect.caffemodel
mv opencv_3rdparty-%{wechat_commit}/detect.prototxt .cache/wechat_qrcode/6fb4976b32695f9f5c6305c19f12537d-detect.prototxt
mv opencv_3rdparty-%{wechat_commit}/sr.caffemodel .cache/wechat_qrcode/cbfcd60361a73beb8c583eea7e8e6664-sr.caffemodel
mv opencv_3rdparty-%{wechat_commit}/sr.prototxt .cache/wechat_qrcode/69db99927a70df953b471daaba03fbef-sr.prototxt

# Install ADE, needed for opencv_gapi
mkdir -p .cache/ade
install -pm 0644 %{S:4} .cache/ade/

%generate_buildrequires
cd modules/python/package
%pyproject_buildrequires

%build
# enabled by default if libraries are presents at build time:
# GTK, GSTREAMER, 1394, V4L, eigen3
# disabling IPP because it is closed source library from intel

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
%if 0%{?fedora} > 38 || 0%{?rhel} > 10
 -DCMAKE_CXX_STANDARD=17 \
%endif
 -DCV_TRACE=OFF \
 -DWITH_IPP=OFF \
 -DWITH_ITT=OFF \
 -DWITH_QT=ON \
 -DWITH_OPENGL=ON \
%if ! %{with tests}
 -DBUILD_TESTS=OFF \
%endif
 -DOpenGL_GL_PREFERENCE=GLVND \
 -DWITH_GDAL=ON \
%{?with_openexr: -DWITH_OPENEXR=ON} \
%{!?with_openexr: -DWITH_OPENEXR=OFF} \
 -DCMAKE_SKIP_RPATH=ON \
 -DWITH_CAROTENE=OFF \
%ifarch x86_64 %{ix86}
 -DCPU_BASELINE=SSE2 \
%ifarch %{ix86}
 -DCPU_DISPATCH=SSE4_2 \
%endif
%endif
 -DCMAKE_BUILD_TYPE=Release \
 %{?with_java: -DBUILD_opencv_java=ON \
 -DOPENCV_JAR_INSTALL_PATH=%{_jnidir} } \
 %{!?with_java: -DBUILD_opencv_java=OFF } \
 %{?with_tbb: -DWITH_TBB=ON } \
 %{!?with_gstreamer: -DWITH_GSTREAMER=OFF } \
 %{!?with_ffmpeg: -DWITH_FFMPEG=OFF } \
 %{?with_cuda: \
 -DWITH_CUDA=ON \
 -DCUDA_TOOLKIT_ROOT_DIR=%{?_cuda_prefix} \
 -DCUDA_VERBOSE_BUILD=ON \
 -DCUDA_PROPAGATE_HOST_FLAGS=OFF \
 -DCUDA_NVCC_FLAGS="-Xcompiler -fPIC" \
 %{?with_dnn_cuda:-DOPENCV_DNN_CUDA=ON} \
 } \
 %{?with_openni: -DWITH_OPENNI=ON } \
 %{!?with_xine: -DWITH_XINE=OFF } \
 -DBUILD_DOCS=ON \
 -DBUILD_EXAMPLES=ON \
 -DBUILD_opencv_python2=OFF \
 -DINSTALL_C_EXAMPLES=ON \
 -DINSTALL_PYTHON_EXAMPLES=ON \
 -DPYTHON3_EXECUTABLE=%{__python3} \
 -DOPENCV_GENERATE_SETUPVARS=OFF \
 %{!?with_linters: \
 -DENABLE_PYLINT=OFF \
 -DENABLE_FLAKE8=OFF \
 } \
 -DBUILD_PROTOBUF=OFF \
 -DPROTOBUF_UPDATE_FILES=ON \
%{?with_opencl: -DOPENCL_INCLUDE_DIR=%{_includedir}/CL -DOPENCV_DNN_OPENCL=ON} \
%{!?with_opencl: -DWITH_OPENCL=OFF } \
 -DOPENCV_EXTRA_MODULES_PATH=opencv_contrib-%{version}/modules \
 -DWITH_LIBV4L=ON \
 -DWITH_OPENMP=ON \
 -DOPENCV_CONFIG_INSTALL_PATH=%{_lib}/cmake/OpenCV \
 -DOPENCV_GENERATE_PKGCONFIG=ON \
%{?with_extras_tests: -DOPENCV_TEST_DATA_PATH=opencv_extra-%{version}/testdata} \
 %{?without_eigen3: -DWITH_EIGEN=OFF} \
 %{?with_gdcm: -DWITH_GDCM=ON } \
 -DWITH_IMGCODEC_GIF=ON \
 %{?with_libmfx: -DWITH_MFX=ON  -DWITH_GAPI_ONEVPL=ON} \
 %{?with_clp: -DWITH_CLP=ON } \
 %{?with_libva: -DWITH_VA=ON } \
 %{!?with_vtk: -DWITH_VTK=OFF} \
 %{?with_vulkan: -DWITH_VULKAN=ON -DVULKAN_INCLUDE_DIRS=%{_includedir}/vulkan }

%cmake_build

cd %{__cmake_builddir}/python_loader/
%pyproject_wheel

%install
%cmake_install
cd %{__cmake_builddir}/python_loader/
%pyproject_install
%pyproject_save_files cv2
# Hack - move the binary
%ifnarch i686
mkdir -p %{buildroot}/%{python3_sitearch}/cv2
mv %{buildroot}/%{python3_sitelib}/cv2/cv2.cpython-*-linux-gnu.so \
  %{buildroot}/%{python3_sitearch}/cv2
%endif
# Correct reference in config-x.yz, keep build one for testing
mkdir test_python
cp %{buildroot}/%{python3_sitelib}/cv2/config-*.py test_python
sed -i -e "s#/builddir[^']*#%{python3_sitearch}/cv2#g" %{buildroot}/%{python3_sitelib}/cv2/config-*.py

rm -rf %{buildroot}%{_datadir}/OpenCV/licenses/
%if %{with java}
ln -s -r %{buildroot}%{_jnidir}/libopencv_java%{javaver}.so %{buildroot}%{_jnidir}/libopencv_java.so
ln -s -r %{buildroot}%{_jnidir}/opencv-%{javaver}.jar %{buildroot}%{_jnidir}/opencv.jar
%endif

# For compatibility with existing opencv.pc application
%{?with_compat_openvc_pc:
  ln -s opencv4.pc %{buildroot}%{_libdir}/pkgconfig/opencv.pc
}


%check
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/%{__cmake_builddir}/lib:$LD_LIBARY_PATH
# Due to complex import method, we need to point to builddir temporarily at least to have test working, undoing
# the fix above and then removing this again
cp %{buildroot}/%{python3_sitelib}/cv2/config-*.py .
cp %{__cmake_builddir}/python_loader/test_python/config-*.py %{buildroot}/%{python3_sitelib}/cv2/
%pyproject_check_import -e cv2.config
cp config-*.py %{buildroot}/%{python3_sitelib}/cv2/

#ifnarch ppc64
%if %{with tests}
    cp %{S:5} %{__cmake_builddir}
    if [ -x /usr/libexec/Xorg ]; then
       Xorg=/usr/libexec/Xorg
    else
       Xorg=/usr/libexec/Xorg.bin
    fi
    $Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xorg.log -config ./xorg.conf -configdir . :99 &
    export DISPLAY=:99
    %ctest || :
%endif
# endif


%files
%doc README.md
%{_bindir}/opencv_*

%files data
%license LICENSE
%dir %{_datadir}/opencv4
%{_datadir}/opencv4/haarcascades
%{_datadir}/opencv4/lbpcascades
%{_datadir}/opencv4/valgrind*
%{_datadir}/opencv4/quality

%files core
%license LICENSE
%{_datadir}/licenses/opencv4/
%{_libdir}/libopencv_core.so.{%{abiver},%{version}}

%files devel
%dir %{_includedir}/opencv4
%{_includedir}/opencv4/opencv2
%{_libdir}/lib*.so
%{?with_compat_openvc_pc:
%{_libdir}/pkgconfig/opencv.pc
}
%{_libdir}/pkgconfig/opencv4.pc
%{_libdir}/cmake/OpenCV/*.cmake

%files doc
%{_datadir}/opencv4/samples

# some files aren't properly listed
#files -n python3-opencv -f %%{pyproject_files}
%files -n python3-opencv
%{python3_sitelib}/opencv*.dist-info
%{python3_sitelib}/cv2
%ifnarch i686
%{python3_sitearch}/cv2
%endif

%if %{with java}
%files java
%{_jnidir}/libopencv_java%{javaver}.so
%{_jnidir}/opencv-%{javaver}.jar
%{_jnidir}/libopencv_java.so
%{_jnidir}/opencv.jar
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.13.0-2
- Prepare for Oreon 11 (RP1)
