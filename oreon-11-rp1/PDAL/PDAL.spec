%global source0_hash none

#global __cmake_in_source_build 1

# BZ 1996330
#ifarch ppc64le
#global _lto_cflags %nil
#endif

%bcond_with docs

Summary:	Point Data Abstraction Library
Name:		PDAL
Version:	2.9.3
Release:	3%{?dist}
# The code is licensed BSD except for:
# - filters/private/csf/* and plugins/i3s/lepcc/* are ASL 2.0
# - vendor/arbiter/*, plugins/nitf/io/nitflib.h and plugins/oci/io/OciWrapper.* are Expat/MIT
# - plugins/e57/libE57Format/{src,include}/* is Boost
License:	BSD-3-Clause AND Apache-2.0 AND MIT AND BSL-1.0
URL:		https://www.pdal.io
Source:		https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}-src.tar.bz2
# commented out due to size (320 MB larger)
#Source1:	http://download.osgeo.org/proj/vdatum/%%{name}-vdatums.zip
# originals
#Source1:   http://download.osgeo.org/proj/vdatum/egm08_25/egm08_25.gtx
#Source2:   http://download.osgeo.org/proj/vdatum/egm08_25/egm08_25.txt
#Source3:   http://download.osgeo.org/proj/vdatum/egm96_15/egm96_15.gtx
#Source4:   http://download.osgeo.org/proj/vdatum/egm96_15/WW15MGH.TXT
#Source5:   http://download.osgeo.org/proj/vdatum/vertcon/README.TXT
#Source6:   http://download.osgeo.org/proj/vdatum/vertcon/vertconc.gtx
#Source7:   http://download.osgeo.org/proj/vdatum/vertcon/vertcone.gtx
#Source8:   http://download.osgeo.org/proj/vdatum/vertcon/vertconw.gtx
#Source9:   http://download.osgeo.org/proj/vdatum/usa_geoid1999.zip
#Source10:  http://download.osgeo.org/proj/vdatum/usa_geoid2003.zip
#Source11:  http://download.osgeo.org/proj/vdatum/usa_geoid2009.zip
#Source12:  http://download.osgeo.org/proj/vdatum/usa_geoid2012.zip
#Source13:  http://download.osgeo.org/proj/vdatum/usa_geoid2012b.zip

# Unbundle some bundled libraries
Patch0:		PDAL_unbundle.patch
# Read GDAL_INCLUDE_DIR from interface
Patch1:         PDAL_gdalinc.patch
# Add missing cstdint include
Patch2:         PDAL_cstdint.patch

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	eigen3-devel
BuildRequires:	gcc-c++
BuildRequires:	gdal
BuildRequires:	gdal-devel
BuildRequires:	geos-devel
BuildRequires:	gtest-devel
BuildRequires:	hdf5-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	libgeotiff-devel
BuildRequires:	libpq-devel
BuildRequires:	libxml2-devel
BuildRequires:	libzstd-devel
BuildRequires:  make
BuildRequires:	netcdf-cxx-devel
BuildRequires:	postgresql-devel
BuildRequires:	postgresql-server
BuildRequires:	proj-devel
BuildRequires:	python3-devel
BuildRequires:	python3-numpy
BuildRequires:	qhull-devel
BuildRequires:	sqlite-devel
BuildRequires:	zlib-devel

%if %{with docs}
BuildRequires:	python3-breathe
BuildRequires:	python3-sphinx
BuildRequires:  python3-sphinx-notfound-page
BuildRequires:	python3-sphinxcontrib-bibtex
BuildRequires:  python3-sphinxcontrib-spelling
BuildRequires:	python3-sphinx_rtd_theme
%endif

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	bash-completion

# https://github.com/connormanning/arbiter bundled in vendor/arbiter
Provides:	bundled(arbiter)
# https://github.com/mkazhdan/PoissonRecon bundled in vendor/kazhdan
Provides:	bundled(PoissonRecon)
# https://github.com/jlblancoc/nanoflann bundled in vendor/nanoflann
Provides:	bundled(nanoflann)
# https://github.com/nlohmann/json bundled in vendor/nlohmann
Provides:	bundled(nlohmann)

%description
PDAL is a BSD licensed library for translating and manipulating point cloud
data of various formats. It is a library that is analogous to the GDAL raster
library. PDAL is focused on reading, writing, and translating point cloud
data from the ever-growing constellation of data formats. While PDAL is not
explicitly limited to working with LiDAR data formats, its wide format
coverage is in that domain.

