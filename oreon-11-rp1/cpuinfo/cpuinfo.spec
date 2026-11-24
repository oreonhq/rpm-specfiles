# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 30c390d5ac7c59ae1c0a8a1aefb9bb70cb4d482bd15e8de706f5c8bf60357fa6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_with check

%bcond_with gitcommit

%if %{with gitcommit}
%global commit0 f858c30bcb16f8effd5ff46996f0514539e17abc
Version:        25.11.14
%define patch_level 0

%else

%global commit0 f858c30bcb16f8effd5ff46996f0514539e17abc
Version:        25.11.14
%define patch_level 1

%endif

%global shortcommit0 f858c30

Summary:        A library to detect information about host CPU
Name:           cpuinfo
License:        BSD-2-Clause
Release:        %{patch_level}.git%{?shortcommit0}%{?dist}.1

URL:            https://github.com/pytorch/%{name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         0001-cpuinfo-fedora-cmake-changes.patch

ExclusiveArch:  x86_64 aarch64 riscv64

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
%if %{with check}
BuildRequires:  gtest-devel
%endif
BuildRequires:  make

%description
cpuinfo is a library to detect essential for performance
optimization information about host CPU.

Features
* Cross-platform availability:
  * Linux, Windows, macOS, Android, and iOS operating systems
  * x86, x86-64, ARM, and ARM64 architectures
* Modern C/C++ interface
  * Thread-safe
  * No memory allocation after initialization
  * No exceptions thrown
* Detection of supported instruction sets, up to AVX512 (x86)
  and ARMv8.3 extensions
* Detection of SoC and core information:
  * Processor (SoC) name
  * Vendor and microarchitecture for each CPU core
  * ID (MIDR on ARM, CPUID leaf 1 EAX value on x86) for each CPU core
* Detection of cache information:
  * Cache type (instruction/data/unified), size and line size
  * Cache associativity
  * Cores and logical processors (hyper-threads) sharing the cache
* Detection of topology information (relative between logical
  processors, cores, and processor packages)
* Well-tested production-quality code:
  * 60+ mock tests based on data from real devices
  * Includes work-arounds for common bugs in hardware and OS kernels
  * Supports systems with heterogenous cores, such as big.LITTLE and Max.Med.Min
* Permissive open-source license (Simplified BSD)

%package devel
Summary:        Headers and libraries for cpuinfo
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the developement libraries and headers
for cpuinfo.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{commit0}

sed -i -e 's@cpuinfo_VERSION 23.11.04@cpuinfo_VERSION %{version}@' CMakeLists.txt

%build
%cmake \
%if %{with check}
    -DCPUINFO_BUILD_UNIT_TESTS=ON \
%else
    -DCPUINFO_BUILD_UNIT_TESTS=OFF \
%endif
    -DCPUINFO_BUILD_MOCK_TESTS=OFF \
    -DCPUINFO_BUILD_BENCHMARKS=OFF

%cmake_build

%install
%cmake_install

%if %{with check}
rm -rf %{buildroot}/%{_includedir}/gmock
rm -rf %{buildroot}/%{_includedir}/gtest
rm -rf %{buildroot}/%{_libdir}/cmake/GTest
rm -rf %{buildroot}/%{_libdir}/libgmock*
rm -rf %{buildroot}/%{_libdir}/libgtest*
rm -rf %{buildroot}/%{_libdir}/pkgconfig/gmock*
rm -rf %{buildroot}/%{_libdir}/pkgconfig/gtest*
%endif

%check
%if %{with check}
%ctest
%endif

%files
%license LICENSE
%{_bindir}/isa-info
%{_bindir}/cpu-info
%{_bindir}/cache-info
%ifarch x86_64
%{_bindir}/cpuid-dump
%endif
%{_libdir}/lib%{name}.so.*

%files devel
%doc README.md
%dir %{_datadir}/%{name}
%{_includedir}/%{name}.h
%{_datadir}/%{name}/%{name}-*.cmake
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
%autochangelog
