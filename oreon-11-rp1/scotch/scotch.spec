%bcond mpich %{undefined flatpak}
%if 0%{?fedora} >= 40 || 0%{?oreon}
%ifarch %{ix86}
%bcond openmpi 0
%else
%bcond openmpi %{undefined flatpak}
%endif
%else
%bcond openmpi %{undefined flatpak}
%endif
%bcond metis 1

# This flag prevents internal links
%undefine _ld_as_needed

Name:          scotch
Summary:       Graph, mesh and hypergraph partitioning library
Version:       7.0.10
Release:       2%{?dist}

License:       CeCILL-C
URL:           https://gitlab.inria.fr/scotch/scotch
Source0:       https://gitlab.inria.fr/scotch/scotch/-/archive/v%{version}/scotch-v%{version}.tar.bz2

BuildRequires: bison
BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: make
BuildRequires: xz-devel
BuildRequires: zlib-devel

%description
Scotch is a software package for graph and mesh/hypergraph partitioning and
sparse matrix ordering. The parallel scotch libraries are packaged in the
ptscotch sub-packages.

%package devel
Summary:       Development libraries for scotch
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development libraries for scotch.


%if %{with metis}
%package devel-metis
Summary:       Metis compatibility header
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}

%description devel-metis
This header is a drop-in replacement for the original metis.h header
to build against the scotch.
%endif


%package doc
Summary:       Documentations and example for scotch and ptscotch
BuildArch:     noarch

%description doc
Contains documentations and example for scotch and ptscotch

###############################################################################

%if %{with mpich}
%package -n ptscotch-mpich
Summary:       PT-Scotch libraries compiled against mpich
BuildRequires: mpich-devel

%description -n ptscotch-mpich
Scotch is a software package for graph and mesh/hypergraph partitioning and
sparse matrix ordering. This sub-package provides parallelized scotch libraries
compiled with mpich.


%package -n ptscotch-mpich-devel
Summary:       Development libraries for PT-Scotch (mpich)
Requires:      pt%{name}-mpich%{?_isa} = %{version}-%{release}

%description -n ptscotch-mpich-devel
This package contains development libraries for PT-Scotch, compiled against
mpich.


%if %{with metis}
%package -n ptscotch-mpich-devel-parmetis
Summary:       Parmetis compatibility header
Requires:      pt%{name}-mpich-devel%{?_isa} = %{version}-%{release}

%description -n ptscotch-mpich-devel-parmetis
This header is a drop-in replacement for the original parmetis.h header
to build against the scotch.
%endif
%endif

###############################################################################

%if %{with openmpi}
%package -n ptscotch-openmpi
Summary:       PT-Scotch libraries compiled against openmpi
BuildRequires: openmpi-devel

%description -n ptscotch-openmpi
Scotch is a software package for graph and mesh/hypergraph partitioning and
sparse matrix ordering. This sub-package provides parallelized scotch libraries
compiled with openmpi.


%package -n ptscotch-openmpi-devel
Summary:       Development libraries for PT-Scotch (openmpi)
Requires:      pt%{name}-openmpi%{?_isa} = %{version}-%{release}

%description -n ptscotch-openmpi-devel
This package contains development libraries for PT-Scotch, compiled against
openmpi.


%if %{with metis}
%package -n ptscotch-openmpi-devel-parmetis
Summary:       Parmetis compatibility header
Requires:      pt%{name}-openmpi-devel%{?_isa} = %{version}-%{release}

%description -n ptscotch-openmpi-devel-parmetis
This header is a drop-in replacement for the original parmetis.h header
to build against the scotch.
%endif
%endif


###############################################################################

%prep
%autosetup -p1 -n %{name}-v%{version}

# Convert the license files to utf8
for file in doc/CeCILL-C_V1-en.txt doc/CeCILL-C_V1-fr.txt; do
    iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
done


%build
%define _vpath_builddir %{_target_platform}
%cmake -DBUILD_PTSCOTCH=OFF \
    -DCOMMON_PTHREAD:BOOL=ON \
    -DSCOTCH_PTHREAD:BOOL=ON \
    -DCOMMON_PTHREAD_AFFINITY_LINUX:BOOL=ON \
%if %{with metis}
    -DBUILD_LIBSCOTCHMETIS=ON \
    -DSCOTCH_METIS_VERSION=5 \
%else
    -DBUILD_LIBSCOTCHMETIS=OFF \
%endif
    -DCMAKE_INSTALL_BINDIR=%{_bindir} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/scotch \
%cmake_build

%if %{with mpich}
%{_mpich_load}
%define _vpath_builddir %{_target_platform}-mpich
%cmake -DBUILD_PTSCOTCH=ON \
    -DCOMMON_PTHREAD:BOOL=ON \
    -DSCOTCH_PTHREAD:BOOL=ON \
    -DCOMMON_PTHREAD_AFFINITY_LINUX:BOOL=ON \
