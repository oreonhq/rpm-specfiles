# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e4ab7009bf0629fd11982d4c2aa83964cf244cffba7347ecd39019a9e38c4564
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global _hardened_build 1

%if 0%{?rhel} || 0%{?oreon}
%bcond_with mingw
%else
%bcond_without mingw
%endif

Name:          libwebp
Version:       1.6.0
Release:       1%{?dist}
URL:           http://webmproject.org/
Summary:       Library and tools for the WebP graphics format
License:       Apache-2.0 AND BSD-3-Clause WITH Google-Patent-WebM AND BSD-3-Clause AND FSFULLRWD
Source0:       https://storage.googleapis.com/downloads.webmproject.org/releases/webp/%{name}-%{version}.tar.gz
Patch0:        libwebp-freeglut.patch
Patch1:        libwebp-mingw-libsuffix.patch
Patch2:        libwebp-cmakedir.patch
Patch3:        libwebp-rpath.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: cmake
BuildRequires: freeglut-devel
BuildRequires: giflib-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel

%if %{with mingw}
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-giflib
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-giflib
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg
%endif

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package tools
Summary:       The WebP command line tools
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description tools
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package devel
Summary:       Development files for libwebp, a library for the WebP format
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.

%{?mingw_debug_package}
%endif

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake
%cmake_build

%if %{with mingw}
%mingw_cmake -DWEBP_BUILD_VWEBP=OFF
%mingw_make_build
%endif

%install
%cmake_install

%if %{with mingw}
%mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%endif

find "%{buildroot}/%{_libdir}" -type f -name "*.la" -delete

%{?mingw_debug_install_post}

%check
%ctest

%files
%doc README.md PATENTS NEWS AUTHORS
%license COPYING
%{_libdir}/%{name}.so.7*
%{_libdir}/%{name}decoder.so.3*
%{_libdir}/%{name}demux.so.2*
%{_libdir}/%{name}mux.so.3*
%{_libdir}/libsharpyuv.so.0*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}decoder.so
%{_libdir}/%{name}demux.so
%{_libdir}/%{name}mux.so
%{_libdir}/libsharpyuv.so
%{_includedir}/webp/
%{_libdir}/pkgconfig/libwebp.pc
%{_libdir}/pkgconfig/libwebpdecoder.pc
%{_libdir}/pkgconfig/libwebpdemux.pc
%{_libdir}/pkgconfig/libwebpmux.pc
%{_libdir}/pkgconfig/libsharpyuv.pc
%{_libdir}/cmake/WebP/

%files tools
%{_bindir}/cwebp
%{_bindir}/dwebp
%{_bindir}/gif2webp
%{_bindir}/img2webp
%{_bindir}/webpinfo
%{_bindir}/webpmux
%{_bindir}/vwebp
%{_mandir}/man*/*

%if %{with mingw}
%files -n mingw32-libwebp
%license PATENTS COPYING
%{mingw32_bindir}/cwebp.exe
%{mingw32_bindir}/dwebp.exe
%{mingw32_bindir}/gif2webp.exe
%{mingw32_bindir}/img2webp.exe
%{mingw32_bindir}/webpinfo.exe
%{mingw32_bindir}/webpmux.exe
%{mingw32_bindir}/libwebp-7.dll
%{mingw32_bindir}/libwebpdecoder-3.dll
%{mingw32_bindir}/libwebpdemux-2.dll
%{mingw32_bindir}/libwebpmux-3.dll
%{mingw32_bindir}/libsharpyuv-0.dll
%{mingw32_includedir}/webp/
%{mingw32_libdir}/pkgconfig/libwebp.pc
%{mingw32_libdir}/pkgconfig/libwebpdecoder.pc
%{mingw32_libdir}/pkgconfig/libwebpdemux.pc
%{mingw32_libdir}/pkgconfig/libwebpmux.pc
%{mingw32_libdir}/pkgconfig/libsharpyuv.pc
%{mingw32_libdir}/cmake/WebP/
%{mingw32_libdir}/libwebp.dll.a
%{mingw32_libdir}/libwebpdecoder.dll.a
%{mingw32_libdir}/libwebpdemux.dll.a
%{mingw32_libdir}/libwebpmux.dll.a
%{mingw32_libdir}/libsharpyuv.dll.a

%files -n mingw64-libwebp
%license PATENTS COPYING
%{mingw64_bindir}/cwebp.exe
%{mingw64_bindir}/dwebp.exe
%{mingw64_bindir}/gif2webp.exe
%{mingw64_bindir}/img2webp.exe
%{mingw64_bindir}/webpinfo.exe
%{mingw64_bindir}/webpmux.exe
%{mingw64_bindir}/libwebp-7.dll
%{mingw64_bindir}/libwebpdecoder-3.dll
%{mingw64_bindir}/libwebpdemux-2.dll
%{mingw64_bindir}/libwebpmux-3.dll
%{mingw64_bindir}/libsharpyuv-0.dll
%{mingw64_includedir}/webp/
%{mingw64_libdir}/pkgconfig/libwebp.pc
%{mingw64_libdir}/pkgconfig/libwebpdecoder.pc
%{mingw64_libdir}/pkgconfig/libwebpdemux.pc
%{mingw64_libdir}/pkgconfig/libwebpmux.pc
%{mingw64_libdir}/pkgconfig/libsharpyuv.pc
%{mingw64_libdir}/cmake/WebP/
%{mingw64_libdir}/libwebp.dll.a
%{mingw64_libdir}/libwebpdecoder.dll.a
%{mingw64_libdir}/libwebpdemux.dll.a
%{mingw64_libdir}/libwebpmux.dll.a
%{mingw64_libdir}/libsharpyuv.dll.a
%endif

%changelog
%autochangelog
