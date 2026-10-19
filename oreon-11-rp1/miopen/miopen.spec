%global source0_hash 3fa0a7c8ef959ad889aac0109e6bf74de2a54f7e3ab057f98e2dc4fb65eb1599
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname MIOpen
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
%global miopen_name libMIOpen1%{pkg_suffix}
%else
%global miopen_name miopen%{pkg_suffix}
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-g / /' -e 's/-mtls-dialect=gnu2//')
%bcond_with debug
%if 0%{?suse_version}
%if %{without debug}
%global build_type RELEASE
%global build_cxxflags %(echo %{optflags} | sed -e 's/-g\\( \\|$\\)/ /')
%endif
%else
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif
%bcond check 1
%global gpu_test default
%if %{with test}
%if %{with check}
%global rocm_gpu_list %{gpu_test}
%endif
%endif
%bcond_without tensile
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100
%bcond_without ninja
%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif
Name:           %{miopen_name}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        AMD's Machine Intelligence Library
License:        MIT AND BSD-2-Clause AND Apache-2.0 AND %{?fedora:LicenseRef-Fedora-Public-Domain}%{?suse_version:SUSE-Public-Domain}
%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
Url:            https://github.com/ROCm/%{upstreamname}
%endif
Patch1:         0001-miopen-add-link-and-compile-pools.patch
%if 0%{?suse_version}
%if 0%{?suse_version} < 1600
%else
%endif
%else
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
Provides:       miopen%{pkg_suffix} = %{version}-%{release}
Requires:       rocm-hip%{pkg_suffix}-devel
Requires:       rocrand%{pkg_suffix}-devel
Requires:       gcc-c++
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fplus-devel
BuildRequires:  frugally-deep-devel
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  half-devel
BuildRequires:  hipblas-7.1-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  rocblas-7.1-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocrand-7.1-devel
BuildRequires:  roctracer-7.1-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
AMD's library for high performance machine learning primitives.

%package devel
Summary: Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       miopen%{pkg_suffix}-devel = %{version}-%{release}
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

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/miopen
%patch -P1 -p1
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

# Readme has executable bit
chmod 644 README.md

# clang-tidy is brittle and not needed for rebuilding from a tarball
sed -i -e 's@clang-tidy@true@' cmake/ClangTidy.cmake

# workaround error on finding lbunzip2
sed -i -e 's@lbunzip2 bunzip2@bunzip2@' CMakeLists.txt

# https://github.com/ROCm/MIOpen/issues/2672
sed -i -e 's@find_path(HALF_INCLUDE_DIR half/half.hpp)@#find_path(HALF_INCLUDE_DIR half/half.hpp)@' CMakeLists.txt
# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.cpp' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done
# On 6.4.0
# ../test/verify.hpp:198:56: error: no member named 'expr' in namespace 'half_float::detail'
#  198 |     if constexpr(std::is_same_v<T, half_float::detail::expr>)
# This is not our float, hack it out
sed -i -e 's@std::is_same_v<T, half_float::detail::expr>@0@' test/verify.hpp

# Tries to download its own googletest
# No good knob to turn it off so hack the cmake
%if %{without test}
sed -i -e 's@add_subdirectory(test)@#add_subdirectory(test)@' CMakeLists.txt
sed -i -e 's@add_subdirectory(speedtests)@#add_subdirectory(speedtests)@' CMakeLists.txt
%endif

%if %{without tensile}
sed -i -e 's@#define ROCBLAS_BETA_FEATURES_API 1@#define ROCBLAS_BETA_FEATURES_API 0@' src/include/miopen/handle.hpp
sed -i -e 's@#define ROCBLAS_BETA_FEATURES_API 1@#define ROCBLAS_BETA_FEATURES_API 0@' src/solver/mha/mha_common.hpp
sed -i -e 's@#define ROCBLAS_BETA_FEATURES_API 1@#define ROCBLAS_BETA_FEATURES_API 0@' src/gemm_v2.cpp
%endif

# Our use of modules confuse install locations
# The db is not installed relative to the lib dir.
# Hardcode its location
sed -i -e 's@GetLibPath().parent_path() / "share/miopen/db"@"/usr/share/miopen/db"@' src/db_path.cpp.in

# Unsupported compiler flags
sed -i -e 's@opts.push_back("-fno-offload-uniform-block");@//opts.push_back("-fno-offload-uniform-block");@' src/comgr.cpp

# Paths to clang
sed -i -e 's@llvm/bin/clang@bin/clang@' src/hip/hip_build_utils.cpp

%build

%if %{with gitcommit}
cd projects/miopen
%endif
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
BUILD_MEM=4
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
%{?suse_version:%{?build_cxxflags:CXXFLAGS="%{build_cxxflags}"}}
%cmake %{cmake_generator} \
       -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
       -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DROCM_SYMLINK_LIBS=OFF \
       -DHIP_PLATFORM=amd \
       -DGPU_TARGETS=%{gpu_list} \
       -DBUILD_TESTING=%{build_test} \
       %{?build_type:-DCMAKE_BUILD_TYPE=%{build_type}} \
       -DCMAKE_SKIP_RPATH=ON \
       -DBoost_USE_STATIC_LIBS=OFF \
       -DMIOPEN_PARALLEL_COMPILE_JOBS=$COMPILE_JOBS \
       -DMIOPEN_PARALLEL_LINK_JOBS=$LINK_JOBS \
       -DMIOPEN_BACKEND=HIP \
       -DMIOPEN_BUILD_DRIVER=OFF \
       -DMIOPEN_ENABLE_AI_IMMED_MODE_FALLBACK=OFF \
       -DMIOPEN_ENABLE_AI_KERNEL_TUNING=OFF \
       -DMIOPEN_TEST_ALL=%{build_test} \
       -DMIOPEN_USE_HIPBLASLT=OFF \
       -DMIOPEN_USE_MLIR=OFF \
       -DMIOPEN_USE_COMPOSABLEKERNEL=OFF
%cmake_build
%if %{with test}
%if 0%{?suse_version}
%cmake_build tests
%else
%cmake_build -t tests
%endif
%endif
%if %{with test}
%if %{with check}
%check

find . -name 'libMIOpen.so.1'
%if 0%{?suse_version}
export LD_LIBRARY_PATH=${PWD}/%{__builddir}/lib:$LD_LIBRARY_PATH
%else
export LD_LIBRARY_PATH=${PWD}/%{_vpath_builddir}/lib:$LD_LIBRARY_PATH
%endif
%ctest
%endif
%endif
%install
%if %{with gitcommit}
cd projects/miopen
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/miopen-hip/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n miopen-7.1-devel -f %{oreon_filedir}/miopen-7.1-devel.list
%files -n miopen-7.1-test -f %{oreon_filedir}/miopen-7.1-test.list

%changelog

%autochangelog
