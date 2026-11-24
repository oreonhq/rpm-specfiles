# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b43e9898e74a44c602fa27307550575638171530050aae5a69eb068422422da1
%global source1_hash e5028403e98e52a173f1d6500ad99023647a177e370638959569d5b5577a2624
%global source2_hash 13d3488ed1f083b106fddaf97e83e8d02cd7ca58bea8093a84ca1939bf1bf313
%global source3_hash c7705ea0c881790865fbf975c3f382d9ef6a7f1f96332214a390c61f10781436
%global source4_hash 3be62c864dcdd8b925e92f6a5b15a7a039819e04a6b3cf088827f08cf2cc07bf
%global source5_hash 9c37d1629d0befdc713cb2afae0c60f05931d0335a144d4227d91d8385a6dfb1
%global source6_hash 77d07e37b4e34caeb9ce934fa78d532c16847538fe2db65ff401cd62416a840f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_with  tests
%bcond_without  compat_openvc_pc
%if %{without tests}
%bcond_with     extras_tests
%else
%bcond_without  extras_tests
%endif
%bcond_with     linters
%if 0%{?oreon}
%bcond_with     ffmpeg
%else
%bcond_without  ffmpeg
%endif
%bcond_without  gstreamer
%if 0%{?oreon}
%bcond_with     eigen3
%else
%bcond_without  eigen3
%endif
%bcond_without  opencl
%if 0%{?oreon}
%bcond_with     openni
%else
%ifarch x86_64 %{arm}
%bcond_without  openni
%else
%bcond_with     openni
%endif
%endif
%bcond_without  tbb
%bcond_with     cuda
%if 0%{?oreon}
%bcond_with     xine
%else
%bcond_without  xine
%endif
%bcond_with     atlas
%bcond_with     openblas
%if 0%{?oreon}
%bcond_with     flexiblas
%else
%bcond_without  flexiblas
%endif
%if 0%{?oreon}
%bcond_with     gdcm
%else
%bcond_without  gdcm
%endif
%if 0%{?rhel} >= 8 || 0%{?oreon}
%bcond_with     vtk
%else
%bcond_without  vtk
%endif

%if 0%{?oreon}
%bcond_with     libmfx
%else
%ifarch x86_64
%bcond_without  libmfx
%else
%bcond_with     libmfx
%endif
%endif
%if 0%{?rhel} >= 8 || 0%{?oreon}
%bcond_with  clp
%else
%bcond_without  clp
%endif
%if 0%{?oreon}
%bcond_with  java
%else
%ifarch %{java_arches}
%bcond_without  java
%else
%bcond_with  java
%endif
%endif

%if 0%{?fedora} || 0%{?oreon}
%bcond_without openexr
%else
%bcond_with openexr
%endif

%bcond_without  libva
%bcond_without  vulkan

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
Release:        1%{?dist}
Summary:        Collection of algorithms for computer vision
License:        BSD-3-Clause AND Apache-2.0 AND ISC
URL:            https://opencv.org
Source0:        %{name}-clean-%{version}.tar.gz
Source1:        %{name}_contrib-clean-%{version}.tar.gz
%{?with_extras_tests:
Source2:        %{name}_extra-clean-%{version}.tar.gz
}
Source3:        face_landmark_model.dat.xz
Source4:        962ce79e0b95591f226431f7b5f152cd-v0.1.2e.zip
Source5:        xorg.conf
%global wechat_commit 3487ef7cde71d93c6a01bb0b84aa0f22c6128f6b
%global wechat_shortcommit %(c=%{wechat_commit}; echo ${c:0:7})
%global wechat_gitdate 20230712
Source6:        https://github.com/WeChatCV/opencv_3rdparty/archive/%{wechat_commit}/wechat-%{wechat_gitdate}.git%{wechat_shortcommit}.tar.gz

