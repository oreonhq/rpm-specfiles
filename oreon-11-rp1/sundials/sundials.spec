%global source0_hash 01fe0742edac64f0d2976436be74ddd3ac6bcdde0e6638ba56b5942aefea42aa
%bcond_with debug
%bcond_with pthread
%bcond_with python
%define _lto_cflags %{nil}
%global with_mpich 1
%ifarch %{ix86}
%global with_openmpi 0
%else
%global with_openmpi 1
%endif
%if 0%{?flatpak}
%global with_mpich 0
%global with_openmpi 0
%endif
%global blaslib openblas
%global blasvar o
%global with_hypre 1
%global with_openmpicheck 1
%global with_mpichcheck 1
%global with_sercheck 1
%global with_superlumt 1
%global with_superludist 0
%global arkodelib_SOVERSION 6
%global cvodelib_SOVERSION 7
%global cvodeslib_SOVERSION 7
%global idalib_SOVERSION 7
%global idaslib_SOVERSION 6
%global kinsollib_SOVERSION 7
%global nveclib_SOVERSION 7
%global sunmatrixlib_SOVERSION 5
%global sunlinsollib_SOVERSION 5
%global sunnonlinsollib_SOVERSION 4
%global sundialslib_SOVERSION 7
%global sundomeigestpower_SOVERSION 1
Summary:        Suite of nonlinear solvers
Name:       sundials
Version:    7.9.0
Release:        1%{?dist}
License:    BSD-3-Clause
URL:        https://computation.llnl.gov/projects/%{name}/
Source0:        https://github.com/LLNL/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:     %{name}-5.5.0-set_superlumt_name.patch
Patch1:     %{name}-5.5.0-set_superlumt64_name.patch
Patch3:     %{name}-7.9.0-klu64.patch
Patch4:     %{name}-7.9.0-set_python_cmake_flags.patch
Patch5:     %{name}-7.9.0-find_petsc64.patch
Patch6:     %{name}-7.9.0-petsc-library-hints.patch
%if 0%{?with_fortran}
%endif
%if 0%{?epel}
%endif
%if 0%{?with_superlumt64_serial}
%endif
%if 0%{?with_superlumt}
%endif
%if 0%{?with_klu64} || 0%{?with_klu64_serial}
%endif
%if 0%{?with_klu}
%endif
%if 0%{?with_fortran}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(nanobind) < 3
BuildRequires:  python3dist(nanobind) >= 2.9.2
BuildRequires:  python3dist(scikit-build-core[pyproject]) >= 0.4.3
Requires:       python3-sundials = %{version}-%{release}
# /oreon:deps
%package -n       python3-sundials+dev
Summary:        Metapackage for python3-sundials dev extras
Requires:       python3-sundials = %{version}-%{release}
Provides:       python3dist(sundials[dev]) = %{version}-%{release}

%description -n python3-sundials+dev
Metapackage for python3-sundials dev extras.

%description
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
SUNDIALS was implemented with the goal of providing robust time integrators
and nonlinear solvers that can easily be incorporated into existing simulation
codes. The primary design goals were to require minimal information from the
user, allow users to easily supply their own data structures underneath the
solvers, and allow for easy incorporation of user-supplied linear solvers and
preconditioners. 

%package devel
Summary:    Suite of nonlinear solvers (developer files)
Requires:   %{name}%{?_isa} = %{version}-%{release}
Provides:   %{name}-fortran-static = %{version}-%{release}
Provides:   %{name}-examples = %{version}-%{release}
%description devel
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the developer files (dynamic libraries, header files,
static libraries and example files).

# Python binding is in beta and is subject to breaking changes
%if %{with python}
%package -n    python3-sundials4py
Summary:       Python binding of Sundials
BuildRequires: python3-pip
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-nanobind
BuildRequires: python3-scikit-build-core >= 0.4.3
BuildRequires: python3-pytest
BuildRequires: python3-numpy >= 2.0.0
BuildRequires: python3-matplotlib
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}
%py_provides   python3-sundials
%description -n python3-sundials4py
Official Python bindings for the SUNDIALS suite of nonlinear and
differential/algebraic equation solvers.
sundials4py is in beta and is subject to breaking changes.
%endif

