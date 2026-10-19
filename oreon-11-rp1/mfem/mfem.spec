%global source0_hash ea3ac13e182c09f05b414b03a9bef7a4da99d45d67ee409112b8f11058447a7c
%bcond_without openmpi
%bcond_without mpich
%bcond check 1 0
%global forgeurl https://github.com/mfem/mfem
Version:        4.10
%global sover   %{version}.0
%forgemeta
Name:           mfem
Release:        1%{?dist}
Summary:        Lightweight, general, scalable C++ library for finite element methods
License:        BSD-3-Clause AND MIT AND BSL-1.0 AND BSD-2-Clause AND Zlib
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch: %{ix86}
Provides:       bundled(AmgXWrapper)
Provides:       bundled(catch2) = 2.13.9
Provides:       bundled(gecko)
Provides:       bundled(picojson)
Provides:       bundled(tinyxml2)
Provides:       bundled(zstr)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  hypre-mpich-devel
BuildRequires:  hypre-openmpi-devel
BuildRequires:  metis-devel
BuildRequires:  mpich-devel
BuildRequires:  ninja-build
BuildRequires:  openmpi-devel
# /oreon:deps
%description
MFEM is a modular parallel C++ library for finite element methods. Its goal is
to enable high-performance scalable finite element discretization research and
application development on a wide variety of platforms, ranging from laptops to
supercomputers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%if %{with openmpi}
%package        openmpi
Summary:        OpenMPI version of %{name}
BuildRequires:  openmpi-devel
BuildRequires:  hypre-openmpi-devel
Requires:       openmpi%{?_isa}
%description openmpi
This package contains the %{name} library compiled against OpenMPI.

%package        openmpi-devel
Summary:        Development files for OpenMPI version of %{name}
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:       openmpi-devel%{?_isa}
%description openmpi-devel
This package contains the %{name} development library compiled
against OpenMPI.
%endif

%if %{with mpich}
%package        mpich
Summary:        MPICH version of %{name}
BuildRequires:  mpich-devel
BuildRequires:  hypre-mpich-devel
Requires:       mpich%{?_isa}
%description mpich
This package contains the %{name} library compiled against MPICH.

%package        mpich-devel
Summary:        Development libraries for MPICH version of %{name}
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:       mpich-devel%{?_isa}
%description mpich-devel
This package contains the %{name} development library compiled
against MPICH.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

OPTIONS=(
    -GNinja \
    -DCMAKE_SKIP_BUILD_RPATH=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
%if %{with check}
    -DMFEM_ENABLE_TESTING=ON \
%else
    -DMFEM_ENABLE_TESTING=OFF \
%endif
    -DMFEM_ENABLE_EXAMPLES=OFF \
    -DMFEM_ENABLE_MINIAPPS=OFF \
    -DMFEM_ENABLE_GOOGLE_BENCHMARKS=OFF \
    -DCMAKE_VERBOSE_MAKEFILE=OFF \
)
%global _vpath_builddir %{_target_platform}
%cmake \
    ${OPTIONS[@]} \
    -DINSTALL_LIB_DIR=%{_libdir} \
    -DINSTALL_INCLUDE_DIR=%{_includedir}/mfem \
    -DINSTALL_CMAKE_DIR=%{_libdir}/cmake/mfem \
    -DMFEM_USE_MPI=OFF \
%cmake_build --target exec
%if %{with openmpi}
%{_openmpi_load}
%global _vpath_builddir %{_target_platform}-openmpi
%cmake \
    ${OPTIONS[@]} \
    -DHYPRE_INCLUDE_DIR=${MPI_INCLUDE}/hypre \
    -DHYPRE_LIBRARY=${MPI_LIB}/libHYPRE.so \
    -DINSTALL_LIB_DIR=${MPI_LIB} \
    -DINSTALL_INCLUDE_DIR=${MPI_INCLUDE}/mfem \
    -DINSTALL_CMAKE_DIR=${MPI_LIB}/cmake/mfem \
    -DMFEM_USE_MPI=ON \
%cmake_build --target exec
%{_openmpi_unload}
%endif
%if %{with mpich}
%{_mpich_load}
%global _vpath_builddir %{_target_platform}-mpich
%cmake \
    ${OPTIONS[@]} \
    -DHYPRE_INCLUDE_DIR=${MPI_INCLUDE}/hypre \
    -DHYPRE_LIBRARY=${MPI_LIB}/libHYPRE.so \
    -DINSTALL_LIB_DIR=${MPI_LIB} \
    -DINSTALL_INCLUDE_DIR=${MPI_INCLUDE}/mfem \
    -DINSTALL_CMAKE_DIR=${MPI_LIB}/cmake/mfem \
    -DMFEM_USE_MPI=ON \
%cmake_build --target exec
%{_mpich_unload}
%endif
%install
%global _vpath_builddir %{_target_platform}
%cmake_install
%if %{with openmpi}
%{_openmpi_load}
%global _vpath_builddir %{_target_platform}-openmpi
%cmake_install
%{_openmpi_unload}
%endif
%if %{with mpich}
%{_mpich_load}
%global _vpath_builddir %{_target_platform}-mpich
%cmake_install
%{_mpich_unload}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%if %{with check}
%check

%global _vpath_builddir %{_target_platform}
%ctest -E unit_tests
%if %{with openmpi}
%{_openmpi_load}
%global _vpath_builddir %{_target_platform}-openmpi
%ctest -E unit_tests
%{_openmpi_unload}
%endif
%if %{with mpich}
%{_mpich_load}
%global _vpath_builddir %{_target_platform}-mpich
%ifnarch s390x
%ctest -E unit_tests
%endif
%{_mpich_unload}
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n mfem-devel -f %{oreon_filedir}/mfem-devel.list
%files -n mfem-openmpi -f %{oreon_filedir}/mfem-openmpi.list
%files -n mfem-openmpi-devel -f %{oreon_filedir}/mfem-openmpi-devel.list
%files -n mfem-mpich -f %{oreon_filedir}/mfem-mpich.list
%files -n mfem-mpich-devel -f %{oreon_filedir}/mfem-mpich-devel.list

%changelog

%autochangelog
