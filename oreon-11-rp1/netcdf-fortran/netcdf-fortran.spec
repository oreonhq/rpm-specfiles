%global source0_hash 44cc7b5626b0b054a8503b8fe7c1b0ac4e0a79a69dad792c212454906a9224ca

Name:           netcdf-fortran
Version:        4.6.2
Release:        3%{?dist}
Summary:        Fortran libraries for NetCDF-4

License:        BSD-3-Clause AND Apache-2.0
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        https://github.com/Unidata/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Use pkgconfig in nf-config to avoid multi-lib issues and remove FFLAGS
Patch1:         netcdf-fortran-pkgconfig.patch
%if 0%{?fedora} >= 38
ExcludeArch:    %{ix86}
%endif

BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  netcdf-devel >= 4.6.0
# For Patch1
BuildRequires:  libtool

%global with_mpich 1
%global with_openmpi 1

%if %{with_mpich}
%global mpi_list mpich
%endif
%if %{with_openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif

%description
Fortran libraries for NetCDF-4.

%package devel
Summary:        Development files for Fortran NetCDF API
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc-gfortran%{?_isa}
Requires:       pkgconfig
Requires:       netcdf-devel%{?_isa}

%description devel
This package contains the NetCDF Fortran header files, shared devel libraries,
and man pages.

%package static
Summary:        Static library for Fortran NetCDF API
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package contains the NetCDF Fortran static library.

%if %{with_mpich}
%package mpich
Summary: NetCDF Fortran mpich libraries
BuildRequires: mpich-devel
BuildRequires: netcdf-mpich-devel

%description mpich
NetCDF Fortran parallel mpich libraries

%package mpich-devel
Summary: NetCDF Fortran mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran%{_isa}
Requires: pkgconfig
Requires: netcdf-mpich-devel
Requires: libcurl-devel

%description mpich-devel
NetCDF Fortran parallel mpich development files

%package mpich-static
Summary: NetCDF Fortran mpich static libraries
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}

%description mpich-static
NetCDF Fortran parallel mpich static libraries
%endif

%if %{with_openmpi}
%package openmpi
Summary: NetCDF Fortran openmpi libraries
BuildRequires: openmpi-devel
BuildRequires: netcdf-openmpi-devel

%description openmpi
NetCDF Fortran parallel openmpi libraries

%package openmpi-devel
Summary: NetCDF Fortran openmpi development files
Requires: %{name}-openmpi%{_isa} = %{version}-%{release}
Requires: openmpi-devel
Requires: gcc-gfortran%{_isa}
Requires: pkgconfig
Requires: netcdf-openmpi-devel
Requires: libcurl-devel

%description openmpi-devel
NetCDF Fortran parallel openmpi development files

%package openmpi-static
Summary: NetCDF Fortran openmpi static libraries
Requires: %{name}-openmpi-devel%{?_isa} = %{version}-%{release}

%description openmpi-static
NetCDF Fortran parallel openmpi static libraries
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf
sed -i -e '1i#!/bin/sh' examples/F90/run_f90_par_examples.sh

%build
#Do out of tree builds
%global _configure ../configure

# Serial build
mkdir build
pushd build
ln -s ../configure .
export F77="gfortran"
export FC="gfortran"
export FCFLAGS="$RPM_OPT_FLAGS"
export FFLAGS="$RPM_OPT_FLAGS"
%configure --enable-extra-example-tests --with-fmoddir=%{_fmoddir}
%make_build
popd

# MPI builds
for mpi in %{mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  ln -s ../configure .
  %configure \
    CC=mpicc CPPFLAGS=-DpgiFortran F77=mpif90 FC=mpif90 \
    FCFLAGS="$FCFLAGS -I$MPI_FORTRAN_MOD_DIR" \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --datarootdir=%{_libdir}/$mpi/share \
    --mandir=%{_libdir}/$mpi/share/man \
    --with-fmoddir=%{_fmoddir}/${mpi} \
    --enable-parallel \
    --enable-parallel-tests
  %make_build
  #make #{?_smp_mflags}
  module purge
  popd
done

%install
%make_install -C build
/bin/rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %make_install -C $mpi
  rm $RPM_BUILD_ROOT/%{_libdir}/$mpi/lib/*.la
  gzip $RPM_BUILD_ROOT/%{_libdir}/$mpi/share/man/man3/*.3
  module purge
done
/bin/rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%check
make -C build check VERBOSE=1
# mpich tests hang on s390x
%ifnarch s390x
# Allow oversubscription with openmpi
export OMPI_MCA_rmaps_base_oversubscribe=1
# openmpi 5+
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi check VERBOSE=1
  module purge
done
%endif

%ldconfig_scriptlets

%files
%license COPYRIGHT F03Interfaces_LICENSE
%doc README.md RELEASE_NOTES.md
%{_libdir}/*.so.*

%files devel
%doc examples
%{_bindir}/nf-config
%{_includedir}/netcdf.inc
%{_fmoddir}/*.mod
%{_libdir}/libnetcdff.settings
%{_libdir}/*.so
%{_libdir}/pkgconfig/netcdf-fortran.pc
%{_mandir}/man3/*

%files static
%{_libdir}/*.a

%if %{with_mpich}
%files mpich
%license COPYRIGHT F03Interfaces_LICENSE
%doc README.md RELEASE_NOTES.md
%{_libdir}/mpich/lib/*.so.*

%files mpich-devel
%{_libdir}/mpich/bin/nf-config
%{_includedir}/mpich-%{_arch}/*
%{_fmoddir}/mpich/*.mod
%{_libdir}/mpich/lib/libnetcdff.settings
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/pkgconfig/%{name}.pc
%{_libdir}/mpich/share/man/man3/*

%files mpich-static
%{_libdir}/mpich/lib/*.a
%endif

%if %{with_openmpi}
%files openmpi
%license COPYRIGHT F03Interfaces_LICENSE
%doc README.md RELEASE_NOTES.md
%{_libdir}/openmpi/lib/*.so.*

%files openmpi-devel
%{_libdir}/openmpi/bin/nf-config
%{_includedir}/openmpi-%{_arch}/*
%{_fmoddir}/openmpi/*.mod
%{_libdir}/openmpi/lib/libnetcdff.settings
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/pkgconfig/%{name}.pc
%{_libdir}/openmpi/share/man/man3/*

%files openmpi-static
%{_libdir}/openmpi/lib/*.a
%endif

%changelog
%autochangelog
