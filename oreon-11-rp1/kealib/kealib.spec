%global source0_hash 815b8d335b8d4b9048baf863cdd3959d12210f158a86f6a0d1954c7d39ce6db0
Name:		kealib
Version:	1.6.2
Release:        1%{?dist}
Summary:        HDF5 Based Raster File Format as a GDAL plugin
License:	MIT
URL:		http://kealib.org/
Source0:        https://github.com/ubarsc/kealib/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         kealib-cmakedir.patch
Patch1:         kealib-gdal312.patch
Requires:	gdal
# oreon:deps
BuildRequires:  ccache
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel
BuildRequires:  hdf5-devel
BuildRequires:  proj-devel
# /oreon:deps
%description
KEALib is a project to provide an implementation of the GDAL
specification within the the HDF5 file format. Specifically, the format
will support raster attribute tables (commonly not included within
other formats), image pyramids, GDAL meta-data, in-built statistics
while also providing large file handling with compression used
throughout the file.

%package devel
Summary:     KEA development headers
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description devel
KEA development headers

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# fix wrong lib entry
sed -i 's+set (PROJECT_LIBRARY_DIR lib)+set (PROJECT_LIBRARY_DIR %{_lib})+g' %{_builddir}/%{name}-%{version}/CMakeLists.txt

%build

%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING="Release" \
    -DGDAL_INCLUDE_DIR:PATH=%{_includedir}/gdal \
    -DGDAL_LIB_PATH:PATH=%{_libdir} \
    -DHDF5_INCLUDE_DIR:PATH=%{_includedir} \
    -DHDF5_LIB_PATH:PATH=%{_libdir} \
    -DHDF5_STATIC_LIBS:BOOL=OFF \
    -DLIBKEA_WITH_GDAL:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} .
%cmake_build
%install
%cmake_install
%ifnarch %ix86
mkdir -p %{buildroot}%{_libdir}/ %{buildroot}%{_libdir}/gdalplugins/
mv %{buildroot}%{_prefix}/lib/libkea* %{buildroot}%{_libdir}/
mv %{buildroot}%{_prefix}/lib/gdalplugins/* %{buildroot}%{_libdir}/gdalplugins/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n kealib-devel -f %{oreon_filedir}/kealib-devel.list

%changelog

%autochangelog
