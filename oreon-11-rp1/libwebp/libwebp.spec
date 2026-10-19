%global source0_hash e4ab7009bf0629fd11982d4c2aa83964cf244cffba7347ecd39019a9e38c4564
%global _hardened_build 1
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
%bcond_without mingw
Name:          libwebp
Version:       1.6.0
Release:        1%{?dist}
URL:           http://webmproject.org/
Summary:        Library and tools for the WebP graphics format
License:       Apache-2.0 AND BSD-3-Clause WITH AdditionRef-WebM-patent-license AND BSD-3-Clause AND FSFULLRWD
Source0:        http://downloads.webmproject.org/releases/webp/%{name}-%{version}.tar.gz
Source1:       libwebp_jni_example.java
Patch0:        libwebp-freeglut.patch
Patch1:        libwebp-mingw-libsuffix.patch
Patch2:        libwebp-cmakedir.patch
Patch3:        libwebp-rpath.patch
%if %{with java}
%endif
%if %{with mingw}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-giflib
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-giflib
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw64-libpng
BuildRequires:  swig
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%if %{with mingw}
%mingw_cmake -DWEBP_BUILD_VWEBP=OFF
%mingw_make_build
%endif
%if %{with java}
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
%cmake_install
%if %{with mingw}
%mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%endif
find "%{buildroot}/%{_libdir}" -type f -name "*.la" -delete
%if %{with java}
mkdir -p %{buildroot}/%{_libdir}/%{name}-java
cp swig/*.jar swig/*.so %{buildroot}/%{_libdir}/%{name}-java/
%endif
%{?mingw_debug_install_post}
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libwebp-tools -f %{oreon_filedir}/libwebp-tools.list
%files -n libwebp-devel -f %{oreon_filedir}/libwebp-devel.list
%files -n libwebp-java -f %{oreon_filedir}/libwebp-java.list
%files -n mingw32-libwebp -f %{oreon_filedir}/mingw32-libwebp.list
%files -n mingw64-libwebp -f %{oreon_filedir}/mingw64-libwebp.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-3
- Prepare for Oreon 11 (RP1)