PDAL is related to Point Cloud Library (PCL) in the sense that both work with
point data, but PDAL’s niche is data translation and processing pipelines, and
PCL’s is more in the algorithmic exploitation domain. There is cross over of
both niches, however, and PDAL provides a user the ability to exploit data
using PCL’s techniques.

%package devel
Summary:	PDAL development header files and libraries
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The pdal-devel package contains the header files and libraries needed to
compile C or C++ applications which will directly interact with PDAL.

%package libs
Summary:	The shared libraries required for PDAL

%description libs
The pdal-libs package provides the essential shared libraries for any
PDAL client program or interface. You will need to install this package
to use PDAL

# commented out due to size
#%%package vdatums
#Summary:	Vertical datum and geoid files for PDAL
#Requires:	%%{name} = %%{version}-%%{release}
#
#%%description vdatums
#This package contains vertical datum and geoid files for PDAL.

%if %{with docs}
%package doc
Summary:	Documentation for PDAL
BuildArch:	noarch

%description doc
This package contains documentation for PDAL.
%endif

# We don't want to provide private PDAL extension libs (to be verified)
%global __provides_exclude_from ^%{_libdir}/libpdal_plugin.*\.so.*$

%prep
%autosetup -p1 -n %{name}-%{version}-src

# Wrong perms on some source files
chmod 0644 pdal/DynamicLibrary.cpp pdal/private/DynamicLibrary.hpp

# Remove some bundled libraries
rm -rf vendor/{eigen,gtest,pdalboost}

%build
%cmake	-D PDAL_LIB_INSTALL_DIR:PATH=%{_lib} \
	-D CMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
	-D CMAKE_VERBOSE_MAKEFILE=ON  \
	-D GEOTIFF_INCLUDE_DIR=%{_includedir}/libgeotiff \
	-D BUILD_PGPOINTCLOUD_TESTS:BOOL=OFF \
	-D WITH_COMPLETION=ON \
	-D WITH_LAZPERF=ON \
	-D WITH_TESTS=ON \
	-D PDAL_HAVE_LIBGEOTIFF=ON \
	-D PDAL_HAVE_LIBXML2=ON \
	-D POSTGRESQL_INCLUDE_DIR=%{_includedir}/pgsql \
	-D POSTGRESQL_LIBRARIES=%{_libdir}/libpq.so .

%cmake_build

# Build documentation
%if %{with docs}
# dependencies yet missing for EPEL8 BZ#1808766
(
cd doc
export PYTHONPATH=$PWD/doc/_ext
sphinx-build -b html . build/html
)
%endif

%install
%cmake_install

# commented out due to size
## unpack vertical datums
#mkdir -p %%{buildroot}%%{_datadir}/proj
#mkdir vdatum
#pushd vdatum
#unzip -o %%{SOURCE1}
#mv *.gtx  %%{buildroot}%%{_datadir}/proj/
#popd
#rm -rf vdatum

%check
#ctest

%files
%{_bindir}/pdal
%{_datadir}/bash-completion/completions/pdal

%files libs
%license LICENSE.txt
%license vendor/arbiter/LICENSE
%license plugins/e57/libE57Format/LICENSE.md
%{_libdir}/libpdalcpp.so.19*
%{_libdir}/libpdal_plugin_kernel_fauxplugin.so.19*
%{_libdir}/libpdal_plugin_reader_pgpointcloud.so.19*
%{_libdir}/libpdal_plugin_writer_pgpointcloud.so.19*

%files devel
%{_bindir}/pdal-config
%{_includedir}/pdal/
# drop unversioned symbolic links (BZ#1841616)
%exclude %{_libdir}/libpdal_plugin_kernel_fauxplugin.so
%exclude %{_libdir}/libpdal_plugin_reader_pgpointcloud.so
%exclude %{_libdir}/libpdal_plugin_writer_pgpointcloud.so
%{_libdir}/libpdalcpp.so
%{_libdir}/cmake/PDAL/
%{_libdir}/pkgconfig/*.pc

# commented out due to size
#%%files vdatums
#%%attr(0644,root,root) %%{_datadir}/proj/*.gtx

%if %{with docs}
%files doc
%doc doc/build/html
%license LICENSE.txt
%endif

%changelog
%autochangelog