%if %{with metis}
    -DBUILD_LIBSCOTCHMETIS=ON \
    -DSCOTCH_PARMETIS_VERSION=3 \
%else
    -DBUILD_LIBSCOTCHMETIS=OFF \
%endif
    -DCMAKE_INSTALL_BINDIR=$MPI_BIN \
    -DCMAKE_INSTALL_LIBDIR=$MPI_LIB \
    -DCMAKE_INSTALL_INCLUDEDIR=$MPI_INCLUDE/scotch
%cmake_build
%{_mpich_unload}
%endif

%if %{with openmpi}
%{_openmpi_load}
%define _vpath_builddir %{_target_platform}-openmpi
%cmake -DBUILD_PTSCOTCH=ON \
    -DCOMMON_PTHREAD:BOOL=ON \
    -DSCOTCH_PTHREAD:BOOL=ON \
    -DCOMMON_PTHREAD_AFFINITY_LINUX:BOOL=ON \
%if %{with metis}
    -DBUILD_LIBSCOTCHMETIS=ON \
    -DSCOTCH_PARMETIS_VERSION=3 \
%else
    -DBUILD_LIBSCOTCHMETIS=OFF \
%endif
    -DCMAKE_INSTALL_BINDIR=$MPI_BIN \
    -DCMAKE_INSTALL_LIBDIR=$MPI_LIB \
    -DCMAKE_INSTALL_INCLUDEDIR=$MPI_INCLUDE/scotch
%cmake_build
%{_openmpi_unload}
%endif


%install
%define _vpath_builddir %{_target_platform}
%cmake_install

%if %{with metis}
# Default to the v5 API for the metis compat library
ln -s libscotchmetisv5.so %{buildroot}%{_libdir}/libscotchmetis.so
# Rename include files to avoid conflicts with original Metis
mv %{buildroot}%{_includedir}/scotch/metis.h %{buildroot}%{_includedir}/scotch/scotchmetis.h
mv %{buildroot}%{_includedir}/scotch/metisf.h %{buildroot}%{_includedir}/scotch/scotchmetisf.h
%endif

##############
%if %{with mpich}
%{_mpich_load}
%define _vpath_builddir %{_target_platform}-mpich
%cmake_install

%if %{with metis}
# Default to the v5 API for the metis compat library
ln -s libscotchmetisv5.so %{buildroot}$MPI_LIB/libscotchmetis.so
# Only the ParMeTiS v3 API is available
ln -s libptscotchparmetisv3.so %{buildroot}$MPI_LIB/libparmetis.so
ln -s libptscotchparmetisv3.so %{buildroot}$MPI_LIB/libptscotchparmetis.so
# Rename include files to avoid conflicts with original Metis
mv %{buildroot}$MPI_INCLUDE/scotch/metis.h %{buildroot}$MPI_INCLUDE/scotch/scotchmetis.h
mv %{buildroot}$MPI_INCLUDE/scotch/metisf.h %{buildroot}$MPI_INCLUDE/scotch/scotchmetisf.h
%endif
%{_mpich_unload}
%endif
################

################
%if %{with openmpi}
%{_openmpi_load}
%define _vpath_builddir %{_target_platform}-openmpi
%cmake_install

%if %{with metis}
# Default to the v5 API for the metis compat library
ln -s libscotchmetisv5.so %{buildroot}$MPI_LIB/libscotchmetis.so
# Only the ParMeTiS v3 API is available
ln -s libptscotchparmetisv3.so %{buildroot}$MPI_LIB/libparmetis.so
ln -s libptscotchparmetisv3.so %{buildroot}$MPI_LIB/libptscotchparmetis.so
# Rename include files to avoid conflicts with original Metis
mv %{buildroot}$MPI_INCLUDE/scotch/metis.h %{buildroot}$MPI_INCLUDE/scotch/scotchmetis.h
mv %{buildroot}$MPI_INCLUDE/scotch/metisf.h %{buildroot}$MPI_INCLUDE/scotch/scotchmetisf.h
%endif
%{_openmpi_unload}
%endif
##################

