%global source0_hash b0e5af6b54c274b9670c7e32ddbf6c802d88c896062d760267695dd0aa7014ff
Summary:        Implementation of the JPEG-2000 standard, Part 1
Name:    jasper
Version: 4.2.9
Release:        1%{?dist}
License: JasPer-2.0
URL:     http://www.ece.uvic.ca/~frodo/jasper/
Source0:        https://github.com/jasper-software/%{name}/archive/refs/tags/version-%{version}.tar.gz#/jasper-%{version}.tar.gz
Patch100: jasper-2.0.2-test-ppc64-disable.patch
Patch101: jasper-2.0.2-test-ppc64le-disable.patch
Patch102: jasper-4.1.0-test-i686-disable.patch
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  libGLU-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
rm -f doc/README
rm -f %{buildroot}%{_libdir}/lib*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest 
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n jasper-devel -f %{oreon_filedir}/jasper-devel.list
%files -n jasper-libs -f %{oreon_filedir}/jasper-libs.list
%files -n jasper-utils -f %{oreon_filedir}/jasper-utils.list

%changelog

%autochangelog
