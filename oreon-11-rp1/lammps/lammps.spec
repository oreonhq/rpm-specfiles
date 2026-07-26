%global source0_hash e33f78a92bbacc2c8639cb2f00b347b4715c8b57aaac2c14dc2cd86e836cfd34

%global git 0
%global commit cd8851c4e75c42744e221ae3c457c6e4645f0ad5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so -DLAPACK_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

Name:           lammps
%if %{git}
Version:        20251210^%{shortcommit}
%else
Version:        20251210
%endif
%global         uversion %(v=%{version}; \
                  patch=${v##*.}; [[ $v = $patch ]] && patch= \
                  v=${v%%.*}; \
                  months=( "" Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec ); \
                  d=${v:6:2}; \
                  m=${v:4:2};
                  y=${v:0:4};
                  echo $([[ -z $patch ]] && echo patch || echo stable)_${d#0}${months[${m#0}]}${y}$([[ -n $patch ]] && echo _update${patch}))
Release:        1%{?dist}
Summary:        Molecular Dynamics Simulator
License:        GPL-2.0-only
Url:            https://www.lammps.org/
%if %{git}
Source0:        https://github.com/lammps/lammps/archive/%{commit}/lammps-%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
%else
Source0:        https://github.com/lammps/lammps/archive/%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz
%endif
Source1:        https://github.com/google/googletest/releases/download/v1.17.0/googletest-1.17.0.tar.gz
Source2:        https://pyyaml.org/download/libyaml/yaml-0.2.5.tar.gz
Source3:        https://download.lammps.org/thirdparty/opencl-loader-2024.05.09.tar.gz
Source4:        https://github.com/spglib/spglib/archive/refs/tags/v1.11.2.1.tar.gz#/spglib-1.11.2.1.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# mpi is broken on s390x see, bug #2322073
ExcludeArch: %{ix86} s390x

BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
%ifnarch %ix86
BuildRequires:  openmpi-devel
BuildRequires:  heffte-openmpi-devel
%ifarch x86_64
#F42 only, https://src.fedoraproject.org/rpms/rocfft/pull-request/1
BuildRequires:  rocm-hip-devel
%endif
BuildRequires:  python%{python3_pkgversion}-mpi4py-openmpi
BuildRequires:  python%{python3_pkgversion}-mpi4py-mpich
%endif
BuildRequires:  mpich-devel
BuildRequires:  heffte-mpich-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  fftw3-devel
BuildRequires:  zlib-devel
BuildRequires:  gsl-devel
BuildRequires:  voro++-devel
BuildRequires:  %{blaslib}-devel
BuildRequires:  hdf5-devel
BuildRequires:  cmake
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  tbb-devel
BuildRequires:  readline-devel
# before F33 there was no kokkos package
%if 0%{?fedora} >= 33
%ifnarch i686 armv7hl
%global         with_kokkos 1
# kokkos needs a lot of memory
%global         _smp_mflags -j1
BuildRequires:  kokkos-devel >= 4.7
%endif
%endif
Requires:       %{name}-data

%global lammps_desc \
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale \
Atomic/Molecular Massively Parallel Simulator.\
\
LAMMPS has potentials for soft materials (biomolecules, polymers) and \
solid-state materials (metals, semiconductors) and coarse-grained or \
mesoscopic systems. It can be used to model atoms or, more generically, as a \
parallel particle simulator at the atomic, meso, or continuum scale. \
\
LAMMPS runs on single processors or in parallel using message-passing \
techniques and a spatial-decomposition of the simulation domain. The code is \
designed to be easy to modify or extend with new functionality.

%description
%{lammps_desc}

%ifnarch %ix86
%global with_openmpi 1
%package openmpi
Summary:        LAMMPS Open MPI binaries and libraries
Requires:       openmpi
Requires:       %{name}-data

%description openmpi
%{lammps_desc}

This package contains LAMMPS Open MPI binaries and libraries
%endif

%package mpich
Summary:        LAMMPS MPICH binaries and libraries
Requires:       mpich
Requires:       %{name}-data

%description mpich
%{lammps_desc}

This package contains LAMMPS MPICH binaries and libraries

%package -n python%{python3_pkgversion}-%{name}
Summary:        LAMMPS Python interface
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-numpy
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description -n python%{python3_pkgversion}-%{name}
%{lammps_desc}

This package contains LAMMPS Python interface

%package headers
Summary:        Development headers for LAMMPS

%description headers
%{lammps_desc}

This package contains development headers for LAMMPS.

%package devel
Summary:        Development libraries for LAMMPS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-headers%{?_isa} = %{version}-%{release}

%description devel
%{lammps_desc}

This package contains development libraries for serial LAMMPS.

%package mpich-devel
Summary:        Development libraries for MPICH LAMMPS
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:       %{name}-headers%{?_isa} = %{version}-%{release}

%description mpich-devel
%{lammps_desc}

This package contains development headers and libraries for MPICH LAMMPS.

%ifnarch %ix86
%package openmpi-devel
Summary:        Development libraries for Open MPI LAMMPS
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:       %{name}-headers%{?_isa} = %{version}-%{release}

%description openmpi-devel
%{lammps_desc}

This package contains development libraries for Open MPI LAMMPS.
%endif

%if 0%{?el7}
%package openmpi3
Summary:        LAMMPS Open MPI 3 binaries and libraries
BuildRequires:  openmpi3-devel
Requires:       openmpi3
Requires:       %{name}-data

%description openmpi3
%{lammps_desc}

This package contains LAMMPS Open MPI 3 binaries and libraries

%package openmpi3-devel
Summary:        Development libraries for Open MPI 3 LAMMPS
Requires:       %{name}-openmpi3%{?_isa} = %{version}-%{release}
Requires:       %{name}-headers%{?_isa} = %{version}-%{release}

%description openmpi3-devel
%{lammps_desc}

This package contains development libraries for Open MPI 3 LAMMPS.
%endif

%package data
Summary:        Data files for LAMMPS
BuildArch:      noarch

%description data
%{lammps_desc}

This package contains data files for LAMMPS.

%generate_buildrequires
cd python
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{git}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-%{uversion}
%endif

%build
%global _vpath_srcdir cmake
%global _vpath_builddir ${mpi:-serial}
set +e
. /etc/profile.d/modules.sh
set -e

for mpi in '' mpich %{?with_openmpi:openmpi} %{?el7:openmpi3} ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  #python wrapper isn't mpi specific
  %{cmake} \
  -C cmake/presets/all_on.cmake \
  -C cmake/presets/nolib.cmake \
  %{cmake_blas_flags} \
  -DCMAKE_CUSTOM_LINKER="default" \
  -DPKG_PYTHON=ON \
  -DPKG_VORONOI=ON \
  -DPKG_ATC=ON \
  -DPKG_H5MD=ON \
  %{?with_kokkos:-DPKG_KOKKOS=ON -DEXTERNAL_KOKKOS=ON} \
  -DENABLE_TESTING=ON \
  -DGTEST_URL=file://%{S:1} \
  -DYAML_URL=file://%{S:2} \
  -DOPENCL_LOADER_URL=file://%{S:3} \
  -DSPGLIB_URL=file://%{S:4} \
  -DDOWNLOAD_POTENTIALS=OFF \
  -DPYTHON_INSTDIR=%{python3_sitelib} \
  -DCMAKE_INSTALL_SYSCONFDIR=/etc \
  -DPKG_GPU=ON -DGPU_API=OpenCL \
  -DBUILD_OMP=ON \
  -DFFT=FFTW3 \
%ifnarch x86_64 %x86
  -DPKG_INTEL=OFF \
%endif
    -DCMAKE_INSTALL_BINDIR=${MPI_BIN:-%{_bindir}} -DCMAKE_INSTALL_LIBDIR=${MPI_LIB:-%{_libdir}} -DLAMMPS_MACHINE="${MPI_SUFFIX#_}" -DLAMMPS_LIB_SUFFIX="${MPI_SUFFIX#_}" -DCMAKE_INSTALL_MANDIR=${MPI_MAN:-%{_mandir}} \
    ${mpi:+-DBUILD_MPI=ON -DFFT_USE_HEFFTE=ON -DCMAKE_EXE_LINKER_FLAGS="%{__global_ldflags} -Wl,-rpath -Wl,${MPI_LIB} -Wl,--enable-new-dtags" -DCMAKE_SHARED_LINKER_FLAGS="%{__global_ldflags} -Wl,-rpath -Wl,${MPI_LIB} -Wl,--enable-new-dtags" $(test "$mpi" != openmpi || echo "-DMPIEXEC_PREFLAGS=--oversubscribe") } \
    $(test -z "${mpi}" && echo -DBUILD_MPI=OFF -DBUILD_LAMMPS_SHELL=ON -DBUILD_TOOLS=ON)
  %cmake_build
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

cd python
%pyproject_wheel

%install
set +e
. /etc/profile.d/modules.sh
set -e

for mpi in '' mpich %{?with_openmpi:openmpi} %{?el7:openmpi3} ; do
  %cmake_install
done

cd python
%pyproject_install
%pyproject_save_files lammps

%check

%global testargs --label-exclude unstable --exclude-regex '\(SimpleCommands\|Variables\|ComputeGlobal\|MolPairStyle:coul_slater_long\|AtomicPairStyle:meam_spline\|FixTimestep:.*\|.*tip4p.*\|FFT3D\)'

%ifnarch %ix86
%global testargs --label-exclude unstable --exclude-regex '\(SimpleCommands\|Variables\|ComputeGlobal\|MolPairStyle:coul_slater_long\|AtomicPairStyle:meam_spline\|FixTimestep:.*\|.*tip4p.*\|Groups\|AtomicPairStyle:lj_cut_sphere\|AtomicPairStyle:lj_expand_sphere\|AtomicPairStyle:meam_ms\|AtomicPairStyle:pedone\|DihedralStyle:cosine_squared_restricted\|BondStyle:harmonic_restrain\|FFT3D\)'
%endif

%ifarch s390x
%global testargs --label-exclude unstable --exclude-regex '\(SimpleCommands\|Variables\|ComputeGlobal\|MolPairStyle:coul_slater_long\|AtomicPairStyle:meam_spline\|FixTimestep:.*\|.*tip4p.*\|LibraryMPI\|MPILoadBalancing\|FileOperations\|Groups\|SetProperty\|AtomicPairStyle:lj_cut_sphere\|AtomicPairStyle:lj_expand_sphere\|AtomicPairStyle:meam_ms\|AtomicPairStyle:pedone\|DihedralStyle:cosine_squared_restricted\|BondStyle:harmonic_restrain\|TestPairList\|FFT3D\)'
%endif

set +e
. /etc/profile.d/modules.sh
set -e

for mpi in '' mpich %{?with_openmpi:openmpi} %{?el7:openmpi3} ; do
  old_PYTHONPATH="${PYTHONPATH}"
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch} && export PYTHONPATH="${MPI_PYTHON3_SITEARCH}:${PYTHONPATH}"
  %ctest --output-on-failure %{?testargs}
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch} && export PYTHONPATH="${old_PYTHONPATH}"
done

%pyproject_check_import -t

%ldconfig_scriptlets

%files
%doc README
%license LICENSE
%{_bindir}/lmp
%{_mandir}/man1/lmp.*
%{_libdir}/liblammps.so.*
%{_bindir}/msi2lmp
%{_mandir}/man1/msi2lmp.*
%{_bindir}/binary2txt
%{_bindir}/chain.x
%{_bindir}/micelle2d.x
%{_bindir}/stl_bin2txt
%{_bindir}/phana
%{_bindir}/reformat-json

%files devel
%{_libdir}/liblammps.so
%{_libdir}/pkgconfig/liblammps.pc
%{_libdir}/cmake/LAMMPS

%ifnarch %ix86
%files openmpi-devel
%{_libdir}/openmpi*/lib/liblammps_openmpi.so
%{_libdir}/openmpi*/lib/pkgconfig/liblammps_openmpi.pc
%{_libdir}/openmpi*/lib/cmake/LAMMPS
%endif

%files mpich-devel
%{_libdir}/mpich*/lib/liblammps_mpich.so
%{_libdir}/mpich*/lib/pkgconfig/liblammps_mpich.pc
%{_libdir}/mpich*/lib/cmake/LAMMPS

%files -n python%{python3_pkgversion}-%{name} -f %{pyproject_files}

%files headers
%license LICENSE
%{_includedir}/%{name}/

%ifnarch %ix86
%files openmpi
%license LICENSE
%{_libdir}/openmpi*/bin/lmp_openmpi
%{_mandir}/openmpi*/man1/lmp_openmpi.*
%{_libdir}/openmpi*/lib/liblammps_openmpi.so.*
%endif

%if 0%{?el7}
%files openmpi3
%license LICENSE
%{_libdir}/openmpi3*/bin/lmp_openmpi3
%{_mandir}/openmpi3*/man1/lmp_openmpi3.*
%{_libdir}/openmpi3*/lib/liblammps_openmpi3.so.*

%files openmpi3-devel
%{_libdir}/openmpi3*/lib/liblammps_openmpi3.so
%{_libdir}/openmpi3*/lib/pkgconfig/liblammps_openmpi3.pc
%{_libdir}/openmpi3/lib/cmake/LAMMPS
%endif

%files mpich
%license LICENSE
%{_libdir}/mpich*/bin/lmp_mpich
%{_mandir}/mpich*/man1/lmp_mpich.*
%{_libdir}/mpich*/lib/liblammps_mpich.so.*

%files data
%license LICENSE
%{_datadir}/%{name}
%config %{_sysconfdir}/profile.d/lammps.*

%changelog
%autochangelog
