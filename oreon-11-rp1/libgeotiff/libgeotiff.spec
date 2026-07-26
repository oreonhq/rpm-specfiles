%global source0_hash c598d04fdf2ba25c4352844dafa81dde3f7fd968daa7ad131228cd91e9d3dc47

%if 0%{?rhel} >= 9
%bcond_with mingw
%else
%bcond_without mingw
%endif

Name:          libgeotiff
Version:       1.7.4
Release:       5%{?dist}

Summary:       GeoTIFF format library
License:       MIT
URL:           http://trac.osgeo.org/geotiff/
Source:        http://download.osgeo.org/geotiff/%{name}/%{name}-%{version}.tar.gz

# Add version suffix to mingw library
Patch:         libgeotiff_cmake.patch
# Use standard Config.cmake files
# https://github.com/OSGeo/libgeotiff/pull/135.patch
Patch:         135_cherry-picked.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libtiff-devel
BuildRequires: libjpeg-devel
BuildRequires: proj-devel
BuildRequires: zlib-devel

%if %{with mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libjpeg
BuildRequires: mingw32-proj
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libjpeg
BuildRequires: mingw64-proj
BuildRequires: mingw64-zlib
%endif

%description
GeoTIFF represents an effort by over 160 different remote sensing,
GIS, cartographic, and surveying related companies and organizations
to establish a TIFF based interchange format for georeferenced
raster imagery.

%package devel
Summary:	Development library and header for the GeoTIFF file format library
Requires:	pkgconfig libtiff-devel
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The GeoTIFF library provides support for development of geotiff image format.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
Obsoletes:     mingw32-%{name}-static
BuildArch:     noarch

%description -n mingw32-%{name}
%{summary}.

%package -n mingw32-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
Requires:      mingw32-%{name} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{name}-tools
%{summary}.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
Obsoletes:     mingw64-%{name}-static
BuildArch:     noarch

%description -n mingw64-%{name}
%{summary}.

%package -n mingw64-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
Requires:      mingw64-%{name} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{name}-tools
%{summary}.

%{?mingw_debug_package}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
export CMAKE_BUILD_TYPE=RelWithDebInfo
# Native build
%cmake -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{name} -DBUILD_DOC=OFF
%cmake_build

%if %{with mingw}
# MinGW build
MINGW32_CMAKE_ARGS=-DCMAKE_INSTALL_INCLUDEDIR=%{mingw32_includedir}/%{name} \
MINGW64_CMAKE_ARGS=-DCMAKE_INSTALL_INCLUDEDIR=%{mingw64_includedir}/%{name} \
%mingw_cmake -DBUILD_DOC=OFF
%mingw_make_build
%endif

%install
%cmake_install
%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%endif

%check
%ctest

%files
%license LICENSE
%doc ChangeLog
%{_bindir}/applygeo
%{_bindir}/geotifcp
%{_bindir}/listgeo
%{_bindir}/makegeo
%{_libdir}/%{name}.so.5*
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/GeoTIFF/

%if %{with mingw}
%files -n mingw32-%{name}
%doc ChangeLog README
%license COPYING
%{mingw32_bindir}/libgeotiff-5.dll
%{mingw32_includedir}/%{name}/
%{mingw32_datadir}/*
%{mingw32_libdir}/libgeotiff.dll.a
%{mingw32_libdir}/pkgconfig/libgeotiff.pc
%{mingw32_libdir}/cmake/GeoTIFF/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{name}
%doc ChangeLog README
%license COPYING
%{mingw64_bindir}/libgeotiff-5.dll
%{mingw64_includedir}/%{name}/
%{mingw64_datadir}/*
%{mingw64_libdir}/libgeotiff.dll.a
%{mingw64_libdir}/pkgconfig/libgeotiff.pc
%{mingw64_libdir}/cmake/GeoTIFF/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe
%endif

%changelog
%autochangelog
