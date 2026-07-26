%global source0_hash a8424ad3b0affd4c57ed26f0f3d8a29604f0e1f2ef2089f497f614b1c94c7236

%global debug_package %{nil}

Name:           robin-map
Version:        1.3.0
Release:        7%{?dist}
Summary:        C++ implementation of a fast hash map and hash set using robin hood hashing

License:        MIT
URL:            https://github.com/Tessil/robin-map
Source0:        https://github.com/Tessil/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake gcc-c++
BuildRequires:  boost-devel
BuildRequires:  boost-static

%description
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing with backward shift
deletion to resolve collisions.

*** This is a header only library. ***
The package you want is %{name}-devel.

%package devel
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       robin-map-static = %{version}-%{release}

%description devel
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing with backward shift
deletion to resolve collisions.

Four classes are provided: tsl::robin_map, tsl::robin_set, tsl::robin_pg_map
and tsl::robin_pg_set. The first two are faster and use a power of two growth
policy, the last two use a prime growth policy instead and are able to cope
better with a poor hash function. Use the prime version if there is a chance of
repeating patterns in the lower bits of your hash (e.g. you are storing
pointers with an identity hash function). See GrowthPolicy for details.

A benchmark of tsl::robin_map against other hash maps may be found here. This
page also gives some advices on which hash table structure you should try for
your use case (useful if you are a bit lost with the multiple hash tables
implementations in the tsl namespace).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Update the minimum cmake version for CMake 4
sed -i -e 's@cmake_minimum_required(VERSION 3.3)@cmake_minimum_required(VERSION 3.5)@' CMakeLists.txt

%build
%cmake

%install
%cmake_install

%check
pushd tests
%cmake
%cmake_build
%{_vpath_builddir}/tsl_robin_map_tests

%files devel
%license LICENSE
%doc README.md
%{_datadir}/cmake/tsl-%{name}/*.cmake
%{_includedir}/tsl/

%changelog
%autochangelog
