%global source1_hash 07d5683d8435bf1ae6febbf0021203fd23570bbab9c56affe1dc0dcf023ac207
%global source0_hash 632a94201a042a2a9aa86803f50ee38b7bf0aa1cfef6ba0eb34ea4007f79a679
%global truename CombBLAS
%bcond_without openmpi
%bcond_without mpich
%bcond check 1
%bcond_with debug
%if %{with debug}
%global _lto_cflags %{nil}
%global debug_flags -VV --debug -j1
%else
%global debug_flags %{nil}
%endif
Name:          combblas
Version:       2.0.0
Release:        15%{?dist}
Summary:        The Combinatorial BLAS Library
License:       BSD-3-Clause-LBNL AND MIT AND BSL-1.0 AND GPL-2.0-or-later
URL:           https://people.eecs.berkeley.edu/~aydin/%{truename}/html/index.html
Source0:        https://github.com/PASSIONLab/%{truename}/archive/refs/tags/v%{version}/%{truename}-%{version}.tar.gz
Source1:       http://eecs.berkeley.edu/~aydin/%{truename}_FILES/testdata_%{name}1.6.1.tgz
Patch1: %{name}-sublibs_soname.patch
Patch2: %{name}-%{version}-removing_MPI_COMM_WORLD.patch
Patch3: 31.patch
%global desc \
The Combinatorial BLAS (CombBLAS) is an extensible distributed-memory parallel \
graph library offering a small but powerful set of linear algebra primitives \
specifically targeting graph analytics.
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
# /oreon:deps
%description
%desc

%if %{with openmpi}
%package openmpi
Summary:       The Combinatorial BLAS Library
Requires:      openmpi%{?_isa}
Provides:      Graph500-openmpi%{?_isa} = 1.2
Provides:      %{truename}-openmpi%{?_isa} = %version-%release
Provides:      %{truename}-openmpi = %version-%release
%description openmpi
%desc

%package openmpi-devel
Summary: Development files for %{name}-openmpi
BuildRequires: openmpi-devel
Requires: openmpi-devel%{?_isa}
Requires: %{name}-openmpi%{?_isa} = %version-%release
%description openmpi-devel
Development files for %{name}-openmpi
%endif

%if %{with mpich}
%package mpich
Summary:       The Combinatorial BLAS Library
BuildRequires: mpich-devel
BuildRequires: make
Requires:      mpich%{?_isa}
Provides:      Graph500-mpich%{?_isa} = 1.2
Provides:      %{truename}-mpich%{?_isa} = %version-%release
Provides:      %{truename}-mpich = %version-%release
%description mpich
%desc

%package mpich-devel
Summary: Development files for %{name}-mpich
Requires: mpich-devel%{?_isa}
Requires: %{name}-mpich%{?_isa} = %version-%release
%description mpich-devel
Development files for %{name}-mpich
%endif

%prep

%autosetup -a 1 -n %{truename}-%{version} -p 1

cp --no-preserve=mode,ownership usort/LICENSE usort/usort-LICENSE
cp --no-preserve=mode,ownership graph500-1.2/COPYING graph500-1.2/graph500-1.2-COPYING
cp --no-preserve=mode,ownership graph500-1.2/generator/LICENSE_1_0.txt graph500-1.2/generator/graph500-1.2-generator-LICENSE_1_0.txt

# Fix permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.*pp" -exec chmod 0644 '{}' \;
find . -type f -name "*.tcc" -exec chmod 0644 '{}' \;

%build

%if %{with openmpi}
%{_openmpi_load}
mkdir -p build/openmpi
%define _vpath_builddir build/openmpi
export LDFLAGS="%{__global_ldflags} -lm -lrt"
%cmake \
 -DCMAKE_INSTALL_PREFIX:PATH=${MPI_HOME} \
 -DCMAKE_INSTALL_LIBDIR:PATH=lib \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=${MPI_INCLUDE} \
 -DMPIEXEC_NUMPROC_FLAG=-n -DMPIEXEC_MAX_NUMPROCS:STRING="`/usr/bin/getconf _NPROCESSORS_ONLN`" \
%if %{with debug}
 -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
 -DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="-O0 -g -DDEBUG" -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="-O0 -g -DDEBUG" \
 -DCMAKE_C_FLAGS_DEBUG:STRING="-O0 -g -DDEBUG" -DCMAKE_CXX_FLAGS_DEBUG:STRING="-O0 -g -DDEBUG" \
 -DCMAKE_C_FLAGS_RELEASE:STRING=" " -DCMAKE_CXX_FLAGS_RELEASE:STRING=" "
%else
 -DCMAKE_BUILD_TYPE:STRING=Release
%endif
%cmake_build
%{_openmpi_unload}
%endif
%if %{with mpich}
%{_mpich_load}
mkdir -p build/mpich
%define _vpath_builddir build/mpich
export LDFLAGS="%{__global_ldflags} -lm -lrt"
%cmake \
 -DCMAKE_INSTALL_PREFIX:PATH=${MPI_HOME} \
 -DCMAKE_INSTALL_LIBDIR:PATH=lib \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=${MPI_INCLUDE} \
 -DMPIEXEC_NUMPROC_FLAG=-n -DMPIEXEC_MAX_NUMPROCS:STRING="`/usr/bin/getconf _NPROCESSORS_ONLN`" \
%if %{with debug}
 -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
 -DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="-O0 -g -DDEBUG" -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="-O0 -g -DDEBUG" \
 -DCMAKE_C_FLAGS_RELEASE:STRING=" " -DCMAKE_CXX_FLAGS_RELEASE:STRING=" "
%else
 -DCMAKE_BUILD_TYPE:STRING=Release
%endif
%cmake_build
%{_mpich_unload}
%endif
%install
%if %{with openmpi}
%{_openmpi_load}
%define _vpath_builddir build/openmpi
%cmake_install
chrpath -r $MPI_LIB %{buildroot}$MPI_LIB/libCombBLAS.so.*
%{_openmpi_unload}
%endif
%if %{with mpich}
%{_mpich_load}
%define _vpath_builddir build/mpich
%cmake_install
chrpath -r $MPI_LIB %{buildroot}$MPI_LIB/libCombBLAS.so.*
%{_mpich_unload}
%endif
find %{buildroot} -type f -name "*.DS_Store" -exec rm -rf '{}' \;
find %{buildroot} -type f -name "._CombBLAS.h" -exec rm -f '{}' \;
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%if %{with openmpi}
%{_openmpi_load}
cp -a TESTDATA build/openmpi/
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$MPI_LIB
%define _vpath_builddir build/openmpi
%ctest %{debug_flags} -E 'Indexing_Test|SpAsgn_Test|FBFS_Test|FMIS_Test|BPMM_Test'
%{_openmpi_unload}
%endif
%if %{with mpich}
%{_mpich_load}
cp -a TESTDATA build/mpich/
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$MPI_LIB
%define _vpath_builddir build/mpich
%ctest %{debug_flags} -E 'Indexing_Test|SpAsgn_Test|FBFS_Test|FMIS_Test|BPMM_Test'
%{_mpich_unload}
%endif
%endif
%if %{with openmpi}
%files -f %{oreon_filedir}/main.list
%files -n combblas-openmpi -f %{oreon_filedir}/combblas-openmpi.list
%files -n combblas-openmpi-devel -f %{oreon_filedir}/combblas-openmpi-devel.list
%files -n combblas-mpich -f %{oreon_filedir}/combblas-mpich.list
%files -n combblas-mpich-devel -f %{oreon_filedir}/combblas-mpich-devel.list

%changelog

%autochangelog
%endif
