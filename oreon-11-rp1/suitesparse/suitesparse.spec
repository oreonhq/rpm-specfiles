%global source0_hash 93ed4c4e546a49fc75884c3a8b807d5af4a91e39d191fbbc60a07380b12a35d1

%global amd_version_major 3
%global btf_version_major 2
%global camd_version_major 3
%global ccolamd_version_major 3
%global cholmod_version_major 5
%global colamd_version_major 3
%global csparse_version_major 4
%global cxsparse_version_major 4
%global gpuqrengine_version_major 3
%global graphblas_version_major 10
%global klu_cholmod_version_major 2
%global klu_version_major 2
%global lagraph_version_major 1
%global lagraphx_version_major 1
%global ldl_version_major 3
%global paru_version_major 1
%global rbio_version_major 4
%global spex_version_major 3
%global spqr_version_major 4
%global SuiteSparse_config_major 7
%global SuiteSparse_gpuruntime_major 3
%global SuiteSparse_metis_major 5
%global umfpack_version_major 6

### CXSparse is a superset of CSparse, and the two share common header
### names, so it does not make sense to build both. CXSparse is built
### by default, but CSparse can be built instead by defining
### enable_csparse as 1 below.
%global enable_csparse 0

# Whether to build a separate version of libraries linked against an ILP64 BLAS
%if 0%{?__isa_bits} == 64
%global build64 1
%endif

%global suitesparse_builds SuiteSparse %{?build64:SuiteSparse64 SuiteSparse64_}

%if 0%{?fedora} || 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

# SuiteSparse uses a modified version of metis, so use it
%bcond_with system_metis

%global commit 6ab1e9eb9e67264218ffbdfc25010650da449a39

Name:           suitesparse
Version:        7.11.0
Release:        2%{?dist}
Summary:        A collection of sparse matrix libraries

# See LICENSE.txt for a breakdown of all licenses:
# Shipped modules licenses:
# * AMD      - BSD-3-Clause
# * BTF      - LGPL-2.1-or-later
# * CAMD     - BSD-3-Clause
# * COLAMD   - BSD-3-Clause
# * CCOLAMD  - BSD-3-Clause
# * CHOLMOD  - LGPL-2.1-or-later AND GPL-2.0-or-later
# * CSparse  - LGPL-2.1-or-later AND BSD-3-Clause
# * CXSparse - LGPL-2.1-or-later AND BSD-3-Clause
# * KLU      - LGPL-2.1-or-later
# * LDL      - LGPL-2.1-or-later
# * RBio     - GPL-2.0-or-later
# * SPQR     - GPL-2.0-or-later
# * UMFPACK  - GPL-2.0-or-later
#
# Not shipped modules licenses:
# * GPUQREngine            - GPL-2.0-or-later
# * GraphBLAS              - Apache-2.0 AND GPL-3.0-or-later
# * SLIP_LU                - LGPL-3.0-or-later OR GPL-2.0-or-later OR (LGPL-3.0-or-later AND GPL-2.0-or-later)
# * MATLAB_Tools           - BSD-3-Clause AND GPL-2.0-or-later
# * Mongoose               - GPL-3.0-only
# * ssget                  - BSD-3-Clause
# * SuiteSparse_GPURuntime - GPL-2.0-or-later

License:        BSD-3-Clause AND LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            http://faculty.cse.tamu.edu/davis/suitesparse.html
Source0:        https://github.com/DrTimothyAldenDavis/SuiteSparse/archive/v%{version}/%{name}-%{version}.tar.gz#/suitesparse-7.11.0.tar.gz
#Source0:        https://github.com/DrTimothyAldenDavis/SuiteSparse/archive/%%{commit}/%%{name}-%%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make

BuildRequires:  gmp-devel
%if %{with system_metis}
BuildRequires:  metis-devel
%else
Provides:       bundled(metis) = 5.1.0
%endif
BuildRequires:  %{blaslib}-devel
BuildRequires:  mpfr-devel
# openblas is still required for 64-bit suffixed versions
BuildRequires:  openblas-devel
BuildRequires:  tbb-devel
BuildRequires:  hardlink

