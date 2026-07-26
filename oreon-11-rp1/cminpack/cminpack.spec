%global source0_hash 3ea7257914ad55eabc43a997b323ba0dfee0a9b010d648b6d5b0c96425102d0e

%undefine __cmake_in_source_build
%global soversion 1

Name:           cminpack
Version:        1.3.8
Release:        12%{?dist}
Summary:        Solver for nonlinear equations and nonlinear least squares problems

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://devernay.free.fr/hacks/cminpack/
Source0:        https://github.com/devernay/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Update path to cblas.h for flexiblas, and fix cmake data install paths.
Patch1:         %{name}-1.3.8-blas.patch
# Use the target instead of the executable name in a custom command.
Patch2:         %{name}-1.3.8-cmake3.patch

BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc
BuildRequires:  gcc-gfortran

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

%files
%license CopyrightMINPACK.txt
%doc README.md
%{_libdir}/libcminpack.so.%{version}
%{_libdir}/libcminpack.so.%{soversion}
%{_libdir}/libcminpacks.so.%{version}
%{_libdir}/libcminpacks.so.%{soversion}
%ifnarch %arm
%{_libdir}/libcminpackld.so.%{version}
%{_libdir}/libcminpackld.so.%{soversion}
%endif

%files devel
%doc docs/*.html docs/*.txt
%{_includedir}/cminpack-1
%{_libdir}/pkgconfig/*
%{_libdir}/cminpack
%{_libdir}/libcminpack.so
%{_libdir}/libcminpacks.so
%ifnarch %arm
%{_libdir}/libcminpackld.so
%endif

%changelog
%autochangelog
