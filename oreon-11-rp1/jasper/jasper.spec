%global source0_hash 987e8c8b4afcff87553833b6f0fa255b5556a0ecc617b45ee1882e10c1b5ec14

# NOTE: packages that can use jasper:
# ImageMagick
# netpbm

Summary: Implementation of the JPEG-2000 standard, Part 1
Name:    jasper
Version: 4.2.8
Release: 2%{?dist}

License: JasPer-2.0
URL:     http://www.ece.uvic.ca/~frodo/jasper/
Source0: https://github.com/jasper-software/%{name}/archive/refs/tags/version-%{version}.tar.gz

# architecture related patches
Patch100: jasper-2.0.2-test-ppc64-disable.patch
Patch101: jasper-2.0.2-test-ppc64le-disable.patch
Patch102: jasper-4.1.0-test-i686-disable.patch

# autoreconf
BuildRequires: cmake
BuildRequires: freeglut-devel 
BuildRequires: libGLU-devel
BuildRequires: libjpeg-devel
BuildRequires: libXmu-devel libXi-devel
BuildRequires: pkgconfig doxygen
BuildRequires: mesa-libGL-devel

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: gcc
BuildRequires: make

%description
This package contains an implementation of the image compression
standard JPEG-2000, Part 1. It consists of tools for conversion to and
from the JP2 and JPC formats.

%package devel
Summary: Header files, libraries and developer documentation
Provides: libjasper-devel = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libjpeg-devel
Requires: pkgconfig
%description devel
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Conflicts: jasper < 1.900.1-4
%description libs
%{summary}.

%package utils
Summary: Nonessential utilities for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description utils
%{summary}, including jiv and tmrdemo.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-version-%{version}

# Need to disable one test to be able to build it on ppc64 arch
# At ppc64 this test just stuck (nothing happend - no exception or error)

%if "%{_arch}" == "ppc64"
%patch 100 -p1 -b .test-ppc64-disable
%endif

# Need to disable two tests to be able to build it on ppc64le arch
# At ppc64le this tests just stuck (nothing happend - no exception or error)

%if "%{_arch}" == "ppc64le"
%patch 101 -p1 -b .test-ppc64le-disable
%endif

%ifarch %ix86
%patch 102 -p1 -b .test-i686-disable
%endif

%build
%cmake \
  -DJAS_ENABLE_DOC:BOOL=OFF \
  -DALLOW_IN_SOURCE_BUILD:BOOL=ON \

%cmake_build 


%install
%cmake_install

# Unpackaged files
rm -f doc/README
rm -f %{buildroot}%{_libdir}/lib*.la


%check
%ctest 

%ldconfig_scriptlets libs

%files
%{_bindir}/imgcmp
%{_bindir}/imginfo
%{_bindir}/jasper
%{_mandir}/man1/img*
%{_mandir}/man1/jasper.1*
%{_docdir}/JasPer/*

%files devel
%doc doc/*
%{_includedir}/jasper/
%{_libdir}/libjasper.so
%{_libdir}/pkgconfig/jasper.pc

%files libs
%doc README.md
%license COPYRIGHT.txt LICENSE.txt
%{_libdir}/libjasper.so.7*

%files utils
%{_bindir}/jiv
%{_mandir}/man1/jiv.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.2.8-2
- Prepare for Oreon 11 (RP1)
