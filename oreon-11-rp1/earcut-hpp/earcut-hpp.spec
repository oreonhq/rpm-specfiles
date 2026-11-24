# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 70c00e90811950b2c3d973ecfd46010680b946f7952306ffa2785c0368fe2db0
%global source1_hash 5d72947e603df0eb87f99e7ecdbd72fd7c291c68e96a92e9bdbfd896b41ceeba
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond ctest 1

Name:           earcut-hpp
Summary:        Fast, header-only polygon triangulation
Version:        3.2.4
Release:        %{autorelease}
License:        ISC
URL:            https://github.com/mapbox/earcut.hpp
Source0:        %{url}/archive/v%{version}/earcut.hpp-%{version}.tar.gz
Source1:        https://github.com/mapbox/earcut/archive/v%{version}/earcut-%{version}.tar.gz
Patch0:         136.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  picojson-devel
%if %{with ctest}
BuildRequires:  cmake(gtest)
%endif
%global debug_package %{nil}

%global common_description %{expand:
A fast, header-only C++ port of earcut.js, the fastest and smallest JavaScript
polygon triangulation library.

Earcut favors raw speed and simplicity over triangulation quality, while being
robust enough to handle most practical datasets without crashing or producing
garbage, with an option to refine the result to Delaunay quality at a small
cost. Originally built for Mapbox GL, it's a good fit for real-time
triangulation of geographical shapes and other practical data.

It implements a modified ear slicing algorithm, optimized by z-order curve and
spatial hashing and extended to handle holes, twisted polygons, degeneracies
and self-intersections in a way that doesn't guarantee correctness of
triangulation, but attempts to always produce acceptable results for practical
data. It's based on ideas from FIST: Fast Industrial-Strength Triangulation of
Polygons by Martin Held and Triangulation by Ear Clipping by David Eberly.}

%description %{common_description}

%package devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1 -n earcut.hpp-%{version}

%build
%cmake \
  -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
  -DEARCUT_BUILD_TESTS:BOOL=%{with ctest} \
  -DEARCUT_BUILD_BENCH:BOOL=OFF \
  -DEARCUT_BUILD_VIZ:BOOL=OFF \
  -DEARCUT_WARNING_IS_ERROR:BOOL=OFF
%cmake_build

%install
%cmake_install

%if %{with ctest}
%check
xdir='%{_vpath_builddir}/_deps/earcut_js-src'
mkdir --parents "${xdir}"
tar --extract --gzip --verbose '--file=%{SOURCE1}' \
    "--directory=${xdir}" --strip-components=1 \
    'earcut-%{version}/bench/tiles-fixture.bin' \
    'earcut-%{version}/test/expected.json' \
    'earcut-%{version}/test/fixtures/'
%ctest
%endif

%files devel
%license LICENSE
%doc README.md
%dir %{_includedir}/mapbox
%{_includedir}/mapbox/earcut.hpp
%{_datadir}/cmake/earcut_hpp/

%changelog
%autochangelog
