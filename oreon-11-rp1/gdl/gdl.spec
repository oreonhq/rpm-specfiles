%global source0_hash 7f2b39cec13d7589e7d810ca2197ffb080f80d3de0de440a8cba26e21cadf8a1
%global commit f29c1fa51cfe3771ad156a05cc3962d4ffbbe102
%global shortcommit %(c=%{commit}; echo ${c:0:7})
ExcludeArch: %{ix86}
%ifarch s390x
%bcond_with grib
%else
%bcond_without grib
%endif
%bcond_without java
%if 0%{?el8}
%bcond_with qhull
%else
%bcond_without qhull
%endif
Name:           gdl
Version:        1.1.3
Release:        1%{?dist}
Summary:        GNU Data Language
License:        GPL-2.0-or-later
URL:            http://gnudatalanguage.sourceforge.net/
Source0:        https://github.com/gnudatalanguage/gdl/releases/download/v%{version}/gdl-v%{version}.tar.gz
Source1:        xorg.conf
Patch1:         gdl-antlr.patch
%if %{with java}
%endif
Provides:       bundled(dSFMT)
Provides:       bundled(plplot) = 5.15.0
%if %{with grib}
%endif
%if %{with qhull}
%endif
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Requires:       hdf5 = %{_hdf5_version}
# oreon:deps
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  antlr-C++
BuildRequires:  antlr-tool
BuildRequires:  cmake
BuildRequires:  eccodes-devel
BuildRequires:  eigen3-static
BuildRequires:  expat-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  gnu-free-mono-fonts
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
BuildRequires:  gsl-devel
BuildRequires:  hdf-static
BuildRequires:  hdf5-devel
BuildRequires:  java-25-devel
BuildRequires:  libdivide-devel
BuildRequires:  libgeotiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtirpc-devel
BuildRequires:  ncurses-devel
BuildRequires:  netcdf-devel
BuildRequires:  proj-devel
BuildRequires:  pslib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpy
BuildRequires:  qhull-devel
BuildRequires:  readline-devel
BuildRequires:  shapelib-devel
BuildRequires:  udunits2-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
A free IDL (Interactive Data Language) compatible incremental compiler
(i.e. runs IDL programs). IDL is a registered trademark of Research
Systems Inc.

%package        common
Summary:        Common files for GDL
Requires:       %{name}-runtime = %{version}-%{release}
Requires:       gnu-free-mono-fonts
Requires:       gnu-free-sans-fonts
Requires:       gnu-free-serif-fonts
BuildArch:      noarch
%description    common
Common files for GDL

%package        -n python%{python3_pkgversion}-gdl
%{?python_provide:%python_provide python%{python3_pkgversion}-gdl}
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:        GDL python module
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
%description    -n python%{python3_pkgversion}-gdl
%{summary}.

%prep

%setup -q -n %{name}-v%{version}
rm -rf src/antlr src/libdivide.h
# Not yet possible to build with external dSFMT
#rm -r src/dSFMT
%patch -P1 -p1 -b .antlr

pushd src
for f in *.g
do
  antlr $f
done
popd

%global _vpath_builddir %{_target_platform}-${variant}
%global __python %{__python3}
%global python_sitearch %{python3_sitearch}
%global cmake_opts \\\
   -DGDL_LIB_DIR:PATH=%{_libdir}/gnudatalanguage \\\
   -DGEOTIFF_INCLUDE_DIR=%{_includedir}/libgeotiff \\\
   -DGRIB=ON \\\
   -DOPENMP=ON \\\
   -DPL_FREETYPE_FONT_PATH:PATH="/usr/share/fonts/gnu-free" \\\
   -DPYTHON_EXECUTABLE=%{__python} \\\
   -DWXWIDGETS=ON \\\
   %{!?with_grib:-DGRIB=OFF} \\\
   %{!?with_qhull:-DQHULL=OFF} \\\
%{nil}
# TODO - build an mpi version
#           INCLUDES="-I/usr/include/mpich2" \
#           --with-mpich=%{_libdir}/mpich2 \

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
export CXXFLAGS="%optflags -fcommon"
variant=default
%cmake %{cmake_opts}
%cmake_build
variant=python
%cmake %{cmake_opts} -DPYTHON_MODULE=ON
%cmake_build
%install
variant=default
%cmake_install
variant=python
%cmake_install
install -d -m 0755 $RPM_BUILD_ROOT%{python_sitearch}
%if "%{_lib}" != "lib"
mv $RPM_BUILD_ROOT%{_prefix}/lib/python*/site-packages/GDL.so \
  $RPM_BUILD_ROOT%{python_sitearch}/GDL.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
