%global source0_hash a695fbe19c0165f295a8531b1e4e855cd94d0875d2f88ec4b61080677e27188a

# Conformance tests disabled by default since it requires 1 GB of test data
#global runcheck 1

#global optional_components 1

# https://bugzilla.redhat.com/show_bug.cgi?id=1751749
%global _target_platform %{_vendor}-%{_target_os}

%if 0%{?flatpak} || 0%{?rhel} || 0%{?oreon}
%bcond_with mingw
%else
%bcond_without mingw
%endif

Name:           openjpeg
Version:        2.5.4
Release:        4%{?dist}
Summary:        C-Library for JPEG 2000

# windirent.h is MIT, the rest is BSD
License:        BSD-2-Clause AND MIT
URL:            https://github.com/uclouvain/openjpeg
Source0:        https://github.com/uclouvain/openjpeg/archive/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?runcheck}
# git clone git@github.com:uclouvain/openjpeg-data.git
Source1:        data.tar.xz
%endif


BuildRequires:  cmake
BuildRequires:  doxygen
# The library itself is C only, but there is some optional C++ stuff, hence the project is not marked as C-only in cmake and hence cmake looks for a c++ compiler
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  jbigkit-devel
BuildRequires:  lcms2-devel
BuildRequires:  liblerc-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  libzstd-devel
BuildRequires:  zlib-devel
%if 0%{?optional_components}
BuildRequires:  java-devel
BuildRequires:  xerces-j2
%endif

%if %{with mingw}
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-zstd

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-zstd
%endif

%global openjpeg2_obs_ver 2.5.3-10

Obsoletes:      openjpeg2 < %{openjpeg2_obs_ver}
Provides:       openjpeg2 = %{version}-%{release}
Obsoletes:      openjpeg-libs < 1.5.1-39
Provides:       openjpeg-libs = 1.5.1-39

%description
The OpenJPEG library is an open-source JPEG 2000 library developed in order to
promote the use of JPEG 2000.

This package contains
* JPEG 2000 codec compliant with the Part 1 of the standard (Class-1 Profile-1
  compliance).
* JP2 (JPEG 2000 standard Part 2 - Handling of JP2 boxes and extended multiple
  component transforms for multispectral and hyperspectral imagery)


%package devel
Summary:        Development files for OpenJPEG 2
Requires:       %{name}%{?_isa} = %{version}-%{release}
# OpenJPEGTargets.cmake refers to the tools
Requires:       %{name}-tools%{?_isa} = %{version}-%{release}
Obsoletes:      openjpeg2-devel < %{openjpeg2_obs_ver}
Provides:       openjpeg2-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use OpenJPEG 2.


%package devel-docs
Summary:        Developer documentation for OpenJPEG 2
BuildArch:      noarch
Obsoletes:      openjpeg2-devel-docs < %{openjpeg2_obs_ver}
Provides:       openjpeg2-devel-docs = %{version}-%{release}

%description devel-docs
The %{name}-devel-docs package contains documentation files for developing
applications that use OpenJPEG 2.


%package tools
Summary:        OpenJPEG 2 command line tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      openjpeg2-tools < %{openjpeg2_obs_ver}
Provides:       openjpeg2-tools = %{version}-%{release}

%description tools
Command line tools for JPEG 2000 file manipulation, using OpenJPEG2:
 * opj2_compress
 * opj2_decompress
 * opj2_dump

%if 0%{?optional_components}
##### MJ2 #####

%package mj2
Summary:        OpenJPEG2 MJ2 module
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description mj2
The OpenJPEG library is an open-source JPEG 2000 library developed in order to
promote the use of JPEG 2000.

This package contains the MJ2 module (JPEG 2000 standard Part 3)


%package mj2-devel
Summary:        Development files for OpenJPEG2 MJ2 module
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-mj2%{?_isa} = %{version}-%{release}

%description mj2-devel
Development files for OpenJPEG2 MJ2 module


%package mj2-tools
Summary:        OpenJPEG2 MJ2 module command line tools
Requires:       %{name}-mj2%{?_isa} = %{version}-%{release}

%description mj2-tools
OpenJPEG2 MJ2 module command line tools

##### JPWL #####

