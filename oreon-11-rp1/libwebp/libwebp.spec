%global _hardened_build 1

# Disable libwebp-java subpackage for RHEL builds
%bcond enable_java %[!0%{?rhel}]

%if %{with enable_java}
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif
%else
%bcond_with java
%endif

%if 0%{?rhel}
%bcond_with mingw
%else
%bcond_without mingw
%endif

Name:          libwebp
Version:       1.6.0
Release:       3%{?dist}
URL:           http://webmproject.org/
Summary:       Library and tools for the WebP graphics format
# Additional IPR is licensed as well. See PATENTS file for details
License:       Apache-2.0 AND BSD-3-Clause WITH AdditionRef-WebM-patent-license AND BSD-3-Clause AND FSFULLRWD
Source0:       http://downloads.webmproject.org/releases/webp/%{name}-%{version}.tar.gz
Source1:       libwebp_jni_example.java
# Fix build with freeglut
Patch0:        libwebp-freeglut.patch
# Add version suffix to mingw libraries
Patch1:        libwebp-mingw-libsuffix.patch
# Fix cmake module install location
Patch2:        libwebp-cmakedir.patch
# Kill rpath
Patch3:        libwebp-rpath.patch

BuildRequires: cmake
BuildRequires: freeglut-devel
BuildRequires: gcc
BuildRequires: giflib-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
%if %{with java}
BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: swig
%endif

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


%if %{with java}
%package java
Summary:       Java bindings for libwebp, a library for the WebP format
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      java-headless
Requires:      jpackage-utils

%description java
Java bindings for libwebp.
%endif


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
%autosetup -p1


%build
# Native build
%cmake
%cmake_build

%if %{with mingw}
# MinGW build
%mingw_cmake -DWEBP_BUILD_VWEBP=OFF
%mingw_make_build
%endif

%if %{with java}
# SWIG generated Java bindings
cp %{SOURCE1} .
cd swig
rm -rf libwebp.jar libwebp_java_wrap.c
mkdir -p java/com/google/webp
swig -ignoremissing -I../src -java \
    -package com.google.webp  \
    -outdir java/com/google/webp \
    -o libwebp_java_wrap.c libwebp.swig

gcc %{__global_ldflags} %{optflags} -shared \
    -I/usr/lib/jvm/java/include \
    -I/usr/lib/jvm/java/include/linux \
    -I../src \
    -L../%{_vpath_builddir} -lwebp libwebp_java_wrap.c \
    -o libwebp_jni.so

cd java
javac com/google/webp/libwebp.java
jar cvf ../libwebp.jar com/google/webp/*.class
%endif


%install
# Native build
%cmake_install

%if %{with mingw}
# MinGW build
%mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%endif

find "%{buildroot}/%{_libdir}" -type f -name "*.la" -delete

%if %{with java}
# SWIG generated Java bindings
mkdir -p %{buildroot}/%{_libdir}/%{name}-java
cp swig/*.jar swig/*.so %{buildroot}/%{_libdir}/%{name}-java/
%endif


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

%if %{with java}
%files java
%doc libwebp_jni_example.java
%{_libdir}/%{name}-java/
%endif

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-3
- Prepare for Oreon 11 (RP1)
