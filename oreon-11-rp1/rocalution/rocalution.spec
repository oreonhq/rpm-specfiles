%global source0_hash 0f8d8c24317b30d7269841b9fe5ab2d24dddd3d5132e84b4f8ac1cd9d30b0ff2
%global upstreamname rocALUTION
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
%if 0%{?suse_version}
%global rocalution_name librocalution1%{pkg_suffix}
%else
%global rocalution_name rocalution%{pkg_suffix}
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
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
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100
%bcond_with ninja
%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif
Name:           %{rocalution_name}
Version:        %{rocm_version}
Release:        4%{?dist}
Summary:        Next generation library for iterative sparse solvers for ROCm platform
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%if %{with test}
%if 0%{?suse_version}
%else
%endif
%endif
%if %{with ninja}
%if 0%{?suse_version}
%define __builder ninja
%endif
%endif
Provides:       rocalution%{pkg_suffix} = %{version}-%{release}
%if 0%{?suse_version}
Obsoletes:      libalution1 <= 6.4.1
%endif
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  rocblas-7.1-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocprim-7.1-static
BuildRequires:  rocrand-7.1-devel
BuildRequires:  rocsparse-7.1-devel
# /oreon:deps
%description
rocALUTION is a sparse linear algebra library that can be used
to explore fine-grained parallelism on top of the ROCm platform
runtime and toolchains. Based on C++ and HIP, rocALUTION
provides a portable, generic, and flexible design that allows
seamless integration with other scientific software packages.

rocALUTION offers various backends for different (parallel) hardware:

Host
* OpenMP: Designed for multi-core CPUs
* HIP: Designed for ROCm-compatible devices
* MPI: Designed for multi-node clusters and multi-GPU setups

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%package devel
Summary: Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rocalution%{pkg_suffix}-devel = %{version}-%{release}
%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%if 0%{?suse_version}
# On TW
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
sed -i -e 's@set(CMAKE_CXX_STANDARD 14)@set(CMAKE_CXX_STANDARD 17)@' clients/CMakeLists.txt
%endif

%build

%cmake %{cmake_generator} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_EXE_LINKER_FLAGS=-fuse-ld=%rocmllvm_bindir/ld.lld \
    -DCMAKE_SHARED_LINKER_FLAGS=-fuse-ld=%rocmllvm_bindir/ld.lld \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DGPU_TARGETS=%{gpu_list} \
    -DCMAKE_MODULE_PATH=%{pkg_prefix}/%{pkg_libdir}/cmake/hip \
    -DHIP_ROOT_DIR=%{pkg_prefix} \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DBUILD_CLIENTS_TESTS=%{build_test}
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocalution/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rocalution-7.1-devel -f %{oreon_filedir}/rocalution-7.1-devel.list
%files -n rocalution-7.1-test -f %{oreon_filedir}/rocalution-7.1-test.list

%changelog

%autochangelog