%package jpwl
Summary:        OpenJPEG2 JPWL module
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description jpwl
The OpenJPEG library is an open-source JPEG 2000 library developed in order to
promote the use of JPEG 2000.

This package contains the JPWL (JPEG 2000 standard Part 11 - Jpeg 2000 Wireless)


%package jpwl-devel
Summary:        Development files for OpenJPEG2 JPWL module
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-jpwl%{?_isa} = %{version}-%{release}

%description jpwl-devel
Development files for OpenJPEG2 JPWL module


%package jpwl-tools
Summary:        OpenJPEG2 JPWL module command line tools
Requires:       %{name}-jpwl%{?_isa} = %{version}-%{release}

%description jpwl-tools
OpenJPEG2 JPWL module command line tools

##### JPIP #####

%package jpip
Summary:        OpenJPEG2 JPIP module
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description jpip
The OpenJPEG library is an open-source JPEG 2000 library developed in order to
promote the use of JPEG 2000.

This package contains the JPWL (JPEG 2000 standard Part 9 - Jpeg 2000 Interactive Protocol)


%package jpip-devel
Summary:        Development files for OpenJPEG2 JPIP module
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-jpwl%{?_isa} = %{version}-%{release}

%description jpip-devel
Development files for OpenJPEG2 JPIP module


%package jpip-tools
Summary:        OpenJPEG2 JPIP module command line tools
License:        BSD-2-Clause AND LGPL-2.0-or-later WITH WxWindows-exception-3.1
Requires:       %{name}-jpip%{?_isa} = %{version}-%{release}
Requires:       jpackage-utils
Requires:       java

%description jpip-tools
OpenJPEG2 JPIP module command line tools

##### JP3D #####

%package jp3d
Summary:        OpenJPEG2 JP3D module
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description jp3d
The OpenJPEG library is an open-source JPEG 2000 library developed in order to
promote the use of JPEG 2000.

This package contains the JP3D (JPEG 2000 standard Part 10 - Jpeg 2000 3D)


%package jp3d-devel
Summary:        Development files for OpenJPEG2 JP3D module
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-jp3d%{?_isa} = %{version}-%{release}

%description jp3d-devel
Development files for OpenJPEG2 JP3D module


%package jp3d-tools
Summary:        OpenJPEG2 JP3D module command line tools
Requires:       %{name}-jp3d%{?_isa} = %{version}-%{release}

%description jp3d-tools
OpenJPEG2 JP3D module command line tools
%endif


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw32-openjpeg2 < %{openjpeg2_obs_ver}
Provides:      mingw32-openjpeg2 = %{version}-%{release}

%description -n mingw32-%{name}
%{summary}.


%package -n mingw32-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
Requires:      mingw32-%{name} = %{version}-%{release}
BuildArch:     noarch
Obsoletes:     mingw32-openjpeg2-tools < %{openjpeg2_obs_ver}
Provides:      mingw32-openjpeg2-tools = %{version}-%{release}

%description -n mingw32-%{name}-tools
%{summary}.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw64-openjpeg2 < %{openjpeg2_obs_ver}
Provides:      mingw64-openjpeg2 = %{version}-%{release}

%description -n mingw64-%{name}
%{summary}.


%package -n mingw64-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
Requires:      mingw64-%{name} = %{version}-%{release}
BuildArch:     noarch
Obsoletes:     mingw64-openjpeg2-tools < %{openjpeg2_obs_ver}
Provides:      mingw64-openjpeg2-tools = %{version}-%{release}

%description -n mingw64-%{name}-tools
%{summary}.


%{?mingw_debug_package}
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n openjpeg-%{version} %{?runcheck:-a 1}

# Remove all third party libraries just to be sure
find thirdparty/ -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} \;


%build
# Native build
# TODO: Consider
# -DBUILD_JPIP_SERVER=ON -DBUILD_JAVA=ON
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DOPENJPEG_INSTALL_LIB_DIR=%{_lib} \
    %{?optional_components:-DBUILD_MJ2=ON -DBUILD_JPWL=ON -DBUILD_JPIP=ON -DBUILD_JP3D=ON} \
    -DBUILD_DOC=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_SHARED_LIBS=ON \
    %{?runcheck:-DBUILD_TESTING:BOOL=ON -DOPJ_DATA_ROOT=$PWD/../data}
