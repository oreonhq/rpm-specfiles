%global source0_hash ae63b0098764803dd42b7b2a6487cbfb3c0ae7b22eb01a2570dbce49316ad279
%ifarch %{ix86}
%bcond openmpi 0
%else
%bcond openmpi %{undefined flatpak}
%endif
%bcond mpich %{undefined flatpak}

Name:           cgnslib
Version:        4.5.1
Release:        3%{?dist}
Summary:        Computational Fluid Dynamics General Notation System
License:        Zlib
URL:            http://www.cgns.org/
Source0:        https://github.com/CGNS/CGNS/archive/v%{version}/%{name}-%{version}.tar.gz
# Allow overriding all BIN/LIB/INCLUDE install dirs
Patch0:         cgnslib-cmake-install-dirs.patch
# Fix invalid Icon and Exec paths in desktop files
Patch1:         cgnslib_desktop.patch
Patch2:         cgnslib-c99.patch
Patch3:         cgnslib-i686.patch
# Allow building with Ninja generator
Patch4:         https://github.com/CGNS/CGNS/pull/845.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  hdf5-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  tcl-devel < 1:9
BuildRequires:  tk-devel < 1:9
BuildRequires:  zlib-devel
Requires:       hdf5%{?_isa} = %{_hdf5_version}
Requires:       %{name}-common = %{version}-%{release}

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
# Require explicitly for dir ownership
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
# Require explicitly for dir ownership
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
# This is needed for GCC10, whenever a new cgnslib release is published, check whether it is still needed
# export FCFLAGS+=-fallow-argument-mismatch
cgnslib_cmake_args="\
        -DCGNS_ENABLE_SCOPING=ON \
        -DCMAKE_SKIP_RPATH=ON \
        -DCGNS_ENABLE_TESTS=ON \
        -DCGNS_ENABLE_FORTRAN=ON \
        -DCGNS_BUILD_CGNSTOOLS=ON \
        -DCGNS_ENABLE_HDF5=ON"
#        -DCMAKE_Fortran_FLAGS_RELEASE:STRING='$FCFLAGS -DNDEBUG $LDFLAGS -lhdf5 -fPIC'"

### Serial version ###
%define _vpath_builddir %{_target_platform}
%cmake \
    -DBIN_INSTALL_DIR=%{_bindir} \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DINCLUDE_INSTALL_DIR=%{_includedir} \
    $cgnslib_cmake_args
%cmake_build

### openmpi version ###
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

