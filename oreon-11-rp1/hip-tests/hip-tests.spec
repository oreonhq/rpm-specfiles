%global source0_hash c575b6df245497c4ec54da8ce2ca440d6c307474d8cc04e6056a1c4053e75d43
%global upstreamname hip-tests
%global rocm_release 7.1
%global rocm_patch 1
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
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' -e 's/flto=thin//' )
%global gpu_list "--offload-arch=gfx1100 --offload-arch=gfx1101 --offload-arch=gfx1102 --offload-arch=gfx1151 --offload-arch=gfx1200 --offload-arch=gfx1201"
%global _gpu_list "--offload-arch=gfx1100"
%bcond check 1
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%global _lto_cflags %{nil}
Name:       hip-tests%{pkg_suffix}
Version:    %{rocm_version}
Release:        1%{?dist}
Summary:        HIP tests
License:    MIT AND BSL-1.0 AND Apache-2.0
URL:        https://github.com/ROCm/rocm-systems
Source0:        https://github.com/ROCm/%{toolchain}-systems/releases/download/%{pkg_module}.%{rocm_patch}/%{name}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:     0001-hip-tests-build-on-fedora.patch
Patch2:     0001-hip-tests-link-with-libamd64.patch
ExclusiveArch:  x86_64
Provides:       bundled(catch2) = 2.13.4
%if %{with check}
%endif
Requires:       cmake
Requires:       rocminfo
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  numactl-devel
BuildRequires:  pkgconfig(opengl)
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocminfo
# /oreon:deps
%description
This repository provides unit tests for HIP implementation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstreamname} -p1

# Change path to clang-cpp
sed -i -e 's@${ROCM_PATH}/llvm/bin/clang-cpp@%{rocmllvm_bindir}/clang-cpp@' catch/CMakeLists.txt

# Change install to libexec
sed -i -e 's@INSTALL_DIR ${CMAKE_INSTALL_DATADIR}/hip@INSTALL_DIR libexec/hip-tests@' catch/packaging/CMakeLists.txt

# Some tests need to include stdlib.h to find malloc/free
sed -i '/hip\/hip_runtime/a#include <stdlib.h>' catch/unit/deviceLib/kerDevAlloc*.cc
sed -i '/hip\/hip_runtime/a#include <stdlib.h>' catch/unit/deviceLib/kerDevFree*.cc

# Need some help finding lamdhip64
sed -i -e 's@-lamdhip64@-L %{pkg_prefix}/%{pkg_libdir} -lamdhip64@' catch/unit/compiler/CMakeLists.txt

# Rename the catch2 license so we can pick it up
mv catch/external/Catch2/LICENSE.txt catch/external/Catch2/LICENSE.catch2.txt

%build

cd catch
export HIPCC_COMPILE_FLAGS_APPEND="-I %{pkg_prefix}/include"
%cmake \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_AR=%{rocmllvm_bindir}/llvm-ar \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_CXX_FLAGS="-O2 -I %{pkg_prefix}/include" \
    -DCMAKE_EXE_LINKER_FLAGS="-L %{pkg_prefix}/%{pkg_libdir} -lamdhip64" \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_RANLIB=%{rocmllvm_bindir}/llvm-ranlib \
    -DHIP_PLATFORM=amd \
    -DOFFLOAD_ARCH_STR=%{gpu_list} \
    -DROCM_PATH=%{pkg_prefix}
%cmake_build -t build_tests
%if %{with check}
%check

cd catch
%ctest --output-on-failure
%endif
%install
cd catch
%cmake_install
rm -rf %{buildroot}%%{pkg_prefix}/libexec/hip-tests/catch_tests/headers
rm -rf %{buildroot}%%{pkg_prefix}/libexec/hip-tests/catch_tests/saxpy.h
%fdupes %{buildroot}%{pkg_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