#############################################################################
#######
%if 0%{?with_64bit_integer}
%package -n sundials64
Summary:    Suite of nonlinear solvers (64bit integer)
%description -n sundials64
SUNDIALS (64bit integer) is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the developer files (dynamic libraries, header files,
static libraries and example files).

%package -n sundials64-devel
Summary:    Suite of nonlinear solvers (64bit integer, developer files)
Requires:   %{name}64%{?_isa} = %{version}-%{release}
%if 0%{?with_klu64_serial}
Requires:   suitesparse64-devel%{?_isa}
Requires:   %{blaslib}-devel%{?_isa}
%endif
Provides:   %{name}64-fortran-static = %{version}-%{release}
Provides:   %{name}64-examples = %{version}-%{release}
%description -n sundials64-devel
SUNDIALS (64bit integer) is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the developer files (dynamic libraries, header files,
static libraries and example files).
%endif
#############################################################################
#########
%if 0%{?with_openmpi}
%package openmpi
Summary:    Suite of nonlinear solvers
BuildRequires: openmpi-devel
BuildRequires: hypre-openmpi-devel
%if 0%{?with_petsc}
BuildRequires: petsc-openmpi-devel >= 3.10
BuildRequires: scalapack-openmpi-devel
BuildRequires: hdf5-openmpi-devel
%endif
%if 0%{?with_superludist}
BuildRequires: superlu_dist-openmpi-devel
%endif
%if 0%{?with_fortran}
BuildRequires: gcc-gfortran%{?_isa}
%endif
%description openmpi
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials Fortran parallel OpenMPI libraries.

%package openmpi-devel
Summary:    Suite of nonlinear solvers
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Provides:   %{name}-openmpi-fortran-static = %{version}-%{release}
%description openmpi-devel
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials parallel OpenMPI devel libraries and
header files.

%if 0%{?with_fortran}
Requires: gcc-gfortran%{?_isa}
%endif

%endif
######
###############################################################################
######
%if 0%{?with_mpich}
%package mpich
Summary:    Suite of nonlinear solvers
BuildRequires: mpich-devel
BuildRequires: hypre-mpich-devel
%if 0%{?with_petsc}
BuildRequires: petsc-mpich-devel >= 3.10
BuildRequires: scalapack-mpich-devel
BuildRequires: hdf5-mpich-devel
%endif
%if 0%{?with_superludist}
BuildRequires: superlu_dist-mpich-devel
%endif
%if 0%{?with_fortran}
BuildRequires: gcc-gfortran%{?_isa}
%endif
%description mpich
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials parallel MPICH libraries.

%package mpich-devel
Summary:    Suite of nonlinear solvers
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
Provides:   %{name}-mpich-fortran-static = %{version}-%{release}
%description mpich-devel
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials parallel MPICH devel libraries and
header files.

%if 0%{?with_fortran}
Requires: gcc-gfortran%{?_isa}
%endif

%endif
######
#############################################################################

%package doc
Summary:   Suite of nonlinear solvers (documentation)
BuildArch: noarch
Obsoletes: sundials-doc < 0:6.6.2-5
Requires:  python3-sphinx-latex
%description doc
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the documentation source files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -qc

pushd %{name}-%{version}
%patch -P 6 -p1 -b .petsc_library_hints
popd

%if 0%{?with_64bit_integer}
cp -a %{name}-%{version} %{name}64-%{version}

pushd %{name}64-%{version}
%if 0%{?with_superlumt64_serial}
%patch -P 1 -p1 -b .set_superlumt64_name
%endif
%if 0%{?with_klu64_serial}
%patch -P 3 -p1 -b .klu64
%endif
%if 0%{?with_petsc64_serial}
%patch -P 5 -p1 -b .petsc64
%endif
popd
%endif

pushd %{name}-%{version}
%patch -P 0 -p1 -b .set_superlumt_name
%if %{with python}
%patch -P 4 -p1 -b .backup
%endif

