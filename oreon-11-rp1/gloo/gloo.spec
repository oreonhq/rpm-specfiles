%global source0_hash 74da6d9089941c7abc21aeced3c551216cdf3b1f04155d4dd80e3e84886ebacf
%global commit0 dc507d1eb822c4396aaca284efff498aba33c7dc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20241203
%global mpi_list openmpi mpich
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${mpi:-serial}
Summary:        Communications library for AI/ML
Name:           gloo
License:        BSD-3-Clause
Version:        0.5.0^git%{date0}.%{shortcommit0}
Release:        1%{?dist}
URL:            https://github.com/facebookincubator/%{name}
Source0:        https://github.com/facebookincubator/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         0001-gloo-fedora-cmake-changes.patch
Patch1:         0002-gloo-fedora-cmake-libuv.patch
Patch2:         0001-gloo-gcc-15-cstdint.patch
ExcludeArch:    i686
Requires:       %{name}-docs
%global base_description \
Gloo is a collective communications library. It comes with a number of\
collective algorithms useful for machine learning applications. These\
include a barrier, broadcast, and allreduce.\
\
Transport of data between participating machines is abstracted so that\
IP can be used at all times, or InifiniBand (or RoCE) when available.\
In the latter case, if the InfiniBand transport is used, GPUDirect can\
be used to accelerate cross machine GPU-to-GPU memory transfers.\
\
Where applicable, algorithms have an implementation that works with\
system memory buffers, and one that works with NVIDIA GPU memory buffers.\
In the latter case, it is not necessary to copy memory between host and\
device; this is taken care of by the algorithm implementations.
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hiredis-devel
BuildRequires:  libibverbs
BuildRequires:  libuv-devel
BuildRequires:  libuv-static
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  rdma-core-devel
BuildRequires:  redis-devel
# /oreon:deps
%description
%{base_description}

%package docs
Summary: Documentation and license for %{name}
Buildarch: noarch
%description docs
Documentation only package used by other packages for
%{name}.

%package devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Libraries and headers for developing applications that
use %{name}.

%package openmpi
Summary: Gloo - openmpi version
BuildRequires:  openmpi-devel
Requires: %{name}-docs
%description openmpi
%{base_description}

This package can use openmpi as a backend.

%package openmpi-devel
Summary:   Development libraries and headers
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel
Libraries and header files for developing applications
that use %{name}-openmpi.

%package mpich
Summary: Gloo - mpich version
BuildRequires:  mpich-devel
Requires: %{name}-docs
%description mpich
%{base_description}

This package can use mpich as a backend.

%package mpich-devel
Summary: Development libraries and headers
BuildRequires:  mpich-devel
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel
Libraries and header files for developing applications
that use %{name}-mpich.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

# cmake version change
sed -i -e 's@cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)@cmake_minimum_required(VERSION 3.5 FATAL_ERROR)@' CMakeLists.txt

%build

%define gloo_cmake_options -DUSE_IBVERBS=ON -DUSE_LIBUV=OFF -DUSE_REDIS=ON
%cmake %gloo_cmake_options \
       -DUSE_MPI=OFF \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR=lib64
%cmake_build
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake %gloo_cmake_options \
         -DUSE_MPI=ON \
         -DCMAKE_INSTALL_PREFIX=$MPI_HOME \
	 -DCMAKE_INSTALL_LIBDIR=lib
   %cmake_build
   module purge
done
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/Gloo/docs
cp -p -r docs/* %{buildroot}%{_datadir}/Gloo/docs
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake_install
  module purge
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gloo-docs -f %{oreon_filedir}/gloo-docs.list
%files -n gloo-devel -f %{oreon_filedir}/gloo-devel.list
%files -n gloo-openmpi -f %{oreon_filedir}/gloo-openmpi.list
%files -n gloo-openmpi-devel -f %{oreon_filedir}/gloo-openmpi-devel.list
%files -n gloo-mpich -f %{oreon_filedir}/gloo-mpich.list
%files -n gloo-mpich-devel -f %{oreon_filedir}/gloo-mpich-devel.list

%changelog

%autochangelog
