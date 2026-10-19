%global source1_hash e5fb89f55b6d5abf1be85cc35a68bc496d908fdf9b9c51ad44ac3cbf67aa35ee
%global source0_hash beb9cbf4475d979e8431a983ee0ae8a9f5b75bb24699b7b8dfa2753db9822c4d
%global upstreamname AMDMIGraphX
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
%global bundled_llvm_version 21.0.0
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%global _source_payload         w7T0.xzdio
%global _binary_payload         w7T0.xzdio
%global _smp_mflags %{nil}
%global gpu_list %{rocm_gpu_list_default}
%bcond check 1
%if %{with check}
%global build_test ON
%else
%global build_test OFF
%endif
Name:           migraphx
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        AMD's graph optimization engine
License:        MIT AND (Apache-2.0 WITH LLVM-exception OR NCSA)
URL:            https://github.com/ROCm/AMDMIGraphX
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{toolchain}-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Source1:        https://github.com/ROCm/rocMLIR/archive/rocm-%{version}.tar.gz#/rocMLIR-%{version}.tar.gz
Patch1:         0001-migraphx-check-if-use_hipblaslt-before-call-gfx_defa.patch
ExclusiveArch:  x86_64
Provides:       bundled(llvm) = %bundled_llvm_version
Provides:       bundled(clang) = %bundled_llvm_version
# oreon:deps
BuildRequires:  ccache
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  half-devel
BuildRequires:  miopen-devel
BuildRequires:  msgpack-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  protobuf-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-clang
BuildRequires:  rocm-cmake
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
# /oreon:deps
%description
AMD MIGraphX is AMD's graph inference engine, which
accelerates machine learning model inference.

%package devel
Summary:        The development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}
tar xf %{SOURCE1}
cd rocMLIR-rocm-%{version}
# patch -p1 < %{SOURCE100}
cp -p LICENSE.TXT ../LICENSE.rocMLIR.TXT
cp -p external/llvm-project/LICENSE.TXT ../LICENSE.llvm-project.TXT

# rm llvm-project bits we do not need
# llvm build is internal to rocMLIR, so we can not remove as much as we would like
rm -rf external/llvm-project/{amd,bolt,clang-tools-extra,clang/test,compiler-rt,flang,flang-rt,libclc,libcxx,lldb,llvm-libgcc,polly}

%build

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
%global _vpath_srcdir rocMLIR-rocm-%{version}
%global _vpath_builddir build-rocmlir
p=$PWD
%cmake -G Ninja \
       -DBUILD_FAT_LIBROCKCOMPILER=ON \
       -DBUILD_SHARED_LIBS=OFF \
       -DCMAKE_BUILD_TYPE=RELEASE \
       -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
       -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
       -DCMAKE_INSTALL_PREFIX=$PWD/install \
       -DROCMLIR_PARALLEL_COMPILE_JOBS=$COMPILE_JOBS \
       -DROCMLIR_PARALLEL_LINK_JOBS=$LINK_JOBS
%cmake_build
%cmake_build -t install
%global _vpath_srcdir $PWD
%global _vpath_builddir build-migraphx
%cmake -G Ninja \
       -DBoost_USE_STATIC_LIBS=OFF \
       -DBUILD_TESTING=%{build_test} \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
       -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_PREFIX_PATH=${p}/install/lib64/cmake \
       -DGPU_TARGETS=%{gpu_list} \
       -DMIGRAPHX_ENABLE_PYTHON=OFF \
       -DMIGRAPHX_USE_COMPOSABLEKERNEL=OFF \
       -DMIGRAPHX_USE_HIPBLASLT=OFF \
       -DMIOPEN_BACKEND=HIP 
%cmake_build -j $COMPILE_JOBS
%install
%global _vpath_builddir build-migraphx
%cmake_install
chrpath -d %{buildroot}%{_libdir}/libmigraphx*.so.*
rm -f %{buildroot}%{_prefix}/share/doc/migraphx/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%global _vpath_builddir build-migraphx
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n migraphx-devel -f %{oreon_filedir}/migraphx-devel.list

%changelog

%autochangelog
