%global source0_hash none

#global pre RC1

%if %{defined rhel} || %{defined flatpak}
%bcond_with mingw
%else
%bcond_with mingw
%endif

Name:          shapelib
Version:       1.6.3
Release:       1%{?dist}
Summary:       C library for handling ESRI Shapefiles
# The core library is dual-licensed LGPLv2 or MIT.
# Some contributed files have different licenses:
# - contrib/csv2shp.c: GPLv2+
# - contrib/dbfinfo.c: Public domain
# - contrib/dbfcat.c:  Public domain
License:       (LGPL-2.0-or-later OR MIT) AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:           http://shapelib.maptools.org/
Source0:       http://download.osgeo.org/shapelib/%{name}-%{version}%{?pre:%pre}.tar.gz
# Man pages from debian package
# wget https://salsa.debian.org/debian-gis-team/shapelib/-/archive/master/shapelib-master.tar.gz
# tar --strip-components=2 -xvf shapelib-master.tar.gz shapelib-master/debian/man
# rm -r man
# Add library version suffix for mingw dlls
Patch1:        shapelib_libver.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: proj-devel >= 4.4.1
# For man pages
BuildRequires: rubygem-ronn

%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-proj

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils
BuildRequires: mingw64-proj
%endif


%description
The Shapefile C Library provides the ability to write
simple C programs for reading, writing and updating (to a
limited extent) ESRI Shapefiles, and the associated
attribute file (.dbf).


%package devel
Summary:       Development files for shapelib
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libshp and the appropriate header files.


%package tools
Summary:       shapelib utility programs
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains various utility programs distributed with shapelib.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw32-%{name}-static < 1.6.2-1
Provides:      mingw32-%{name}-static = %{version}-%{release}

%description -n mingw32-%{name}
%{summary}.


%package -n mingw32-%{name}-tools
Summary:       Tools for the  MinGW Windows %{name} library
Requires:      mingw32-%{name} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{name}-tools
%{summary}.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw64-%{name}-static < 1.6.2-1
Provides:      mingw64-%{name}-static = %{version}-%{release}

%description -n mingw64-%{name}
%{summary}.


%package -n mingw64-%{name}-tools
Summary:       Tools for the  MinGW Windows %{name} library
Requires:      mingw64-%{name} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{name}-tools
%{summary}.
%endif


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1


%build
# Native build
%cmake -DBUILD_TESTING=OFF -DUSE_RPATH=OFF -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DCMAKE_INSTALL_CMAKEDIR=%{_libdir}/cmake/%{name}
%cmake_build

%if %{with mingw}
# MinGW build
MINGW32_CMAKE_ARGS="-DCMAKE_INSTALL_CMAKEDIR=%{mingw32_libdir}/cmake/%{name}" \
MINGW64_CMAKE_ARGS="-DCMAKE_INSTALL_CMAKEDIR=%{mingw64_libdir}/cmake/%{name}" \
%mingw_cmake -DBUILD_TESTING=OFF
%mingw_make_build
%endif


%install
%cmake_install
%if %{with mingw}
%mingw_make_install
%endif


%{?mingw_debug_install_post}


%files
%doc README README.tree ChangeLog web/*.html
%license LICENSE*
%{_libdir}/libshp.so.%{version}
%{_libdir}/libshp.so.4*

%files devel
%{_includedir}/shapefil.h
%{_libdir}/libshp.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%files tools
%doc contrib/doc/
%{_bindir}/*
%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE*
%{mingw32_bindir}/libshp-4.dll
%{mingw32_includedir}/shapefil.h
%{mingw32_libdir}/libshp.dll.a
%{mingw32_libdir}/pkgconfig/shapelib.pc
%{mingw32_libdir}/cmake/%{name}/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{name}
%license LICENSE*
%{mingw64_bindir}/libshp-4.dll
%{mingw64_includedir}/shapefil.h
%{mingw64_libdir}/libshp.dll.a
%{mingw64_libdir}/pkgconfig/shapelib.pc
%{mingw64_libdir}/cmake/%{name}/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe
%endif


%changelog
%autochangelog