# Don't install executables
rm -f %{buildroot}%{_bindir}/*
rm -f %{buildroot}%{_libdir}/mpich/bin/*
rm -f %{buildroot}%{_libdir}/openmpi/bin/*
rm -rf %{buildroot}%{_mandir}/*


%check
%define _vpath_builddir %{_target_platform}
%ctest || :

%if %{with mpich}
%{_mpich_load}
%define _vpath_builddir %{_target_platform}-mpich
%ctest || :
%{_mpich_unload}
%endif

%if %{with openmpi}
%{_openmpi_load}
%define _vpath_builddir %{_target_platform}-openmpi
%ctest || :
%{_openmpi_unload}
%endif


%files
%license doc/CeCILL-C_V1-en.txt
%{_libdir}/libscotch.so.7*
%{_libdir}/libesmumps.so.7*
%{_libdir}/libscotcherr.so.7*
%{_libdir}/libscotcherrexit.so.7*
%if %{with metis}
%{_libdir}/libscotchmetisv3.so.7*
%{_libdir}/libscotchmetisv5.so.7*
%endif

%files devel
%dir %{_includedir}/scotch
%{_includedir}/scotch/scotch.h
%{_includedir}/scotch/scotchf.h
%{_includedir}/scotch/esmumps.h
%{_libdir}/libesmumps.so
%{_libdir}/libscotch.so
%{_libdir}/libscotcherr.so
%{_libdir}/libscotcherrexit.so
%if %{with metis}
%{_libdir}/libscotchmetisv3.so
%{_libdir}/libscotchmetisv5.so
%endif
%dir %{_libdir}/cmake/scotch/
%{_libdir}/cmake/scotch/esmumpsTargets*
%{_libdir}/cmake/scotch/SCOTCH*
%{_libdir}/cmake/scotch/scotchTargets*
%{_libdir}/cmake/scotch/scotcherrTargets*
%{_libdir}/cmake/scotch/scotcherrexitTargets*

%if %{with metis}
%files devel-metis
%dir %{_includedir}/scotch
%{_includedir}/scotch/scotchmetis.h
%{_includedir}/scotch/scotchmetisf.h
%{_libdir}/libscotchmetis.so
%{_libdir}/cmake/scotch/scotchmetisTargets*
%endif

%files doc
%license doc/CeCILL-C_V1-en.txt
%doc doc/*.pdf
%doc doc/scotch_example.f

%if %{with mpich}
%files -n ptscotch-mpich
%license doc/CeCILL-C_V1-en.txt
%{_libdir}/mpich/lib/adm2dgr
%{_libdir}/mpich/lib/libesmumps.so.7*
%{_libdir}/mpich/lib/libscotch.so.7*
%{_libdir}/mpich/lib/libscotcherr.so.7*
%{_libdir}/mpich/lib/libscotcherrexit.so.7*
%{_libdir}/mpich/lib/libptscotch.so.7*
%{_libdir}/mpich/lib/libptesmumps.so.7*
%{_libdir}/mpich/lib/libptscotcherr.so.7*
%{_libdir}/mpich/lib/libptscotcherrexit.so.7*
%if %{with metis}
%{_libdir}/mpich/lib/libscotchmetisv3.so.7*
%{_libdir}/mpich/lib/libscotchmetisv5.so.7*
%{_libdir}/mpich/lib/libptscotchparmetisv3.so.7*
%endif

%files -n ptscotch-mpich-devel
%dir %{_includedir}/mpich*/scotch
%{_includedir}/mpich*/scotch/ptscotch.h
%{_includedir}/mpich*/scotch/ptscotchf.h
%{_includedir}/mpich*/scotch/scotch.h
%{_includedir}/mpich*/scotch/scotchf.h
%{_includedir}/mpich*/scotch/esmumps.h
%{_libdir}/mpich/lib/libesmumps.so
%{_libdir}/mpich/lib/libscotch.so
%{_libdir}/mpich/lib/libscotcherr.so
%{_libdir}/mpich/lib/libscotcherrexit.so
%{_libdir}/mpich/lib/libptesmumps.so
%{_libdir}/mpich/lib/libptscotch.so
%{_libdir}/mpich/lib/libptscotcherr.so
%{_libdir}/mpich/lib/libptscotcherrexit.so
%if %{with metis}
%{_libdir}/mpich/lib/libscotchmetisv3.so
%{_libdir}/mpich/lib/libscotchmetisv5.so
%{_libdir}/mpich/lib/libptscotchparmetisv3.so
%endif
%dir %{_libdir}/mpich/lib/cmake/scotch/
%{_libdir}/mpich/lib/cmake/scotch/ptesmumpsTargets*
%{_libdir}/mpich/lib/cmake/scotch/SCOTCHConfig.cmake
%{_libdir}/mpich/lib/cmake/scotch/SCOTCHConfigVersion.cmake
%{_libdir}/mpich/lib/cmake/scotch/esmumpsTargets*
%{_libdir}/mpich/lib/cmake/scotch/ptscotchTargets*
%{_libdir}/mpich/lib/cmake/scotch/ptscotcherrTargets*
%{_libdir}/mpich/lib/cmake/scotch/ptscotcherrexitTargets*
%{_libdir}/mpich/lib/cmake/scotch/scotchTargets*
%{_libdir}/mpich/lib/cmake/scotch/scotcherrTargets*
%{_libdir}/mpich/lib/cmake/scotch/scotcherrexitTargets*

