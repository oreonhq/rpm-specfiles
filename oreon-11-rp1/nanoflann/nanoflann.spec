%global source0_hash 14e82a1de64a8b26486322d36817449a8bc2e63ea3b91bfee64f320155790a9c
%global debug_package %{nil}
%global forgeurl https://github.com/jlblancoc/nanoflann
Version:        1.13.0
%forgemeta
Name:           nanoflann
Release:        1%{?dist}
Summary:        A C++11 header-only library for Nearest Neighbor (NN) search with KD-trees
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(gtest)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
nanoflann is a C++11 header-only library for building KD-Trees of datasets with
different topologies: R2, R3 (point clouds), SO(2) and SO(3) (2D and 3D rotation
groups). No support for approximate NN is provided.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%description    devel
nanoflann is a C++11 header-only library for building KD-Trees of datasets with
different topologies: R2, R3 (point clouds), SO(2) and SO(3) (2D and 3D rotation
groups). No support for approximate NN is provided.

The %{name}-devel package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

rm -r tests/gtest-1.8.0

%build

%cmake -DNANOFLANN_USE_SYSTEM_GTEST=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n nanoflann-devel -f %{oreon_filedir}/nanoflann-devel.list

%changelog

%autochangelog
