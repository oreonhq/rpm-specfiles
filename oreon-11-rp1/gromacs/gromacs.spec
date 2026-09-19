%global source0_hash 194bded22cdb008d8793d166cb37b5183360486bed2b4de7b49be1e87e335f8d

#global _rcname rc1
#global _rc -%%_rcname

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

# 32-bit arch
# https://gitlab.com/gromacs/gromacs/-/merge_requests/2453
# openmpi 5 & s390x
ExcludeArch:    i686 armv7hl s390x

%global with_opencl 1

%global simd None
%ifarch x86_64
%global simd SSE2
%endif
%ifarch ppc64p7
%global simd IBM_VMX
%endif
# IBM_VSX is broken with >=gcc-9
#ifarch ppc64le
#global simd IBM_VSX
#endif
%ifarch aarch64
%global simd ARM_NEON_ASIMD
%endif

Name:		gromacs
Version:	2026.0
Release:	1%{?dist}
Summary:	Fast, Free and Flexible Molecular Dynamics
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	LGPL-2.1-or-later
URL:		http://www.gromacs.org

Source0:	https://ftp.gromacs.org/gromacs/gromacs-%{version}%{?_rc}.tar.gz
Source1:	https://ftp.gromacs.org/manual/manual-%{version}%{?_rc}.pdf
Source2:	https://ftp.gromacs.org/regressiontests/regressiontests-%{version}%{?_rc}.tar.gz
Source3:	gromacs-README.fedora
BuildRequires:	gcc-c++
BuildRequires:  cmake3 >= 3.18.4
BuildRequires:	%{blaslib}-devel
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	hwloc
BuildRequires:	hwloc-devel
BuildRequires:	lmfit-devel >= 6.0
BuildRequires:	muParser-devel
%if %{with_opencl}
BuildRequires:	ocl-icd-devel
BuildRequires:	opencl-headers
Recommends:	gromacs-opencl = %{version}-%{release}
%endif
BuildRequires:	tng-devel
# Dependencies used for regressiontest
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
%define compdir %{?bash_completions_dir}%{!?bash_completions_dir:/etc/bash_completion.d}
Requires:	gromacs-common = %{version}-%{release}
Requires:	gromacs-libs = %{version}-%{release}
Obsoletes:	gromacs-ngmx < 5.0.4-1
Obsoletes:	gromacs-csh < 2016.1-2
Obsoletes:	gromacs-zsh < 2016.1-2

%description
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides single and double precision binaries.
The documentation is in the package gromacs-common.

mdrun has been compiled with thread parallellization, so it runs in parallel
on shared memory systems. If you want to run on a cluster, you probably want
to install one of the MPI parallellized packages.

N.B. All binaries have names starting with g_, for example mdrun has been
renamed to g_mdrun.

%package common
Summary:	GROMACS shared data and documentation
BuildArch:	noarch
Provides:	gromacs-bash = %{version}-%{release}
Obsoletes:	gromacs-bash < 5.0.4-1

%description common
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package includes architecture independent data and HTML documentation.

%if %{with_opencl}
%package opencl
Summary:	GROMACS OpenCL kernels
# suggest installing a GPU-based OpenCL implementation
Suggests:	beignet
Suggests:	mesa-libOpenCL
# or at least a CPU-based one
Suggests:	pocl

%description opencl
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package includes the OpenCL kernels.
%endif

%package doc
Summary:	GROMACS manual
BuildArch:	noarch
Obsoletes: gromacs-common < 5.0.5-2

%description doc
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package the manual in PDF format.

%package devel
Summary:	GROMACS header files and development libraries
Requires:	gromacs-libs = %{version}-%{release}
# cmake files refer to /usr/bin/gmx as well
Requires:	gromacs = %{version}-%{release}
Obsoletes:	gromacs-mpich-devel < 2016-0.1.20160318gitbec9c87
Obsoletes:	gromacs-openmpi-devel < 2016-0.1.20160318gitbec9c87

%description devel
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains header files and development libraries for the GROMACS
molecular dynamics software. You need it if you want to write your own analysis
programs.