%cmake_build

%if %{with mingw}
# MinGW build
%mingw_cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_PKGCONFIG_FILES=ON .
%mingw_make_build
%endif


%install
# Native build
%cmake_install

# Docs are installed through %%doc
rm -rf %{buildroot}%{_datadir}/doc/

%if 0%{?optional_components}
# Move the jar to the correct place
mkdir -p %{buildroot}%{_javadir}
mv %{buildroot}%{_datadir}/opj_jpip_viewer.jar %{buildroot}%{_javadir}/opj2_jpip_viewer.jar
cat > %{buildroot}%{_bindir}/opj2_jpip_viewer <<EOF
java -jar %{_javadir}/opj2_jpip_viewer.jar "$@"
EOF
chmod +x %{buildroot}%{_bindir}/opj2_jpip_viewer
%endif

%if %{with mingw}
# MinGW build
%mingw_make_install

# Delete files to exclude from package
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_datadir}/doc
rm -rf %{buildroot}%{mingw64_datadir}/doc


%mingw_debug_install_post
%endif


%check
%if 0%{?runcheck}
%ctest
%endif


%files
%license LICENSE
%doc AUTHORS.md NEWS.md README.md THANKS.md
%{_libdir}/libopenjp2.so.*
%{_mandir}/man3/libopenjp2.3*

%files devel
%dir %{_includedir}/openjpeg-2.5/
%{_includedir}/openjpeg-2.5/openjpeg.h
%{_includedir}/openjpeg-2.5/opj_config.h
%{_libdir}/libopenjp2.so
%{_libdir}/cmake/openjpeg-2.5/
%{_libdir}/pkgconfig/libopenjp2.pc

%files devel-docs
%doc %{__cmake_builddir}/doc/html

%files tools
%{_bindir}/opj_compress
%{_bindir}/opj_decompress
%{_bindir}/opj_dump
%{_mandir}/man1/opj_compress.1*
%{_mandir}/man1/opj_decompress.1*
%{_mandir}/man1/opj_dump.1*

%if 0%{?optional_components}
%files mj2
%{_libdir}/libopenmj2.so.*

%files mj2-devel
%{_libdir}/libopenmj2.so

%files mj2-tools
%{_bindir}/opj2_mj2*

%files jpwl
%{_libdir}/libopenjpwl.so.*

%files jpwl-devel
%{_libdir}/libopenjpwl.so
%{_libdir}/pkgconfig/libopenjpwl.pc

%files jpwl-tools
%{_bindir}/opj2_jpwl*

%files jpip
%{_libdir}/libopenjpip.so.*

%files jpip-devel
%{_libdir}/libopenjpip.so
%{_libdir}/pkgconfig/libopenjpip.pc

%files jpip-tools
%{_bindir}/opj2_jpip*
%{_bindir}/opj2_dec_server
%{_javadir}/opj2_jpip_viewer.jar

%files jp3d
%{_libdir}/libopenjp3d.so.*

%files jp3d-devel
%{_includedir}/openjpeg-2.0/openjp3d.h
%{_libdir}/libopenjp3d.so
%{_libdir}/pkgconfig/libopenjp3d.pc

%files jp3d-tools
%{_bindir}/opj2_jp3d*
%endif

%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE
%{mingw32_bindir}/libopenjp2.dll
%{mingw32_libdir}/libopenjp2.dll.a
%{mingw32_includedir}/openjpeg-2.5/
%{mingw32_libdir}/pkgconfig/libopenjp2.pc
%{mingw32_libdir}/cmake/openjpeg-2.5/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/opj_compress.exe
%{mingw32_bindir}/opj_decompress.exe
%{mingw32_bindir}/opj_dump.exe

%files -n mingw64-%{name}
%license LICENSE
%{mingw64_bindir}/libopenjp2.dll
%{mingw64_libdir}/libopenjp2.dll.a
%{mingw64_includedir}/openjpeg-2.5/
%{mingw64_libdir}/pkgconfig/libopenjp2.pc
%{mingw64_libdir}/cmake/openjpeg-2.5/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/opj_compress.exe
%{mingw64_bindir}/opj_decompress.exe
%{mingw64_bindir}/opj_dump.exe
%endif

%changelog
%autochangelog
