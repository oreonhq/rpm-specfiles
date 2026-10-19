%global source0_hash 6763ab479b364fdb9dfe7c5559e8bcad3b4e5c8dfa340640d404faa265f122eb
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname rocsolver
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
%if 0%{?suse_version}
%global rocsolver_name librocsolver0%{pkg_suffix}
%else
%global rocsolver_name rocsolver%{pkg_suffix}
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' -e 's/-flto=thin//')
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%bcond_without compress
%if %{with compress}
%global build_compress ON
%else
%global build_compress OFF
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif
%global _smp_mflags %{nil}
%global build_fflags %{nil}
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
%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif
Name:           rocsolver%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        Next generation LAPACK implementation for ROCm platform
License:        BSD-3-Clause AND BSD-2-Clause
ExclusiveArch:  x86_64
URL:            https://github.com/ROCm/rocm-libraries
%if %{with gitcommit}
Source0:        https://github.com/ROCm/%{toolchain}-%{pkg_libdir}raries/releases/download/%{pkg_module}.%{rocm_patch}/%{upstreamname}.tar.gz#/%{name}.%{rocm_patch}.tar.gz
%else
%endif
Patch0:         0001-rocsolver-ninja-job-pools.patch
Patch2:         0001-rocsolver-parallel-jobs.patch
%if %{with compress}
%endif
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
Provides:       rocsolver%{pkg_suffix} = %{version}-%{release}
# oreon:deps
BuildRequires:  blas-static
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  lapack-static
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  rocblas-7.1-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocprim-7.1-static
BuildRequires:  rocsparse-7.1-devel
# /oreon:deps
%description
rocSOLVER is a work-in-progress implementation of a subset
of LAPACK functionality on the ROCm platform.

%if 0%{?suse_version}
%package -n %{rocsolver_name}
Summary:        Shared libraries for %{name}
%description -n %{rocsolver_name}
%{summary}

%ldconfig_scriptlets -n %{rocsolver_name}
%endif

%package devel
Summary: Libraries and headers for %{name}
Requires:       %{rocsolver_name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{rocsolver_name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/rocsolver
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1 
%else
%autosetup -p1 -n %{upstreamname}
%endif

# As of 6.4, there are 2 long running hip jobs
# There are ~20 gpu targets
# Most builders will have between 4 and 32 cores
# Default to 2 cpu's per hip job
# Increase to half of the systems maximum
# Real cores, No hyperthreading
HIP_JOBS=`lscpu | grep 'Core(s)' | awk '{ print $4 }'`
if [ ${HIP_JOBS}x = x ]; then
    HIP_JOBS=1
fi
# Try again..
if [ ${HIP_JOBS} = 1 ]; then
    HIP_JOBS=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${HIP_JOBS}x = x ]; then
        HIP_JOBS=4
    fi
fi
HIP_JOBS=`eval "expr ${HIP_JOBS} / 2"`

# Take into account memmory usage per core, do not thrash real memory
BUILD_MEM=32
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
HIP_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$HIP_JOBS_MEM" -lt "$HIP_JOBS" ]; then
    HIP_JOBS=$HIP_JOBS_MEM
fi

sed -i -e "s@-parallel-jobs=4@-parallel-jobs=${HIP_JOBS}@" library/src/CMakeLists.txt

%build

%if %{with gitcommit}
cd projects/rocsolver
%endif
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
BUILD_MEM=8
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
%cmake %{cmake_generator} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_RPATH=ON \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DGPU_TARGETS=%{gpu_list} \
    -DBUILD_OFFLOAD_COMPRESS=%{build_compress} \
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DROCSOLVER_PARALLEL_COMPILE_JOBS=${COMPILE_JOBS} \
    -DROCSOLVER_PARALLEL_LINK_JOBS=${LINK_JOBS} \
    -DBUILD_PARALLEL_HIP_JOBS=ON
%if %{with ninja}
%cmake_build
%else
%cmake_build -j ${JOBS}
%endif
%install
%if %{with gitcommit}
cd projects/rocsolver
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocsolver/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?suse_version}
%files -f %{oreon_filedir}/main.list
%files -n rocsolver-7.1-devel -f %{oreon_filedir}/rocsolver-7.1-devel.list
%files -n rocsolver-7.1-test -f %{oreon_filedir}/rocsolver-7.1-test.list

%changelog

%autochangelog
%endif
