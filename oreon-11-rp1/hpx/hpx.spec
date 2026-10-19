%global source0_hash 01ec47228a2253b41e318bb09c83325a75021eb6ef3262400fbda30ac7389279
Name:           hpx
Version:        1.11.0
Release:        1%{?dist}
Summary:        General Purpose C++ Runtime System
License:        BSL-1.0
URL:            https://hpx.stellar-group.org/
Source0:        https://github.com/STEllAR-GROUP/hpx/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         gcc-16.patch
ExcludeArch: s390x ppc64le
%global hpx_desc \
HPX is a general purpose C++ runtime system for parallel and distributed \
applications of any scale. \
\
The goal of HPX is to create a high quality, freely available, \
open source implementation of the ParalleX model for conventional systems, \
such as classic Linux based Beowulf clusters or multi-socket highly parallel \
SMP nodes. At the same time, we want to have a very modular and well designed \
runtime system architecture which would allow us to port our implementation \
onto new computer system architectures. We want to use real world applications\
to drive the development of the runtime system, coining out required \
functionality and converging onto a stable API which will provide a smooth \
migration path for developers. The API exposed by HPX is modeled after the \
interfaces defined by the C++11 ISO standard and adheres to the \
programming guidelines used by the Boost collection of C++ libraries.
# oreon:deps
BuildRequires:  asio-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gperftools-devel
BuildRequires:  hwloc-devel
BuildRequires:  libatomic
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
# /oreon:deps
%description
%{hpx_desc}

This package contains the libraries

%package examples
Summary: HPX examples
Requires:       hpx = %{version}-%{release}
%description examples
%{hpx_desc}

This package contains the examples

%package devel
Summary:    Development headers and libraries for hpx
Requires:   hpx = %{version}-%{release}
Requires:   asio-devel
Requires:   boost-devel
Requires:   hwloc-devel
Requires:   gperftools-devel
Requires:   gcc-c++
ExcludeArch: i686
%description devel
%{hpx_desc}

This package contains development headers and libraries

%package mpich
Summary:        HPX MPICH libraries
Requires:       mpich-devel
BuildRequires:  mpich-devel
%description mpich
%{hpx_desc}

This package contains the libraries

%package mpich-examples
Summary: HPX MPICH examples
Requires:       mpich
Requires:       hpx-mpich = %{version}-%{release}
BuildRequires:  mpich-devel
%description mpich-examples
%{hpx_desc}

This package contains the examples

%package mpich-devel
Summary:    Development headers and libraries for hpx
Requires:   hpx-mpich = %{version}-%{release}
Requires:   boost-devel
Requires:   hwloc-devel
Requires:   mpich-devel
Requires:   gperftools-devel
Requires:   asio-devel
%description mpich-devel
%{hpx_desc}.

This package contains development headers and libraries

%package openmpi
Summary:        HPX Open MPI libraries
Requires:       openmpi-devel
BuildRequires:  openmpi-devel
%description openmpi
%{hpx_desc}

This package contains the libraries

%package openmpi-examples
Summary: HPX Open MPI examples
Requires:       openmpi
Requires:       hpx-openmpi = %{version}-%{release}
BuildRequires:  openmpi-devel
BuildRequires: make
%description openmpi-examples
%{hpx_desc}.

This package contains the examples

%package openmpi-devel
Summary:    Development headers and libraries for hpx
Requires:   hpx-openmpi = %{version}-%{release}
Requires:   boost-devel
Requires:   hwloc-devel
Requires:   openmpi-devel
Requires:   gperftools-devel
Requires:   asio-devel
%description openmpi-devel
%{hpx_desc}

This package contains development headers and libraries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%define _lto_cflags %{nil}
%ifarch aarch64 
%define cmake_opts -DHPX_WITH_GENERIC_CONTEXT_COROUTINES=ON
%endif
%ifarch ppc64le aarch64 armv7hl
%global _smp_mflags -j1
%endif
%ifarch armv7hl
%define cmake_opts -DCMAKE_CXX_FLAGS="$RPM_OPT_FLAGS -O1" -DHPX_WITH_GENERIC_CONTEXT_COROUTINES=ON
%endif
%ifarch s390x
%define cmake_opts -DCMAKE_SHARED_LINKER_FLAGS="$RPM_OPT_FLAGS -latomic" -DCMAKE_EXE_LINKER_FLAGS="$RPM_OPT_FLAGS -latomic"
%endif
. /etc/profile.d/modules.sh
for mpi in '' openmpi mpich ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  mkdir -p ${mpi:-serial}
  %define _vpath_builddir %{_target_platform}-${mpi:-serial}
  test -n "${mpi}" && export CC=mpicc && export CXX=mpicxx
  %{cmake} ${mpi:+-DHPX_WITH_PARCELPORT_MPI=ON} %{?cmake_opts:%{cmake_opts}} -DHPX_WITH_BUILD_BINARY_PACKAGE=ON -DLIB_INSTALL_DIR=%_libdir/${mpi}/${mpi:+lib/} -DLIBDIR=%_libdir/${mpi}/${mpi:+lib/} -DCMAKE_INSTALL_LIBDIR=%_libdir/${mpi}/${mpi:+lib/}
  %cmake_build
  test -n "${mpi}" && unset CC CXX
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done
%install
. /etc/profile.d/modules.sh
for mpi in openmpi mpich '' ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch} && mkdir -p %{buildroot}/${MPI_BIN}
  %define _vpath_builddir %{_target_platform}-${mpi:-serial}
  %cmake_install
  pushd %{buildroot}/%{_bindir}
  for exe in  *; do
    test -n '${exe##hpx*}' && mv "${exe}" "hpx_${exe}"
  done
  popd
  test -n "${mpi}" && mv %{buildroot}/%{_bindir}/* %{buildroot}/${MPI_BIN}/            
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done
rm %{buildroot}/%{_datadir}/%{name}/LICENSE_1_0.txt
%fdupes %{buildroot}%{_prefix}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

. /etc/profile.d/modules.sh
for mpi in '' openmpi mpich ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %ctest --tests-regex tests.examples %{?testargs}
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n hpx-examples -f %{oreon_filedir}/hpx-examples.list
%files -n hpx-devel -f %{oreon_filedir}/hpx-devel.list
%files -n hpx-mpich -f %{oreon_filedir}/hpx-mpich.list
%files -n hpx-mpich-examples -f %{oreon_filedir}/hpx-mpich-examples.list
%files -n hpx-mpich-devel -f %{oreon_filedir}/hpx-mpich-devel.list
%files -n hpx-openmpi -f %{oreon_filedir}/hpx-openmpi.list
%files -n hpx-openmpi-examples -f %{oreon_filedir}/hpx-openmpi-examples.list
%files -n hpx-openmpi-devel -f %{oreon_filedir}/hpx-openmpi-devel.list

%changelog

%autochangelog
