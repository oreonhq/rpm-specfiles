%global source0_hash 8ca0c52746174603500f0adb6f2a215d69c9ca2aab2acb3caa06fb791d8d01bf
%global sover           3
%global aom_version     v%{version}
%bcond_without jpegxl
Name:       aom
Version:    3.15.1
Release:        1%{?dist}
Summary:        Royalty-free next-generation video format
License:    BSD-3-Clause
URL:        http://aomedia.org/
Source0:        https://storage.googleapis.com/aom-releases/lib%{name}-%{version}.tar.gz
Patch:      aom-nostatic.patch
%if %{with jpegxl}
%endif
%if %{with vmaf}
%endif
Provides:       av1 = %{version}-%{release}
Requires:       libaom%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  nasm
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-interpreter
BuildRequires:  python3-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n lib%{name}-%{version}
# Set GIT revision in version
sed -i 's@set(aom_version "")@set(aom_version "%{aom_version}")@' cmake/version.cmake
# Disable PDF generation which is buggy
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
%oreon_autofiles libaom usr/*/lib*.so.*
%oreon_autofiles libaom-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libaom-devel-docs usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libaom -f %{oreon_filedir}/libaom.list
%files -n libaom-devel -f %{oreon_filedir}/libaom-devel.list
%files -n libaom-devel-docs -f %{oreon_filedir}/libaom-devel-docs.list

%changelog

%autochangelog
