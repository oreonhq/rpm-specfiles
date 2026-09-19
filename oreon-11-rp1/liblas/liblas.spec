%global source0_hash 72d0e479c8381ad7f0a072082fab28b9ff5089b1e4fbaeca376cf0ae10be4b9a

%global commit 0756b73ed41211d1bb8d9b96c6767f2350d8fe2b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           liblas
Version:        1.8.2
Release:        0.30%{?shortcommit:.git%shortcommit}%{?dist}
Summary:        Library for reading and writing the very common LAS LiDAR format

License:        BSD-3-Clause AND BSL-1.0
URL:            https://github.com/libLAS/libLAS
%if 0%{?commit:1}
Source0:        https://github.com/libLAS/libLAS/archive/%{commit}/libLAS-%{shortcommit}.tar.gz
%else
Source0:        https://download.osgeo.org/%{name}/libLAS-%{version}.tar.bz2
%endif

# Fix incorrect includedir and libdir paths
Patch1:         liblas_pkgconfig.patch
# Fix FTBFS with boost 1.73
Patch2:         liblas_boost173.patch
# Don't switch to std=c++11 if gdal is detected, liblas requires std=c++14 to build
Patch3:         liblas_stdc++14.patch
# Fix build with gcc15
Patch4:         liblas-gcc15.patch
# Increase minimum cmake version to 3.5
Patch5:         liblas_cmakever.patch
# Fix loading of cmake module not finding PROJ::proj
# https://github.com/libLAS/libLAS/issues/229
Patch6:         liblas-proj.patch

BuildRequires:  gcc-c++
BuildRequires:  boost-devel >= 1.53
BuildRequires:  cmake
BuildRequires:  gdal-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  laszip-devel
BuildRequires:  libgeotiff-devel
BuildRequires:  zlib-devel
# FIXME? 
#  The imported target "ZLIB::zlibstatic" references the file
#     "/usr/lib/libz.a"
#  but this file does not exist.
BuildRequires:  zlib-ng-compat-static

%description
libLAS is a C/C++ library for reading and writing the very common LAS LiDAR
format. The ASPRS LAS format is a sequential binary format used to store
data from LiDAR sensors and by LiDAR processing software for data
interchange and archival.

%package devel
Summary:	libLAS development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

Requires:	boost-devel >= 1.53
Requires:	gdal-devel
Requires:	laszip-devel
Requires:	libgeotiff-devel

%description devel
libLAS deveolpment files.

%package tools
Summary:	libLAS utility applications
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
libLAS utility applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?commit:1}
%autosetup -p1 -n libLAS-%{commit}
%else
%autosetup -p1 -n libLAS-%{version}
%endif

%build
%cmake \
        -DCMAKE_SKIP_RPATH:BOOL=ON \
        -DLIBLAS_LIB_SUBDIR:PATH="%{_lib}" \
        -DWITH_GDAL:BOOL=ON \
        -DWITH_LASZIP:BOOL=ON \
        -DWITH_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%exclude %{_datadir}/%{name}/
%{_libdir}/*.so.3
%{_libdir}/*.so.2.*

%files devel
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/cmake/libLAS/
%{_libdir}/pkgconfig/liblas.pc
%{_libdir}/*.so

%files tools
%doc AUTHORS README.txt
%{_bindir}/*

%changelog
%autochangelog
