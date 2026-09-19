%global source0_hash none

%undefine __cmake_in_source_build
%global mfx_abi 1
%global mfx_version %{mfx_abi}.35

Summary: Hardware-accelerated video processing on Intel integrated GPUs library
Name: intel-mediasdk
Version: 23.2.2
Release: 10%{?dist}
URL: https://github.com/Intel-Media-SDK/MediaSDK
Source0: %{url}/archive/%{name}-%{version}.tar.gz
# fix build with GCC 13
Patch0: %{name}-gcc13.patch
# gtest 1.17 requires C++17
# Downstream-only because the upstream project is archived
Patch1: %{name}-cpp17.patch
License: MIT
ExclusiveArch: x86_64
BuildRequires: cmake3
BuildRequires: gcc-c++
BuildRequires: gmock-devel
BuildRequires: libdrm-devel
BuildRequires: libpciaccess-devel
BuildRequires: libva-devel
BuildRequires: libX11-devel
BuildRequires: ocl-icd-devel
BuildRequires: wayland-devel
Obsoletes: libmfx < %{mfx_version}
Provides: libmfx = %{mfx_version}
Provides: libmfx%{_isa} = %{mfx_version}

%global __provides_exclude_from ^%{_libdir}/mfx/libmfx_.*\\.so$

%description
Intel Media SDK provides a plain C API to access hardware-accelerated video
decode, encode and filtering on Intel Gen graphics hardware platforms.
Implementation written in C++ 11 with parts in C-for-Media (CM).

Supported video encoders: HEVC, AVC, MPEG-2, JPEG, VP9 Supported video decoders:
HEVC, AVC, VP8, VP9, MPEG-2, VC1, JPEG Supported video pre-processing filters:
Color Conversion, Deinterlace, Denoise, Resize, Rotate, Composition

%package devel
Summary: SDK for hardware-accelerated video processing on Intel integrated GPUs
Provides: libmfx-devel = %{mfx_version}
Provides: libmfx%{_isa}-devel = %{mfx_version}
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
Intel Media SDK provides a plain C API to access hardware-accelerated video
decode, encode and filtering on Intel Gen graphics hardware platforms.
Implementation written in C++ 11 with parts in C-for-Media (CM).

Supported video encoders: HEVC, AVC, MPEG-2, JPEG, VP9 Supported video decoders:
HEVC, AVC, VP8, VP9, MPEG-2, VC1, JPEG Supported video pre-processing filters:
Color Conversion, Deinterlace, Denoise, Resize, Rotate, Composition

%package tracer
Summary: Dump the calls of an application to the Intel Media SDK library
Requires: %{name}%{_isa} = %{version}-%{release}

%description tracer
Media SDK Tracer is a tool which permits to dump logging information from the
calls of the application to the Media SDK library. Trace log obtained from this
tool is a recommended information to provide to Media SDK team on submitting
questions and issues.

%prep
%setup -q -n MediaSDK-%{name}-%{version}
%patch 0 -p1 -b .gcc13
%patch 1 -p1 -b .cpp17

%build
%cmake3 \
    -DBUILD_DISPATCHER=ON \
    -DBUILD_SAMPLES=OFF \
    -DBUILD_TESTS=ON \
    -DBUILD_TOOLS=OFF \
    -DENABLE_OPENCL=ON \
    -DENABLE_WAYLAND=ON \
    -DENABLE_X11=ON \
    -DENABLE_X11_DRI3=ON \
    -DUSE_SYSTEM_GTEST=ON \

%cmake3_build

%install
%cmake3_install

%check
%cmake3_build -- test

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.rst
%{_libdir}/libmfx.so.%{mfx_abi}
%{_libdir}/libmfx.so.%{mfx_version}
%{_libdir}/libmfxhw64.so.%{mfx_abi}
%{_libdir}/libmfxhw64.so.%{mfx_version}
%dir %{_libdir}/mfx
%{_libdir}/mfx/libmfx_*_hw64.so
%dir %{_datadir}/mfx
%{_datadir}/mfx/plugins.cfg

%files devel
%dir %{_includedir}/mfx
%{_includedir}/mfx/mfx*.h
%{_libdir}/libmfx.so
%{_libdir}/libmfxhw64.so
%{_libdir}/pkgconfig/libmfx.pc
%{_libdir}/pkgconfig/libmfxhw64.pc
%{_libdir}/pkgconfig/mfx.pc

%files tracer
%{_bindir}/mfx-tracer-config
%{_libdir}/libmfx-tracer.so
%{_libdir}/libmfx-tracer.so.%{mfx_abi}
%{_libdir}/libmfx-tracer.so.%{mfx_version}

%changelog
%autochangelog
