%global source0_hash fa2b40c5caea96d1bb93a97486262aed8731b69ce25a84a6bf5d25323e33f631

%if 0%{?rhel} >= 9
%bcond_with gnuplot
%else
%bcond_without gnuplot
%endif

%if 0%{?rhel}
%bcond_with mingw
%else
%bcond_without mingw
%endif

Name:          leptonica
Version:       1.87.0
Release:       3%{?dist}
Summary:       C library for efficient image processing and image analysis operations

License:       Leptonica
URL:           https://github.com/danbloomberg/leptonica
Source0:        https://github.com/DanBloomberg/leptonica/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
# Add soversion suffix on win32
# Don't add _<CONFIG> suffix to pkgconfig filename
Patch0:        leptonica_cmake.patch
# https://github.com/DanBloomberg/leptonica/issues/785
# https://bugzilla.redhat.com/show_bug.cgi?id=2435534
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=123978
# workaround a miscompilation bug in GCC 16 that breaks tesseract
Patch1:        0001-Workaround-GCC-16-miscompilation-issue-785-RHBZ-2435.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: giflib-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libtool
BuildRequires: libwebp-devel
BuildRequires: make
BuildRequires: zlib-devel

# Needed for several tests
%if %{with gnuplot}
BuildRequires: gnuplot
%endif

%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libpng
BuildRequires: mingw32-zlib
BuildRequires: mingw32-giflib
BuildRequires: mingw32-libwebp

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libpng
BuildRequires: mingw64-zlib
BuildRequires: mingw64-giflib
BuildRequires: mingw64-libwebp
%endif


%description
The library supports many operations that are useful on
 * Document images
 * Natural images

Fundamental image processing and image analysis operations
 * Rasterop (aka bitblt)
 * Affine transforms (scaling, translation, rotation, shear)
   on images of arbitrary pixel depth
 * Projective and bi-linear transforms
 * Binary and gray scale morphology, rank order filters, and
   convolution
 * Seed-fill and connected components
 * Image transformations with changes in pixel depth, both at
   the same scale and with scale change
 * Pixelwise masking, blending, enhancement, arithmetic ops,
   etc.


%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for
developing applications that use %{name}.


%package tools
Summary:       Leptonica utility tools
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains leptonica utility tools.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows Leptonica library
Obsoletes:     mingw32-%{name}-static < %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows Leptonica library.


%package -n mingw64-%{name}
Summary:       MinGW Windows Leptonica library
Obsoletes:     mingw64-%{name}-static < %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows Leptonica library.
%endif


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
# Native build
%cmake -DSYM_LINK=ON -DBUILD_PROG=ON
%cmake_build

%if %{with mingw}
# MinGW build
%mingw_cmake -DSYM_LINK=ON -DBUILD_PROG=ON -DSW_BUILD=OFF
%mingw_make_build
%endif


%install
%cmake_install
%if %{with mingw}
%mingw_make_install
%endif


%{?mingw_debug_install_post}


%check
%ctest


%files
%license leptonica-license.txt
%doc README.html version-notes.html
%{_libdir}/libleptonica.so.6*

%files devel
%{_includedir}/%{name}
%{_libdir}/libleptonica.so
%{_libdir}/liblept.so
%{_libdir}/pkgconfig/lept.pc
%{_libdir}/cmake/leptonica/

%files tools
%{_bindir}/*

%if %{with mingw}
%files -n mingw32-%{name}
%license leptonica-license.txt
%{mingw32_bindir}/*.exe
%{mingw32_bindir}/libleptonica-6.dll
%{mingw32_includedir}/leptonica/
%{mingw32_libdir}/libleptonica.dll.a
%{mingw32_libdir}/pkgconfig/lept.pc
%{mingw32_libdir}/cmake/leptonica/


%files -n mingw64-%{name}
%license leptonica-license.txt
%{mingw64_bindir}/*.exe
%{mingw64_bindir}/libleptonica-6.dll
%{mingw64_includedir}/leptonica/
%{mingw64_libdir}/libleptonica.dll.a
%{mingw64_libdir}/pkgconfig/lept.pc
%{mingw64_libdir}/cmake/leptonica/
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.87.0-3
- Prepare for Oreon 11 (RP1)