%package libs
Summary:	GROMACS shared libraries

%description libs
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains libraries needed for operation of GROMACS.

%package openmpi
Summary:	GROMACS Open MPI binaries and libraries
Requires:	gromacs-common = %{version}-%{release}
%if %{with_opencl}
Recommends:	gromacs-opencl = %{version}-%{release}
%endif
Obsoletes:	gromacs-openmpi-libs < 2016-0.1.20160318gitbec9c87
BuildRequires:	openmpi-devel

%description openmpi
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

mdrun has been compiled with thread parallellization (for running on
a single node) and with Open MPI (for running on multiple nodes).
This package single and double precision binaries and libraries.

%package mpich
Summary:	GROMACS MPICH binaries and libraries
Requires:	gromacs-common = %{version}-%{release}
%if %{with_opencl}
Recommends:	gromacs-opencl = %{version}-%{release}
%endif
Obsoletes:	gromacs-mpich-libs < 2016-0.1.20160318gitbec9c87
BuildRequires:	mpich-devel

%description mpich
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

mdrun has been compiled with thread parallellization (for running on
a single node) and with MPICH (for running on multiple nodes).
This package single and double precision binaries and libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 %{?SOURCE2:-a 2} -n gromacs-%{version}%{?_rc}
install -Dpm644 %{SOURCE1} ./serial/docs/manual/gromacs.pdf
# Delete bundled stuff so that it doesn't get used accidentally
# Don't remove tinyxml2 as gromacs needs an old version to build
# test, see: https://redmine.gromacs.org/issues/2389
# googletest has modifications not in the packaged version
# clfft is not packaged
# Changes needed to CMakeLists to use packaged Boost stl_interfaces
rm -r src/external/{build-fftw,fftpack,lmfit,muparser,tng_io}

# increase timeout of tests
sed -i 's/set(_timeout [0-9]*)/set(_timeout 9000)/' src/testutils/TestMacros.cmake

%build
# Default options, used for all compilations
# note: Fedora's tinyxml2 is too new, so use the bundled one to build the test (only)
%global defopts \\\
 -DBUILD_TESTING:BOOL=ON \\\
 -DCMAKE_SKIP_INSTALL_RPATH=ON \\\
 -DGMX_BLAS_USER=%{blaslib} \\\
 -DGMX_BUILD_UNITTESTS:BOOL=ON \\\
 -DGMX_USE_LMFIT=EXTERNAL \\\
 -DGMX_EXTERNAL_TNG:BOOL=ON \\\
 -DGMX_EXTERNAL_TINYXML2:BOOL=OFF \\\
 -DGMX_USE_MUPARSER=EXTERNAL \\\
 -DGMX_LAPACK_USER=%{blaslib} \\\
 -DGMX_USE_RDTSCP=OFF \\\
 -DGMX_INSTALL_LEGACY_API=ON \\\
 -DGMX_VERSION_STRING_OF_FORK='Fedora%{fedora}' \\\
 -DGMX_SIMD=%{simd}

#HEFFTE only works with CUDA for now
%if %{with_opencl}
# OpenCL is available for single precision only
%global single -DGMX_GPU=OpenCL
%endif
%global double -DGMX_DOUBLE:BOOL=ON
%global mpi -DGMX_MPI:BOOL=ON -DGMX_THREAD_MPI:BOOL=OFF -DGMX_DEFAULT_SUFFIX:BOOL=OFF -DBUILD_SHARED_LIBS:BOOL=OFF -DGMX_USE_HEFFTE=OFF
%global _vpath_srcdir ..

