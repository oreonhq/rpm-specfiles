%global source0_hash 728b522b3bb05580c26e374bfae2a262bf8007b3b2c7d4c9480e4363953270c7
%bcond_without openmpi
%bcond mpich %[!(0%{?rhel} >= 10)]
Summary:        Intel MPI benchmarks
Name:    intel-mpi-benchmarks
Version: 2021.11
Release:        1%{?dist}
License: BSD-3-Clause
URL:     https://software.intel.com/en-us/articles/intel-mpi-benchmarks
Source0:        https://github.com/intel/mpi-benchmarks/archive/IMB-v%{version}.tar.gz
ExcludeArch: %{ix86}
%global desc The Intel MPI Benchmarks perform a set of MPI performance measurements for\
point-to-point and global communication operations for a range of message\
sizes. The generated benchmark data fully characterizes:\
 - Performance of a cluster system, including node performance, network\
   latency, and throughput\
 - Efficiency of the MPI implementation used
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
# /oreon:deps
%description
%{desc}

%package license
Summary: License of Intel MPI benchmarks
BuildArch: noarch
%description license
This package contains the license of Intel MPI benchmarks.

%if %{with openmpi}
%package openmpi
Summary: Intel MPI benchmarks compiled against openmpi
BuildRequires: openmpi-devel
Requires: openmpi
Requires: %{name}-license = %{version}-%{release}
Obsoletes: mpitests-openmpi < 7.4
%description openmpi
%{desc}

This package was built against the Open MPI implementation of MPI.
%endif

%if %{with mpich}
%package mpich
Summary: Intel MPI benchmarks compiled against mpich
BuildRequires: mpich-devel
Requires: mpich
Requires: %{name}-license = %{version}-%{release}
Obsoletes: mpitests-mpich < 7.4
%description mpich
%{desc}

This package was built against the MPICH implementation of MPI.
%endif

%patchlist
0001-fix-compiler-warnings-for-gcc.patch
0002-remove-Werror-flag.patch
0003-do-not-override-optimization-flags.patch

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mpi-benchmarks-IMB-v%{version}
%oreon_prep
%build

do_build() {
  mkdir .$MPI_COMPILER
  cp -al * .$MPI_COMPILER
  mv .$MPI_COMPILER build-$MPI_COMPILER
  cd build-$MPI_COMPILER
  export CC=mpicc
  export CXX=mpicxx
  make -f Makefile OPTFLAGS="%{optflags}" MPI_HOME="$MPI_HOME" all
  cd ..
}
%if %{with openmpi}
%{_openmpi_load}
do_build
%{_openmpi_unload}
%endif
%if %{with mpich}
%{_mpich_load}
do_build
%{_mpich_unload}
%endif
%install
do_install() {
  mkdir -p %{buildroot}$MPI_BIN
  cd build-$MPI_COMPILER
  for f in IMB-*; do
    cp "$f" "%{buildroot}$MPI_BIN/"
  done
  cd ..
}
%if %{with openmpi}
%{_openmpi_load}
do_install
%{_openmpi_unload}
%endif
%if %{with mpich}
%{_mpich_load}
do_install
%{_mpich_unload}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n intel-mpi-benchmarks-license -f %{oreon_filedir}/intel-mpi-benchmarks-license.list
%files -n intel-mpi-benchmarks-openmpi -f %{oreon_filedir}/intel-mpi-benchmarks-openmpi.list
%files -n intel-mpi-benchmarks-mpich -f %{oreon_filedir}/intel-mpi-benchmarks-mpich.list

%changelog

%autochangelog
