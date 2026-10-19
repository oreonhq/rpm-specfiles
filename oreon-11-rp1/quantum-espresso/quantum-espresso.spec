%global source0_hash 1064201ff27d129ac4e23acfdc44726d1935c63ee5484c5f74b350af2afe4d9d
%global         forgeurl0 https://gitlab.com/QEF/q-e
%global         version0  7.5
%global         tag0      qe-%{version0}
%global         forgeurl1 https://gitlab.com/max-centre/components/devicexlib
%global         commit1   a6b89ef77b1ceda48e967921f1f5488d2df9226d
%global         forgeurl2 https://github.com/wannier-developers/wannier90
%global         commit2   1d6b187374a2d50b509e5e79e2cab01a79ff7ce1
%bcond          check     0
Name:           quantum-espresso
Release:        1%{?dist}
%forgemeta -a
Version:        %[ %{defined tag0} ? "%version0" : "%forgeversion" ]
Summary:        A suite for electronic-structure calculations and materials modeling
ExcludeArch:    %{ix86} s390x
Provides:       bundled(FoXlibf)
Provides:       bundled(deviceXlib)
License:  %{shrink:
    GPL-2.0-or-later
}
URL:            http://www.quantum-espresso.org/
Source0:        %{forgeurl0}/-/archive/%{tag0}/q-e-%{tag0}.tar.bz2
Source1:        pseudo.tar.gz
Source2:        %{forgesource1}
Source3:        %{forgesource2}
Patch:          https://gitlab.com/QEF/q-e/-/merge_requests/2561.patch
Patch:          https://gitlab.com/QEF/q-e/-/merge_requests/2792.patch
%global _description_devel %{expand:
Development files for %{name} package}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-gfortran
BuildRequires:  libmbd-devel
BuildRequires:  libmbd-mpich-devel
BuildRequires:  libmbd-openmpi-devel
BuildRequires:  mpich-devel
BuildRequires:  ninja-build
BuildRequires:  openmpi-devel
BuildRequires:  python3
BuildRequires:  scalapack-mpich-devel
BuildRequires:  scalapack-openmpi-devel
# /oreon:deps
%description
%{_description}

Serial version.

%package openmpi
Summary:        %{name} - openmpi version
%description openmpi
%{_description}

OpenMPI version.

%package mpich
Summary:        %{name} - mpich version
%description mpich
%{_description}

MPICH version.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{_description_devel}

Serial version.

%package openmpi-devel
Summary:        Development files for %{name} - openmpi version
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel
%{_description_devel}

OpenMPI version.

%package mpich-devel
Summary:        Development files for %{name} - mpich version
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel
%{_description_devel}

MPICH version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
tar -xf %{SOURCE2} --strip-components=1 -C external/devxlib
tar -xf %{SOURCE3} --strip-components=1 -C external/wannier90

# Set unique build directories for each serial/mpi variant
# $MPI_SUFFIX will be evaluated in the loops below, set by mpi modules
%global _vpath_builddir %{_vendor}-%{_target_os}-build${MPI_SUFFIX:-_serial}

%conf
# Temporary fix to the "executable .note.GNU-stack section" issue
export LDFLAGS="$LDFLAGS -z noexecstack"

cmake_common_args=(
  "-G Ninja"
  "-DQE_ENABLE_TEST:BOOL=ON"
  "-DQE_MBD_INTERNAL:BOOL=OFF"
  "-DQE_FFTW_VENDOR:STRING=FFTW3"
  "-DQE_ENABLE_OPENMP:BOOL=ON"
  "-DQE_ENABLE_DOC:BOOL=OFF"
  # Disable many external package support for now
  "-DQE_ENABLE_PLUGINS:STRING=''"
  "-DQE_ENABLE_FOX=OFF"
  "-DQE_ENABLE_ENVIRON=OFF"
  # TODO: review other flags
)
for mpi in '' mpich openmpi; do
  if [ -n "$mpi" ]; then
    module load mpi/${mpi}-%{_arch}
    cmake_mpi_args=(
      "-DQE_ENABLE_MPI:BOOL=ON"
      "-DCMAKE_INSTALL_PREFIX:PATH=${MPI_HOME}"
      "-DQE_INSTALL_Fortran_MODULES:PATH=${MPI_FORTRAN_MOD_DIR}"
      "-DCMAKE_INSTALL_LIBDIR:PATH=lib"
    )
  else
    cmake_mpi_args=(
      "-DQE_ENABLE_MPI:BOOL=OFF"
      "-DQE_INSTALL_Fortran_MODULES:PATH=%{_fmoddir}"
    )
  fi

  %cmake \
    ${cmake_common_args[@]} \
    ${cmake_mpi_args[@]}

  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done

%build

for mpi in '' mpich openmpi; do
  [ -n "$mpi" ] && module load mpi/${mpi}-%{_arch}
  %cmake_build
  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done
%install
for mpi in '' mpich openmpi; do
  [ -n "$mpi" ] && module load mpi/${mpi}-%{_arch}
  %cmake_install
  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done
rm -r %{buildroot}%{_libdir}/openmpi/bin/epw_pp.py
rm -r %{buildroot}%{_libdir}/mpich/bin/epw_pp.py
rm -r %{buildroot}%{_datadir}/GUI
rm -r %{buildroot}%{_libdir}/openmpi/share/GUI
rm -r %{buildroot}%{_libdir}/mpich/share/GUI
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with check}
tar -xf %{SOURCE1}
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
CTEST_ARGS=""
CTEST_ARGS="$CTEST_ARGS -LE pw_plugins"
for mpi in '' mpich openmpi; do
  [ -n "$mpi" ] && module load mpi/${mpi}-%{_arch}
  %ctest $CTEST_ARGS
  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done
%endif
%files -f %{oreon_filedir}/main.list
%files -n quantum-espresso-openmpi -f %{oreon_filedir}/quantum-espresso-openmpi.list
%files -n quantum-espresso-mpich -f %{oreon_filedir}/quantum-espresso-mpich.list
%files -n quantum-espresso-devel -f %{oreon_filedir}/quantum-espresso-devel.list
%files -n quantum-espresso-openmpi-devel -f %{oreon_filedir}/quantum-espresso-openmpi-devel.list
%files -n quantum-espresso-mpich-devel -f %{oreon_filedir}/quantum-espresso-mpich-devel.list

%changelog

%autochangelog
