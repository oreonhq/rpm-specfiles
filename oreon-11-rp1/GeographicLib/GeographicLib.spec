%global source0_hash 78d77cc8216843b78d14b41970ed9de3dedc34b9cd50ad84af2849c63a41eff8

Name:           GeographicLib
Version:        2.7
Release:        3%{?dist}
Summary:        Library for geographic coordinate transformations

License:        MIT
URL:            https://github.com/geographiclib/geographiclib
Source0:        https://github.com/geographiclib/geographiclib/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++

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

%autosetup -p1 -n geographiclib-%{version}

%build
# Native build
%cmake \
  -DLIBDIR=%{_lib} \
  -DPKGDIR=%{_lib}/pkgconfig \
  -DSBINDIR=bin \
  -DCMAKEDIR=%{_lib}/cmake/%{name} \
  -DEXAMPLEDIR=%{_defaultdocdir}/%{name}/examples
%cmake_build
# MinGW build
%mingw_cmake -DDOCDIR= -DMANDIR= -DEXAMPLEDIR=
%mingw_make_build

%install
# Native build
%cmake_install
# MinGW build
%mingw_make_install

%mingw_debug_install_post

%check
%cmake_build -t testprograms
%ctest

%files
%doc AUTHORS NEWS
%license LICENSE.txt
%{_bindir}/Cart3Convert
%{_bindir}/CartConvert
%{_bindir}/Conformal3Proj
%{_bindir}/ConicProj
%{_bindir}/GeoConvert
%{_bindir}/Geod3Solve
%{_bindir}/GeodesicProj
%{_bindir}/GeodSolve
%{_bindir}/GeoidEval
%{_bindir}/Gravity
%{_bindir}/IntersectTool
%{_bindir}/MagneticField
%{_bindir}/Planimeter
%{_bindir}/RhumbSolve
%{_bindir}/TransverseMercatorProj
%{_bindir}/geographiclib-get-geoids
%{_bindir}/geographiclib-get-gravity
%{_bindir}/geographiclib-get-magnetic
%{_libdir}/libGeographicLib.so.26*
%{_mandir}/man1/*.1.*
%{_mandir}/man8/*.8.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libGeographicLib.so
%{_libdir}/cmake/GeographicLib
%{_libdir}/pkgconfig/geographiclib.pc

%files doc
%license LICENSE.txt
%doc %{_defaultdocdir}/%{name}/

%files -n mingw32-%{name}
%license LICENSE.txt
%{mingw32_bindir}/Cart3Convert.exe
%{mingw32_bindir}/CartConvert.exe
%{mingw32_bindir}/Conformal3Proj.exe
%{mingw32_bindir}/ConicProj.exe
%{mingw32_bindir}/GeoConvert.exe
%{mingw32_bindir}/Geod3Solve.exe
%{mingw32_bindir}/GeodesicProj.exe
%{mingw32_bindir}/GeodSolve.exe
%{mingw32_bindir}/GeoidEval.exe
%{mingw32_bindir}/Gravity.exe
%{mingw32_bindir}/IntersectTool.exe
%{mingw32_bindir}/MagneticField.exe
%{mingw32_bindir}/Planimeter.exe
%{mingw32_bindir}/RhumbSolve.exe
%{mingw32_bindir}/TransverseMercatorProj.exe
%{mingw32_bindir}/libGeographicLib.dll
%{mingw32_includedir}/%{name}/
%{mingw32_libdir}/libGeographicLib.dll.a
%{mingw32_libdir}/cmake/GeographicLib/
%{mingw32_libdir}/pkgconfig/geographiclib.pc

%files -n mingw64-%{name}
%license LICENSE.txt
%{mingw64_bindir}/Cart3Convert.exe
%{mingw64_bindir}/CartConvert.exe
%{mingw64_bindir}/Conformal3Proj.exe
%{mingw64_bindir}/ConicProj.exe
%{mingw64_bindir}/GeoConvert.exe
%{mingw64_bindir}/Geod3Solve.exe
%{mingw64_bindir}/GeodesicProj.exe
%{mingw64_bindir}/GeodSolve.exe
%{mingw64_bindir}/GeoidEval.exe
%{mingw64_bindir}/Gravity.exe
%{mingw64_bindir}/IntersectTool.exe
%{mingw64_bindir}/MagneticField.exe
%{mingw64_bindir}/Planimeter.exe
%{mingw64_bindir}/RhumbSolve.exe
%{mingw64_bindir}/TransverseMercatorProj.exe
%{mingw64_bindir}/libGeographicLib.dll
%{mingw64_includedir}/%{name}/
%{mingw64_libdir}/libGeographicLib.dll.a
%{mingw64_libdir}/cmake/GeographicLib/
%{mingw64_libdir}/pkgconfig/geographiclib.pc

%changelog
%autochangelog