# Not packaged in Fedora
Provides:       bundled(cpu_features) = 0.6.0
# GraphBLAS redefines malloc() so must use bundled versions
Provides:       bundled(lz4) = 1.9.3
Provides:       bundled(zstd) = 1.5.5

Obsoletes:      umfpack <= 5.0.1
Obsoletes:      ufsparse <= 2.1.1
Provides:       ufsparse = %{version}-%{release}

%description
suitesparse is a collection of libraries for computations involving sparse
matrices.  The package includes the following libraries:
  AMD                 approximate minimum degree ordering
  BTF                 permutation to block triangular form (beta)
  CAMD                constrained approximate minimum degree ordering
  COLAMD              column approximate minimum degree ordering
  CCOLAMD             constrained column approximate minimum degree ordering
  CHOLMOD             sparse Cholesky factorization
  CSparse             a concise sparse matrix package
  CXSparse            CSparse extended: complex matrix, int and long int support
  KLU                 sparse LU factorization, primarily for circuit simulation
  LDL                 a simple LDL factorization
  SQPR                a multithread, multifrontal, rank-revealing sparse QR
                      factorization method
  UMFPACK             sparse LU factorization
  SuiteSparse_config  configuration file for all the above packages.
  RBio                read/write files in Rutherford/Boeing format


%package devel
Summary:        Development headers for SuiteSparse
Requires:       %{name} = %{version}-%{release}
Obsoletes:      umfpack-devel <= 5.0.1
Obsoletes:      ufsparse-devel <= 2.1.1
Provides:       ufsparse-devel = %{version}-%{release}

%description devel
The suitesparse-devel package contains files needed for developing
applications which use the suitesparse libraries.


%package static
Summary:        Static version of SuiteSparse libraries
Requires:       %{name}-devel = %{version}-%{release}
Provides:       ufsparse-static = %{version}-%{release}

%description static
The suitesparse-static package contains the statically linkable
version of the suitesparse libraries.


%if 0%{?build64}
%package -n %{name}64
Summary:        A collection of sparse matrix libraries (ILP64 version)

%description -n %{name}64
The suitesparse collection compiled against an ILP64 BLAS library.


%package -n %{name}64-devel
Summary:        Development headers for SuiteSparse (ILP64 version)
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}64 = %{version}-%{release}

%description -n %{name}64-devel
The suitesparse64-devel package contains files needed for developing
applications which use the suitesparse libraries (ILP64 version).


%package -n %{name}64-static
Summary:        Static version of SuiteSparse libraries (ILP64 version)
Requires:       %{name}-devel = %{version}-%{release}

%description -n %{name}64-static
The suitesparse64-static package contains the statically linkable
version of the suitesparse libraries (ILP64 version).


%package -n %{name}64_
Summary:        A collection of sparse matrix libraries (ILP64 version)

%description -n %{name}64_
The suitesparse collection compiled against an ILP64 BLAS library.


%package -n %{name}64_-devel
Summary:        Development headers for SuiteSparse (ILP64 version)
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}64_ = %{version}-%{release}

%description -n %{name}64_-devel
The suitesparse64_-devel package contains files needed for developing
applications which use the suitesparse libraries (ILP64 version) compiled
against a BLAS library with the "64_" symbol name suffix (see openblas-*64_
packages).


%package -n %{name}64_-static
Summary:        Static version of SuiteSparse libraries (ILP64 version)
Requires:       %{name}-devel = %{version}-%{release}

%description -n %{name}64_-static
The suitesparse64_-static package contains the statically linkable
version of the suitesparse libraries (ILP64 version) compiled against a
BLAS library with the "64_" symbol name suffix (see openblas-*64_ packages).
%endif


%package doc
Summary:        Documentation files for SuiteSparse
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation files for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -c -q
mkdir Doc Licenses
pushd SuiteSparse-%{version}
#patch 0 -p1 -b .postfix
%if !0%{?enable_csparse}
  sed -i -e /CSparse/d Makefile
%endif
  # Build fails
  sed -i -e /Mongoose/d Makefile