### mpich version ###
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
### openmpi version ###
%if %{with openmpi}
(
%{_openmpi_load}
%define _vpath_builddir %{_target_platform}-openmpi
%cmake_install

# Move fortran module to correct location
mkdir -p %{buildroot}$MPI_FORTRAN_MOD_DIR
mv %{buildroot}$MPI_INCLUDE/cgns.mod %{buildroot}$MPI_FORTRAN_MOD_DIR

# Drop desktop files
rm -f %{buildroot}$MPI_BIN/*.desktop
%{_openmpi_unload}
)
%endif

### mpich version ###
%if %{with mpich}
(
%{_mpich_load}
%define _vpath_builddir %{_target_platform}-mpich
%cmake_install

# Move fortran module to correct location
mkdir -p %{buildroot}$MPI_FORTRAN_MOD_DIR
mv %{buildroot}$MPI_INCLUDE/cgns.mod %{buildroot}$MPI_FORTRAN_MOD_DIR

# Drop desktop files
rm -f %{buildroot}$MPI_BIN/*.desktop
%{_mpich_unload}
)
%endif

### Serial version ###
%define _vpath_builddir %{_target_platform}
%cmake_install

# Move fortran module to correct location
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/cgns.mod %{buildroot}%{_libdir}/gfortran/modules

# Move desktop files to correct location
mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_bindir}/*.desktop %{buildroot}%{_datadir}/applications

find %{buildroot} -name '*.a' -delete -print

%check
### Serial version ###
(
%define _vpath_builddir %{_target_platform}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
%ctest || :
)

### openmpi version ###
%if %{with openmpi}
(
%{_openmpi_load}
%define _vpath_builddir %{_target_platform}-openmpi
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$LD_LIBRARY_PATH
ctest || :
%{_mpich_unload}
)
%endif

### mpich version ###
%if %{with mpich}
(
%{_mpich_load}
%define _vpath_builddir %{_target_platform}-mpich
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$LD_LIBRARY_PATH
ctest || :
%{_mpich_unload}
)
%endif

%files
%{_bindir}/adf2hdf
%{_bindir}/cgconfig
%{_bindir}/cgnscalc
%{_bindir}/cgnscheck
%{_bindir}/cgnscompress
%{_bindir}/cgnsconvert
%{_bindir}/cgnsdiff
%{_bindir}/cgnslist
%{_bindir}/cgnsplot
%{_bindir}/cgnsnodes
%{_bindir}/cgnsnames
%{_bindir}/cgnstools/
%{_bindir}/cgnsupdate
%{_bindir}/cgnsview
%{_bindir}/hdf2adf
%{_bindir}/unitconv

%files libs
%{_libdir}/libcgns.so.4.5

%files devel
%{_includedir}/cgnsBuild.defs
%{_includedir}/cgns_io.h
%{_includedir}/cgnslib.h
%{_includedir}/cgnstypes.h
%{_includedir}/cgnstypes_f.h
%{_includedir}/cgnstypes_f03.h
%{_includedir}/cgnswin_f.h
%{_includedir}/cgnsconfig.h
%{_libdir}/libcgns.so
%{_libdir}/cmake/cgns/
%{_fmoddir}/cgns.mod

%files common
%doc release_docs/RELEASE.md README.md
%license license.txt
%{_datadir}/cgnstools/
%{_datadir}/applications/cgnscalc.desktop
%{_datadir}/applications/cgnsnodes.desktop
%{_datadir}/applications/cgnsplot.desktop
%{_datadir}/applications/cgnsview.desktop
%{_datadir}/applications/unitconv.desktop

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/adf2hdf
%{_libdir}/openmpi/bin/cgconfig
%{_libdir}/openmpi/bin/cgnscalc
%{_libdir}/openmpi/bin/cgnscheck
%{_libdir}/openmpi/bin/cgnscompress
%{_libdir}/openmpi/bin/cgnsconvert
%{_libdir}/openmpi/bin/cgnsdiff
%{_libdir}/openmpi/bin/cgnslist
%{_libdir}/openmpi/bin/cgnsplot
%{_libdir}/openmpi/bin/cgnsnodes
%{_libdir}/openmpi/bin/cgnsnames
%{_libdir}/openmpi/bin/cgnstools/
%{_libdir}/openmpi/bin/cgnsupdate
%{_libdir}/openmpi/bin/cgnsview
%{_libdir}/openmpi/bin/hdf2adf
%{_libdir}/openmpi/bin/unitconv

%files openmpi-libs
%{_libdir}/openmpi/lib/libcgns.so.4.5

%files openmpi-devel
%{_includedir}/openmpi*/cgnsBuild.defs
%{_includedir}/openmpi*/cgns_io.h
%{_includedir}/openmpi*/cgnslib.h
%{_includedir}/openmpi*/cgnstypes.h
%{_includedir}/openmpi*/cgnstypes_f.h
%{_includedir}/openmpi*/cgnstypes_f03.h
%{_includedir}/openmpi*/cgnswin_f.h
%{_includedir}/openmpi*/cgnsconfig.h
%{_includedir}/openmpi*/pcgnslib.h
%{_libdir}/openmpi/lib/libcgns.so
%{_libdir}/openmpi/lib/cmake/cgns/
%{_fmoddir}/openmpi/cgns.mod
%endif

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/adf2hdf
%{_libdir}/mpich/bin/cgconfig
%{_libdir}/mpich/bin/cgnscalc
%{_libdir}/mpich/bin/cgnscheck
%{_libdir}/mpich/bin/cgnscompress
%{_libdir}/mpich/bin/cgnsconvert
%{_libdir}/mpich/bin/cgnsdiff
%{_libdir}/mpich/bin/cgnslist
%{_libdir}/mpich/bin/cgnsplot
%{_libdir}/mpich/bin/cgnsnodes
%{_libdir}/mpich/bin/cgnsnames
%{_libdir}/mpich/bin/cgnstools/
%{_libdir}/mpich/bin/cgnsupdate
%{_libdir}/mpich/bin/cgnsview
%{_libdir}/mpich/bin/hdf2adf
%{_libdir}/mpich/bin/unitconv

%files mpich-libs
%{_libdir}/mpich/lib/libcgns.so.4.5

%files mpich-devel
%{_includedir}/mpich*/cgnsBuild.defs
%{_includedir}/mpich*/cgns_io.h
%{_includedir}/mpich*/cgnslib.h
%{_includedir}/mpich*/cgnstypes.h
%{_includedir}/mpich*/cgnstypes_f.h
%{_includedir}/mpich*/cgnstypes_f03.h
%{_includedir}/mpich*/cgnswin_f.h
%{_includedir}/mpich*/cgnsconfig.h
%{_includedir}/mpich*/pcgnslib.h
%{_libdir}/mpich/lib/libcgns.so
%{_libdir}/mpich/lib/cmake/cgns/
%{_fmoddir}/mpich/cgns.mod
%endif

%changelog
%autochangelog
