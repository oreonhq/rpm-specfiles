# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1ed0cee48ac8c77da235c8ca8ab85d031d43cd790eda36af87fed4cf316cf2df
%global source1_hash d810b855bed2aaf8741aa7145f3fa0d54bcdecbd33401b1fa09ea6373b920164
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%{?!python3_pkgversion:%global python3_pkgversion 3}
%global sover 33

Name:           openexr
Version:        3.4.13
Release:        1%{?dist}
Summary:        Provides the specification and reference implementation of the EXR file format

License:        BSD-3-Clause WITH AdditionRef-OpenEXR-Additional-IP-Rights-Grant OR Apache-2.0
URL:            https://www.openexr.com/
Source0:        https://github.com/AcademySoftwareFoundation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        tests.zip
Patch1:         march-x86-64-v3.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  unzip
BuildRequires:  boost-devel
BuildRequires:  imath-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  zlib-devel
%if 0%{?fedora} || 0%{?oreon}
BuildRequires:  libdeflate-devel
%else
Provides:       bundled(libdeflate) = 1.25
%endif

Obsoletes:      OpenEXR < 2.5.3
Provides:       OpenEXR = %{version}-%{release}

%description
OpenEXR is an open-source high-dynamic-range floating-point image file format
for high-quality image processing and storage. This document presents a brief
overview of OpenEXR and explains concepts that are specific to this format.

This package containes the binaries for OpenEXR.

%package libs
Summary:        OpenEXR Libraries
Provides:       OpenEXR-libs = %{version}-%{release}
Obsoletes:      OpenEXR-libs < 2.5.3

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

%package devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Provides:       OpenEXR-devel = %{version}-%{release}
Provides:       OpenEXR-devel%{?_isa} = %{version}-%{release}
Obsoletes:      OpenEXR-devel < 2.5.3

Provides:       ilmbase-devel = %{version}-%{release}
Provides:       ilmbase-devel%{?_isa} = %{version}-%{release}
Obsoletes:      ilmbase-devel < 2.5.3

Summary:        Development files for %{name}

%description devel
%{summary}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1

%build
%cmake
unzip -o %{SOURCE1} -d %{_vpath_builddir}/src/test/bin/
%cmake_build

%install
%cmake_install

%check
%ifarch aarch64
EXCLUDE_REGEX='DWA[AB]Compression'
%endif
%ifarch s390x
EXCLUDE_REGEX='ReadDeep|DWA[AB]Compression|testCompression|Rgba|SampleImages|SharedFrameBuffer|testAttributes|testConversion|testExistingStreams|testLargeDataWindowOffsets|testTiledCompression'
%endif
%ifarch %{ix86}
EXCLUDE_REGEX='Iex'
%endif
%ctest --exclude-regex "$EXCLUDE_REGEX"

%files
%{_bindir}/exr2aces
%{_bindir}/exrenvmap
%{_bindir}/exrheader
%{_bindir}/exrinfo
%{_bindir}/exrmakepreview
%{_bindir}/exrmaketiled
%{_bindir}/exrmanifest
%{_bindir}/exrmetrics
%{_bindir}/exrmultipart
%{_bindir}/exrmultiview
%{_bindir}/exrstdattr

%files libs
%doc CHANGES.md CONTRIBUTING.md GOVERNANCE.md SECURITY.md CODE_OF_CONDUCT.md CONTRIBUTORS.md README.md
%license LICENSE.md
%{_libdir}/libIex-3_4.so.%{sover}{,.*}
%{_libdir}/libIlmThread-3_4.so.%{sover}{,.*}
%{_libdir}/libOpenEXR-3_4.so.%{sover}{,.*}
%{_libdir}/libOpenEXRCore-3_4.so.%{sover}{,.*}
%{_libdir}/libOpenEXRUtil-3_4.so.%{sover}{,.*}

%files devel
%{_docdir}/OpenEXR/
%{_includedir}/OpenEXR/
%{_libdir}/libIex{,-3_4}.so
%{_libdir}/libIlmThread{,-3_4}.so
%{_libdir}/libOpenEXR{,-3_4}.so
%{_libdir}/libOpenEXRCore{,-3_4}.so
%{_libdir}/libOpenEXRUtil{,-3_4}.so
%{_libdir}/cmake/OpenEXR/
%{_libdir}/pkgconfig/OpenEXR.pc

%changelog
%autochangelog
