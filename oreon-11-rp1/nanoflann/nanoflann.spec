%global source0_hash 14e82a1de64a8b26486322d36817449a8bc2e63ea3b91bfee64f320155790a9c

# header-only library
%global debug_package %{nil}

%global forgeurl https://github.com/jlblancoc/nanoflann
Version:        1.8.0
%forgemeta

Name:           nanoflann
Release:        %autorelease
Summary:        A C++11 header-only library for Nearest Neighbor (NN) search with KD-trees
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  cmake(gtest)

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

%check
%ctest

%files devel
%license COPYING
%doc README.md
%{_includedir}/nanoflann.hpp
%{_libdir}/pkgconfig/nanoflann.pc
%{_datadir}/cmake/nanoflann/

%changelog
%autochangelog
