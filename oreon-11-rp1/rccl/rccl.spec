%global source0_hash 50ba486bc8a466a68bff9d6c9d7b3ebf8de9426906720fa44023b5390602b3b8
%if 0%{?suse_version}
%global rccl_name librccl1
%else
%global rccl_name rccl
%endif
%global upstreamname RCCL
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-flto=thin//' -e 's/-mtls-dialect=gnu2//')
%global _lto_cflags %{nil}
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif
%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif
Name:           %{rccl_name}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Communication Collectives Library
Url:            https://github.com/ROCm/rccl
License:        BSD-3-Clause AND MIT AND Apache-2.0
Source0:        https://github.com/ROCm/%{name}/archive/%{toolchain}-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%if %{with test}
%if 0%{?suse_version}
%else
%endif
%endif
Requires:       %{name}-data = %{version}-%{release}
Provides:       rccl = %{version}-%{release}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  hipify
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-smi-devel
# /oreon:deps
%description
RCCL (pronounced "Rickle") is a stand-alone library of standard
collective communication routines for GPUs, implementing all-reduce,
all-gather, reduce, broadcast, reduce-scatter, gather, scatter, and
all-to-all. There is also initial support for direct GPU-to-GPU
send and receive operations. It has been optimized to achieve high
bandwidth on platforms using PCIe, xGMI as well as networking using
InfiniBand Verbs or TCP/IP sockets. RCCL supports an arbitrary
number of GPUs installed in a single node or multiple nodes, and
can be used in either single- or multi-process (e.g., MPI)
applications.

The collective operations are implemented using ring and tree
algorithms and have been optimized for throughput and latency. For
best performance, small operations can be either batched into
larger operations or aggregated through the API.

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%package devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rccl-devel = %{version}-%{release}
%description devel
Headers and libraries for %{name}

%package data
Summary:        Data for %{name}
BuildArch:      noarch
%description data
Data for %{name}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rccl-rocm-%{version}

# Allow user to set AMDGPU_TARGETS
sed -i -e '/AMD GPU targets to compile for/d' CMakeLists.txt

# No /opt/rocm/.info/version
sed -i -e 's@cat ${ROCM_PATH}/.info/version@echo %{rocm_version}@' CMakeLists.txt

# wrong path
# https://github.com/ROCm/rccl/issues/1649
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' src/include/hip_rocm_version_info.h

# Problems building on SUSE
# ENABLE_MSCCLPP=OFF
sed -i -e 's@if (ENABLE_MSCCLPP AND NOT(${HOST_OS_ID} STREQUAL "ubuntu" OR ${HOST_OS_ID} STREQUAL "centos"))@if (ENABLE_MSCCLPP)@' CMakeLists.txt

# Building --with test
# .../test/common/TestBed.cpp:607:16: error: no member named 'setfill' in namespace 'std'
#   607 |     ss << std::setfill(' ') << std::setw(20) << ncclFuncNames[funcType] << " ";
# https://github.com/ROCm/rccl/issues/1749
sed -i '/#include <map.*/a#include <iomanip>' test/common/TestBed.hpp

# On Tumbleweed Q3,2025
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
# Convert the c++14 to c++17
sed -i -e 's@set(CMAKE_CXX_STANDARD   14)@set(CMAKE_CXX_STANDARD 17)@' CMakeLists.txt

# Do not force install
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' cmake/Dependencies.cmake

# RCCL uses -parallel-jobs for both compiling and linking
# compiling is set to 12, which may be more than the cores on the build machine.
# linking is set by reserving 16GB pre thread, can be too little.
# Use our own heuristics here
# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Try again..
if [ ${COMPILE_JOBS} = 1 ]; then
    COMPILE_JOBS=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${COMPILE_JOBS}x = x ]; then
        COMPILE_JOBS=4
    fi
fi

# Take into account memmory usage per core, do not thrash real memory
# inflate this to prevent competing with normal compile jobs
BUILD_MEM=16
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
LINK_MEM=65
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`

sed -i -e "s@rccl PRIVATE -parallel-jobs=12@rccl PRIVATE -parallel-jobs=${COMPILE_JOBS}@" CMakeLists.txt
sed -i -e "s@-parallel-jobs=\${num_linker_jobs}@-parallel-jobs=${LINK_JOBS}@" CMakeLists.txt

%build

%cmake \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_rccl} \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DBUILD_TESTS=%{build_test} \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=/usr/bin/hipcc \
    -DCMAKE_CXX_COMPILER=/usr/bin/hipcc \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_SKIP_RPATH=ON \
    -DENABLE_MSCCLPP=OFF \
    -DEXPLICIT_ROCM_VERSION=%{rocm_version} \
    -DHIP_PLATFORM=amd \
    -DRCCL_ROCPROFILER_REGISTER=OFF \
    -DROCM_PATH=%{_prefix} \
    -DROCM_SYMLINK_LIBS=OFF
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_prefix}/share/doc/rccl/LICENSE.txt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rccl-devel -f %{oreon_filedir}/rccl-devel.list
%files -n rccl-data -f %{oreon_filedir}/rccl-data.list
%files -n rccl-test -f %{oreon_filedir}/rccl-test.list

%changelog

%autochangelog