%if %{with metis}
%files -n ptscotch-mpich-devel-parmetis
%dir %{_includedir}/mpich*/scotch
%{_includedir}/mpich*/scotch/scotchmetis.h
%{_includedir}/mpich*/scotch/scotchmetisf.h
%{_includedir}/mpich*/scotch/parmetis.h
%{_libdir}/mpich/lib/libparmetis.so
%{_libdir}/mpich/lib/libptscotchparmetis.so
%{_libdir}/mpich/lib/libscotchmetis.so
%{_libdir}/mpich/lib/cmake/scotch/ptscotchparmetisTargets*
%{_libdir}/mpich/lib/cmake/scotch/scotchmetisTargets*
%endif
%endif


%if %{with openmpi}
%files -n ptscotch-openmpi
%license doc/CeCILL-C_V1-en.txt
%{_libdir}/openmpi/lib/adm2dgr
%{_libdir}/openmpi/lib/libesmumps.so.7*
%{_libdir}/openmpi/lib/libscotch.so.7*
%{_libdir}/openmpi/lib/libscotcherr.so.7*
%{_libdir}/openmpi/lib/libscotcherrexit.so.7*
%{_libdir}/openmpi/lib/libptscotch.so.7*
%{_libdir}/openmpi/lib/libptesmumps.so.7*
%{_libdir}/openmpi/lib/libptscotcherr.so.7*
%{_libdir}/openmpi/lib/libptscotcherrexit.so.7*
%if %{with metis}
%{_libdir}/openmpi/lib/libscotchmetisv3.so.7*
%{_libdir}/openmpi/lib/libscotchmetisv5.so.7*
%{_libdir}/openmpi/lib/libptscotchparmetisv3.so.7*
%endif

%files -n ptscotch-openmpi-devel
%dir %{_includedir}/openmpi*/scotch
%{_includedir}/openmpi*/scotch/ptscotch.h
%{_includedir}/openmpi*/scotch/ptscotchf.h
%{_includedir}/openmpi*/scotch/scotch.h
%{_includedir}/openmpi*/scotch/scotchf.h
%{_includedir}/openmpi*/scotch/esmumps.h
%{_libdir}/openmpi/lib/libesmumps.so
%{_libdir}/openmpi/lib/libscotch.so
%{_libdir}/openmpi/lib/libscotcherr.so
%{_libdir}/openmpi/lib/libscotcherrexit.so
%{_libdir}/openmpi/lib/libptesmumps.so
%{_libdir}/openmpi/lib/libptscotch.so
%{_libdir}/openmpi/lib/libptscotcherr.so
%{_libdir}/openmpi/lib/libptscotcherrexit.so
%if %{with metis}
%{_libdir}/openmpi/lib/libscotchmetisv3.so
%{_libdir}/openmpi/lib/libscotchmetisv5.so
%{_libdir}/openmpi/lib/libptscotchparmetisv3.so
%endif
%dir %{_libdir}/openmpi/lib/cmake/scotch/
%{_libdir}/openmpi/lib/cmake/scotch/ptesmumpsTargets*
%{_libdir}/openmpi/lib/cmake/scotch/SCOTCHConfig.cmake
%{_libdir}/openmpi/lib/cmake/scotch/SCOTCHConfigVersion.cmake
%{_libdir}/openmpi/lib/cmake/scotch/esmumpsTargets*
%{_libdir}/openmpi/lib/cmake/scotch/ptscotchTargets*
%{_libdir}/openmpi/lib/cmake/scotch/ptscotcherrTargets*
%{_libdir}/openmpi/lib/cmake/scotch/ptscotcherrexitTargets*
%{_libdir}/openmpi/lib/cmake/scotch/scotchTargets*
%{_libdir}/openmpi/lib/cmake/scotch/scotcherrTargets*
%{_libdir}/openmpi/lib/cmake/scotch/scotcherrexitTargets*

%if %{with metis}
%files -n ptscotch-openmpi-devel-parmetis
%dir %{_includedir}/openmpi*/scotch
%{_includedir}/openmpi*/scotch/scotchmetis.h
%{_includedir}/openmpi*/scotch/scotchmetisf.h
%{_includedir}/openmpi*/scotch/parmetis.h
%{_libdir}/openmpi/lib/libparmetis.so
%{_libdir}/openmpi/lib/libptscotchparmetis.so
%{_libdir}/openmpi/lib/libscotchmetis.so
%{_libdir}/openmpi/lib/cmake/scotch/ptscotchparmetisTargets*
%{_libdir}/openmpi/lib/cmake/scotch/scotchmetisTargets*
%endif
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0.10-2
- Import
