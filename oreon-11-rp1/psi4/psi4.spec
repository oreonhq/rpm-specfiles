%global source0_hash none

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global cmake_blas_flags -DBLAS_TYPE=FLEXIBLAS -DLAPACK_TYPE=FLEXIBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so -DLAPACK_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

# Disable x86 architectures since libint2 is not available there
ExcludeArch: %{ix86}
# The builds experience random crashes across platforms which suggests out-of-memory issues, reduce to four threads
%define _smp_mflags -j4

Name:           psi4
Epoch:          1
Version:        1.9.1
Release:        6%{?dist}
Summary:        An ab initio quantum chemistry package
# Automatically converted from old format: LGPLv3 and MIT - review is highly recommended.
License:        LGPL-3.0-only AND LicenseRef-Callaway-MIT
URL:            http://www.psicode.org/
Source0:        https://github.com/psi4/psi4/archive/v%{version}/psi4-%{version}.tar.gz

# Fix memory error, patch extracted from https://github.com/psi4/psi4/pull/3194
Patch0:         psi4-1.9.1-libint2.patch
# Tests should call python3 not python
Patch1:         psi4-1.3.2-python3.patch
# Fix memory overflow issue
Patch2:         psi4-1.9.1-overflow.patch
# Disable test that uses qcengine, since psi4 backend of python-qcengine is broken (BZ#2309462)
Patch3:         psi4-1.9.1-noqcetest.patch
# Disable test that uses qcengine, since psi4 backend of python-qcengine is broken (BZ#2309462)
Patch4:         psi4-1.9.1-noecpgrad.patch
# Don't strip the library
Patch5:         psi4-1.9.1-nostrip.patch
# Patch build system so that libxc 7.0.0 is accepted
Patch6:         psi4-1.9.1-libxc7.patch
# Add an include to fix the build error "uint64_t does not name a type"
Patch7:         psi4-1.9.1-uint64.patch

BuildRequires:  cmake
BuildRequires:  bison-devel
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  perl-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  zlib-devel

BuildRequires:  %{blaslib}-devel
BuildRequires:  CheMPS2-devel
BuildRequires:  libint2-devel >= 2.9.0-1
BuildRequires:  libxc-devel
BuildRequires:  pybind11-static
BuildRequires:  gau2grid-devel
BuildRequires:  libefp-devel
BuildRequires:  libecpint-devel

# Libint2 cmake requires this too
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel

BuildRequires:  python3-devel >= 2.7
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-deepdiff
BuildRequires:  python3-sphinx >= 1.1
BuildRequires:  python3-pydantic
BuildRequires:  python3-qcengine
BuildRequires:  python3-qcelemental
BuildRequires:  python3-optking
BuildRequires:  python3-pint
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
# For the documentation
BuildRequires:  tex(latex)
BuildRequires:  tex-preview
BuildRequires:  dvipng
BuildRequires:  graphviz

# These are required also at runtime
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-pydantic
Requires:       python3-qcengine
Requires:       python3-qcelemental
Requires:       python3-deepdiff
Requires:       python3-optking
# For directory ownership
Requires:       cmake

%if %{with tests}
# Needed for running tests
BuildRequires:  perl(Env)
%endif

Requires:  %{name}-data = %{epoch}:%{version}-%{release}
# Libint can break the api between releases
Requires:  libint2(api)%{?_isa} = %{_libint2_apiversion}

# Don't have documentation in the cmake version yet.. 
Obsoletes: psi4-doc < 1:0.3-1

# As there are no static libraries anymore, the build system doesn't
# allow building a devel package, but the CMake configuration is still
# architecture dependent.
Provides:       psi4-devel = %{version}-%{release}
Obsoletes:      psi4-devel < %{version}-%{release}

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

# Massage the Python site directory for the installer
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
#libefp turned off since it needs a separate Python wrapper

# Build program
%cmake_build

%install
%cmake_install

# Get rid of spurious files
rm -rf %{buildroot}%{_builddir}
rm -rf %{buildroot}%{_datadir}/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/TargetLAPACK/
rm -rf %{buildroot}%{_datadir}/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/cmake/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/cmake/TargetLAPACK/

%check
# Run quick tests to see the program works.
# quicktests are too long, whole test suite way too long.
cd %{_vpath_builddir}/tests
ctest -L smoketests --output-on-failure

%files
%license COPYING COPYING.LESSER
%doc README.md
%{python3_sitearch}/psi4/
%{_datadir}/cmake/psi4/
%{_includedir}/psi4/
%{_bindir}/psi4

%files data
%license COPYING COPYING.LESSER
%{_datadir}/psi4/

%changelog
%autochangelog
