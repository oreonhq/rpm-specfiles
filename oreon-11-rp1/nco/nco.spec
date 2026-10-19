%global source0_hash 705ffa98a78d468cdfaa5858f09213142265120fc26a78249a442ae2fa92ae96
%global builddocs 1
Name:           nco
Version:        5.3.9
Release:        1%{?dist}
Summary:        Suite of programs for manipulating NetCDF/HDF4 files
License:        BSD-3-Clause
URL:            http://nco.sourceforge.net/
Source0:        https://github.com/nco/nco/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         nco-install_C_headers.patch
%ifarch %java_arches
%endif
%if 0%{?builddocs}
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  make
BuildRequires:  netcdf-devel
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  udunits2-devel
# /oreon:deps
%package devel
Summary:        Development files for NCO
Requires:       %{name} = %{version}-%{release}
%package static
Summary:        Static libraries for NCO
Requires:       %{name}-devel = %{version}-%{release}
%description
The netCDF Operators, NCO, are a suite of command line programs known
as operators.  The operators facilitate manipulation and analysis of
self-describing data stored in the freely available netCDF and HDF
formats (http://www.unidata.ucar.edu/packages/netcdf and
http://hdf.ncsa.uiuc.edu, respectively).  Each NCO operator (e.g.,
ncks) takes netCDF or HDF input file(s), performs an operation (e.g.,
averaging, hyperslabbing, or renaming), and outputs a processed netCDF
file.  Although most users of netCDF and HDF data are involved in
scientific research, these data formats, and thus NCO, are generic and
are equally useful in fields from agriculture to zoology.  The NCO
User's Guide illustrates NCO use with examples from the field of
climate modeling and analysis.  The NCO homepage is
http://nco.sourceforge.net/.

%description devel
This package contains the NCO header and development files.

%description static
This package contains the NCO static libs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .install_C_headers

%build

export CPPFLAGS=-I%{_includedir}/udunits2
%configure \
%ifarch %java_arches
  HAVE_ANTLR=yes \
%endif
  --disable-dependency-tracking --includedir=%{_includedir}/nco
%make_build
%if 0%{?builddocs}
make -C doc html pdf
%endif
%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
chrpath -d -k $RPM_BUILD_ROOT%{_bindir}/* || :
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n nco-devel -f %{oreon_filedir}/nco-devel.list
%files -n nco-static -f %{oreon_filedir}/nco-static.list

%changelog

%autochangelog