mv src/arkode/README.md src/README-arkode.md
mv src/cvode/README.md src/README-cvode.md
mv src/cvodes/README.md src/README-cvodes.md
mv src/ida/README.md src/README-ida.md
mv src/idas/README.md src/README.idas.md
mv src/kinsol/README.md src/README-kinsol.md
popd

%if %{with python}
cp -a %{name}-%{version} %{name}-%{version}-python
#generate_buildrequires
pushd %{name}-%{version}-python
%pyproject_buildrequires
popd
%endif

%if 0%{?with_openmpi}
cp -a %{name}-%{version} buildopenmpi_dir
%endif
%if 0%{?with_mpich}
cp -a %{name}-%{version} buildmpich_dir
%endif

%build

%global _smp_ncpus_max 1
%if 0%{?with_superlumt}
export LIBSUPERLUMTLINK=-lsuperlu_mt
%endif
export LIBBLASLINK=-l%{blaslib}%{blasvar}
export INCBLAS=%{_includedir}/%{blaslib}
export CFLAGS="%{build_cflags}"
export FFLAGS="%{build_fflags} -fPIC"
%define _vpath_srcdir %{name}-%{version}
mkdir -p %{name}-%{version}/build
%define _vpath_builddir %{name}-%{version}/build
%cmake \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
%if 0%{?with_klu}
 -DSUNDIALS_ENABLE_KLU:BOOL=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} \
 -DKLU_LIBRARY:FILEPATH=%{_libdir}/libklu.so \
 -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
 -DAMD_LIBRARY=%{_libdir}/libamd.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%endif
%if 0%{?with_superlumt}
 -DSUNDIALS_ENABLE_SUPERLUMT:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_LIBRARY:FILEPATH=%{_libdir}/libsuperlu_mt.so \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
%endif
 -DSUNDIALS_ENABLE_PETSC:BOOL=OFF \
 -DBLAS_LIBRARIES:FILEPATH=%{_libdir}/lib%{blaslib}%{blasvar}.so \
 -DSUNDIALS_ENABLE_PROFILING:BOOL=OFF \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK" \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir} \
 -DSUNDIALS_ENABLE_LAPACK:BOOL=OFF \
 -DCMAKE_MODULE_LINKER_FLAGS:STRING="%{__global_ldflags}" \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON \
 -DSUNDIALS_ENABLE_MPI:BOOL=OFF \
%if 0%{?with_fortran}
 -DF77_INTERFACE_ENABLE:BOOL=ON \
 -DSUNDIALS_ENABLE_FORTRAN:BOOL=ON \
 -DFortran_INSTALL_MODDIR:PATH=%{_fmoddir}/%{name} \
%endif
%if 0%{?with_sercheck}
 -DSUNDIALS_ENABLE_F90_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_F77_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_CXX_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_C_EXAMPLES:BOOL=ON \
%endif
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DSUNDIALS_ENABLE_OPENMP:BOOL=ON \
%if %{with pthread}
 -DSUNDIALS_ENABLE_PTHREAD:BOOL=ON \
%endif
 -DSUNDIALS_INDEX_SIZE:STRING=32 \
 -DSUNDIALS_PRECISION:STRING=double \
 -DSUNDIALS_ENABLE_SUPERLUDIST:BOOL=OFF \
 -DSUNDIALS_ENABLE_HYPRE:BOOL=OFF \
 -DSUNDIALS_EXAMPLES_INSTALL_PATH:PATH=%{_libexecdir}/%{name}-%{version}/examples \
 -DSUNDIALS_ENABLE_MONITORING:BOOL=ON \
 -DSUNDIALS_ENABLE_PYTHON:BOOL=OFF
%define _vpath_srcdir %{name}-%{version}
%define _vpath_builddir %{name}-%{version}/build 
%cmake_build
%if %{with python}
pushd %{name}-%{version}-python
%pyproject_wheel
popd
%endif
%if 0%{?with_64bit_integer}
%if 0%{?with_superlumt64_serial}
export LIBSUPERLUMTLINK=-lsuperlu_mt64
%endif
export LIBBLASLINK=-l%{blaslib}%{blasvar}64
export INCBLAS=%{_includedir}/%{blaslib}64
export CFLAGS="%{build_cflags}"
export FFLAGS="%{build_fflags} -fPIC"
export LDFLAGS="%{__global_ldflags}"
%define _vpath_srcdir %{name}64-%{version}
mkdir -p %{name}64-%{version}/build
%define _vpath_builddir %{name}64-%{version}/build
%cmake \
 -DCMAKE_RELEASE_POSTFIX:STRING=64 \
 -DSUNDIALS_INDEX_SIZE:STRING=64 \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
