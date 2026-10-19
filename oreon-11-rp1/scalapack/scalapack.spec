%global source0_hash a2f0c9180a210bf7ffe126c9cb81099cf337da1a7120ddb4cbe4894eb7b7d022
%bcond_without openmpi
  %bcond_with openmpi3
  %bcond_without mpich
%bcond_without optimized_blas
%if "%{?_lib}" == "lib64"
%global _cmake_lib_suffix64 -DLIB_SUFFIX=64
%endif
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global blaslib flexiblas
%if %{with optimized_blas}
%global blasflags -DBLA_VENDOR=FlexiBLAS
%else
%global blasflags -DBLA_VENDOR=Generic
%endif
%else
%global blaslib openblas
%if %{with optimized_blas}
%global blasflags -DLAPACK_LIBRARIES=-l%{blaslib} -DBLAS_LIBRARIES=-l%{blaslib}
%else
%global blasflags -DLAPACK_LIBRARIES=-llapack -DBLAS_LIBRARIES=-lblas
%endif
%endif
Summary:        A subset of LAPACK routines redesigned for heterogeneous computing
Name: scalapack
Version: 2.2.2
Release:        1%{?dist}
License: BSD-3-Clause-Open-MPI
URL: http://www.netlib.org/scalapack/
Source0:        https://github.com/Reference-ScaLAPACK/scalapack/archive/v%{version}.tar.gz
%if %{with optimized_blas}
%else
%endif
%if %{with mpich}
%endif
%if %{with openmpi}
%endif
%if %{with openmpi3}
%endif
Patch1: scalapack-2.2.2-fix-libsuffix.patch
Patch2: scalapack-2.2.2-fix-cmake-minimum.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-gfortran
BuildRequires:  glibc-devel
BuildRequires:  mpich-devel-static
BuildRequires:  openmpi-devel
# /oreon:deps
%description
The ScaLAPACK (or Scalable LAPACK) library includes a subset 
of LAPACK routines redesigned for distributed memory MIMD 
parallel computers. It is currently written in a 
Single-Program-Multiple-Data style using explicit message 
passing for inter-processor communication. It assumes 
matrices are laid out in a two-dimensional block cyclic 
decomposition.

ScaLAPACK is designed for heterogeneous computing and is 
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on 
block-partitioned algorithms in order to minimize the frequency 
of data movement between different levels of the memory hierarchy. 
(For such machines, the memory hierarchy includes the off-processor 
memory of other processors, in addition to the hierarchy of registers, 
cache, and local memory on each processor.) The fundamental building 
blocks of the ScaLAPACK library are distributed memory versions (PBLAS) 
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra 
Communication Subprograms (BLACS) for communication tasks that arise 
frequently in parallel linear algebra computations. In the ScaLAPACK 
routines, all inter-processor communication occurs within the PBLAS and the 
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK 
routines resemble their LAPACK equivalents as much as possible. 

%package common
Summary: Common files for scalapack
Provides: blacs-common = %{version}-%{release}
Obsoletes: blacs-common <= 2.0.2
%description common
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for inter-processor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all inter-processor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

This package contains common files which are not specific
to any MPI implementation.

%if %{with mpich}

%package mpich
Summary: ScaLAPACK libraries compiled against mpich
Requires: %{name}-common = %{version}-%{release}
Requires: mpich
Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < 1.7.5-19
Provides: %{name}-lam = %{version}-%{release}
Obsoletes: %{name}-lam <= 1.7.5-7
Provides: blacs-mpich = %{version}-%{release}
Obsoletes: blacs-mpich <= 2.0.2
%description mpich
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for inter-processor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all inter-processor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

This package contains ScaLAPACK libraries compiled with mpich.

%package mpich-devel
Summary: Development libraries for ScaLAPACK (mpich)
Requires: %{name}-mpich = %{version}-%{release}
Requires: mpich-devel
Provides: %{name}-lam-devel = %{version}-%{release}
Obsoletes: %{name}-lam-devel <= 1.7.5-7
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < 1.7.5-19
Provides: blacs-mpich-devel = %{version}-%{release}
Obsoletes: blacs-mpich-devel <= 2.0.2
%description mpich-devel
This package contains development libraries for ScaLAPACK, compiled against mpich.

