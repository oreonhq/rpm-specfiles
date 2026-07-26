%global source0_hash d53573e5a399b2b4ab1fcc36e8421c1b6fab36345c0af14f8fa20326e3365f1f

# Copyright (c) 2016 Dave Love, Liverpool University
# Copyright (c) 2018 Dave Love, University of Manchester
# MIT licence, per Fedora policy.

# This flag prevents the linkage to libptscotch.so
%undefine _ld_as_needed

%bcond_without mpich

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif
%if 0%{?rhel} || 0%{?rhel} >= 9
%bcond_with colamd
%else
%bcond_without colamd
%endif

%if %{with openmpi}
%global openmpi openmpi
%else
%global openmpi %nil
%endif
%if %{with mpich}
%global mpich mpich
%else
%global mpich %nil
%endif

# Following scalapack
%bcond_without optimized_blas

%global blaslib flexiblas

# Choose if using 64-bit integers for indexing sparse matrices
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%bcond_with index64
%endif

%if %{with index64}
%global OPENBLASLINK -lflexiblas64
%global OPENBLASLIB /libflexiblas64.so
%else
%global OPENBLASLINK -lflexiblas
%global OPENBLASLIB /libflexiblas.so
%endif

%bcond check 0

# Enable CombBLAS support
%bcond_with CombBLAS

# RHEL8 does not provide Metis64
%if %{with index64}
BuildRequires: metis64-devel
%global METISLINK -lmetis64
%global METISLIB %{_libdir}/libmetis64.so
%global METISINC %{_includedir}/metis64.h
%else
BuildRequires: metis-devel
%global METISLINK -lmetis
%global METISLIB %{_libdir}/libmetis.so
%global METISINC %{_includedir}/metis.h
%endif

Name: superlu_dist
Version: 8.2.0
Release: 10%{?dist}
Epoch:   1
Summary: Solution of large, sparse, nonsymmetric systems of linear equations
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://crd-legacy.lbl.gov/~xiaoye/SuperLU/
Source0: https://github.com/xiaoyeli/superlu_dist/archive/v%version/%name-%version.tar.gz

Patch0: %name-%version-fix-release-number.patch
Patch1: %name-fix_pkgconfig_creation.patch
Patch3: %name-scotch_parmetis.patch

# Longer tests take 1000 sec or timeout, so don't run them
Patch4: %name-only_short_tests.patch

BuildRequires: scotch-devel
BuildRequires: gcc-c++, dos2unix, chrpath
BuildRequires: cmake
%if %{with optimized_blas}
BuildRequires: %{blaslib}-devel
%endif
%if %{with colamd}
BuildRequires: suitesparse-devel
%endif

%global desc \
SuperLU is a general purpose library for the direct solution of large,\
sparse, nonsymmetric systems of linear equations.  The library is\
written in C and is callable from either C or Fortran program.  It\
uses MPI, OpenMP and CUDA to support various forms of parallelism.  It\
supports both real and complex datatypes, both single and double\
precision, and 64-bit integer indexing.  The library routines performs\
an LU decomposition with partial pivoting and triangular system solves\
through forward and back substitution.  The LU factorization routines\
can handle non-square matrices but the triangular solves are performed\
only for square matrices.  The matrix columns may be preordered\
(before factorization) either through library or user supplied\
routines.  This preordering for sparsity is completely separate from\
the factorization.  Working precision iterative refinement subroutines\
are provided for improved backward stability.  Routines are also\
provided to equilibrate the system, estimate the condition number,\
calculate the relative backward error, and estimate error bounds for\
the refined solutions.\
\
This version uses MPI and OpenMP.

%description
%desc

%if %{with openmpi}
%package openmpi
Summary:       Solution of large, sparse, nonsymmetric systems of linear equations - openmpi
BuildRequires: openmpi-devel
# ptscotch-openmpi-devel-parmetis unavailable on rhel8 ??
BuildRequires: ptscotch-openmpi-devel >= 6.0.5 %{!?el8:ptscotch-openmpi-devel-parmetis >= 6.0.5}
%if %{with CombBLAS}
BuildRequires: combblas-openmpi-devel >= 2.0.0
%endif
Requires:      gcc-gfortran%{?_isa}

%description openmpi
%desc
This is the openmpi version.

%package openmpi-devel
Summary: Development files for %name-openmpi
Requires: openmpi-devel%{?_isa}
Requires: %name-openmpi%{?_isa} = %{epoch}:%version-%release
Provides: %name-openmpi-static = %{epoch}:%version-%release

%description openmpi-devel
Development files for %name-openmpi
%endif

%package doc
Summary: Documentation for %name
BuildArch: noarch

%description doc
Documentation for %name

%if %{with mpich}
%package mpich
Summary:       Solution of large, sparse, nonsymmetric systems of linear equations - mpich
BuildRequires: mpich-devel
BuildRequires: ptscotch-mpich-devel  >= 6.0.5
BuildRequires: ptscotch-mpich-devel-parmetis  >= 6.0.5
%if %{with CombBLAS}
BuildRequires: combblas-mpich-devel >= 2.0.0
%endif
Requires:      gcc-gfortran%{?_isa}

