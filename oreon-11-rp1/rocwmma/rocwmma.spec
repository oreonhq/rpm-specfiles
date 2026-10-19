%global source0_hash 96bed5cd6f2d3334cfbd4a9e6dab132cc2ec60150409712661dc69e774427707
%global upstreamname rocWMMA
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
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%global debug_package %{nil}
%endif
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%global _gpu_list "gfx908;gfx90a;gfx942;gfx950;gfx1100;gfx1101;gfx1102;gfx1151;gfx1200;gfx1201"
%global gpu_list gfx1100
%global _smp_mflags %{nil}
Name:           rocwmma%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Matrix Multiple and Accumulate library
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch0:         0001-rocwmma-ninja-job-pools.patch
%if %{with test}
%endif
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  rocblas-7.1-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-omp-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocm-smi-7.1-devel
BuildRequires:  rocminfo-7.1
# /oreon:deps
%description
rocWMMA is a C++ library for accelerating mixed-precision matrix
multiply-accumulate (MMA) operations leveraging AMD GPU hardware.
rocWMMA makes it easier to break down MMA problems into fragments
and distribute block-wise MMA operations in parallel across GPU
wavefronts. Our API consists of a header library, that you can
use to compile MMA acceleration directly into GPU kernel device
code. This can benefit from compiler optimization in the
generation of kernel assembly, and doesn't incur additional
overhead costs of linking to external runtime libraries or having
to launch separate kernels.

%package devel
Summary:        Headers for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build

cat /proc/cpuinfo
cat /proc/meminfo
lscpu
COMPILE_JOBS=`lscpu | grep 'Core(s)' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
if [ ${COMPILE_JOBS} = 1 ]; then
    COMPILE_JOBS=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${COMPILE_JOBS}x = x ]; then
        COMPILE_JOBS=4
    fi
fi
BUILD_MEM=2
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
LINK_MEM=32
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`
JOBS=${COMPILE_JOBS}
if [ "$LINK_JOBS" -lt "$JOBS" ]; then
    JOBS=$LINK_JOBS
fi
%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=%build_type \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_CXX_FLAGS="-O2 -I%{pkg_prefix}/include" \
    -DCMAKE_EXE_LINKER_FLAGS="-L%{pkg_prefix}/%{pkg_libdir} -lamdhip64" \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DGPU_TARGETS=%{gpu_list} \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DROCWMMA_BUILD_SAMPLES=OFF \
    -DROCWMMA_BUILD_TESTS=%{build_test} \
    -DROCWMMA_PARALLEL_COMPILE_JOBS=${COMPILE_JOBS} \
    -DROCWMMA_PARALLEL_LINK_JOBS=${LINK_JOBS}
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocwmma/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/bin/rocwmma/*.cmake
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rocwmma-7.1-devel -f %{oreon_filedir}/rocwmma-7.1-devel.list
%files -n rocwmma-7.1-test -f %{oreon_filedir}/rocwmma-7.1-test.list

%changelog

%autochangelog
