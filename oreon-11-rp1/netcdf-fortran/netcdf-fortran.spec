%global source0_hash fc8df99e78cd2aa5ea7b312bce5307b1bea73a118d4860b3b4358971ec376c54
Name:           netcdf-fortran
Version:        4.6.4
Release:        1%{?dist}
Summary:        Fortran libraries for NetCDF-4
License:        BSD-3-Clause AND Apache-2.0
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        https://github.com/Unidata/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         netcdf-fortran-pkgconfig.patch
%global with_mpich 1
%global with_openmpi 1
%global mpi_list mpich
%global mpi_list %{?mpi_list} openmpi
# oreon:deps
BuildRequires:  gcc-gfortran
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  netcdf-devel
BuildRequires:  netcdf-mpich-devel
BuildRequires:  netcdf-openmpi-devel
BuildRequires:  openmpi-devel
# /oreon:deps
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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf
sed -i -e '1i#!/bin/sh' examples/F90/run_f90_par_examples.sh

%build

%global _configure ../configure
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make -C build check VERBOSE=1
%ifnarch s390x
export OMPI_MCA_rmaps_base_oversubscribe=1
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi check VERBOSE=1
  module purge
done
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n netcdf-fortran-devel -f %{oreon_filedir}/netcdf-fortran-devel.list
%files -n netcdf-fortran-static -f %{oreon_filedir}/netcdf-fortran-static.list
%files -n netcdf-fortran-mpich -f %{oreon_filedir}/netcdf-fortran-mpich.list
%files -n netcdf-fortran-mpich-devel -f %{oreon_filedir}/netcdf-fortran-mpich-devel.list
%files -n netcdf-fortran-mpich-static -f %{oreon_filedir}/netcdf-fortran-mpich-static.list
%files -n netcdf-fortran-openmpi -f %{oreon_filedir}/netcdf-fortran-openmpi.list
%files -n netcdf-fortran-openmpi-devel -f %{oreon_filedir}/netcdf-fortran-openmpi-devel.list
%files -n netcdf-fortran-openmpi-static -f %{oreon_filedir}/netcdf-fortran-openmpi-static.list

%changelog

%autochangelog
