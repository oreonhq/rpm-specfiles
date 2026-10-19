%global source0_hash 882b97aa3ae5db682c3b2dc8edef4e29bcc7ecea51c70592e71bc1f34112ad00
%bcond_with docs
Summary:        Point Data Abstraction Library
Name:		PDAL
Version:	2.10.2
Release:        1%{?dist}
License:	BSD-3-Clause AND Apache-2.0 AND MIT AND BSL-1.0
URL:		https://www.pdal.io
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}-src.tar.bz2
Patch0:		PDAL_unbundle.patch
Patch1:         PDAL_gdalinc.patch
Patch2:         PDAL_cstdint.patch
%if %{with docs}
%endif
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	bash-completion
Provides:	bundled(arbiter)
Provides:	bundled(PoissonRecon)
Provides:	bundled(nanoflann)
Provides:	bundled(nlohmann)
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  gdal
BuildRequires:  gdal-devel
BuildRequires:  geos-devel
BuildRequires:  gtest-devel
BuildRequires:  hdf5-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libgeotiff-devel
BuildRequires:  libpq-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  netcdf-cxx-devel
BuildRequires:  postgresql-devel
BuildRequires:  postgresql-server
BuildRequires:  proj-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  qhull-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%if %{with docs}
(
cd doc
export PYTHONPATH=$PWD/doc/_ext
sphinx-build -b html . build/html
)
%endif
%install
%cmake_install
%oreon_autofiles PDAL-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles PDAL-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n PDAL-devel -f %{oreon_filedir}/PDAL-devel.list
%files -n PDAL-libs -f %{oreon_filedir}/PDAL-libs.list

%changelog

%autochangelog