%if 0%{?with_klu64_serial}
 -DSUNDIALS_ENABLE_KLU:BOOL=ON \
 -DKLU_LIBRARY:FILEPATH=%{_libdir}/libklu64.so \
 -DKLU_INCLUDE_DIR:PATH=%{_includedir}/SuiteSparse64 \
 -DAMD_LIBRARY=%{_libdir}/libamd64.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf64.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUITESPARSECONFIG_LIBRARY:FILEPATH=%{_libdir}/libsuitesparseconfig64.so \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd64.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%endif
%if 0%{?with_superlumt64_serial}
 -DSUNDIALS_ENABLE_SUPERLUMT:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT64 \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_LIBRARY:FILEPATH=%{_libdir}/libsuperlu_mt64.so \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
%endif
 -DSUNDIALS_ENABLE_PETSC:BOOL=OFF \
 -DBLAS_LIBRARIES:FILEPATH=%{_libdir}/lib%{blaslib}%{blasvar}64.so \
 -DSUNDIALS_ENABLE_PROFILING:BOOL=OFF \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK" \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/sundials64 \
 -DSUNDIALS_ENABLE_LAPACK:BOOL=OFF \
 -DCMAKE_MODULE_LINKER_FLAGS:STRING="%{__global_ldflags}" \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
 -DSUNDIALS_INSTALL_CMAKEDIR:PATH=%{_lib}/cmake/sundials64 \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON \
 -DSUNDIALS_ENABLE_MPI:BOOL=OFF \
%if 0%{?with_fortran}
 -DF77_INTERFACE_ENABLE:BOOL=ON \
 -DSUNDIALS_ENABLE_FORTRAN:BOOL=ON \
 -DFortran_INSTALL_MODDIR:PATH=%{_fmoddir}/%{name}64 \
%endif
%if 0%{?with_sercheck}
 -DSUNDIALS_ENABLE_F90_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_F77_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_CXX_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_C_EXAMPLES:BOOL=ON \
%endif
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DSUNDIALS_ENABLE_OPENMP:BOOL=ON \
%if %{with pthread}
 -DSUNDIALS_ENABLE_PTHREAD:BOOL=ON \
%endif
 -DSUNDIALS_PRECISION:STRING=double \
 -DSUNDIALS_ENABLE_SUPERLUDIST:BOOL=OFF \
 -DSUNDIALS_ENABLE_HYPRE:BOOL=OFF \
 -DSUNDIALS_EXAMPLES_INSTALL_PATH:PATH=%{_libexecdir}/%{name}64-%{version}/examples \
 -DSUNDIALS_ENABLE_MONITORING:BOOL=ON \
 -DSUNDIALS_ENABLE_PYTHON:BOOL=OFF
%define _vpath_srcdir %{name}64-%{version}
%define _vpath_builddir %{name}64-%{version}/build 
%cmake_build
%endif
%if 0%{?with_openmpi}
%{_openmpi_load}
export LIBBLASLINK=-l%{blaslib}%{blasvar}
export INCBLAS=%{_includedir}/%{blaslib}
%if 0%{?with_superlumt64}
export LIBSUPERLUMTLINK=-lsuperlu_mt64
%endif
%if 0%{?with_superlumt}
export LIBSUPERLUMTLINK=-lsuperlu_mt
%endif
%if 0%{?with_hypre}
export LIBHYPRELINK="-L$MPI_LIB -lHYPRE"
%endif
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
export FC=$MPI_BIN/mpif77
export CFLAGS="%{build_cflags}"
export FFLAGS="%{build_fflags} -fPIC"
%define _vpath_srcdir buildopenmpi_dir
mkdir -p buildopenmpi_dir/build
%define _vpath_builddir buildopenmpi_dir/build
%cmake \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
%if 0%{?with_klu64}
 -DSUNDIALS_INDEX_SIZE:STRING=64 \
 -DSUNDIALS_ENABLE_KLU=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu64.so \
 -DAMD_LIBRARY=%{_libdir}/libamd64.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf64.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd64.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DKLU_INCLUDE_DIR:PATH=%{_includedir}/SuiteSparse64 \
