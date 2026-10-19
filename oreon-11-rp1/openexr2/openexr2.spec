%global source3_hash 9b764cbb7bab0842638ce8ab668d8cbf317444e94a194cc1c0bcda4d063ba953
%global source2_hash 5d9b2550db3ccaa1cae24348d08402b36c02d225fa154e745630c43464fa9935
%global source1_hash 0ca2bf0732a3799ca8add88a73592aafd7bbb5b93f53ec56529036b894411fce
%global source0_hash db261a7fcc046ec6634e4c5696a2fc2ce8b55f50aac6abe034308f54c8495f55
%global sover 25
%global imfsover 26
%global srcname openexr
%global pkgname %{srcname}2
Name:           %{pkgname}
Version:        2.5.8
Release:        12%{?dist}
Summary:        Provides the specification and reference implementation of the EXR file format
License:        BSD-3-Clause
URL:            https://www.openexr.com/
Source0:        https://github.com/AcademySoftwareFoundation/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/AcademySoftwareFoundation/%{srcname}/raw/v3.1.11/src/test/OpenEXRTest/v1.7.test.interleaved.exr
Source2:        https://github.com/AcademySoftwareFoundation/%{srcname}/raw/v3.1.11/src/test/OpenEXRTest/v1.7.test.planar.exr
Source3:        https://github.com/AcademySoftwareFoundation/%{srcname}/raw/v3.1.11/src/test/OpenEXRTest/v1.7.test.tiled.exr
Patch0:         openexr-gcc11.patch
Patch1:         openexr2-cstdint.patch
Patch2:         0001-use-NO_COMPRESSION-in-OpenEXTest-testBackwardCompati.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
# /oreon:deps
%description
OpenEXR is an open-source high-dynamic-range floating-point image file format
for high-quality image processing and storage. This document presents a brief
overview of OpenEXR and explains concepts that are specific to this format.

NOTE: This is a compatibility package for projects that don't yet support
OpenEXR 3.0.

%package libs
Summary:        OpenEXR Libraries
%description libs
OpenEXR is an open-source high-dynamic-range floating-point image file format
for high-quality image processing and storage. This document presents a brief
overview of OpenEXR and explains concepts that are specific to this format.

OpenEXR Features:

* High dynamic range and color precision.  Support for 16-bit floating-point,
* 32-bit floating-point, and 32-bit integer pixels.
* Multiple image compression algorithms, both lossless and lossy. Some of
  the included codecs can achieve 2:1 lossless compression ratios on images
  with film grain.  The lossy codecs have been tuned for visual quality and
  decoding performance.
* Extensibility. New compression codecs and image types can easily be added
  by extending the C++ classes included in the OpenEXR software distribution.
  New image attributes (strings, vectors, integers, etc.) can be added to
  OpenEXR image headers without affecting backward compatibility with existing
  OpenEXR applications.
* Support for stereoscopic image workflows and a generalization
  to multi-views.
* Flexible support for deep data: pixels can store a variable-length list
  of samples and, thus, it is possible to store multiple values at different
  depths for each pixel. Hard surfaces and volumetric data representations are
  accommodated.
* Multipart: ability to encode separate, but related, images in one file.
  This allows for access to individual parts without the need to read other
  parts in the file.
* Versioning: OpenEXR source allows for user configurable C++
  namespaces to provide protection when using multiple versions of the library
  in the same process space.

The IlmBase Library:

Also a part of OpenEXR, the IlmBase library is a basic, light-weight, and
efficient representation of 2D and 3D vectors and matrices and other simple but
useful mathematical objects, functions, and data types common in computer
graphics applications, including the “half” 16-bit floating-point type.

NOTE: This is a compatibility package for projects that don't yet support
OpenEXR 3.0.

%package devel
Conflicts:      openexr-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Summary:        Development files for %{name}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcname}-%{version}
mv %{SOURCE1} %{SOURCE2} %{SOURCE3} OpenEXR/IlmImfTest/

%build

%cmake -DPYILMBASE_ENABLE=OFF \
       -DOPENEXR_BUILD_UTILS=OFF 
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_docdir}/OpenEXR/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch armv7hl aarch64 s390x i686 ppc64le riscv64
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n openexr2-libs -f %{oreon_filedir}/openexr2-libs.list
%files -n openexr2-devel -f %{oreon_filedir}/openexr2-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.8-12
- Import
