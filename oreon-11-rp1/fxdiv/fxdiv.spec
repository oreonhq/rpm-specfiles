%global source0_hash ec74d882a0a47cfd9c0f95bc4fae9901a4ade802a96a3b76e02671bb7340a4c5

%global commit0 63058eff77e11aa15bf531df5dd34395ec3017c8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20201208
%global upstream_name FXdiv

Summary:        Header for division via fixed-point math
Name:           fxdiv
License:        MIT
Version:        1.0^git%{date0}.%{shortcommit0}
Release:        9%{?dist}

# Only a header
BuildArch:      noarch

URL:            https://github.com/Maratyszcza/%{name}
Source0:        %{url}/archive/%{commit0}/%{upstream_name}-%{shortcommit0}.tar.gz

Patch0:        0001-Prep-fxdiv-cmake-for-fedora-packaging.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gtest-devel

%description
Header-only library for division via fixed-point multiplication by inverse

On modern CPUs and GPUs integer division is several times slower
than multiplication. FXdiv implements an algorithm to replace an
integer division with a multiplication and two shifts. This
algorithm improves performance when an application performs repeated
divisions by the same divisor.

Features
  * Integer division for uint32_t, uint64_t, and size_t
  * Header-only library, no installation or build required
  * Compatible with C99, C++, OpenCL, and CUDA
  * Uses platform-specific compiler intrinsics for optimal performance
  * Covered with unit tests and microbenchmarks

%package devel

Summary:        Header for division via fixed-point math
Provides:       %{name}-static = %{version}-%{release}

%description devel
Header-only library for division via fixed-point multiplication by inverse

On modern CPUs and GPUs integer division is several times slower
than multiplication. FXdiv implements an algorithm to replace an
integer division with a multiplication and two shifts. This
algorithm improves performance when an application performs repeated
divisions by the same divisor.

Features
  * Integer division for uint32_t, uint64_t, and size_t
  * Header-only library, no installation or build required
  * Compatible with C99, C++, OpenCL, and CUDA
  * Uses platform-specific compiler intrinsics for optimal performance
  * Covered with unit tests and microbenchmarks

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{commit0}

%build

%cmake \
       -DFXDIV_USE_SYSTEM_LIBS=ON \
       -DFXDIV_BUILD_TESTS=ON \
       -DFXDIV_BUILD_BENCHMARKS=OFF \
       
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/fxdiv.h

%changelog
%autochangelog
