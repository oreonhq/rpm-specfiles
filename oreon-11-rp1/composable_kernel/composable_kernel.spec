%global source0_hash 902d93c0d5ff6a531219d353061974c1ce146839d0f63034cd14092b70954451
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname composablekernel
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
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-g / /' )
%global ck_gpu_list "gfx11-generic;gfx12-generic"
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%global _smp_mflags %{nil}
%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif
%bcond_with ck_contraction
%if %{with ck_contraction}
%global build_ck_contraction ON
%else
%global build_ck_contraction OFF
%endif
%bcond_with ck_conv
%if %{with ck_conv}
%global build_ck_conv ON
%else
%global build_ck_conv OFF
%endif
%bcond_with ck_gemm
%if %{with ck_gemm}
%global build_ck_gemm ON
%else
%global build_ck_gemm OFF
%endif
%bcond_with ck_mha
%if %{with ck_mha}
%global build_ck_mha ON
%else
%global build_ck_mha OFF
%endif
%bcond_with ck_other
%if %{with ck_other}
%global build_ck_other ON
%else
%global build_ck_other OFF
%endif
%bcond_with ck_reduction
%if %{with ck_reduction}
%global build_ck_reduction ON
%else
%global build_ck_reduction OFF
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif
%global _rocm_lto_cflags %{nil}
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
Name:           composable_kernel%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        Performance Portable Programming Model for Machine Learning Tensor Operators
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries
%if %{with gitcommit}
Source0:        https://github.com/ROCm/%{toolchain}-%{pkg_libdir}raries/releases/download/%{pkg_module}.%{rocm_patch}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
Source0:        https://github.com/ROCm/%{toolchain}-%{pkg_libdir}raries/releases/download/%{pkg_module}.%{rocm_patch}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%endif
Patch1:         0001-composable_kernel-per-dir-build.patch
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
# /oreon:deps
%description
Composable Kernel (CK) library aims to provide a programming
model for writing performance critical kernels for machine
learning workloads across multiple architectures including
GPUs, CPUs, etc, through general purpose kernel languages,
like HIP C++.

CK utilizes two concepts to achieve performance portability
and code maintainability:

- A tile-based programming model
- Algorithm complexity reduction for complex ML operators,
  using innovative technique we call "Tensor Coordinate
  Transformation".

%package devel
Summary: Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{without library}
Provides:       %{name}-static = %{version}-%{release}
%endif
%description devel
%{summary}

%package test
Summary: Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description test
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/composablekernel
%patch -P1 -p1
%else
%autosetup -p1 -n %{upstreamname}
%endif

# do not error on warnings
sed -i -e 's@add_compile_options(-Werror)@#add_compile_options(-Werror)@' CMakeLists.txt
sed -i -e '/-Werror/d' cmake/EnableCompilerWarnings.cmake
# No extra warnings
sed -i -e 's@add_compile_options(-Weverything)@#add_compile_options(-Weverything)@' CMakeLists.txt
sed -i -e '/-Wextra/d' cmake/EnableCompilerWarnings.cmake
sed -i -e '/-Wunused/d' cmake/EnableCompilerWarnings.cmake
sed -i -e '/-Weverything/d' cmake/EnableCompilerWarnings.cmake
sed -i -e 's@-Wno-unknown-warning-option@-Wno-unknown-warning-option -Wno-unused-parameter@' cmake/EnableCompilerWarnings.cmake

# Do not time the kernel loading
# https://github.com/ROCm/composable_kernel/issues/1780
sed -i -e 's@CK_TIME_KERNEL 1@CK_TIME_KERNEL 0@' include/ck/ck.hpp

# No way easy way to turn off examples building
# https://github.com/ROCm/composable_kernel/issues/1781
sed -i -e 's@add_subdirectory(example)@#add_subdirectory(example)@' CMakeLists.txt
# No profiler
sed -i -e 's@add_subdirectory(profiler)@#add_subdirectory(profiler)@' CMakeLists.txt

# Does not honor BUILD_SHARED
# https://github.com/ROCm/composable_kernel/issues/1782
sed -i -e 's@STATIC@SHARED@' library/src/utility/CMakeLists.txt library/src/tensor_operation_instance/gpu/CMakeLists.txt
sed -i -e 's@POSITION_INDEPENDENT_CODE ON@POSITION_INDEPENDENT_CODE ON SOVERSION \"%{version}\"@' library/src/utility/CMakeLists.txt library/src/tensor_operation_instance/gpu/CMakeLists.txt

# We are building from a tarball, not a git repo
sed -i -e 's@find_package(Git REQUIRED)@#find_package(Git REQUIRED)@' CMakeLists.txt
sed -i -e 's@execute_process(COMMAND "${GIT_EXECUTABLE}"@#execute_process(COMMAND "${GIT_EXECUTABLE}"@' CMakeLists.txt

%build

%if %{with gitcommit}
cd projects/composablekernel
%endif
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
if [ ${COMPILE_JOBS} = 1 ]; then
    COMPILE_JOBS=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${COMPILE_JOBS}x = x ]; then
        COMPILE_JOBS=4
    fi
fi
BUILD_MEM=6
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
LINK_MEM=12
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`
%cmake -G Ninja \
    -DBUILD_TESTING=%{build_test} \
    -DCK_BUILD_DEVICE_CONV=%{build_ck_conv} \
    -DCK_BUILD_DEVICE_CONTRACTION=%{build_ck_contraction} \
    -DCK_BUILD_DEVICE_GEMM=%{build_ck_gemm} \
    -DCK_BUILD_DEVICE_MHA=%{build_ck_mha} \
    -DCK_BUILD_DEVICE_OTHER=%{build_ck_other} \
    -DCK_BUILD_DEVICE_REDUCTION=%{build_ck_reduction} \
    -DCK_PARALLEL_COMPILE_JOBS=${COMPILE_JOBS} \
    -DCK_PARALLEL_LINK_JOBS=${LINK_JOBS} \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_CXX_FLAGS="-fuse-ld=bfd" \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \
    -DCMAKE_HIP_ARCHITECTURES=%ck_gpu_list \
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_HIP_COMPILER_ROCM_ROOT=%{pkg_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DENABLE_CLANG_CPP_CHECKS=OFF \
    -DGPU_ARCHS=%ck_gpu_list \
    -DHIP_PLATFORM=amd \
    -DROCM_SYMLINK_LIBS=OFF
%cmake_build
%install
%if %{with gitcommit}
cd projects/composablekernel
%endif
%cmake_install
%if %{without cklibs}
cp -p -r include/ck_tile %{buildroot}%{pkg_prefix}/include
%endif
%fdupes %{buildroot}%{pkg_prefix}
rm -f %{buildroot}%{pkg_prefix}/share/doc/composablekernel/LICENSE
%oreon_autofiles composable_kernel-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles composable_kernel-test usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n composable_kernel-devel -f %{oreon_filedir}/composable_kernel-devel.list
%files -n composable_kernel-test -f %{oreon_filedir}/composable_kernel-test.list

%changelog

%autochangelog