%description mpich
%desc
This is the mpich version.

%package mpich-devel
Summary: Development files for %name-mpich
Requires: mpich-devel%{?_isa}
Requires: ptscotch-mpich-devel%{?_isa} ptscotch-mpich-devel-parmetis%{?_isa}
Requires: %name-mpich%{?_isa} = %{epoch}:%version-%release
Provides: %name-mpich-static = %{epoch}:%version-%release

%description mpich-devel
Development files for %name-mpich
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n superlu_dist-%version -N

dos2unix CMakeLists.txt
%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .fix_pkgconfig_creation
%patch -P 4 -p1 -b .only_short_tests

%build
%if %{with openmpi}
%{_openmpi_load}
mkdir -p build/openmpi
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
export CFLAGS="%optflags -std=gnu17 -DPRNTlevel=0 -DDEBUGlevel=0"
export CXXFLAGS="%optflags -std=gnu++17 -I$MPI_INCLUDE"
export LDFLAGS="%build_ldflags -L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit"
%cmake -B build/openmpi -DCMAKE_BUILD_TYPE:STRING=Release \
 -DBUILD_STATIC_LIBS:BOOL=FALSE \
 -DCMAKE_Fortran_COMPILER:FILEPATH=$MPI_BIN/mpifort \
 -DMPIEXEC_EXECUTABLE:FILEPATH=$MPI_BIN/mpiexec \
%if %{with CombBLAS}
 -DTPL_COMBBLAS_INCLUDE_DIRS:PATH="$MPI_INCLUDE/CombBLAS;$MPI_INCLUDE/CombBLAS/3DSpGEMM;$MPI_INCLUDE/CombBLAS/Applications;$MPI_INCLUDE/CombBLAS/BipartiteMatchings" \
 -DTPL_COMBBLAS_LIBRARIES:STRING=$MPI_LIB/libCombBLAS.so -DTPL_ENABLE_COMBBLASLIB:BOOL=ON \
%endif
%if %{with colamd}
 -DTPL_ENABLE_COLAMD=ON -DTPL_COLAMD_INCLUDE_DIRS:PATH=%{_includedir}/suitesparse -DTPL_COLAMD_LIBRARIES:STRING=%{_libdir}/libcolamd.so \
 -DMPI_C_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch -lcolamd" \
%else
 -DTPL_ENABLE_COLAMD=OFF \
 -DMPI_C_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch" \
%endif
 -DTPL_ENABLE_INTERNAL_BLASLIB:BOOL=OFF -DTPL_BLAS_LIBRARIES:FILEPATH=%{_libdir}%{OPENBLASLIB} -DTPL_ENABLE_LAPACKLIB:BOOL=OFF -DTPL_LAPACK_LIBRARIES:BOOL=OFF \
 -DMPI_C_HEADER_DIR:PATH="$MPI_INCLUDE -I%{METISINC}" \
 -DMPI_CXX_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch -fopenmp" \
%if 0%{?fedora}
 -DTPL_PARMETIS_INCLUDE_DIRS:PATH=$MPI_INCLUDE \
 -DTPL_PARMETIS_LIBRARIES:STRING="$MPI_LIB/libptscotchparmetis.so;%{METISLIB}" \
%endif
%if %{with index64}
 -DXSDK_INDEX_SIZE=64 \
%else
 -DXSDK_INDEX_SIZE=32 \
%endif
 -DTPL_ENABLE_PARMETISLIB:BOOL=OFF \
 -Denable_double:BOOL=ON -Denable_complex16:BOOL=ON \
 -Denable_examples:BOOL=ON -Denable_tests:BOOL=ON -DBUILD_TESTING:BOOL=ON \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_BINDIR:PATH=$MPI_BIN -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE/%{name} \
 -DCMAKE_INSTALL_LIBDIR:PATH=$MPI_LIB -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON

%make_build V=1 -C build/openmpi
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
mkdir -p build/mpich
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
export CFLAGS="%optflags -std=gnu17 -DPRNTlevel=0 -DDEBUGlevel=0"
export CXXFLAGS="%optflags -std=gnu++17 -I$MPI_INCLUDE"
export LDFLAGS="%build_ldflags -L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit"
%cmake -B build/mpich -DCMAKE_BUILD_TYPE:STRING=Release \
 -DBUILD_STATIC_LIBS:BOOL=FALSE \
 -DCMAKE_Fortran_COMPILER:FILEPATH=$MPI_BIN/mpifort \
 -DMPIEXEC_EXECUTABLE:FILEPATH=$MPI_BIN/mpiexec \