%if 0%{?with_petsc64}
 -DSUNDIALS_ENABLE_PETSC:BOOL=ON \
 -DPETSC_INCLUDES:STRING=-I%{_includedir}/petsc64 \
 -DPETSC_LIBRARIES:STRING="-L%{_libdir} -lpetsc64" \
%endif
%if 0%{?with_superlumt}
 -DSUNDIALS_ENABLE_SUPERLUMT:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT64 \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_LIBRARY:FILEPATH=%{_libdir}/libsuperlu_mt64.so \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
%endif
%endif
%if 0%{?with_klu}
 -DSUNDIALS_INDEX_SIZE:STRING=32 \
 -DSUNDIALS_ENABLE_KLU=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu.so \
 -DAMD_LIBRARY=%{_libdir}/libamd.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
%if 0%{?with_petsc}
 -DSUNDIALS_ENABLE_PETSC:BOOL=ON \
 -DPETSC_INCLUDES:STRING=-I$MPI_INCLUDE/petsc \
 -DPETSC_LIBRARIES:STRING="-L$MPI_LIB -lpetsc" \
%endif
%if 0%{?with_superlumt}
 -DSUNDIALS_ENABLE_SUPERLUMT:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_LIBRARY:FILEPATH=%{_libdir}/libsuperlu_mt.so \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
%endif
%endif
 -DSUNDIALS_ENABLE_PROFILING:BOOL=OFF \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK $LIBHYPRELINK" \
 -DMPI_INCLUDE_PATH:PATH=$MPI_INCLUDE \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE \
 -DSUNDIALS_ENABLE_LAPACK:BOOL=OFF \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}/openmpi/lib \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DSUNDIALS_ENABLE_MPI:BOOL=ON \
%if 0%{?with_fortran}
 -DMPI_Fortran_COMPILER:STRING=$MPI_BIN/mpif77 \
 -DF77_INTERFACE_ENABLE:BOOL=ON \
%if 0%{?with_openmpicheck}
 -DSUNDIALS_ENABLE_F90_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_F77_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_CXX_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_C_EXAMPLES:BOOL=ON \
%endif
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
 -DSUNDIALS_ENABLE_FORTRAN:BOOL=ON \
%endif
 -DFortran_INSTALL_MODDIR:PATH=$MPI_FORTRAN_MOD_DIR/%{name} \
%endif
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DSUNDIALS_ENABLE_OPENMP:BOOL=ON \
%if %{with pthread}
 -DSUNDIALS_ENABLE_PTHREAD:BOOL=ON \
%endif
%if 0%{?with_superludist}
 -DSUNDIALS_ENABLE_SUPERLUDIST:BOOL=ON \
 -DSUPERLUDIST_INCLUDE_DIR:PATH=$MPI_INCLUDE/superlu_dist \
 -DSUPERLUDIST_LIBRARY_DIR:PATH=$MPI_LIB \
 -DSUPERLUDIST_LIBRARIES:STRING=libsuperlu_dist.so \
%endif
%if 0%{?with_hypre}
 -DSUNDIALS_ENABLE_HYPRE:BOOL=ON \
 -DHYPRE_INCLUDE_DIR:PATH=$MPI_INCLUDE/hypre \
 -DHYPRE_LIBRARY_DIR:PATH=$MPI_LIB \
%endif
 -DSUNDIALS_EXAMPLES_INSTALL_PATH:PATH=%{_libexecdir}/%{name}-%{version}/examples \
 -DSUNDIALS_ENABLE_MONITORING:BOOL=ON