%if %{with system_metis}
  # Remove bundled metis
  rm -r SuiteSparse_metis
  # SuiteSparse looks for SuiteSparse_metis.h specifically
  ln -s %{_includedir}/metis/metis.h include/SuiteSparse_metis.h
%endif

  # Fix pragma ivdep so gcc understands it.
  for fil in $(grep -Frl 'pragma ivdep' .); do
    sed -i.orig 's/pragma ivdep/pragma GCC ivdep/' $fil
    touch -r ${fil}.orig $fil
    rm -f ${fil}.orig
  done

  # drop non-standard -O3
  sed -i -e '/OPTS.*-O3/d' CHOLMOD/SuiteSparse_metis/GKlib/GKlibSystem.cmake

  # collect docs and licenses in one place to ship
  find -iname lesser.txt -o -iname lesserv3.txt -o -iname license.txt -o \
    -iname gpl.txt -o -iname GPLv2.txt -o -iname license \
    -a -not -type d | while read f; do
        b="${f%%/*}"
        r="${f#$b}"
        x="$(echo "$r" | sed 's|/doc/|/|gi')"
        install -m0644 -D "$f" "../Licenses/$b/$x"
    done

  find -type f -a \( -iname \*.pdf -o -iname ChangeLog -o -iname README\* -o -iname \*.txt \) |
    while read f; do
        b="${f%%/*}"
        r="${f#$b}"
        x="$(echo "$r" | sed 's|/doc/|/|gi')"
        install -m0644 -D "$f" "../Doc/$b/$x"
    done
popd
%if 0%{?build64}
cp -al SuiteSparse-%{version} SuiteSparse64-%{version}
cp -al SuiteSparse-%{version} SuiteSparse64_-%{version}
%endif

# hardlink duplicate documentation files
hardlink -cv Licenses/

%build
# FindSuiteSparse_config looks for "build"
%global _vpath_builddir build
for build in %{suitesparse_builds}
do
  pushd $build-%{version}
    %set_build_flags
    CMAKE_OPTIONS="-DCMAKE_C_FLAGS_RELEASE:STRING=-DNDEBUG -DCMAKE_CXX_FLAGS_RELEASE:STRING=-DNDEBUG -DCMAKE_Fortran_FLAGS_RELEASE:STRING=-DNDEBUG -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
                   -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCOMPACT=ON"
%if %{with system_metis}
    CMAKE_OPTIONS="$CMAKE_OPTIONS -DSUITESPARSE_METIS_FOUND=true -DSUITESPARSE_METIS_INCLUDE_DIR=%{_includedir}/metis -DSUITESPARSE_METIS_LIBRARIES=%{_libdir}/libmetis.so"
%endif
    # Set flags for ILP64 build
    if [ $build = SuiteSparse64 ]
    then
       CMAKE_OPTIONS="$CMAKE_OPTIONS -DSUITESPARSE_INCLUDEDIR_POSTFIX=$build -DSUITESPARSE_PKGFILEDIR=%{_libdir}/$build -DCMAKE_RELEASE_POSTFIX=64 -DBLA_VENDOR=OpenBLAS -DALLOW_64BIT_BLAS=yes"
       export CFLAGS="$CFLAGS -DBLAS_OPENBLAS_64"
    elif [ $build = SuiteSparse64_ ]
    then
       CMAKE_OPTIONS="$CMAKE_OPTIONS -DSUITESPARSE_INCLUDEDIR_POSTFIX=$build -DSUITESPARSE_PKGFILEDIR=%{_libdir}/$build -DCMAKE_RELEASE_POSTFIX=64_ -DBLA_VENDOR=OpenBLAS -DALLOW_64BIT_BLAS=yes -DBLAS_LIBRARIES=%{_libdir}/libopenblas64_.so"
       export CFLAGS="$CFLAGS -DBLAS_OPENBLAS_64"
    else
       CMAKE_OPTIONS="$CMAKE_OPTIONS -DSUITESPARSE_INCLUDEDIR_POSTFIX=suitesparse -DBLA_VENDOR=FlexiBLAS"
    fi   
    %make_build CMAKE_OPTIONS="$CMAKE_OPTIONS" JOBS=%{_smp_build_ncpus}
  popd