%if %{with CombBLAS}
 -DTPL_COMBBLAS_INCLUDE_DIRS:PATH="$MPI_INCLUDE/CombBLAS;$MPI_INCLUDE/CombBLAS/3DSpGEMM;$MPI_INCLUDE/CombBLAS/Applications;$MPI_INCLUDE/CombBLAS/BipartiteMatchings" \
 -DTPL_COMBBLAS_LIBRARIES:STRING=$MPI_LIB/libCombBLAS.so -DTPL_ENABLE_COMBBLASLIB:BOOL=ON \
%endif
%if %{with colamd}
 -DTPL_ENABLE_COLAMD=ON -DTPL_COLAMD_INCLUDE_DIRS:PATH=%{_includedir}/suitesparse -DTPL_COLAMD_LIBRARIES:STRING=%{_libdir}/libcolamd.so \
 -DMPI_C_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch -lcolamd" \
%else
 -DTPL_ENABLE_COLAMD=OFF \
 -DMPI_C_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch" \
%endif
 -DTPL_ENABLE_INTERNAL_BLASLIB:BOOL=OFF -DTPL_BLAS_LIBRARIES:FILEPATH=%{_libdir}%{OPENBLASLIB} -DTPL_ENABLE_LAPACKLIB:BOOL=OFF -DTPL_LAPACK_LIBRARIES:BOOL=OFF \
 -DMPI_C_HEADER_DIR:PATH="$MPI_INCLUDE -I%{METISINC}" \
 -DMPI_CXX_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch" \
%if 0%{?fedora}
 -DTPL_PARMETIS_INCLUDE_DIRS:PATH=$MPI_INCLUDE \
 -DTPL_PARMETIS_LIBRARIES:STRING="$MPI_LIB/libptscotchparmetis.so;%{METISLIB}" \
%endif
%if %{with index64}
 -DXSDK_INDEX_SIZE=64 \
%else
 -DXSDK_INDEX_SIZE=32 \
%endif
 -DTPL_ENABLE_PARMETISLIB:BOOL=OFF \
 -Denable_double:BOOL=ON -Denable_complex16:BOOL=ON \
 -Denable_examples:BOOL=ON -Denable_tests:BOOL=ON -DBUILD_TESTING:BOOL=ON \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_BINDIR:PATH=$MPI_BIN -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE/%{name} \
 -DCMAKE_INSTALL_LIBDIR:PATH=$MPI_LIB -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON

%make_build -C build/mpich
%{_mpich_unload}
%endif

%install
%if %{with openmpi}
%{_openmpi_load}
%make_install -C build/openmpi
# Make sure all header files are installed
install -m644 SRC/*.h %buildroot$MPI_INCLUDE/superlu_dist/
rm -rf %buildroot$MPI_LIB/EXAMPLE
rm -rf %buildroot$MPI_LIB/superlu_dist/FORTRAN/CMakeFiles
chrpath -r $MPI_LIB %buildroot$MPI_LIB/libsuperlu_dist*.so*
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
%make_install -C build/mpich
# Make sure all header files are installed
install -m644 SRC/*.h %buildroot$MPI_INCLUDE/superlu_dist/

rm -rf %buildroot$MPI_LIB/EXAMPLE
rm -rf %buildroot$MPI_LIB/superlu_dist/FORTRAN/CMakeFiles
chrpath -r $MPI_LIB %buildroot$MPI_LIB/libsuperlu_dist*.so*
%{_mpich_unload}
%endif

%if %{with check}
%check
%if %{with openmpi}
%{_openmpi_load}
# Waiting for excluding OpenMPI support in i686
%ifnarch %{ix86}
#mpirun -n 4 -v ../build/openmpi/EXAMPLE/pddrive -r 2 -c 2 g20.rua
%ctest -- --test-dir build/openmpi -VV
%endif
%{_openmpi_unload}
%endif

%ifnarch s390x
%if %{with mpich}
%{_mpich_load}
#mpirun -n 4 -v ../build/mpich/EXAMPLE/pddrive -r 2 -c 2 g20.rua
%ctest -- --test-dir build/mpich -VV
%{_mpich_unload}
%endif
%endif
%endif
# Check

%if %{with openmpi}
%files openmpi
%license License.txt
%_libdir/openmpi/lib/*.so.8
%_libdir/openmpi/lib/*.so.%{version}

%files openmpi-devel
%_libdir/openmpi/lib/*.so
%_libdir/openmpi/lib/*.a
%_libdir/openmpi/lib/pkgconfig/*.pc
%_includedir/openmpi-%_arch/superlu_dist/
%endif

%files doc
%license License.txt
%doc DOC/ug.pdf EXAMPLE

%if %{with mpich}
%files mpich
%license License.txt
%_libdir/mpich/lib/*.so.8
%_libdir/mpich/lib/*.so.%{version}

%files mpich-devel
%_libdir/mpich/lib/*.so
%_libdir/mpich/lib/*.a
%_libdir/mpich/lib/pkgconfig/*.pc
%_includedir/mpich-%_arch/superlu_dist/
%endif

%changelog
%autochangelog