%define _vpath_srcdir buildopenmpi_dir
%define _vpath_builddir buildopenmpi_dir/build
%cmake_build
%{_openmpi_unload}
%endif
%if 0%{?with_mpich}
%{_mpich_load}
export LIBBLASLINK=-l%{blaslib}%{blasvar}
export INCBLAS=%{_includedir}/%{blaslib}
%if 0%{?with_superlumt64}
export LIBSUPERLUMTLINK=-lsuperlu_mt64
%endif
%if 0%{?with_superlumt}
export LIBSUPERLUMTLINK=-lsuperlu_mt
%endif
%if 0%{?with_hypre}
export LIBHYPRELINK="-L$MPI_LIB -lHYPRE"
%endif
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
export FC=$MPI_BIN/mpif77
export CFLAGS="%{build_cflags}"
export FFLAGS="%{build_fflags} -fPIC"
%define _vpath_srcdir buildmpich_dir
mkdir -p buildmpich_dir/build
%define _vpath_builddir buildmpich_dir/build
%cmake \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
%if 0%{?with_klu64}
 -DSUNDIALS_INDEX_SIZE:STRING=64 \
 -DSUNDIALS_ENABLE_KLU=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu64.so \
 -DAMD_LIBRARY=%{_libdir}/libamd64.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf64.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd64.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
%if 0%{?with_superlumt}
 -DSUNDIALS_ENABLE_SUPERLUMT:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT64 \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_LIBRARY:FILEPATH=%{_libdir}/libsuperlu_mt64.so \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
%endif
%if 0%{?with_petsc64}
 -DSUNDIALS_ENABLE_PETSC:BOOL=ON \
 -DPETSC_INCLUDES:STRING=-I%{_includedir}/petsc64 \
 -DPETSC_LIBRARIES:STRING="-L%{_libdir} -lpetsc64" \
%endif
%endif
%if 0%{?with_klu}
 -DSUNDIALS_INDEX_SIZE:STRING=32 \
 -DSUNDIALS_ENABLE_KLU=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu.so \
 -DAMD_LIBRARY=%{_libdir}/libamd.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
%if 0%{?with_superlumt}
 -DSUNDIALS_ENABLE_SUPERLUMT:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_LIBRARY:FILEPATH=%{_libdir}/libsuperlu_mt.so \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
%endif
%if 0%{?with_petsc}
 -DSUNDIALS_ENABLE_PETSC:BOOL=ON \
 -DPETSC_INCLUDES:STRING=-I$MPI_INCLUDE/petsc \
 -DPETSC_LIBRARIES:STRING="-L$MPI_LIB -lpetsc" \
%endif
%endif
 -DSUNDIALS_ENABLE_PROFILING:BOOL=OFF \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK $LIBHYPRELINK" \
 -DSUNDIALS_ENABLE_LAPACK:BOOL=OFF \
 -DMPI_INCLUDE_PATH:PATH=$MPI_INCLUDE \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}/mpich/lib \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DSUNDIALS_ENABLE_MPI:BOOL=ON \
%if 0%{?with_fortran}
 -DMPI_Fortran_COMPILER:STRING=$MPI_BIN/mpif77 \
 -DF77_INTERFACE_ENABLE:BOOL=ON \
%if 0%{?with_openmpicheck}
 -DSUNDIALS_ENABLE_F90_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_F77_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_CXX_EXAMPLES:BOOL=ON \
 -DSUNDIALS_ENABLE_C_EXAMPLES:BOOL=ON \
%endif
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
 -DSUNDIALS_ENABLE_FORTRAN:BOOL=ON \
%endif
 -DFortran_INSTALL_MODDIR:PATH=$MPI_FORTRAN_MOD_DIR/%{name} \
%endif
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DSUNDIALS_ENABLE_OPENMP:BOOL=ON \
%if %{with pthread}
 -DSUNDIALS_ENABLE_PTHREAD:BOOL=ON \
%endif
%if 0%{?with_hypre}
 -DSUNDIALS_ENABLE_HYPRE:BOOL=ON \
 -DHYPRE_INCLUDE_DIR:PATH=$MPI_INCLUDE/hypre \
 -DHYPRE_LIBRARY_DIR:PATH=$MPI_LIB \