done

%install
for build in %{suitesparse_builds}
do
  pushd $build-%{version}
    %make_install
  popd
done

%check
# Build demos as a check
for build in %{suitesparse_builds}
do
  pushd $build-%{version}
    %make_build JOBS=%{_smp_build_ncpus} demos
  popd
done

%files
%license Licenses
%{_libdir}/libamd.so.%{amd_version_major}*
%{_libdir}/libbtf.so.%{btf_version_major}*
%{_libdir}/libcamd.so.%{camd_version_major}*
%{_libdir}/libccolamd.so.%{ccolamd_version_major}*
%{_libdir}/libcholmod.so.%{cholmod_version_major}*
%{_libdir}/libcolamd.so.%{colamd_version_major}*
%if "%{?enable_csparse}" == "1"
%{_libdir}/libcsparse.so.%{csparse_version_major}*
%endif
%{_libdir}/libcxsparse.so.%{cxsparse_version_major}*
%{_libdir}/libgraphblas.so.%{graphblas_version_major}*
%{_libdir}/libklu_cholmod.so.%{klu_cholmod_version_major}*
%{_libdir}/libklu.so.%{klu_version_major}*
%{_libdir}/liblagraph.so.%{lagraph_version_major}*
%{_libdir}/liblagraphx.so.%{lagraphx_version_major}*
%{_libdir}/libldl.so.%{ldl_version_major}*
%{_libdir}/libparu.so.%{paru_version_major}*
%{_libdir}/librbio.so.%{rbio_version_major}*
%{_libdir}/libspex.so.%{spex_version_major}*
%{_libdir}/libspexpython.so.%{spex_version_major}*
%{_libdir}/libspqr.so.%{spqr_version_major}*
%{_libdir}/libsuitesparseconfig.so.%{SuiteSparse_config_major}*
%{_libdir}/libumfpack.so.%{umfpack_version_major}*

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/AMD/
%{_libdir}/cmake/BTF/
%{_libdir}/cmake/CAMD/
%{_libdir}/cmake/CCOLAMD/
%{_libdir}/cmake/CHOLMOD/
%{_libdir}/cmake/COLAMD/
%{_libdir}/cmake/CXSparse/
%{_libdir}/cmake/GraphBLAS/
%{_libdir}/cmake/KLU/
%{_libdir}/cmake/KLU_CHOLMOD/
%{_libdir}/cmake/LAGraph/
%{_libdir}/cmake/LDL/
%{_libdir}/cmake/ParU/
%{_libdir}/cmake/RBio/
%{_libdir}/cmake/SPEX/
%{_libdir}/cmake/SPQR/
%{_libdir}/cmake/SuiteSparse_config/
%{_libdir}/cmake/SuiteSparse/
%{_libdir}/cmake/UMFPACK/
%exclude %{_libdir}/cmake/*/*_static*.cmake
%{_libdir}/pkgconfig/AMD.pc
%{_libdir}/pkgconfig/BTF.pc
%{_libdir}/pkgconfig/CAMD.pc
%{_libdir}/pkgconfig/CCOLAMD.pc
%{_libdir}/pkgconfig/CHOLMOD.pc
%{_libdir}/pkgconfig/COLAMD.pc
%{_libdir}/pkgconfig/CXSparse.pc
%{_libdir}/pkgconfig/GraphBLAS.pc
%{_libdir}/pkgconfig/KLU.pc
%{_libdir}/pkgconfig/KLU_CHOLMOD.pc
%{_libdir}/pkgconfig/LAGraph.pc
%{_libdir}/pkgconfig/LDL.pc
%{_libdir}/pkgconfig/ParU.pc
%{_libdir}/pkgconfig/RBio.pc
%{_libdir}/pkgconfig/SPEX.pc
%{_libdir}/pkgconfig/SPQR.pc
%{_libdir}/pkgconfig/SuiteSparse_config.pc
%{_libdir}/pkgconfig/UMFPACK.pc
%{_libdir}/lib*.so
%if 0%{?build64}
%exclude %{_libdir}/lib*64*.so
%endif

%files static
%{_libdir}/cmake/*/*_static*.cmake
%{_libdir}/lib*.a
%if 0%{?build64}
%exclude %{_libdir}/lib*64*.a
%endif

