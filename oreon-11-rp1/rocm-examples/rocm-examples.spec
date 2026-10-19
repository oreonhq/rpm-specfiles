%global source0_hash d64a82ba472126bb426c54abd1b2516479a375db895171bbc4024a7c8d0f4e94
%global upstreamname rocm-examples
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
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%global gpu_list %rocm_gpu_list_test
%global _gpu_list gfx1100
Name:           rocm-examples%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        A collection of examples for the ROCm software stack
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT AND Apache-2.0
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{name}.%{rocm_patch}.tar.gz
%if 0%{?suse_version}
%else
%endif
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  google-benchmark-devel
BuildRequires:  gtest-devel
BuildRequires:  hipblas-7.1-devel
BuildRequires:  hipcub-7.1-devel
BuildRequires:  hipfft-7.1-devel
BuildRequires:  hipify-7.1
BuildRequires:  hiprand-7.1-devel
BuildRequires:  hipsolver-7.1-devel
BuildRequires:  rocblas-7.1-devel
BuildRequires:  rocfft-7.1-devel
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocsolver-7.1-devel
BuildRequires:  rocsparse-7.1-devel
BuildRequires:  rocthrust-7.1-devel
# /oreon:deps
%description
This repository is a collection of examples to enable new users
to start using ROCm, as well as provide more advanced examples
for experienced users.

The examples are structured in several categories:
* HIP-Basic showcases some basic functionality without
  any additional dependencies

* Libraries contains examples for ROCm-libraries, that
  provide higher-level functionality

* Applications showcases some common applications, using
  HIP to accelerate them

* AI contains instructions on how to use ROCm for AI

* Tutorials contains the code accompanying the HIP Tutorials
  that can be found in the HIP documentation.

* For a full overview over the examples see the section
  repository contents.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# No External, not going to bundle things outside of this project.
# Not having glfw-devel turns off building examples that use External/glad
#
# Need to keep CmdParser
rm -rf External/{glad,KHR}

# https://github.com/ROCm/rocm-examples/issues/217
for f in `find . -name 'CMakeLists.txt'`; do
    sed -i -e 's@/opt/rocm@%{pkg_prefix}@' $f
done
for f in `find . -name 'Makefile'`; do
    sed -i -e 's@/opt/rocm@%{pkg_prefix}@' $f
done

# On SLE 15.6
# libstdc++ is too old and there are several compiling problems like this ..
# .../Tutorials/reduction/include/Reduction/v0.hpp:31:10: fatal error: 'execution' file not found
%if 0%{?suse_version}
%if %{suse_version} <= 1500
sed -i -e 's@add_subdirectory(Tutorials)@#add_subdirectory(Tutorials)@' CMakeLists.txt
sed -i -e 's@add_subdirectory(module_api)@message("no module_api")@'    HIP-Basic/CMakeLists.txt
%endif
%endif

# Some custom commands need to use hip_flags
sed -i -e 's@${CMAKE_HIP_COMPILER}@${CMAKE_HIP_COMPILER} -I%{pkg_prefix}/include@' HIP-Basic/llvm_ir_to_executable/CMakeLists.txt

%build

export ROCM_ROOT=%{pkg_prefix}
%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_CXX_FLAGS="-I %{pkg_prefix}/include" \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_HIP_ARCHITECTURES=%{gpu_list} \
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_HIP_COMPILER_ROCM_ROOT=%{pkg_prefix} \
    -DCMAKE_HIP_FLAGS="-I %{pkg_prefix}/include" \
    -DGPU_TARGETS=%{gpu_list} \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DHIP_PLATFORM=amd
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
