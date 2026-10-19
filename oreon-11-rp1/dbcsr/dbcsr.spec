%global source0_hash 3d897220fbb4498215331efad6905eb7744881b4cf04eb5c5fb4db7c48a56ef9
%bcond_with opencl
%bcond_without openmpi
Name:          dbcsr
Version:       2.10.0
Release:        1%{?dist}
Summary:        Distributed Block Compressed Sparse Row matrix library
License:       GPL-2.0-or-later
URL:           https://cp2k.github.io/dbcsr/develop/
Source0:        https://github.com/cp2k/dbcsr/releases/download/v%{version}/dbcsr-%{version}.tar.gz
%if %{with opencl}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  python3-fypp
# /oreon:deps
%description
%{_description}

This package contains the non-MPI single process and multi-threaded versions.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran%{_isa}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%global mpi_list mpich

%if %{with openmpi}
%global mpi_list %{mpi_list} openmpi
%package openmpi
Summary: DBCSR - openmpi version
BuildRequires:  openmpi-devel
%description openmpi
%{_description}

This package contains the parallel single- and multi-threaded versions
using OpenMPI.

%package openmpi-devel
Summary: Development files for %{name}-openmpi
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel
The %{name}-openmpi-devel package contains libraries and header files for
developing applications that use %{name}-openmpi.
%endif

%package mpich
Summary: DBCSR - mpich version
BuildRequires:  mpich-devel
%description mpich
%{_description}

This package contains the parallel single- and multi-threaded versions
using mpich.

%package mpich-devel
Summary: Development files for %{name}-mpich
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel
The %{name}-mpich-devel package contains libraries and header files for
developing applications that use %{name}-mpich.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Use system fypp, other tools not needed
rm -r tools

# $mpi will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${mpi:-serial}

%build

export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
export FFLAGS="%{optflags} -fPIC"
%cmake \
  -DCMAKE_INSTALL_Fortran_MODULES=%{_fmoddir} \
  -DUSE_MPI=OFF \
  %{?with_opencl:-DUSE_ACCEL=opencl -DUSE_SMM=libxsmm}
%cmake_build
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake \
    -DCMAKE_INSTALL_Fortran_MODULES=$MPI_FORTRAN_MOD_DIR \
    %{?with_opencl:-DUSE_ACCEL=opencl -DUSE_SMM=libxsmm} \
    -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \
    -DCMAKE_INSTALL_LIBDIR:PATH=$MPI_LIB \
    -DUSE_MPI_F08=ON \
    -DTEST_MPI_RANKS=2
  %cmake_build
  module purge
done
%install
%cmake_install
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake_install
  module purge
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  fail=
  [ $mpi = mpich -a %{_arch} = s390x ] && fail=no
  %ctest || test $fail
  module purge
done
%files -f %{oreon_filedir}/main.list
%files -n dbcsr-devel -f %{oreon_filedir}/dbcsr-devel.list
%files -n dbcsr-openmpi -f %{oreon_filedir}/dbcsr-openmpi.list
%files -n dbcsr-openmpi-devel -f %{oreon_filedir}/dbcsr-openmpi-devel.list
%files -n dbcsr-mpich -f %{oreon_filedir}/dbcsr-mpich.list
%files -n dbcsr-mpich-devel -f %{oreon_filedir}/dbcsr-mpich-devel.list

%changelog

%autochangelog
