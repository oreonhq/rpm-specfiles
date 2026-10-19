%global source0_hash 19964494662243773a89c8f20e78a6903b5c886fdb472703b6c9f5bec36d3120
%global upstreamname aqlprofile
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%global gpu_list %{rocm_gpu_list_test}
%global _gpu_list gfx1100
%global toolchain clang
Name:           aqlprofile%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        Architected Queuing Language Profiling Library
License:        MIT
ExclusiveArch:  x86_64
Url:            https://github.com/ROCm/%{upstreamname}
Source0:        https://github.com/ROCm/%{name}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{name}-%{version}.tar.gz
%if %{with test}
%if 0%{?suse_version}
%else
%endif
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-clang-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-llvm-static
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
# /oreon:deps
%description
AQLprofile is an open source library that enables advanced GPU
profiling and tracing on AMD platforms. It works in conjunction
with rocprofiler-sdk to support profiling methods such as
performance counters (PMC) and SQ thread trace (SQTT).
AQLprofile provides the foundational mechanisms for constructing
AQL packets and managing profiling operations across multiple
AMD GPU architecture families.

%package devel
Summary:        The development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%if %{with test}
%package test
Summary:        The test package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Do not hardcode CMAKE_BUILD_TYPE
# https://github.com/ROCm/aqlprofile/issues/12
sed -i -e 's@CMAKE_BUILD_TYPE@DO_NO_HARDCODE_CMAKE_BUILD_TYPE@' cmake_modules/env.cmake

%build

%cmake \
    -DAQLPROFILE_BUILD_TESTS=%{build_test} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_HIP_ARCHITECTURES=%{gpu_list} \
    -DCMAKE_HIP_COMPILER_ROCM_ROOT=%{pkg_prefix} \
    -DCMAKE_HIP_COMPILER=%{rocmllvm_bindir}/amdclang++ \
    -DCMAKE_HIP_FLAGS="-I %{pkg_prefix}/include" \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DGPU_TARGETS=%{gpu_list}
%cmake_build
%install
%cmake_install
%oreon_autofiles aqlprofile-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n aqlprofile-devel -f %{oreon_filedir}/aqlprofile-devel.list

%changelog

%autochangelog