%endif
 -DSUNDIALS_EXAMPLES_INSTALL_PATH:PATH=%{_libexecdir}/%{name}-%{version}/examples \
 -DSUNDIALS_ENABLE_MONITORING:BOOL=ON
%define _vpath_srcdir buildmpich_dir
%define _vpath_builddir buildmpich_dir/build
%cmake_build
%{_mpich_unload}
%endif
%install
%if 0%{?with_openmpi}
%{_openmpi_load}
%define _vpath_srcdir buildopenmpi_dir
%define _vpath_builddir buildopenmpi_dir/build
%cmake_install
rm -f %{buildroot}$MPI_INCLUDE/%{name}/LICENSE
rm -f %{buildroot}$MPI_INCLUDE/%{name}/NOTICE
%{_openmpi_unload}
%endif
%if 0%{?with_mpich}
%{_mpich_load}
%define _vpath_srcdir buildmpich_dir
%define _vpath_builddir buildmpich_dir/build
%cmake_install
rm -f %{buildroot}$MPI_INCLUDE/%{name}/LICENSE
rm -f %{buildroot}$MPI_INCLUDE/%{name}/NOTICE
%{_mpich_unload}
%endif
%if 0%{?with_64bit_integer}
%define _vpath_srcdir %{name}64-%{version}
%define _vpath_builddir %{name}64-%{version}/build
%cmake_install
find %{buildroot}%{_libexecdir}/%{name}64-%{version}/examples \
 -type f \( -name Makefile -o -name CMakeLists.txt \) \
 -exec sed -i -E 's/(sundials_[[:alnum:]_]+)/\164/g' {} +
%endif
%define _vpath_srcdir %{name}-%{version}
%define _vpath_builddir %{name}-%{version}/build
%cmake_install
rm -f %{buildroot}%{_prefix}/LICENSE
rm -f %{buildroot}%{_includedir}/%{name}/LICENSE
rm -f %{buildroot}%{_includedir}/%{name}/NOTICE
%if %{with python}
pushd %{name}-%{version}-python
%pyproject_install
popd
rm -rf %{buildroot}%{python3_sitearch}/%{_lib}
rm -rf %{buildroot}%{python3_sitearch}/include
%oreon_autofiles python3-sundials4py usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%if 0%{?with_openmpi}
%if 0%{?with_openmpicheck}
%{_openmpi_load}
%define _vpath_builddir buildopenmpi_dir
%define _vpath_builddir buildopenmpi_dir/build
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
%if %{with debug}
%ctest -VV --debug
%else
%ctest
%endif
%endif
%{_openmpi_unload}
%endif
%if 0%{?with_mpich}
%if 0%{?with_mpichcheck}
%{_mpich_load}
%define _vpath_builddir buildmpich_dir
%define _vpath_builddir buildmpich_dir/build
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
%if %{with debug}
%ctest -VV --debug
%else
%ctest
%endif
%endif
%{_mpich_unload}
%endif
%if 0%{?with_sercheck}
%define _vpath_srcdir %{name}-%{version}
%define _vpath_builddir %{name}-%{version}/build
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%if %{with debug}
%ctest -VV --debug
%else
%ctest
%endif
%endif
%if 0%{?with_64bit_integer}
%define _vpath_srcdir %{name}64-%{version}
%define _vpath_builddir %{name}64-%{version}/build
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%if %{with debug}
%ctest -VV --debug
%else
%ctest
%endif
%endif
%if %{with python}
pushd %{name}-%{version}-python
%pyproject_check_import
MPLBACKEND=Agg %pytest
popd
%endif
%files
%files -n sundials-devel -f %{oreon_filedir}/sundials-devel.list
%files -n python3-sundials4py -f %{oreon_filedir}/python3-sundials4py.list
%files -n sundials-openmpi -f %{oreon_filedir}/sundials-openmpi.list
%files -n sundials-openmpi-devel -f %{oreon_filedir}/sundials-openmpi-devel.list
%files -n sundials-mpich -f %{oreon_filedir}/sundials-mpich.list
%files -n sundials-mpich-devel -f %{oreon_filedir}/sundials-mpich-devel.list
%files -n sundials-doc -f %{oreon_filedir}/sundials-doc.list

%changelog

%autochangelog
