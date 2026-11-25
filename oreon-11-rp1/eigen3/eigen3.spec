# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e4de6b08f33fd8b8985d2f204381408c660bffa6170ac65b68ae1bd3cd575c0a
%global source1_hash d00f3604eb9ee8258746757eb7817ab3d4a938165a083f5aab317ef0f6d3c895
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global debug_package %{nil}

%if (0%{?fedora} >= 33 || 0%{?rhel} >= 9) && !0%{?oreon}
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

%bcond mingw %{undefined rhel} && %{undefined oreon}
%bcond sparsehash %{undefined rhel} && %{undefined oreon}
%bcond suitesparse %{undefined rhel} && %{undefined oreon}
%bcond SuperLU %{undefined rhel} && %{undefined oreon}
%bcond scotch %{undefined rhel} && %{undefined oreon}
%bcond metis %{undefined rhel} && %{undefined oreon}

Name:           eigen3
Version:        5.0.1
Release:        2%{?dist}
Summary:        A lightweight C++ template library for vector and matrix math

License:        Apache-2.0 AND MPL-2.0 AND BSD-3-Clause AND Minpack
URL:            http://eigen.tuxfamily.org/index.php?title=Main_Page
Source0:        https://gitlab.com/libeigen/eigen/-/archive/%{version}/eigen-%{version}.tar.bz2
Source1:        mingw_TryRunResults.cmake

Patch0:         eigen3_docs.patch
Patch1:         eigen3_libinstalldir.patch
Patch2:         eigen3-doxygen.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  %{blaslib}-devel
BuildRequires:  fftw-devel
%if 0
BuildRequires:  glew-devel
%endif
BuildRequires:  gmp-devel
%if 0
BuildRequires:  gsl-devel
%endif
BuildRequires:  mpfr-devel
BuildRequires:  gcc-gfortran
%if %{with sparsehash}
BuildRequires:  sparsehash-devel
%endif
%if %{with suitesparse}
BuildRequires:  suitesparse-devel
%endif
%if %{with SuperLU}
BuildRequires:  SuperLU-devel
%endif
%if %{with scotch}
BuildRequires:  scotch-devel
%endif
%if %{with metis}
BuildRequires:  metis-devel
%endif

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  doxygen
BuildRequires:  graphviz

%if %{with mingw}
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gcc-gfortran
BuildRequires:  mingw32-fftw
BuildRequires:  mingw32-gmp
BuildRequires:  mingw32-mpfr

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gcc-gfortran
BuildRequires:  mingw64-fftw
BuildRequires:  mingw64-gmp
BuildRequires:  mingw64-mpfr
%endif

%description
%{summary}.

%package devel
Summary:        A lightweight C++ template library for vector and matrix math
BuildArch:      noarch
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%package blas
Summary:        BLAS library built on top of eigen3

%description blas
%{summary}.

%package lapack
Summary:        LAPACK library built on top of eigen3

%description lapack
%{summary}.

%package doc
Summary:        Developer documentation for Eigen
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description doc
Developer documentation for Eigen.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:        %{summary}
BuildArch:      noarch

%description -n mingw32-%{name}
%{summary}

%package -n mingw64-%{name}
Summary:        %{summary}
BuildArch:      noarch

%description -n mingw64-%{name}
%{summary}
%endif

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1 -n eigen-%{version}

%build
%cmake \
    -DINCLUDE_INSTALL_DIR=%{_includedir}/%{name} \
    -DCMAKEPACKAGE_INSTALL_DIR=%{_datadir}/cmake/%{name} \
    %{cmake_blas_flags} \
%if %{with SuperLU}
    -DSUPERLU_INCLUDES=%{_includedir}/SuperLU \
%endif
%if %{with scotch}
    -DSCOTCH_INCLUDES=%{_includedir} -DSCOTCH_LIBRARIES="scotch" \
%endif
%if %{with metis}
    -DMETIS_INCLUDES=%{_includedir} -DMETIS_LIBRARIES="metis" \
%endif
    -DEIGEN_TEST_CXX11=ON

%cmake_build
%cmake_build --target doc

rm -f %{_vpath_builddir}/doc/html/installdox
rm -f %{_vpath_builddir}/doc/html/unsupported/installdox

%if %{with mingw}
MINGW32_CMAKE_ARGS="-DINCLUDE_INSTALL_DIR=%{mingw32_includedir}/%{name} -DCMAKEPACKAGE_INSTALL_DIR=%{mingw32_datadir}/cmake/%{name}" \
MINGW64_CMAKE_ARGS="-DINCLUDE_INSTALL_DIR=%{mingw64_includedir}/%{name} -DCMAKEPACKAGE_INSTALL_DIR=%{mingw64_datadir}/cmake/%{name}" \
%mingw_cmake -C%{SOURCE1} -DEIGEN_BUILD_PKGCONFIG:BOOL=ON -DEIGEN_TEST_CXX11=ON -DEIGEN_BUILD_BLAS=OFF -DEIGEN_BUILD_LAPACK=OFF
%endif

%install
%cmake_install
%if %{with mingw}
%mingw_make_install
%endif

%check

%files devel
%license COPYING.BSD COPYING.APACHE COPYING.MPL2 COPYING.MINPACK COPYING.README
%{_includedir}/%{name}
%{_datadir}/cmake/%{name}
%{_datadir}/pkgconfig/%{name}.pc

%files blas
%{_libdir}/libeigen_blas.so
%{_libdir}/libeigen_blas_static.a

%files lapack
%{_libdir}/libeigen_lapack.so
%{_libdir}/libeigen_lapack_static.a

%files doc
%doc %{_vpath_builddir}/doc/html

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING.BSD COPYING.APACHE COPYING.MPL2 COPYING.MINPACK COPYING.README
%{mingw32_includedir}/%{name}
%{mingw32_datadir}/pkgconfig/%{name}.pc
%{mingw32_datadir}/cmake/%{name}/

%files -n mingw64-%{name}
%license COPYING.BSD COPYING.APACHE COPYING.MPL2 COPYING.MINPACK COPYING.README
%{mingw64_includedir}/%{name}
%{mingw64_datadir}/pkgconfig/%{name}.pc
%{mingw64_datadir}/cmake/%{name}/
%endif

%changelog
%autochangelog
