%global source6_hash 77d07e37b4e34caeb9ce934fa78d532c16847538fe2db65ff401cd62416a840f
%global source0_hash b0528f5a1d379d59d4701cb28c36e22214cc51cf64594e5b56f2d3e6c0233095
%global source1_hash c58f6344170c39abf187c56f3843b59cab1fd3e89cf19ba2ce25dc061659b27f
%global source2_hash 3b4d40ee83dada41976fb00514e0c15f5895d6f64a63da3f0a187f0c8eaa21f6
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
%bcond_with     linters
%bcond_without  ffmpeg
%bcond_without  gstreamer
%bcond_without  eigen3
%bcond_without  opencl
%ifarch x86_64 %{arm}
%bcond_without  openni
%else
%bcond_with     openni
%endif
%bcond_without  tbb
%bcond_with     cuda
%bcond_without  xine
%bcond_with     atlas
%bcond_with     openblas
%bcond_without  flexiblas
%bcond_without  gdcm
%bcond_without  vtk
%ifarch x86_64
%bcond_without  libmfx
%else
%bcond_with     libmfx
%endif
%bcond_without  clp
%ifarch %{java_arches}
%bcond_without  java
%else
%bcond_with  java
%endif
%bcond_with openexr
%bcond_without  libva
%bcond_without  vulkan
%if 0%{!?_cuda_version:1} && 0%{?with_cuda:1}
%global _cuda_version 11.2
%global _cuda_rpm_version 11-2
%global _cuda_prefix /usr/local/cuda-%{_cuda_version}
%bcond_without dnn_cuda
%endif
Name:           opencv
Version:        5.0.0
%global javaver %(foo=%{version}; echo ${foo//./})
%global majorver %(foo=%{version}; a=(${foo//./ }); echo ${a[0]} )
%global minorver %(foo=%{version}; a=(${foo//./ }); echo ${a[1]} )
%global padding  %(digits=00; num=%{minorver}; echo ${digits:${#num}:${#digits}} )
%global abiver   %(echo %{majorver}%{padding}%{minorver} )
Release:        1%{?dist}
Summary:        Collection of algorithms for computer vision
License:        BSD-3-Clause AND Apache-2.0 AND ISC
URL:            https://opencv.org
Source0:        https://github.com/opencv/opencv/archive/refs/tags/%{version}.tar.gz#/opencv-%{version}.tar.gz
Source1:        https://github.com/opencv/opencv_contrib/archive/refs/tags/%{version}.tar.gz#/opencv_contrib-%{version}.tar.gz
%{?with_extras_tests:
Source2:        https://github.com/opencv/opencv_extra/archive/refs/tags/%{version}.tar.gz#/opencv_extra-%{version}.tar.gz
}
Source3:        https://raw.githubusercontent.com/opencv/opencv_3rdparty/%{face_landmark_commit}/face_landmark_model.dat#/face_landmark_model.dat
Source4:        https://github.com/opencv/ade/archive/v0.1.2e.zip#/962ce79e0b95591f226431f7b5f152cd-v0.1.2e.zip
Source5:        xorg.conf
%global wechat_commit 3487ef7cde71d93c6a01bb0b84aa0f22c6128f6b
%global wechat_shortcommit %(c=%{wechat_commit}; echo ${c:0:7})
%global wechat_gitdate 20230712
Source6:        https://github.com/WeChatCV/opencv_3rdparty/archive/%{wechat_commit}/wechat-%{wechat_gitdate}.git%{wechat_shortcommit}.tar.gz#/opencv-wechat-%{wechat_gitdate}.tar.gz
Patch0:        opencv-4.1.0-install_3rdparty_licenses.patch
Patch1:        opencv-vtk.patch
Patch3:        opencv.python.patch
%{?with_cuda:
%{?with_dnn_cuda:BuildRequires: libcudnn8-devel}
}
%{?with_eigen3:BuildRequires:  eigen3-devel}
%{?with_openexr:
}
%{?with_openni:
}
%{?with_tbb:
}
%{?with_linters:
}
%{?with_ffmpeg:
}
%{?with_gstreamer:BuildRequires:  gstreamer1-devel gstreamer1-plugins-base-devel}
%{?with_xine:BuildRequires:  xine-lib-devel}
%{?with_opencl:BuildRequires:  opencl-headers}
%{?with_vtk:BuildRequires: vtk-devel}
%{?with_vtk:
  %{?with_java:
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
}
%{?with_vulkan:BuildRequires:  vulkan-headers}
%ifnarch i686
%endif
%if %{with tests}
%endif
Requires:       opencv-core%{_isa} = %{version}-%{release}
Requires:       opencv-data = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-opencv = %{version}-%{release}
# /oreon:deps
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

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
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
%oreon_autofiles python3-opencv usr/lib/python3*/site-packages/opencv* usr/lib64/python3*/site-packages/opencv* usr/bin/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/opencv* usr/lib64/python3*/site-packages/opencv* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -n opencv-core -f %{oreon_filedir}/opencv-core.list
%files -n opencv-data -f %{oreon_filedir}/opencv-data.list
%files -n opencv-calib3d -f %{oreon_filedir}/opencv-calib3d.list
%files -n opencv-dnn -f %{oreon_filedir}/opencv-dnn.list
%files -n opencv-features2d -f %{oreon_filedir}/opencv-features2d.list
%files -n opencv-flann -f %{oreon_filedir}/opencv-flann.list
%files -n opencv-gapi -f %{oreon_filedir}/opencv-gapi.list
%files -n opencv-highgui -f %{oreon_filedir}/opencv-highgui.list
%files -n opencv-imgcodecs -f %{oreon_filedir}/opencv-imgcodecs.list
%files -n opencv-imgproc -f %{oreon_filedir}/opencv-imgproc.list
%files -n opencv-ml -f %{oreon_filedir}/opencv-ml.list
%files -n opencv-objdetect -f %{oreon_filedir}/opencv-objdetect.list
%files -n opencv-photo -f %{oreon_filedir}/opencv-photo.list
%files -n opencv-stitching -f %{oreon_filedir}/opencv-stitching.list
%files -n opencv-video -f %{oreon_filedir}/opencv-video.list
%files -n opencv-videoio -f %{oreon_filedir}/opencv-videoio.list
%files -n opencv-alphamat -f %{oreon_filedir}/opencv-alphamat.list
%files -n opencv-aruco -f %{oreon_filedir}/opencv-aruco.list
%files -n opencv-bgsegm -f %{oreon_filedir}/opencv-bgsegm.list
%files -n opencv-bioinspired -f %{oreon_filedir}/opencv-bioinspired.list
%files -n opencv-ccalib -f %{oreon_filedir}/opencv-ccalib.list
%files -n opencv-cvv -f %{oreon_filedir}/opencv-cvv.list
%files -n opencv-datasets -f %{oreon_filedir}/opencv-datasets.list
%files -n opencv-dnn_objdetect -f %{oreon_filedir}/opencv-dnn_objdetect.list
%files -n opencv-dnn_superres -f %{oreon_filedir}/opencv-dnn_superres.list
%files -n opencv-dpm -f %{oreon_filedir}/opencv-dpm.list
%files -n opencv-face -f %{oreon_filedir}/opencv-face.list
%files -n opencv-freetype -f %{oreon_filedir}/opencv-freetype.list
%files -n opencv-fuzzy -f %{oreon_filedir}/opencv-fuzzy.list
%files -n opencv-hdf -f %{oreon_filedir}/opencv-hdf.list
%files -n opencv-hfs -f %{oreon_filedir}/opencv-hfs.list
%files -n opencv-img_hash -f %{oreon_filedir}/opencv-img_hash.list
%files -n opencv-intensity_transform -f %{oreon_filedir}/opencv-intensity_transform.list
%files -n opencv-line_descriptor -f %{oreon_filedir}/opencv-line_descriptor.list
%files -n opencv-mcc -f %{oreon_filedir}/opencv-mcc.list
%files -n opencv-optflow -f %{oreon_filedir}/opencv-optflow.list
%files -n opencv-phase_unwrapping -f %{oreon_filedir}/opencv-phase_unwrapping.list
%files -n opencv-plot -f %{oreon_filedir}/opencv-plot.list
%files -n opencv-quality -f %{oreon_filedir}/opencv-quality.list
%files -n opencv-rapid -f %{oreon_filedir}/opencv-rapid.list
%files -n opencv-reg -f %{oreon_filedir}/opencv-reg.list
%files -n opencv-rgbd -f %{oreon_filedir}/opencv-rgbd.list
%files -n opencv-saliency -f %{oreon_filedir}/opencv-saliency.list
%files -n opencv-shape -f %{oreon_filedir}/opencv-shape.list
%files -n opencv-signal -f %{oreon_filedir}/opencv-signal.list
%files -n opencv-stereo -f %{oreon_filedir}/opencv-stereo.list
%files -n opencv-structured_light -f %{oreon_filedir}/opencv-structured_light.list
%files -n opencv-superres -f %{oreon_filedir}/opencv-superres.list
%files -n opencv-surface_matching -f %{oreon_filedir}/opencv-surface_matching.list
%files -n opencv-text -f %{oreon_filedir}/opencv-text.list
%files -n opencv-tracking -f %{oreon_filedir}/opencv-tracking.list
%files -n opencv-videostab -f %{oreon_filedir}/opencv-videostab.list
%files -n opencv-viz -f %{oreon_filedir}/opencv-viz.list
%files -n opencv-wechat_qrcode -f %{oreon_filedir}/opencv-wechat_qrcode.list
%files -n opencv-ximgproc -f %{oreon_filedir}/opencv-ximgproc.list
%files -n opencv-xobjdetect -f %{oreon_filedir}/opencv-xobjdetect.list
%files -n opencv-xphoto -f %{oreon_filedir}/opencv-xphoto.list
%files -n opencv-devel -f %{oreon_filedir}/opencv-devel.list
%files -n opencv-doc -f %{oreon_filedir}/opencv-doc.list
%files -n python3-opencv -f %{oreon_filedir}/python3-opencv.list
%files -n opencv-java -f %{oreon_filedir}/opencv-java.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.13.0-2
- Prepare for Oreon 11 (RP1)
