%global source0_hash 78d77cc8216843b78d14b41970ed9de3dedc34b9cd50ad84af2849c63a41eff8
Name:           GeographicLib
Version:        2.7
Release:        3%{?dist}
Summary:        Library for geographic coordinate transformations
License:        MIT
URL:            https://github.com/geographiclib/geographiclib
Source0:        https://github.com/geographiclib/geographiclib/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
GeographicLib is a small set of C++ classes for performing conversions 
between geographic, UTM, UPS, MGRS, geocentric, and local Cartesian 
coordinates, for gravity (e.g., EGM2008), geoid height and geomagnetic 
field (e.g., WMM2010) calculations, and for solving geodesic problems. 
The emphasis is on returning accurate results with errors close to round-off 
(about 5–15 nanometers). New accurate algorithms for Geodesics on an 
ellipsoid of revolution and Transverse Mercator projection have been 
developed for this library. The functionality of the library can be accessed 
from user code, from the Utility programs provided, or via the 
Implementations in other languages.

%package devel
Summary:        Development files and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
%description devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary:        Development documentation for %name
BuildArch:      noarch
%description doc
This package contains doxygen-generated html API documentation for
the %{name} library.

%package -n mingw32-%{name}
Summary:        MinGW Windows %{name} library
BuildArch:      noarch
%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:        MinGW Windows %{name} library
BuildArch:      noarch
%description -n mingw64-%{name}
MinGW Windows %{name} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir geographiclib-%{version}
%oreon_prep
%build

%cmake \
  -DLIBDIR=%{_lib} \
  -DPKGDIR=%{_lib}/pkgconfig \
  -DSBINDIR=bin \
  -DCMAKEDIR=%{_lib}/cmake/%{name} \
  -DEXAMPLEDIR=%{_defaultdocdir}/%{name}/examples
%cmake_build
%mingw_cmake -DDOCDIR= -DMANDIR= -DEXAMPLEDIR=
%mingw_make_build
%install
%cmake_install
%mingw_make_install
%mingw_debug_install_post
%oreon_autofiles GeographicLib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles GeographicLib-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-GeographicLib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-GeographicLib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%cmake_build -t testprograms
%ctest
%files -f %{oreon_filedir}/main.list
%files -n GeographicLib-devel -f %{oreon_filedir}/GeographicLib-devel.list
%files -n GeographicLib-doc -f %{oreon_filedir}/GeographicLib-doc.list
%files -n mingw32-GeographicLib -f %{oreon_filedir}/mingw32-GeographicLib.list
%files -n mingw64-GeographicLib -f %{oreon_filedir}/mingw64-GeographicLib.list

%changelog

%autochangelog
