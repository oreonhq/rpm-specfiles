# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 98771b055ae66111d7e6854bb5091abde97d9d4161a0a2defa21cf0c61981653
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global sover           3
%global aom_version     v3.15.3

%if 0%{?fedora} || 0%{?rhel} >= 9 || 0%{?oreon}
%ifarch x86_64
%bcond_without vmaf
%endif
%if 0%{?fedora} > 40 || 0%{?rhel} > 9
%bcond_with jpegxl
%else
%bcond_without jpegxl
%endif
%endif

Name:       aom
Version:    3.15.3
Release:        %{autorelease}
Summary:    Royalty-free next-generation video format

License:    BSD-3-Clause
URL:        http://aomedia.org/
Source0:        https://aomedia.googlesource.com/%{name}/+archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:      aom-nostatic.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  git-core
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  python3-devel
BuildRequires:  nasm
%if %{with jpegxl}
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libhwy)
%endif
%if %{with vmaf}
BuildRequires:  pkgconfig(libvmaf)
%endif

Provides:       av1 = %{version}-%{release}
Requires:       libaom%{?_isa} = %{version}-%{release}

%description
The Alliance for Open Media’s focus is to deliver a next-generation
video format that is:

 - Interoperable and open;
 - Optimized for the Internet;
 - Scalable to any modern device at any bandwidth;
 - Designed with a low computational footprint and optimized for hardware;
 - Capable of consistent, highest-quality, real-time video delivery; and
 - Flexible for both commercial and non-commercial content, including
   user-generated content.

This package contains the reference encoder and decoder.

%package -n libaom
Summary:        Library files for aom

%description -n libaom
Library files for aom, the royalty-free next-generation
video format.

%package -n libaom-devel
Summary:        Development files for aom
Requires:       aom%{?_isa} = %{version}-%{release}
Requires:       libaom%{?_isa} = %{version}-%{release}

%description -n libaom-devel
Development files for aom, the royalty-free next-generation
video format.

%package -n libaom-devel-docs
Summary:        Documentation for libaom
Requires:       libaom-devel%{?_isa} = %{version}-%{release}

%description -n libaom-devel-docs
Documentation for libaom, the royalty-free next-generation
video format.

%prep
%oreon_sha256
%autosetup -p1 -c %{name}-%{version}
sed -i 's@set(aom_version "")@set(aom_version "%{aom_version}")@' cmake/version.cmake
sed -i "s@GENERATE_LATEX         = YES@GENERATE_LATEX         = NO@" libs.doxy_template

%build
%cmake  -DENABLE_CCACHE=1 \
        -DCMAKE_SKIP_RPATH=1 \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCONFIG_WEBM_IO=1 \
        -DENABLE_DOCS=1 \
        -DENABLE_TESTS=0 \
        -DCONFIG_ANALYZER=0 \
        -DBUILD_SHARED_LIBS=1 \
%if %{with jpegxl}
        -DCONFIG_TUNE_BUTTERAUGLI=1 \
%endif
%if %{with vmaf}
        -DCONFIG_TUNE_VMAF=1 \
%endif
        %{nil}
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS CHANGELOG README.md
%license LICENSE PATENTS
%{_bindir}/aomdec
%{_bindir}/aomenc

%files -n libaom
%license LICENSE PATENTS
%{_libdir}/libaom.so.%{sover}*

%files -n libaom-devel
%{_includedir}/%{name}
%{_libdir}/libaom.so
%{_libdir}/cmake/AOM/
%{_libdir}/pkgconfig/%{name}.pc

%files -n libaom-devel-docs
%doc %{_vpath_builddir}/docs/html/

%changelog
%autochangelog
