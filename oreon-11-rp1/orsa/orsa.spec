%global source0_hash 959abd0f9ed4311cf28a31d088b8afecd50674bd0d9a8360ac4a5c2752f22879
%bcond_without openmpi
Name:           orsa
Version:        0.7.0
Release:        1%{?dist}
Summary:        Orbit Reconstruction, Simulation and Analysis
License:        GPL-2.0-or-later
URL:            http://orsa.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        ORSA_MPI
Patch0:         orsa-gcc43.patch
Patch1:         orsa-configure.patch
Patch2:         orsa-file.patch
Patch3:         orsa-gsl-2.patch
Patch4:         orsa-linking.patch
Patch5:         orsa-configure-c99.patch
Source2:        config.guess
Source3:        config.sub
Requires:       %{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  cln-devel
BuildRequires:  fftw2-devel
BuildRequires:  gcc-c++
BuildRequires:  ginac-devel
BuildRequires:  gsl-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mpich-devel-static
BuildRequires:  openmpi-devel
BuildRequires:  qt3-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
ORSA is an interactive tool for scientific grade Celestial Mechanics
computations. Asteroids, comets, artificial satellites, Solar and extra-Solar
planetary systems can be accurately reproduced, simulated, and analyzed. 

%package devel
Summary:        Development files for %{name}
Requires:       fftw2-devel
Requires:       gsl-devel
Requires:       zlib-devel
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-headers = %{version}-%{release}
%description devel
This package contains development files for %{name}.

%if %{with openmpi}
%package openmpi
Summary:        A build of %{name} with support for OpenMPI
BuildRequires: openmpi-devel
Requires:       %{name}-common = %{version}-%{release}
%description openmpi
This package contains a build of %{name} with support for OpenMPI.

%package openmpi-devel
Summary:        Development files for %{name} build with support for OpenMPI
Requires: %{name}-openmpi = %{version}-%{release}
Requires: %{name}-headers = %{version}-%{release}
%description openmpi-devel
This package contains development files for a build of %{name}
 with support for OpenMPI.
%endif

%package mpich
Summary:        A build of %{name} with support for MPICH MPI
BuildRequires:  mpich-devel-static
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-mpich2 = %{version}-%{release}
Obsoletes:      %{name}-mpich2 < 0.7.0-24
%description mpich
This package contains a build of %{name} with support for MPICH MPI.

%package mpich-devel
Summary:        Development files for %{name} build with support for MPICH MPI
Requires:       %{name}-mpich = %{version}-%{release}
Requires:       %{name}-headers = %{version}-%{release}
Provides:       %{name}-mpich2-devel = %{version}-%{release}
Obsoletes:      %{name}-mpich2-devel < 0.7.0-24
%description mpich-devel
This package contains development files for a build of %{name}
with support for MPICH MPI.

%package headers
Summary:        Headers for development with %{name}
%description headers
This package contains C++ header files for development with %{name}.

%package common
Summary:        Common files for %{name}
%description common
This package contains files shared across the MPI/non-MPI builds of %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Install user hints for MPI support
install -p -m644 %{SOURCE1} .

# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp %{SOURCE2} %{SOURCE3} .

%build

autoreconf -iv
sed -i 's|-g -Wall -W -pipe -ftemplate-depth-64 -O3 -fno-exceptions -funroll-loops -fstrict-aliasing -fno-gcse|$CXXFLAGS|' configure
%global _configure ../configure
%global dobuild() \
mkdir $MPI_COMPILER && \
pushd $MPI_COMPILER && \
%configure $WITH_MPI --prefix=$MPI_HOME --bindir=$MPI_BIN --libdir=$MPI_LIB --program-suffix=$MPI_SUFFIX \\\
           --disable-dependency-tracking --disable-static \\\
           "CLN_CONFIG=`which pkg-config` cln" \\\
           "GINACLIB_CONFIG=`which pkg-config` ginac" \\\
           CXXFLAGS="$CXXFLAGS -DHAVE_INLINE -DINLINE_FUN=inline" && \
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool && \
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool && \
%make_build && \
popd
%global openmpi_bin %{_libdir}/openmpi/bin
%global openmpi_lib %{_libdir}/openmpi/lib
%global mpich_bin %{_libdir}/mpich/bin
%global mpich_lib %{_libdir}/mpich/lib
echo -e "\n##############################\nNow making the non-MPI version\n##############################\n"
MPI_COMPILER=serial MPI_SUFFIX= WITH_MPI=--without-mpi MPI_HOME=%{_prefix} MPI_BIN=%{_bindir} MPI_LIB=%{_libdir} %dobuild
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
%if %{with openmpi}
echo -e "\n##############################\nNow making the OpenMPI version\n##############################\n"
%{_openmpi_load}
WITH_MPI=--with-mpi %dobuild
%{_openmpi_unload}
%endif
echo -e "\n##############################\nNow making the MPICH version\n##############################\n"
%{_mpich_load}
WITH_MPI=--with-mpi %dobuild
%{_mpich_unload}
%install
%make_install -C serial CPPROG="cp -p"
rm %{buildroot}%{_libdir}/{liborsa.la,libxorsa.la}
%if %{with openmpi}
%{_openmpi_load}
%make_install -C $MPI_COMPILER CPPROG="cp -p"
rm %{buildroot}$MPI_LIB/{liborsa.la,libxorsa.la}
%{_openmpi_unload}
%endif
%{_mpich_load}
%make_install -C $MPI_COMPILER CPPROG="cp -p"
rm %{buildroot}$MPI_LIB/{liborsa.la,libxorsa.la}
%{_mpich_unload}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n orsa-devel -f %{oreon_filedir}/orsa-devel.list
%files -n orsa-openmpi -f %{oreon_filedir}/orsa-openmpi.list
%files -n orsa-openmpi-devel -f %{oreon_filedir}/orsa-openmpi-devel.list
%files -n orsa-mpich -f %{oreon_filedir}/orsa-mpich.list
%files -n orsa-mpich-devel -f %{oreon_filedir}/orsa-mpich-devel.list
%files -n orsa-headers -f %{oreon_filedir}/orsa-headers.list
%files -n orsa-common -f %{oreon_filedir}/orsa-common.list

%changelog

%autochangelog