Patch0:         opencv-4.1.0-install_3rdparty_licenses.patch
Patch1:         opencv-vtk.patch
Patch3:         opencv.python.patch
Patch4:         Fix-macro-definition-for-Power10-architecture.patch
Patch5:         opencv-ffmpeg9.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
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
BuildRequires:  python3-beautifulsoup4
BuildRequires:  gflags-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  libGLU-devel
BuildRequires:  hdf5-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
%{?with_vtk:BuildRequires: vtk-devel}
%{?with_vtk:
  %{?with_java:
BuildRequires:  vtk-java
   }
}
%{?with_tbb:
  %{?with_eigen3:
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
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
echo '%{source5_hash}  %{SOURCE5}' | sha256sum -c -
echo '%{source6_hash}  %{SOURCE6}' | sha256sum -c -
%setup -q -a1 %{?with_extras_tests:-a2} -a6

pushd 3rdparty
shopt -s extglob
rm -r !(dlpack|quirc|flatbuffers)
shopt -u extglob
popd &>/dev/null

%patch -P 0 -p1 -b .install_3rdparty_licenses
%patch -P 3 -p1 -b .python_install_binary
%patch -P 4 -p1 -b .ppc_macro
%patch -P 5 -p1 -b .ffmpeg9

pushd %{name}_contrib-%{version}
%patch -P 1 -p1 -b .vtk
popd

mkdir -p .cache/data
install -pm 0644 %{S:3} .cache/data
pushd .cache/data
  xz -d face_landmark_model.dat.xz
  mv face_landmark_model.dat 7505c44ca4eb54b4ab1e4777cb96ac05-face_landmark_model.dat
popd
mkdir -p .cache/wechat_qrcode
mv opencv_3rdparty-%{wechat_commit}/detect.caffemodel .cache/wechat_qrcode/238e2b2d6f3c18d6c3a30de0c31e23cf-detect.caffemodel
mv opencv_3rdparty-%{wechat_commit}/detect.prototxt .cache/wechat_qrcode/6fb4976b32695f9f5c6305c19f12537d-detect.prototxt
mv opencv_3rdparty-%{wechat_commit}/sr.caffemodel .cache/wechat_qrcode/cbfcd60361a73beb8c583eea7e8e6664-sr.caffemodel
mv opencv_3rdparty-%{wechat_commit}/sr.prototxt .cache/wechat_qrcode/69db99927a70df953b471daaba03fbef-sr.prototxt

mkdir -p .cache/ade
install -pm 0644 %{S:4} .cache/ade/

%generate_buildrequires
cd modules/python/package
%pyproject_buildrequires

%build

%cmake \
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
%ifnarch i686
mkdir -p %{buildroot}/%{python3_sitearch}/cv2
mv %{buildroot}/%{python3_sitelib}/cv2/cv2.cpython-*-linux-gnu.so \
  %{buildroot}/%{python3_sitearch}/cv2
%endif
mkdir test_python
cp %{buildroot}/%{python3_sitelib}/cv2/config-*.py test_python
sed -i -e "s#/builddir[^']*#%{python3_sitearch}/cv2#g" %{buildroot}/%{python3_sitelib}/cv2/config-*.py

rm -rf %{buildroot}%{_datadir}/OpenCV/licenses/
%if %{with java}
ln -s -r %{buildroot}%{_jnidir}/libopencv_java%{javaver}.so %{buildroot}%{_jnidir}/libopencv_java.so
ln -s -r %{buildroot}%{_jnidir}/opencv-%{javaver}.jar %{buildroot}%{_jnidir}/opencv.jar
%endif

%{?with_compat_openvc_pc:
  ln -s opencv4.pc %{buildroot}%{_libdir}/pkgconfig/opencv.pc
}

%check
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/%{__cmake_builddir}/lib:$LD_LIBARY_PATH
cp %{buildroot}/%{python3_sitelib}/cv2/config-*.py .
cp %{__cmake_builddir}/python_loader/test_python/config-*.py %{buildroot}/%{python3_sitelib}/cv2/
%pyproject_check_import -e cv2.config
cp config-*.py %{buildroot}/%{python3_sitelib}/cv2/

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
%autochangelog
