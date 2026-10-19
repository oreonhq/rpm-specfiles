%global source0_hash none
%global forgeurl https://github.com/uber/h3
Version:        4.5.0
%forgemeta
Name:           h3
Release:        1%{?dist}
Summary:        Hexagonal hierarchical geospatial indexing system
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
H3 is a geospatial indexing system using a hexagonal grid that can be
(approximately) subdivided into finer and finer hexagonal grids, combining the
benefits of a hexagonal grid with S2's hierarchical subdivisions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

%forgeautosetup -p1

%build

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DENABLE_DOCS=OFF \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch s390x
%ctest -E 'testPolygonToCellsReportedExperimental_test103|testPolygonToCellsReportedExperimental_test105'
%else
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n h3-devel -f %{oreon_filedir}/h3-devel.list

%changelog

%autochangelog
