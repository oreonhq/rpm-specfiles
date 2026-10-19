%global source0_hash 9d750d34576069bcc4f39677af08cde2862fbe4b8c0d9af504877c2fae2ae273
%global catch_version 1.9.6
%global variant_version 1.1.5
%global debug_package %{nil}
Name:           geometry-hpp
Version:        2.0.3
Release:        1%{?dist}
Summary:        Generic C++ interfaces for geometry types, collections, and features
License:        ISC
URL:            https://github.com/mapbox/geometry.hpp
Source0:        https://github.com/mapbox/geometry.hpp/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{url}/pull/74.patch#/geometry-hpp-optional-benchmarks.patch
Patch:          geometry-hpp-mason.patch
# oreon:deps
BuildRequires:  catch1-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mapbox-variant-devel
BuildRequires:  mapbox-variant-static
# /oreon:deps
%description
Provides header-only, generic C++ interfaces for geometry
types, geometry collections, and features.

These types are designed to be easy to parse and serialize
to GeoJSON and to be a robust and high performance container
for data processing and conversion.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Requires:       mapbox-variant-devel >= %{variant_version}
%description    devel
Provides header-only, generic C++ interfaces for geometry
types, geometry collections, and features.

These types are designed to be easy to parse and serialize
to GeoJSON and to be a robust and high performance container
for data processing and conversion.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n geometry.hpp-%{version}

%conf
%cmake -DWERROR:BOOL=OFF -DBENCHMARKS:BOOL=OFF

%build

%cmake_build
%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{_vpath_builddir}/unit-tests
%files -f %{oreon_filedir}/main.list
%files -n geometry-hpp-devel -f %{oreon_filedir}/geometry-hpp-devel.list

%changelog

%autochangelog
