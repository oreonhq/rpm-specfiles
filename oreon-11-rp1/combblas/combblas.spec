%global source0_hash none

%global truename CombBLAS

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif
%bcond_without mpich

# Tests are performed really slowly with current version of OpenMPI (4.1.5)
%bcond check 1

# CTest flags for debugging only
%bcond_with debug
%if %{with debug}
%global _lto_cflags %{nil}
%global debug_flags -VV --debug -j1
%else
%global debug_flags %{nil}
%endif

Name:          combblas
Version:       2.0.0
Release:       15%{?dist}
Summary:       The Combinatorial BLAS Library

# Main license for CombBLAS is BSD-3-Clause-LBNL
# graph500-1.2/ under BSD license
# graph500-1.2/generator/ under Boost license
# include/Tommy/ under BSD license
# include/CombBLAS/ under MIT or Expat license
# psort-1.0/include/ under a mixed GPLv2+/MIT/BSD licenses
# usort/ under MIT or Expat license
License:       BSD-3-Clause-LBNL AND MIT AND BSL-1.0 AND GPL-2.0-or-later
URL:           https://people.eecs.berkeley.edu/~aydin/%{truename}/html/index.html
Source0:       https://github.com/PASSIONLab/%{truename}/archive/refs/tags/v%{version}/%{truename}-%{version}.tar.gz
Source1:       http://eecs.berkeley.edu/~aydin/%{truename}_FILES/testdata_%{name}1.6.1.tgz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: chrpath

# Use a versioned soname for all libraries
Patch1: %{name}-sublibs_soname.patch

# https://github.com/PASSIONLab/CombBLAS/commit/ecf96214a0c666662954cf24b84df97f61d52dc9
Patch2: %{name}-%{version}-removing_MPI_COMM_WORLD.patch

# CMake 4.0 support
# Cherry-picked from https://github.com/PASSIONLab/CombBLAS/pull/31
Patch3: 31.patch

%global desc \
The Combinatorial BLAS (CombBLAS) is an extensible distributed-memory parallel \
graph library offering a small but powerful set of linear algebra primitives \
specifically targeting graph analytics.

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

###

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

# Remove DS_Store directories and hidden files
find %{buildroot} -type f -name "*.DS_Store" -exec rm -rf '{}' \;
find %{buildroot} -type f -name "._CombBLAS.h" -exec rm -f '{}' \;

%if %{with check}
%check
# Both failed tests have been reported to upstream:
# https://bitbucket.org/berkeleylab/combinatorial-blas-2.0/issues/3/indexing_test-failed
# https://bitbucket.org/berkeleylab/combinatorial-blas-2.0/issues/4/spasgn_test-failed
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
%files openmpi
%doc README_DEVELOPERS graph500-1.2/Graph500.html graph500-1.2/Graph500.org
%license LICENSE usort/usort-LICENSE graph500-1.2/graph500-1.2-COPYING graph500-1.2/generator/graph500-1.2-generator-LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libCombBLAS.so.2.0.0
%{_libdir}/openmpi/lib/libGraphGenlib.so.1.2
%{_libdir}/openmpi/lib/libUsortlib.so.2.0.0

%files openmpi-devel
%{_libdir}/openmpi/lib/libCombBLAS.so
%{_libdir}/openmpi/lib/libGraphGenlib.so
%{_libdir}/openmpi/lib/libUsortlib.so
%{_libdir}/openmpi/lib/cmake/%{truename}/
%{_includedir}/openmpi-%{_arch}/psort/
%{_includedir}/openmpi-%{_arch}/usort/
%{_includedir}/openmpi-%{_arch}/Tommy/
%{_includedir}/openmpi-%{_arch}/graph500/
%{_includedir}/openmpi-%{_arch}/%{truename}/
%endif

%if %{with mpich}
%files mpich
%doc README_DEVELOPERS graph500-1.2/Graph500.html graph500-1.2/Graph500.org
%license LICENSE usort/usort-LICENSE graph500-1.2/graph500-1.2-COPYING graph500-1.2/generator/graph500-1.2-generator-LICENSE_1_0.txt
%{_libdir}/mpich/lib/libCombBLAS.so.2.0.0
%{_libdir}/mpich/lib/libGraphGenlib.so.1.2
%{_libdir}/mpich/lib/libUsortlib.so.2.0.0

%files mpich-devel
%{_libdir}/mpich/lib/libCombBLAS.so
%{_libdir}/mpich/lib/libGraphGenlib.so
%{_libdir}/mpich/lib/libUsortlib.so
%{_libdir}/mpich/lib/cmake/%{truename}/
%{_includedir}/mpich-%{_arch}/psort/
%{_includedir}/mpich-%{_arch}/usort/
%{_includedir}/mpich-%{_arch}/Tommy/
%{_includedir}/mpich-%{_arch}/graph500/
%{_includedir}/mpich-%{_arch}/%{truename}/
%endif

%changelog
%autochangelog
