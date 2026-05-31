%global source0_hash 3c20919cda9a505db07b5216baa980bacdaa0702da715b43f176fb07eff7e716

# When distributed in RHEL, EPEL shouldn't be used. Mingw shouldn't be in RHEL,
# so it shouldn't be used anywhere, but in fedora.
%if 0%{?fedora} || (0%{?oreon} >= 11)
%bcond_without mingw
%else
%bcond_with mingw
%endif

Name:          geos
Version:       3.14.1
Release:       2%{?dist}
Summary:       GEOS is a C++ port of the Java Topology Suite

License:       LGPL-2.1-only
URL:           http://trac.osgeo.org/geos/
Source0:        http://download.osgeo.org/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++

%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
%endif


%description
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). As such, it aims to contain the complete functionality of
JTS in C++. This includes all the OpenGIS "Simple Features for SQL" spatial
predicate functions and spatial operators, as well as specific JTS topology
functions such as IsValid()


%package devel
Summary:       Development files for GEOS
Requires:      %{name} = %{version}-%{release}

%description devel
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). As such, it aims to contain the complete functionality of
JTS in C++. This includes all the OpenGIS "Simple Features for SQL" spatial
predicate functions and spatial operators, as well as specific JTS topology
functions such as IsValid().

This package contains the development files to build applications that
use GEOS.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows GEOS library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows GEOS library.


%package -n mingw64-%{name}
Summary:       MinGW Windows GEOS library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows GEOS library.


%{?mingw_debug_package}
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
# Native build
%cmake -DDISABLE_GEOS_INLINE=ON -DBUILD_DOCUMENTATION=ON
%cmake_build
%cmake_build --target docs

%if %{with mingw}
# MinGW build
%mingw_cmake -DDISABLE_GEOS_INLINE=ON -DVERSION_MINGW_SHARED_LIBS=ON
%mingw_make_build
%endif


%install
%cmake_install

%if %{with mingw}
%mingw_make_install
%endif

# Drop cross-compiled geos-config which is not useful
rm -f %{buildroot}%{mingw32_bindir}/geos-config
rm -f %{buildroot}%{mingw64_bindir}/geos-config


%if %{with mingw}
%mingw_debug_install_post
%endif


%check
%ifnarch s390x
# FIXME: test_docs failed on F42 mass rebuild, retest in future
%ctest -E test_docs
%endif


%files
%doc AUTHORS NEWS.md README.md
%license COPYING
%{_bindir}/geosop
%{_libdir}/libgeos.so.3.14.1
%{_libdir}/libgeos_c.so.1*

%files devel
%doc %{__cmake_builddir}/doxygen/doxygen_docs
%{_bindir}/geos-config
%{_includedir}/geos/
%{_includedir}/geos_c.h
%{_includedir}/geos.h
%{_libdir}/libgeos_c.so
%{_libdir}/libgeos.so
%{_libdir}/cmake/GEOS/
%{_libdir}/pkgconfig/%{name}.pc

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/geosop.exe
%{mingw32_bindir}/libgeos-3.14.1.dll
%{mingw32_bindir}/libgeos_c-1.dll
%{mingw32_includedir}/geos/
%{mingw32_includedir}/geos_c.h
%{mingw32_includedir}/geos.h
%{mingw32_libdir}/libgeos.dll.a
%{mingw32_libdir}/libgeos_c.dll.a
%{mingw32_libdir}/cmake/GEOS/
%{mingw32_libdir}/pkgconfig/%{name}.pc

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/geosop.exe
%{mingw64_bindir}/libgeos-3.14.1.dll
%{mingw64_bindir}/libgeos_c-1.dll
%{mingw64_includedir}/geos/
%{mingw64_includedir}/geos_c.h
%{mingw64_includedir}/geos.h
%{mingw64_libdir}/libgeos.dll.a
%{mingw64_libdir}/libgeos_c.dll.a
%{mingw64_libdir}/cmake/GEOS/
%{mingw64_libdir}/pkgconfig/%{name}.pc
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.14.1-2
- Import