%package mpich-static
Summary: Static libraries for ScaLAPACK (mpich)
Provides: %{name}-lam-static = %{version}-%{release}
Obsoletes: %{name}-lam-static <= 1.7.5-7
Requires: %{name}-mpich-devel = %{version}-%{release}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < 1.7.5-19
Provides: blacs-mpich-static = %{version}-%{release}
Obsoletes: blacs-mpich-static <= 2.0.2
%description mpich-static
This package contains static libraries for ScaLAPACK, compiled against mpich.

%endif

%if %{with openmpi}
%package openmpi
Summary: ScaLAPACK libraries compiled against openmpi
Requires: %{name}-common = %{version}-%{release}
Requires: openmpi
Provides: blacs-openmpi = %{version}-%{release}
Obsoletes: blacs-openmpi <= 2.0.2
%description openmpi
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for inter-processor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all inter-processor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

This package contains ScaLAPACK libraries compiled with openmpi.

%package openmpi-devel
Summary: Development libraries for ScaLAPACK (openmpi)
Requires: %{name}-openmpi = %{version}-%{release}
Requires: openmpi-devel
Provides: blacs-openmpi-devel = %{version}-%{release}
Obsoletes: blacs-openmpi-devel <= 2.0.2
%description openmpi-devel
This package contains development libraries for ScaLAPACK, compiled against openmpi.

%package openmpi-static
Summary: Static libraries for ScaLAPACK (openmpi)
Requires: %{name}-openmpi-devel = %{version}-%{release}
Provides: blacs-openmpi-static = %{version}-%{release}
Obsoletes: blacs-openmpi-static <= 2.0.2
%description openmpi-static
This package contains static libraries for ScaLAPACK, compiled against openmpi.
%endif

%if %{with openmpi3}
%package openmpi3
Summary: ScaLAPACK libraries compiled against openmpi3
Requires: %{name}-common = %{version}-%{release}
Requires: openmpi3
Provides: blacs-openmpi3 = %{version}-%{release}
Obsoletes: blacs-openmpi3 <= 2.0.2
%description openmpi3
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for inter-processor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all inter-processor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

This package contains ScaLAPACK libraries compiled with openmpi3.

%package openmpi3-devel
Summary: Development libraries for ScaLAPACK (openmpi3)
Requires: %{name}-openmpi3 = %{version}-%{release}
Requires: openmpi3-devel
Provides: blacs-openmpi3-devel = %{version}-%{release}
Obsoletes: blacs-openmpi3-devel <= 2.0.2
%description openmpi3-devel
This package contains development libraries for ScaLAPACK, compiled against openmpi3.

%package openmpi3-static
Summary: Static libraries for ScaLAPACK (openmpi3)
Requires: %{name}-openmpi3-devel = %{version}-%{release}
Provides: blacs-openmpi3-static = %{version}-%{release}
Obsoletes: blacs-openmpi3-static <= 2.0.2
%description openmpi3-static
This package contains static libraries for ScaLAPACK, compiled against openmpi3.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}-%{version}
%patch -P1 -p1 -b .libsuffix
%patch -P2 -p1 -b .fix-cmake-minimum

# fix incorrect version in CMakeLists.txt
sed -i 's|2.2.1|%{version}|g' %{name}-%{version}/CMakeLists.txt

for i in %{?with_mpich:mpich} %{?with_openmpi:openmpi} %{?with_openmpi3:openmpi3}; do
  cp -a %{name}-%{version} %{name}-%{version}-$i
done

%build

