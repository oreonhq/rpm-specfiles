%global source0_hash 95075e1fd0b51d97b1b96b73ebe03b1a551fbcc9cd2b2b6f487ccccedcff5964
%ifarch %{ix86}
%bcond openmpi 0
%else
%bcond openmpi %{undefined flatpak}
%endif
%bcond mpich %{undefined flatpak}
Name:           cgnslib
Version:        4.5.2
Release:        1%{?dist}
Summary:        Computational Fluid Dynamics General Notation System
License:        Zlib
URL:            http://www.cgns.org/
Source0:        https://github.com/CGNS/CGNS/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         cgnslib-cmake-install-dirs.patch
Patch1:         cgnslib_desktop.patch
Patch2:         cgnslib-c99.patch
Patch3:         cgnslib-i686.patch
Requires:       hdf5%{?_isa} = %{_hdf5_version}
Requires:       %{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  hdf5-devel
BuildRequires:  hdf5-mpich-devel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Computational Fluid Dynamics General Notation System (CGNS) provides a
general, portable, and extensible standard for the storage and retrieval of
computational fluid dynamics (CFD) analysisdata. It consists of a collection
of conventions, and free and open software implementing those conventions. It
is self-descriptive, machine-independent, well-documented, and administered by
an international steering committee.

%package common
Summary:        Common files for %{name}
BuildArch:      noarch
%description common
Common files for %{name}.

%package libs
Summary:       %{name} library
%description libs
%{name} library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hdf5-devel%{?_isa}
Requires:       gcc-gfortran%{?_isa}
%description    devel
This package contains libraries and header files for
developing applications that use %{name} libraries.

###############################################################################

%if %{with openmpi}
%package        openmpi
Summary:        %{name} compiled against openmpi
Requires:       %{name}-common = %{version}-%{release}
BuildRequires:  openmpi-devel
BuildRequires:  hdf5-openmpi-devel
%description    openmpi
%{name} compiled against openmpi.

%package openmpi-libs
Summary:       %{name} library
%description openmpi-libs
%{name} library.

%package        openmpi-devel
Summary:        Development files for %{name} compiled against openmpi
Requires:       openmpi-devel
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
%description    openmpi-devel
Development files for %{name} compiled against openmpi.
%endif

###############################################################################

%if %{with mpich}
%package        mpich
Summary:        %{name} compiled against mpich
Requires:       %{name}-common = %{version}-%{release}
BuildRequires:  mpich-devel
BuildRequires:  hdf5-mpich-devel
%description    mpich
%{name} compiled against mpich.

%package mpich-libs
Summary:       %{name} library
%description mpich-libs
%{name} library.

%package        mpich-devel
Summary:        Development files for %{name} compiled against mpich
Requires:       mpich-devel
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
%description    mpich-devel
Development files for %{name} compiled against mpich.
%endif

###############################################################################

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n CGNS-%{version}

# Remove executable bit
chmod a-x src/cgnstools/utilities/cgns_to_vtk.c

%build

cgnslib_cmake_args="\
        -DCGNS_ENABLE_SCOPING=ON \
        -DCMAKE_SKIP_RPATH=ON \
        -DCGNS_ENABLE_TESTS=OFF \
        -DCGNS_ENABLE_FORTRAN=ON \
        -DCGNS_BUILD_CGNSTOOLS=ON \
        -DCGNS_ENABLE_HDF5=ON"
%define _vpath_builddir %{_target_platform}
%cmake \
    -DBIN_INSTALL_DIR=%{_bindir} \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DINCLUDE_INSTALL_DIR=%{_includedir} \
    $cgnslib_cmake_args
%cmake_build
%if %{with openmpi}
(
%{_openmpi_load}
%define _vpath_builddir %{_target_platform}-openmpi
export CXX=mpicxx
export FC=mpifort
%cmake \
    -DHDF5_NEED_MPI=ON -DCGNS_ENABLE_PARALLEL=ON \
    -DBIN_INSTALL_DIR=$MPI_BIN \
    -DLIB_INSTALL_DIR=$MPI_LIB \
    -DINCLUDE_INSTALL_DIR=$MPI_INCLUDE \
    -DCMAKE_Fortran_FLAGS_RELEASE="%{optflags} -I $MPI_FORTRAN_MOD_DIR" \
    $cgnslib_cmake_args
%cmake_build
%{_openmpi_unload}
)
%endif
%if %{with mpich}
(
%{_mpich_load}
%define _vpath_builddir %{_target_platform}-mpich
export CXX=mpicxx
export FC=mpifort
%cmake \
    -DHDF5_NEED_MPI=ON -DCGNS_ENABLE_PARALLEL=ON \
    -DBIN_INSTALL_DIR=$MPI_BIN \
    -DLIB_INSTALL_DIR=$MPI_LIB \
    -DINCLUDE_INSTALL_DIR=$MPI_INCLUDE \
    -DCMAKE_Fortran_FLAGS_RELEASE="%{optflags} -I $MPI_FORTRAN_MOD_DIR" \
    $cgnslib_cmake_args
%cmake_build
%{_mpich_unload}
)
%endif
%install
%if %{with openmpi}
(
%{_openmpi_load}
%define _vpath_builddir %{_target_platform}-openmpi
%cmake_install
mkdir -p %{buildroot}$MPI_FORTRAN_MOD_DIR
mv %{buildroot}$MPI_INCLUDE/cgns.mod %{buildroot}$MPI_FORTRAN_MOD_DIR
rm -f %{buildroot}$MPI_BIN/*.desktop
%{_openmpi_unload}
)
%endif
%if %{with mpich}
(
%{_mpich_load}
%define _vpath_builddir %{_target_platform}-mpich
%cmake_install
mkdir -p %{buildroot}$MPI_FORTRAN_MOD_DIR
mv %{buildroot}$MPI_INCLUDE/cgns.mod %{buildroot}$MPI_FORTRAN_MOD_DIR
rm -f %{buildroot}$MPI_BIN/*.desktop
%{_mpich_unload}
)
%endif
%define _vpath_builddir %{_target_platform}
%cmake_install
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/cgns.mod %{buildroot}%{_libdir}/gfortran/modules
mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_bindir}/*.desktop %{buildroot}%{_datadir}/applications
find %{buildroot} -name '*.a' -delete -print
%oreon_autofiles cgnslib-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cgnslib-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cgnslib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cgnslib-openmpi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cgnslib-openmpi-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cgnslib-openmpi-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cgnslib-mpich usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cgnslib-mpich-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cgnslib-mpich-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

(
%define _vpath_builddir %{_target_platform}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
%ctest || :
)
%if %{with openmpi}
(
%{_openmpi_load}
%define _vpath_builddir %{_target_platform}-openmpi
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$LD_LIBRARY_PATH
ctest || :
%{_mpich_unload}
)
%endif
%if %{with mpich}
(
%{_mpich_load}
%define _vpath_builddir %{_target_platform}-mpich
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$LD_LIBRARY_PATH
ctest || :
%{_mpich_unload}
)
%endif
%files -f %{oreon_filedir}/main.list
%files -n cgnslib-common -f %{oreon_filedir}/cgnslib-common.list
%files -n cgnslib-libs -f %{oreon_filedir}/cgnslib-libs.list
%files -n cgnslib-devel -f %{oreon_filedir}/cgnslib-devel.list
%files -n cgnslib-openmpi -f %{oreon_filedir}/cgnslib-openmpi.list
%files -n cgnslib-openmpi-libs -f %{oreon_filedir}/cgnslib-openmpi-libs.list
%files -n cgnslib-openmpi-devel -f %{oreon_filedir}/cgnslib-openmpi-devel.list
%files -n cgnslib-mpich -f %{oreon_filedir}/cgnslib-mpich.list
%files -n cgnslib-mpich-libs -f %{oreon_filedir}/cgnslib-mpich-libs.list
%files -n cgnslib-mpich-devel -f %{oreon_filedir}/cgnslib-mpich-devel.list

%changelog

%autochangelog
