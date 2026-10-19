%global source0_hash 10a76d214e01baa0480828fa473c2ef6209983c80941eca10b5a69df4de02cee
%undefine __cmake_in_source_build
%global soversion 1
Name:           cminpack
Version:        1.3.14
Release:        1%{?dist}
Summary:        Solver for nonlinear equations and nonlinear least squares problems
License:        LicenseRef-Callaway-BSD
URL:            http://devernay.free.fr/hacks/cminpack/
Source0:        https://github.com/devernay/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         %{name}-1.3.8-blas.patch
Patch2:         %{name}-1.3.8-cmake3.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
# /oreon:deps
%description
cminpack is an ISO C99 implementation of the FORTRAN Minpack solver package.
It is fully re-entrant and thread-safe.

%package devel
Summary: Header files and libraries for cminpack
Requires: %{name} = %{version}-%{release}
Requires: flexiblas-devel
%description devel
Contains the development headers and libraries needed to build a program with
cminpack.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p0 -b .blas
%patch -P2 -p1 -b .cmake3

%build

%cmake \
  -DUSE_FPIC=ON \
  -DSHARED_LIBS=ON \
  -DBUILD_EXAMPLES=ON \
  -DBUILD_EXAMPLES_FORTRAN=ON \
  -DCMINPACK_LIB_INSTALL_DIR=%{_lib} \
  -DUSE_BLAS=ON \
  -DCMAKE_BUILD_TYPE=none
%cmake_build
%install
%cmake_install
%oreon_autofiles cminpack-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cminpack-devel -f %{oreon_filedir}/cminpack-devel.list

%changelog

%autochangelog
