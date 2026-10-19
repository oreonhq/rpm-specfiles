%global source0_hash 33c27231c478c3b35da7c7758fbdd02da1fe407abcb16ddfe195f69d164f930d
%global sover 22
Name:           netcdf
Version:        4.10.1
Release:        1%{?dist}
Summary:        Libraries for the Unidata network Common Data Form
License:        BSD-3-Clause
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        https://github.com/Unidata/netcdf-c/archive/v%{version}/%{name}-%{version}.tar.gz
%ifarch aarch64
%global _lto_cflags %{nil}
%endif
%ifarch %{valgrind_arches}
%endif
Requires:       hdf5%{?_isa} = %{_hdf5_version}
%global with_mpich %{undefined flatpak}
  %global with_openmpi %{undefined flatpak}
%if %{with_mpich}
%global mpi_list mpich
%endif
%if %{with_openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif
%ifarch s390x
%bcond_with parallel_tests
%else
%bcond_without parallel_tests
%endif
# oreon:deps
BuildRequires:  blosc-devel
BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  gawk
BuildRequires:  hdf-static
BuildRequires:  hdf5-devel
BuildRequires:  hdf5-mpich-devel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel
BuildRequires:  libzstd-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  openssh-clients
BuildRequires:  zlib-devel
# /oreon:deps
%description
NetCDF (network Common Data Form) is an interface for array-oriented 
data access and a freely-distributed collection of software libraries 
for C, Fortran, C++, and perl that provides an implementation of the 
interface.  The NetCDF library also defines a machine-independent 
format for representing scientific data.  Together, the interface, 
library, and format support the creation, access, and sharing of 
scientific data. The NetCDF software was developed at the Unidata 
Program Center in Boulder, Colorado.

NetCDF data is: 

   o Self-Describing: A NetCDF file includes information about the
     data it contains.

   o Network-transparent:  A NetCDF file is represented in a form that
     can be accessed by computers with different ways of storing
     integers, characters, and floating-point numbers.

   o Direct-access:  A small subset of a large dataset may be accessed
     efficiently, without first reading through all the preceding
     data.

   o Appendable:  Data can be appended to a NetCDF dataset along one
     dimension without copying the dataset or redefining its
     structure. The structure of a NetCDF dataset can be changed,
     though this sometimes causes the dataset to be copied.

   o Sharable:  One writer and multiple readers may simultaneously
     access the same NetCDF file.

%package devel
Summary:        Development files for netcdf
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig%{?_isa}
Requires:       hdf5-devel%{?_isa}
Requires:       libcurl-devel%{?_isa}
%description devel
This package contains the netCDF C header files, shared devel libs, and 
man pages.

%package static
Summary:        Static libs for netcdf
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description static
This package contains the netCDF C static libs.

%if %{with_mpich}
%package mpich
Summary: NetCDF mpich libraries
Requires: hdf5-mpich%{?_isa} = %{_hdf5_version}
BuildRequires: mpich-devel
BuildRequires: hdf5-mpich-devel >= 1.8.4
Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < 4.3.0-4
%description mpich
NetCDF parallel mpich libraries

%package mpich-devel
Summary: NetCDF mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: pkgconfig%{?_isa}
Requires: hdf5-mpich-devel%{?_isa}
Requires: libcurl-devel%{?_isa}
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < 4.3.0-4
%description mpich-devel
NetCDF parallel mpich development files

%package mpich-static
Summary: NetCDF mpich static libraries
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < 4.3.0-4
%description mpich-static
NetCDF parallel mpich static libraries
%endif

%if %{with_openmpi}
%package openmpi
Summary: NetCDF openmpi libraries
Requires: hdf5-openmpi%{?_isa} = %{_hdf5_version}
BuildRequires: openmpi-devel
BuildRequires: hdf5-openmpi-devel >= 1.8.4
%description openmpi
NetCDF parallel openmpi libraries

%package openmpi-devel
Summary: NetCDF openmpi development files
Requires: %{name}-openmpi%{_isa} = %{version}-%{release}
Requires: openmpi-devel%{?_isa}
Requires: pkgconfig%{?_isa}
Requires: hdf5-openmpi-devel%{?_isa}
Requires: libcurl-devel%{?_isa}
%description openmpi-devel
NetCDF parallel openmpi development files

%package openmpi-static
Summary: NetCDF openmpi static libraries
Requires: %{name}-openmpi-devel%{?_isa} = %{version}-%{release}
%description openmpi-static
NetCDF parallel openmpi static libraries
%endif

%prep

%autosetup -p1 -n %{name}-c-%{version}
# For Patch0
./bootstrap

%build

%global _configure ../configure
export LDFLAGS="%{__global_ldflags} -L%{_libdir}/hdf"
export CFLAGS="%{optflags} -fno-strict-aliasing"
%global configure_opts \\\
           --enable-shared \\\
           --enable-netcdf-4 \\\
           --enable-dap \\\
           --enable-extra-example-tests \\\
           CPPFLAGS="-I%{_includedir}/hdf" \\\
           LIBS="-ltirpc" \\\
           --enable-hdf4 \\\
           --disable-dap-remote-tests \\\
%{nil}
mkdir build
pushd build
ln -s ../configure .
%configure %{configure_opts} \
  --with-plugin-dir=%{_libdir}/hdf5/plugin
sed -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' -i libtool
%make_build
popd
for mpi in %{?mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  ln -s ../configure .
  %configure %{configure_opts} \
    CC=mpicc \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --datarootdir=%{_libdir}/$mpi/share \
    --mandir=%{_libdir}/$mpi/share/man \
    --with-plugin-dir=%{_libdir}/$mpi/hdf5/plugin \
    %{?with_parallel_tests:--enable-parallel-tests}
  sed -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' -i libtool
  %make_build
  module purge
  popd
done
%install
make -C build install DESTDIR=${RPM_BUILD_ROOT}
/bin/rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
for mpi in %{?mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi install DESTDIR=${RPM_BUILD_ROOT}
  module purge
done
find $RPM_BUILD_ROOT/%{_libdir} -name \*.la -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifarch %{ix86} s390x
fail=0
%else
fail=1
%endif
make -C build check || ( cat build/*/test-suite.log && exit $fail )
export OMPI_MCA_rmaps_base_oversubscribe=1
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
%ifnarch armv7hl
for mpi in %{?mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi check || ( cat $mpi/*/test-suite.log && exit $fail )
  module purge
done
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n netcdf-devel -f %{oreon_filedir}/netcdf-devel.list
%files -n netcdf-static -f %{oreon_filedir}/netcdf-static.list
%files -n netcdf-mpich -f %{oreon_filedir}/netcdf-mpich.list
%files -n netcdf-mpich-devel -f %{oreon_filedir}/netcdf-mpich-devel.list
%files -n netcdf-mpich-static -f %{oreon_filedir}/netcdf-mpich-static.list
%files -n netcdf-openmpi -f %{oreon_filedir}/netcdf-openmpi.list
%files -n netcdf-openmpi-devel -f %{oreon_filedir}/netcdf-openmpi-devel.list
%files -n netcdf-openmpi-static -f %{oreon_filedir}/netcdf-openmpi-static.list

%changelog

%autochangelog
