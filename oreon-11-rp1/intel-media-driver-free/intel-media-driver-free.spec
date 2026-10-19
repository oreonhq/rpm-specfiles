%global source0_hash none
Name:       intel-media-driver-free
Version:    25.4.6
Release:        1%{?dist}
Summary:        The Intel Media Driver for VAAPI
License:    MIT and BSD
URL:        https://github.com/intel/media-driver
Source0:        intel-media-%{version}-free.tar.gz
Source1:    intel-media-driver.metainfo.xml
Source2:    strip.py
ExclusiveArch:  i686 x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libdrm-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libva-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(igdgmm)
BuildRequires:  pkgconfig(libcmrt)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python-unversioned-command
BuildRequires:  python3
BuildRequires:  python3-devel
# /oreon:deps
%description
The Intel Media Driver for VAAPI is a new VA-API (Video Acceleration API)
user mode driver supporting hardware accelerated decoding, encoding,
and video post processing for GEN based graphics hardware.
https://01.org/intel-media-for-linux

%package -n     libva-intel-media-driver
Summary:        The Intel Media Driver for VAAPI.
%description -n libva-intel-media-driver
The Intel Media Driver for VAAPI is a new VA-API (Video Acceleration API)
user mode driver supporting hardware accelerated decoding, encoding,
and video post processing for GEN based graphics hardware.
https://01.org/intel-media-for-linux

%package -n     libigfxcmrt
Summary:        Library to load own GPU kernels on render engine via Intel media driver.
Requires:       libva-intel-media-driver%{?_isa} = %{version}-%{release}
%description -n libigfxcmrt
libigfxcmrt is a runtime library needed when user wants to execute their own GPU kernels on render engine.
It calls Intel media driver to load the kernels and allocate the resources.
It provides a set of APIs for user to call directly from application.

%package -n     libigfxcmrt-devel
Summary:        Development files for libigfxcmrt
Requires:       libigfxcmrt%{?_isa} = %{version}-%{release}
%description -n libigfxcmrt-devel
The libigfxcmrt-devel package contains libraries and header files for
developing applications that use libigfxcmrt.

%prep

%autosetup -p1 -n media-driver-intel-media-%{version}%{?pre}
# Fix license perm
chmod -x LICENSE.md README.md CMakeLists.txt

# Remove pre-built (but unused) files
rm -rv Tools/MediaDriverTools/UMDPerfProfiler/MediaPerfParser

%build

%ifarch %{ix86}
export CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"
%endif
%cmake \
%ifarch %{ix86}
  -DARCH:STRING=32 \
%endif
  -DENABLE_NONFREE_KERNELS:BOOL=OFF \
  -DENABLE_KERNELS:BOOL=OFF \
  -DBUILD_KERNELS:BOOL=OFF \
  -DLIBVA_DRIVERS_PATH=%{_libdir}/dri \
  -DBUILD_CMRTLIB=ON \
  -DMEDIA_BUILD_FATAL_WARNINGS=OFF \
  -DVC1_Decode_Supported="no" \
  -DAVC_Encode_VME_Supported="no" \
  -DAVC_Encode_VDEnc_Supported="no" \
  -DHEVC_Encode_VME_Supported="no" \
  -DHEVC_Encode_VDEnc_Supported="no" \
  -DAVC_Decode_Supported="no" \
  -DHEVC_Decode_Supported="no" \
  -DAVC_Decode_Supported="no" \
  -DVVC_Decode_Supported="no" \
  -G Ninja
%cmake_build
%install
%cmake_install
chmod +x %{buildroot}%{_libdir}/dri/iHD_drv_video.so
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles libva-intel-media-driver usr/*/lib*.so.*
%oreon_autofiles libigfxcmrt usr/*/lib*.so.*
%oreon_autofiles libigfxcmrt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libva-intel-media-driver -f %{oreon_filedir}/libva-intel-media-driver.list
%files -n libigfxcmrt -f %{oreon_filedir}/libigfxcmrt.list
%files -n libigfxcmrt-devel -f %{oreon_filedir}/libigfxcmrt-devel.list

%changelog

%autochangelog
