%global source0_hash f9bd86f580f57a53a0768c0045d1417f9f9a1d66d851ed7f662f496200043373
%bcond libxsmm %[ "%{_arch}" == "x86_64" ]
%global _lto_cflags %nil
Name:          cp2k
Version:       2026.2
Release:        1%{?dist}
Summary:        Ab Initio Molecular Dynamics
License:       GPL-2.0-or-later
URL:           https://www.cp2k.org/
Source0:        https://github.com/cp2k/cp2k/releases/download/v%{version}/cp2k-%{version}.tar.bz2
Patch:         https://github.com/cp2k/cp2k/pull/3968.patch
Patch:         https://github.com/cp2k/cp2k/pull/3972.patch
ExcludeArch:   %{ix86} s390x
%if %{with libxsmm}
%endif
Requires:      %{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  blacs-mpich-devel
BuildRequires:  blacs-openmpi-devel
BuildRequires:  cmake
BuildRequires:  cmake(DBCSR)
BuildRequires:  cmake(Spglib)
BuildRequires:  dbcsr-mpich-devel
BuildRequires:  dbcsr-openmpi-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  libxc-devel
BuildRequires:  mpich-devel
BuildRequires:  ninja-build
BuildRequires:  openmpi-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libxsmm)
BuildRequires:  python3
BuildRequires:  python3-fypp
BuildRequires:  scalapack-mpich-devel
BuildRequires:  scalapack-openmpi-devel
# /oreon:deps
%description
%{_description}

This package contains the non-MPI single process and multi-threaded versions.

%package common
Summary:       Molecular simulations software - common files
BuildArch:     noarch
%description common
%{_description}

This package contains the documentation and the manual.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package openmpi
Summary:        Molecular simulations software - openmpi version
BuildRequires:  openmpi-devel
BuildRequires:  blacs-openmpi-devel
BuildRequires:  dbcsr-openmpi-devel
BuildRequires:  scalapack-openmpi-devel
Requires:       %{name}-common = %{version}-%{release}
%description openmpi
%{_description}

This package contains the parallel single- and multi-threaded versions
using OpenMPI.

%package openmpi-devel
Summary:        Development files for %{name}
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package mpich
Summary:        Molecular simulations software - mpich version
BuildRequires:  mpich-devel
BuildRequires:  blacs-mpich-devel
BuildRequires:  dbcsr-mpich-devel
BuildRequires:  scalapack-mpich-devel
Requires:       %{name}-common = %{version}-%{release}
%description mpich
%{_description}

This package contains the parallel single- and multi-threaded versions
using mpich.

%package mpich-devel
Summary:        Development files for %{name}
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

%autosetup -p1
rm tools/build_utils/fypp
rm -r exts/dbcsr

# $MPI_SUFFIX will be evaluated in the loops below, set by mpi modules
%global _vpath_builddir %{_vendor}-%{_target_os}-build${MPI_SUFFIX:-_serial}

%build

cmake_common_args=(
  "-G Ninja"
  "-DCP2K_DEBUG_MODE:BOOL=OFF"
  "-DCP2K_BLAS_VENDOR:STRING=FlexiBLAS"
  "-DCP2K_USE_STATIC_BLAS:BOOL=OFF"
  "-DCP2K_USE_FFTW3:BOOL=ON"
  "-DCP2K_USE_COSMA:BOOL=OFF"  # Not packaged
  "-DCP2K_USE_LIBXSMM:BOOL=%{?with_libxsmm:ON}%{?without_libxsmm:OFF}"
  "-DCP2K_USE_LIBXC:BOOL=ON"
  "-DCP2K_USE_LIBINT2:BOOL=OFF"  # Detection is broken
  "-DCP2K_USE_SPGLIB:BOOL=ON"
)
for mpi in '' mpich openmpi; do
  if [ -n "$mpi" ]; then
    module load mpi/${mpi}-%{_arch}
    cmake_mpi_args=(
      "-DCMAKE_INSTALL_PREFIX:PATH=${MPI_HOME}"
      "-DCMAKE_INSTALL_Fortran_MODULES:PATH=${MPI_FORTRAN_MOD_DIR}/cp2k"
      "-DCMAKE_INSTALL_LIBDIR:PATH=lib"
      "-DCP2K_CMAKE_SUFFIX:STRING=${MPI_SUFFIX}"
      "-DCP2K_DATA_DIR:PATH=%{_datadir}/cp2k/data"
      "-DCP2K_USE_MPI_F08:BOOL=ON"
    )
  else
    cmake_mpi_args=(
      "-DCP2K_USE_MPI:BOOL=OFF"
      "-DCMAKE_INSTALL_Fortran_MODULES:PATH=%{_fmoddir}/cp2k"
    )
  fi
  %cmake \
    ${cmake_common_args[@]} \
    ${cmake_mpi_args[@]}
  %cmake_build
  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done
%install
for mpi in '' mpich openmpi; do
  [ -n "$mpi" ] && module load mpi/${mpi}-%{_arch}
  %cmake_install
  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done
rm -f %{_buildrootdir}/**/%{_bindir}/*_unittest.*
rm -f %{_buildrootdir}/**/%{_libdir}/openmpi/bin/*_unittest.*
rm -f %{_buildrootdir}/**/%{_libdir}/mpich/bin/*_unittest.*
%oreon_autofiles cp2k-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cp2k-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cp2k-openmpi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cp2k-openmpi-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cp2k-mpich usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cp2k-mpich-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export CP2K_DATA_DIR=%{buildroot}%{_datadir}/cp2k/data
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
test_common_args=(
  "--skip_regtests"
  "--ompthreads 2"
)
for mpi in '' mpich openmpi ; do
  if [ -n "$mpi" ]; then
    module load mpi/${mpi}-%{_arch}
    bindir=${MPI_BIN}
    libdir=${MPI_LIB}
    test_mpi_args=(
      "--mpiranks 2"
      "psmp"
    )
  else
    bindir=%{_bindir}
    libdir=%{_libdir}
    test_mpi_args=(
      "ssmp"
    )
  fi
  env PATH=%{buildroot}${bindir}:${PATH} \
    LD_LIBRARY_PATH=%{buildroot}${libdir} \
    tests/do_regtest.py ${test_common_args[@]} %{_vpath_builddir}/bin ${test_mpi_args[@]}
  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done
%files -f %{oreon_filedir}/main.list
%files -n cp2k-common -f %{oreon_filedir}/cp2k-common.list
%files -n cp2k-devel -f %{oreon_filedir}/cp2k-devel.list
%files -n cp2k-openmpi -f %{oreon_filedir}/cp2k-openmpi.list
%files -n cp2k-openmpi-devel -f %{oreon_filedir}/cp2k-openmpi-devel.list
%files -n cp2k-mpich -f %{oreon_filedir}/cp2k-mpich.list
%files -n cp2k-mpich-devel -f %{oreon_filedir}/cp2k-mpich-devel.list

%changelog

%autochangelog