. /etc/profile.d/modules.sh
for p in '' _d ; do
  for mpi in '' mpich openmpi ; do
    test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
    mkdir -p ${mpi:-serial}${p}
    pushd ${mpi:-serial}${p}
    test -z "${mpi}" && cp -al ../regressiontests* tests/ # use with -DREGRESSIONTEST_PATH=${PWD}/tests below
    %{cmake3} %{defopts} \
      $(test -n "${mpi}" && echo %{mpi} -DGMX_BINARY_SUFFIX=${MPI_SUFFIX}${p} -DGMX_LIBS_SUFFIX=${MPI_SUFFIX}${p} -DCMAKE_INSTALL_BINDIR=${MPI_BIN} -DCMAKE_INSTALL_LIBDIR=${MPI_LIB}) \
      $(test -z "${mpi}" && echo "-DREGRESSIONTEST_PATH=${PWD}/tests") \
      $(test -n "$p" && echo %{double} || echo %{?single})
    %cmake_build
    popd
    test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
  done
done

%install
. /etc/profile.d/modules.sh
for p in '' _d ; do
  for mpi in '' mpich openmpi ; do
    test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
    pushd ${mpi:-serial}${p}
    %cmake_install
    popd
    test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
  done
done

mkdir -p %{buildroot}%{_docdir}/gromacs
install -pm 644 AUTHORS COPYING README %{buildroot}%{_docdir}/gromacs
# Install manual & packager's note
install -cpm 644 serial/docs/manual/gromacs.pdf %{buildroot}%{_docdir}/gromacs/manual.pdf
install -cpm 644 %{SOURCE3} %{buildroot}%{_docdir}/gromacs/README.fedora

pushd %{buildroot}
# rm GMXRC, not needed when installed in /usr
rm ./%{_bindir}/GMXRC*

# serial stuff in mpi-versoin
rm ./%{_libdir}/*mpi*/bin/GMXRC* ./%{_libdir}/*mpi*/bin/*.pl

for bin in demux.pl xplor2gmx.pl; do
  mv ./%{_bindir}/$bin ./%{_bindir}/g_${bin}
done

# Move completion files around
mkdir -p ./%{compdir}
for bin in gmx{,_d}; do
  cat ./%{_bindir}/gmx-completion{,-$bin}.bash > ./%{compdir}/${bin}
  rm ./%{_bindir}/gmx-completion-${bin}.bash
done
rm ./%{_bindir}/gmx-completion.bash ./%{_libdir}/*mpi*/bin/gmx-completion*.bash

%ldconfig_scriptlets libs

%check
# exclude physicalvalidationtests (graomcs default) & regressiontests/complex (unstable)
%global testargs --exclude-regex '\(regressiontests/complex\|GmxAnaTest\)'
. /etc/profile.d/modules.sh
for p in '' _d ; do
  for mpi in '' mpich openmpi ; do
    test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
    pushd ${mpi:-serial}${p}
    [[ ${mpi} = openmpi ]] && export OMPI_MCA_rmaps_base_oversubscribe=1 PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
    %cmake_build --target tests
    %ctest %{?testargs}
    [[ ${mpi} = openmpi ]] && unset OMPI_MCA_rmaps_base_oversubscribe PRTE_MCA_rmaps_default_mapping_policy
    popd
    test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
  done
done

%files
%{_bindir}/gmx*
%{_bindir}/g_*

%files common
%{_docdir}/gromacs
%exclude %{_docdir}/gromacs/manual.pdf
%{compdir}/gmx*
%{_mandir}/man1/gmx*.1*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/template
%if %{with_opencl}
%exclude %{_datadir}/%{name}/opencl

%files opencl
%{_datadir}/%{name}/opencl
%endif

%files doc
%{_docdir}/gromacs/manual.pdf

%files libs
%{_libdir}/libgromacs*.so.*
%{_libdir}/libgmxapi*.so.*
%{_libdir}/libnblib*.so.*

%files devel
%{_includedir}/%{name}
%{_includedir}/gmxapi
%{_includedir}/nblib
%{_libdir}/libgromacs*.so
%{_libdir}/libgmxapi*.so
%{_libdir}/libnblib*.so
%{_libdir}/pkgconfig/libgromacs*.pc
%{_datadir}/%{name}/template
%{_datadir}/cmake/gromacs*
%{_datadir}/cmake/gmxapi*

%files openmpi
%{_libdir}/openmpi/bin/gmx_openmpi*

%files mpich
%{_libdir}/mpich/bin/gmx_mpich*

%changelog
%autochangelog
