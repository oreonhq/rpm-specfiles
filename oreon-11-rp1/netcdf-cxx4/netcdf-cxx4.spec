%global source0_hash e3fe3d2ec06c1c2772555bf1208d220aab5fee186d04bd265219b0bc7a978edc
%bcond_without mpich
%bcond_without openmpi
Name:           netcdf-cxx4
Version:        4.3.1
Release:        1%{?dist}
Summary:        NetCDF-4 C++ library
License:        BSD-3-Clause
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        https://github.com/Unidata/netcdf-cxx4/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         netcdf-cxx4-bigendian.patch
Patch1:         netcdf-cxx4-logging.patch
%if %{with mpich}
%global mpi_list mpich
%endif
%if %{with openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  netcdf-devel
BuildRequires:  netcdf-mpich-devel
BuildRequires:  netcdf-openmpi-devel
BuildRequires:  openmpi-devel
BuildRequires:  openssh-clients
# /oreon:deps
%description
netCDF-4 C++ library.

%package devel
Summary:        Development files for netCDF-4 C++ API
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       netcdf-devel%{?_isa}
%description devel
Development files for netCDF-4 C++ API.

%package static
Summary:        Static library for netCDF-4 C++ API
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Static library for netCDF-4 C++ API.

%if %{with mpich}
%package mpich
Summary: NetCDF mpich libraries
BuildRequires: mpich-devel
BuildRequires: netcdf-mpich-devel
Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < 4.2-8
%description mpich
NetCDF parallel mpich libraries

%package mpich-devel
Summary: NetCDF mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: netcdf-mpich-devel
Requires: libcurl-devel
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < 4.2-8
%description mpich-devel
NetCDF parallel mpich development files

%package mpich-static
Summary: NetCDF mpich static libraries
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < 4.2-8
%description mpich-static
NetCDF parallel mpich static libraries
%endif

%if %{with openmpi}
%package openmpi
Summary: NetCDF openmpi libraries
BuildRequires: openmpi-devel
BuildRequires: netcdf-openmpi-devel
%description openmpi
NetCDF parallel openmpi libraries

%package openmpi-devel
Summary: NetCDF openmpi development files
Requires: %{name}-openmpi%{_isa} = %{version}-%{release}
Requires: openmpi-devel
Requires: pkgconfig
Requires: netcdf-openmpi-devel
Requires: libcurl-devel
%description openmpi-devel
NetCDF parallel openmpi development files

%package openmpi-static
Summary: NetCDF openmpi static libraries
Requires: %{name}-openmpi-devel%{?_isa} = %{version}-%{release}
%description openmpi-static
NetCDF parallel openmpi static libraries
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Fix line endings
sed -i -e 's/\r//' examples/*.cpp

%build

%global _configure ../configure
mkdir build
pushd build
ln -s ../configure .
%configure
make %{?_smp_mflags}
popd
export CC=mpicc
export CXX=mpicxx
for mpi in %{mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  ln -s ../configure .
  %configure \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --datarootdir=%{_libdir}/$mpi/share \
    --mandir=%{_libdir}/$mpi/share/man
  make %{?_smp_mflags}
  module purge
  popd
done
%install
make -C build install DESTDIR=${RPM_BUILD_ROOT}
/bin/rm ${RPM_BUILD_ROOT}%{_libdir}/*.la
/bin/rm ${RPM_BUILD_ROOT}%{_libdir}/libh5bzip2.so
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi install DESTDIR=${RPM_BUILD_ROOT}
  rm $RPM_BUILD_ROOT/%{_libdir}/$mpi/lib/*.la
  rm $RPM_BUILD_ROOT/%{_libdir}/$mpi/lib/libh5bzip2.so
  module purge
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make -C build check || ( cat build/*/test-suite.log && exit 1 )
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi check || ( cat ${mpi}/*/test-suite.log && exit 1 )
  module purge
done
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n netcdf-cxx4-devel -f %{oreon_filedir}/netcdf-cxx4-devel.list
%files -n netcdf-cxx4-static -f %{oreon_filedir}/netcdf-cxx4-static.list
%files -n netcdf-cxx4-mpich -f %{oreon_filedir}/netcdf-cxx4-mpich.list
%files -n netcdf-cxx4-mpich-devel -f %{oreon_filedir}/netcdf-cxx4-mpich-devel.list
%files -n netcdf-cxx4-mpich-static -f %{oreon_filedir}/netcdf-cxx4-mpich-static.list
%files -n netcdf-cxx4-openmpi -f %{oreon_filedir}/netcdf-cxx4-openmpi.list
%files -n netcdf-cxx4-openmpi-devel -f %{oreon_filedir}/netcdf-cxx4-openmpi-devel.list
%files -n netcdf-cxx4-openmpi-static -f %{oreon_filedir}/netcdf-cxx4-openmpi-static.list

%changelog

%autochangelog