%if 0%{?build64}
%files -n %{name}64
%license Licenses
%{_libdir}/libamd64.so.%{amd_version_major}*
%{_libdir}/libbtf64.so.%{btf_version_major}*
%{_libdir}/libcamd64.so.%{camd_version_major}*
%{_libdir}/libccolamd64.so.%{ccolamd_version_major}*
%{_libdir}/libcholmod64.so.%{cholmod_version_major}*
%{_libdir}/libcolamd64.so.%{colamd_version_major}*
%if "%{?enable_csparse}" == "1"
%{_libdir}/libcsparse64.so.%{csparse_version_major}*
%endif
%{_libdir}/libcxsparse64.so.%{cxsparse_version_major}*
%{_libdir}/libgraphblas64.so.%{graphblas_version_major}*
%{_libdir}/libklu_cholmod64.so.%{klu_cholmod_version_major}*
%{_libdir}/libklu64.so.%{klu_version_major}*
%{_libdir}/liblagraph64.so.%{lagraph_version_major}*
%{_libdir}/liblagraphx64.so.%{lagraphx_version_major}*
%{_libdir}/libldl64.so.%{ldl_version_major}*
%{_libdir}/libparu64.so.%{paru_version_major}*
%{_libdir}/librbio64.so.%{rbio_version_major}*
%{_libdir}/libspex64.so.%{spex_version_major}*
%{_libdir}/libspexpython64.so.%{spex_version_major}*
%{_libdir}/libspqr64.so.%{spqr_version_major}*
%{_libdir}/libsuitesparseconfig64.so.%{SuiteSparse_config_major}*
%{_libdir}/libumfpack64.so.%{umfpack_version_major}*

%files -n %{name}64-devel
%{_includedir}/SuiteSparse64/
%{_libdir}/lib*64.so
%{_libdir}/SuiteSparse64

%files -n %{name}64-static
%{_libdir}/lib*64.a

%files -n %{name}64_
%license Licenses
%{_libdir}/libamd64_.so.%{amd_version_major}*
%{_libdir}/libbtf64_.so.%{btf_version_major}*
%{_libdir}/libcamd64_.so.%{camd_version_major}*
%{_libdir}/libccolamd64_.so.%{ccolamd_version_major}*
%{_libdir}/libcholmod64_.so.%{cholmod_version_major}*
%{_libdir}/libcolamd64_.so.%{colamd_version_major}*
%if "%{?enable_csparse}" == "1"
%{_libdir}/libcsparse64_.so.%{csparse_version_major}*
%endif
%{_libdir}/libcxsparse64_.so.%{cxsparse_version_major}*
%{_libdir}/libgraphblas64_.so.%{graphblas_version_major}*
%{_libdir}/libklu_cholmod64_.so.%{klu_cholmod_version_major}*
%{_libdir}/libklu64_.so.%{klu_version_major}*
%{_libdir}/liblagraph64_.so.%{lagraph_version_major}*
%{_libdir}/liblagraphx64_.so.%{lagraphx_version_major}*
%{_libdir}/libldl64_.so.%{ldl_version_major}*
%{_libdir}/libparu64_.so.%{paru_version_major}*
%{_libdir}/librbio64_.so.%{rbio_version_major}*
%{_libdir}/libspex64_.so.%{spex_version_major}*
%{_libdir}/libspexpython64_.so.%{spex_version_major}*
%{_libdir}/libspqr64_.so.%{spqr_version_major}*
%{_libdir}/libsuitesparseconfig64_.so.%{SuiteSparse_config_major}*
%{_libdir}/libumfpack64_.so.%{umfpack_version_major}*

%files -n %{name}64_-devel
%{_includedir}/SuiteSparse64_/
%{_libdir}/lib*64_.so
%{_libdir}/SuiteSparse64_

%files -n %{name}64_-static
%{_libdir}/lib*64_.a
%endif

%files doc
%doc Doc/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.11.0-2
- Import