%global build_type_safety_c 0
CC="$CC -std=gnu89"
%global build_fflags %(echo %build_fflags -fallow-argument-mismatch| sed 's|-Werror=format-security||g')
%global dobuild() \
cd %{name}-%{version}-$MPI_COMPILER_NAME ; \
%ifarch i686 \
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DBUILD_STATIC_LIBS:BOOL=ON -DMPI_BASE_DIR=%{_libdir}/$MPI_COMPILER_NAME %{blasflags}; \
%cmake_build ;\
%cmake -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=OFF -DMPI_BASE_DIR=%{_libdir}/$MPI_COMPILER_NAME %{blasflags}; \
%cmake_build ;\
%else \
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DBUILD_STATIC_LIBS:BOOL=ON -DMPI_BASE_DIR=%{_libdir}/$MPI_COMPILER_NAME %{blasflags} %{?_cmake_lib_suffix64}; \
%cmake_build ;\
%cmake -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=OFF -DMPI_BASE_DIR=%{_libdir}/$MPI_COMPILER_NAME %{blasflags} %{?_cmake_lib_suffix64}; \
%cmake_build ;\
%endif \
cd ..
%if %{with mpich}
export MPI_COMPILER_NAME=mpich
%{_mpich_load}
%dobuild
%{_mpich_unload}
%endif
%if %{with openmpi}
export MPI_COMPILER_NAME=openmpi
%{_openmpi_load}
%dobuild
%{_openmpi_unload}
%endif
%if %{with openmpi3}
export MPI_COMPILER_NAME=openmpi3
%{_openmpi3_load}
%dobuild
%{_openmpi3_unload}
%endif
%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/cmake
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
for i in %{?with_mpich:mpich} %{?with_openmpi:openmpi} %{?with_openmpi3:openmpi3}; do
  mkdir -p %{buildroot}%{_libdir}/$i/lib/
  pushd %{name}-%{version}-$i
  %cmake_install
  cp -f %{_vpath_builddir}/lib/libscalapack.a %{buildroot}%{_libdir}/$i/lib/
  popd
  mkdir -p %{buildroot}%{_includedir}/$i-%{_arch}/
  mkdir -p %{buildroot}%{_includedir}/blacs/
  install -p %{name}-%{version}-$i/BLACS/SRC/Bdef.h %{buildroot}%{_includedir}/blacs/
  for f in *.so*; do
    mv %{buildroot}%{_libdir}/$f %{buildroot}%{_libdir}/$i/lib/
  done
  mv %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_libdir}/$i/lib/
done
cd %{name}-%{version}
cp -f README ../
%if %{with openmpi}
sed -i 's|mpi|ompi|g' %{buildroot}%{_libdir}/openmpi/lib/pkgconfig/scalapack.pc
sed -i 's|L%{_libdir}|L${libdir}|' %{buildroot}%{_libdir}/openmpi/lib/pkgconfig/scalapack.pc
sed -i 's|prefix=/usr|prefix=/usr/%{_lib}/openmpi|' %{buildroot}%{_libdir}/openmpi/lib/pkgconfig/scalapack.pc
sed -i 's|libdir=%{_libdir}|libdir=${prefix}/lib|' %{buildroot}%{_libdir}/openmpi/lib/pkgconfig/scalapack.pc
%endif
%if %{with mpich}
sed -i 's|mpi|mpich|g' %{buildroot}%{_libdir}/mpich/lib/pkgconfig/scalapack.pc
sed -i 's|L%{_libdir}|L${libdir}|' %{buildroot}%{_libdir}/mpich/lib/pkgconfig/scalapack.pc
sed -i 's|libdir=%{_libdir}|libdir=%{_libdir}/mpich/lib|' %{buildroot}%{_libdir}/mpich/lib/pkgconfig/scalapack.pc
%endif
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%if %{with optimized_blas}
%if %{with openmpi}
sed -i 's|lapack blas|flexiblas|g' %{buildroot}%{_libdir}/openmpi/lib/pkgconfig/scalapack.pc
%endif
%if %{with mpich}
sed -i 's|lapack blas|flexiblas|g' %{buildroot}%{_libdir}/mpich/lib/pkgconfig/scalapack.pc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n scalapack-common -f %{oreon_filedir}/scalapack-common.list
%files -n scalapack-mpich -f %{oreon_filedir}/scalapack-mpich.list
%files -n scalapack-mpich-devel -f %{oreon_filedir}/scalapack-mpich-devel.list
%files -n scalapack-mpich-static -f %{oreon_filedir}/scalapack-mpich-static.list
%files -n scalapack-openmpi -f %{oreon_filedir}/scalapack-openmpi.list
%files -n scalapack-openmpi-devel -f %{oreon_filedir}/scalapack-openmpi-devel.list
%files -n scalapack-openmpi-static -f %{oreon_filedir}/scalapack-openmpi-static.list

%changelog

%autochangelog
