%global source0_hash cad4ee47fbb744269146e64298f9efa206bc03e7b86671e9729d8986bb4bc30e
%if %{with flexiblas}
%global blaslib flexiblas
%else
%global blaslib openblas
%endif
Name:           ncl
Version:        6.6.2
Release:        1%{?dist}
Summary:        NCAR Command Language and NCAR Graphics
License:        LicenseRef-Callaway-BSD
URL:            http://www.ncl.ucar.edu
Source0:        https://github.com/NCAR/ncl/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        Site.local.ncl
Source2:        ncarg.csh
Source3:        ncarg.sh
ExcludeArch:    %{ix86} ppc64le
Patch0:         ncl-5.1.0-paths.patch
Patch1:         ncarg-4.4.1-deps.patch
Patch2:         ncl-5.1.0-ppc64.patch
Patch3:         ncl-libs.patch
Patch4:         ncl-format.patch
Patch5:         ncl-boz.patch
Patch6:         ncl-gdal.patch
Patch7:         ncl-hdf4.3.patch
Patch8:         ncl-gcc15.patch
Patch9:         ncl-nc-set-log-level.patch
Patch10:        ncl-5.0.0-no_install_dep.patch
Patch11:        ncl-5.0.0-build_n_scripts.patch
Patch12:        ncl-5.1.0-netcdff.patch
Patch13:        ncl-5.1.0-includes.patch
Patch16:        ncl-5.2.1-secondary.patch
Patch17:        ncl-proj8.patch
Requires:       %{name}-common = %{version}-%{release}
Requires:       udunits2
Provides:       ncarg = %{version}-%{release}
Obsoletes:      ncarg < %{version}-%{release}
# oreon:deps
BuildRequires:  /bin/csh
BuildRequires:  byacc
BuildRequires:  cairo-devel
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  flexiblas-devel
BuildRequires:  g2clib-static
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gdal-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf-devel
BuildRequires:  hdf-static
BuildRequires:  imake
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  netcdf-fortran-devel
BuildRequires:  proj-devel
BuildRequires:  udunits2-devel
# /oreon:deps
%description
NCAR Command Language (NCL) is an interpreted language designed specifically
for scientific data processing and visualization.  Portable, robust, and free,
NCL supports netCDF3/4, GRIB1/2, HDF-SDS, HDF4-EOS, binary, shapefiles, and
ASCII files.  Numerous analysis functions are built-in.  High quality graphics
are easily created and customized with hundreds of graphic resources.  Many
example scripts and their corresponding graphics are available.

%package common
Summary:        Common files for NCL and NCAR Graphics
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description common
%{summary}.

%package devel
Summary:        Development files for NCL and NCAR Graphics
Requires:       %{name} = %{version}-%{release}
Requires:       cairo-devel
Provides:       ncl-static = %{version}-%{release}
Provides:       ncarg-devel = %{version}-%{release}
Obsoletes:      ncarg-devel < %{version}-%{release}
%description devel
%{summary}.

%package examples
Summary:        Example programs and data using NCL
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch
%description examples
Example programs and data using NCL.

%prep

%setup -q -n ncl-%{version}
%patch -P0 -p1 -b .paths
%patch -P1 -p1 -b .deps
%patch -P2 -p1 -b .ppc64
%patch -P3 -p1 -b .libs
%patch -P4 -p1 -b .format
%patch -P5 -p1 -b .boz
%patch -P6 -p1 -b .gdal
%patch -P7 -p1 -b .hdf
%patch -P8 -p1 -b .gcc15
%patch -P9 -p1 -b .nc_set_log_level
%patch -P10 -p1 -b .no_install_dep
%patch -P11 -p1 -b .build_n_scripts
%patch -P12 -p1 -b .netcdff
%patch -P13 -p1 -b .includes
%patch -P16 -p1 -b .secondary
%patch -P17 -p1 -b .proj

sed -ri -e 's,-lblas_ncl,-l%{blaslib},' \
        -e 's,-llapack_ncl,-l%{blaslib},' config/Project
#Spurrious exec permissions
find -name '*.[fh]' -exec chmod -x {} +

#Use ppc config if needed
%ifarch ppc ppc64
cp config/LINUX.ppc32.GNU config/LINUX
%endif

#Fixup LINUX config (to expose vsnprintf prototype)
sed -i -e '/StdDefines/s/-DSYSV/-D_ISOC99_SOURCE/' config/LINUX

rm -rf external/blas external/lapack

# fix the install directories, etc.
sed -e 's;@prefix@;%{_prefix};' \
 -e 's;@mandir@;%{_mandir};' \
 -e 's;@datadir@;%{_datadir};' \
 -e 's;@libdir@;%{_libdir};' \
 -e 's;@g2clib@;%{g2clib};' \
 %{SOURCE1} > config/Site.local

#Setup the profile scripts
cp %{SOURCE2} %{SOURCE3} .
sed -i -e s,@LIB@,%{_lib},g ncarg.csh ncarg.sh

sed -i -e 's;load "\$NCARG_ROOT/lib/ncarg/nclex\([^ ;]*\);loadscript(ncargpath("nclex") + "\1);' \
    -e 's;"\$NCARG_ROOT/lib/ncarg/\(data\|database\);ncargpath("\1") + ";' \
    -e 's;\$NCARG_ROOT/lib/ncarg/nclscripts;$NCARG_ROOT/share/ncarg/nclscripts;' \
    `find ni/src -name \*.ncl`

%build

./config/ymkmf
%global build_type_safety_c 0
FCOPTIONS="$RPM_OPT_FLAGS -fPIC -fno-second-underscore -fno-range-check -fopenmp"
make Build CCOPTIONS="$RPM_OPT_FLAGS -std=c99 -fPIC -fno-strict-aliasing -fopenmp -fcommon -DH5_USE_110_API" \
 F77=gfortran F77_LD=gfortran CTOFLIBS="-lgfortran" FCOPTIONS="$FCOPTIONS" COPT= FOPT=
%install
export NCARG=`pwd`
%make_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 0644 ncarg.csh ncarg.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
for x in {database,{font,graph}caps}
do
  mv $RPM_BUILD_ROOT%{_datadir}/ncarg/$x $RPM_BUILD_ROOT%{_libdir}/ncarg/
  ln -s ../../%{_lib}/ncarg/$x $RPM_BUILD_ROOT%{_datadir}/ncarg/
done
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/ncarg
for x in $RPM_BUILD_ROOT%{_datadir}/ncarg/*
do
  [ ! -e $RPM_BUILD_ROOT%{_prefix}/lib/ncarg/$(basename $x) ] &&
    ln -s ../../share/ncarg/$(basename $x) $RPM_BUILD_ROOT%{_prefix}/lib/ncarg/
done
rm -r $RPM_BUILD_ROOT%{_datadir}/ncarg/udunits
ln -s ../udunits $RPM_BUILD_ROOT%{_datadir}/ncarg/
for manpage in $RPM_BUILD_ROOT%{_mandir}/man3/*
do
   manname=`basename $manpage`
   mv $manpage $RPM_BUILD_ROOT%{_mandir}/man3/%{name}_$manname
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ncl-common -f %{oreon_filedir}/ncl-common.list
%files -n ncl-devel -f %{oreon_filedir}/ncl-devel.list
%files -n ncl-examples -f %{oreon_filedir}/ncl-examples.list

%changelog

%autochangelog
