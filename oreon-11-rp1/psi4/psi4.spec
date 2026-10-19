%global source0_hash ccd69bdc1d8319470513b4d3c1e0d737fc7788a50d7e48f8db762a0fcf795dad
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global blaslib flexiblas
%global cmake_blas_flags -DBLAS_TYPE=FLEXIBLAS -DLAPACK_TYPE=FLEXIBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so -DLAPACK_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif
ExcludeArch: %{ix86}
%define _smp_mflags -j4
Name:           psi4
Epoch:          1
Version:        1.9.1
Release:        6%{?dist}
Summary:        An ab initio quantum chemistry package
License:        LGPL-3.0-only AND LicenseRef-Callaway-MIT
URL:            http://www.psicode.org/
Source0:        https://github.com/psi4/psi4/archive/v%{version}/psi4-%{version}.tar.gz
Patch0:         psi4-1.9.1-libint2.patch
Patch1:         psi4-1.3.2-python3.patch
Patch2:         psi4-1.9.1-overflow.patch
Patch3:         psi4-1.9.1-noqcetest.patch
Patch4:         psi4-1.9.1-noecpgrad.patch
Patch5:         psi4-1.9.1-nostrip.patch
Patch6:         psi4-1.9.1-libxc7.patch
Patch7:         psi4-1.9.1-uint64.patch
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-pydantic
Requires:       python3-qcengine
Requires:       python3-qcelemental
Requires:       python3-deepdiff
Requires:       python3-optking
Requires:       cmake
%if %{with tests}
%endif
Requires:  %{name}-data = %{epoch}:%{version}-%{release}
Requires:  libint2(api)%{?_isa} = %{_libint2_apiversion}
Obsoletes: psi4-doc < 1:0.3-1
Provides:       psi4-devel = %{version}-%{release}
Obsoletes:      psi4-devel < %{version}-%{release}
# oreon:deps
BuildRequires:  CheMPS2-devel
BuildRequires:  bison-devel
BuildRequires:  boost-devel
BuildRequires:  byacc
BuildRequires:  cmake
BuildRequires:  dvipng
BuildRequires:  eigen3-devel
BuildRequires:  flex
BuildRequires:  flexiblas-devel
BuildRequires:  gau2grid-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  libecpint-devel
BuildRequires:  libefp-devel
BuildRequires:  libint2-devel
BuildRequires:  libxc-devel
BuildRequires:  mpfr-devel
BuildRequires:  perl(Env)
BuildRequires:  perl-devel
BuildRequires:  pybind11-static
BuildRequires:  python3-deepdiff
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-optking
BuildRequires:  python3-pint
BuildRequires:  python3-pydantic
BuildRequires:  python3-pytest
BuildRequires:  python3-qcelemental
BuildRequires:  python3-qcengine
BuildRequires:  python3-scipy
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  tex(latex)
BuildRequires:  tex-preview
BuildRequires:  zlib-devel
# /oreon:deps
%description
PSI4 is an open-source suite of ab initio quantum chemistry programs
designed for efficient, high-accuracy simulations of a variety of
molecular properties. We can routinely perform computations with more
than 2500 basis functions running serially or in parallel.

%package data
Summary:   Data files necessary for operation of PSI4
BuildArch: noarch
%description data
This package contains necessary data files for PSI4, e.g., basis sets
and the quadrature grids.

%prep

%setup -q
%patch -P0 -p1 -b .libint2
%patch -P1 -p1 -b .python3
%patch -P2 -p1 -b .overflow
%patch -P3 -p1 -b .noqcetest
%patch -P4 -p1 -b .noecpgrad
%patch -P5 -p1 -b .nostrip
%patch -P6 -p1 -b .libxc7
%patch -P7 -p1 -b .uint64

%build

export F77=gfortran
export FC=gfortran
export pymoddir=$(echo %{python3_sitearch} | sed "s|%{_libdir}||g")
%cmake \
       -DENABLE_OPENMP=ON -DENABLE_XHOST=OFF \
       -DPYMOD_INSTALL_LIBDIR=${pymoddir} \
       %{cmake_blas_flags} -DENABLE_AUTO_LAPACK=ON \
       -DCMAKE_Fortran_COMPILER=gfortran -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ \
       -DCUSTOM_C_FLAGS='%{optflags} -std=c11 -DNDEBUG' -DCUSTOM_CXX_FLAGS='%{optflags} -DNDEBUG' \
       -DCUSTOM_Fortran_FLAGS='-I%{_libdir}/gfortran/modules %{optflags} -DNDEBUG' \
       -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR="%{_lib}" \
       -DENABLE_CheMPS2=ON -DENABLE_libefp=OFF -DENABLE_ecpint=ON
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_builddir}
rm -rf %{buildroot}%{_datadir}/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/TargetLAPACK/
rm -rf %{buildroot}%{_datadir}/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/cmake/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/cmake/TargetLAPACK/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cd %{_vpath_builddir}/tests
ctest -L smoketests --output-on-failure
%files -f %{oreon_filedir}/main.list
%files -n psi4-data -f %{oreon_filedir}/psi4-data.list

%changelog

%autochangelog
