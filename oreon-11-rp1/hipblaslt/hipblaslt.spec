%global source0_hash 05d73038b1b4f66f3df4eb595b7cb0c8935f7aa18d0e07dbe5cc740a4b691898
%if 0%{!?suse_version:1}
%define python_exec python3
%define python_expand python3
%endif
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname hipblaslt
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
%global hipblaslt_name libhipblaslt0%{pkg_suffix}
%else
%global hipblaslt_name hipblaslt%{pkg_suffix}
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%global build_fflags %{nil}
%global _lto_cflags %{nil}
%global _smp_mflags %{nil}
%bcond_with test
%if %{with test}
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif
%global tensile_version 4.33.0
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%global gpu_list %{rocm_gpu_list_hipblaslt}
%global _gpu_list "gfx1100"
%bcond_with ninja
%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif
%bcond_with nanobind
Name:           %{hipblaslt_name}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        ROCm general matrix operations beyond BLAS
License:        MIT AND BSD-3-Clause
URL:            https://github.com/ROCm/rocm-libraries
%if %{with gitcommit}
Source0:        https://github.com/ROCm/%{toolchain}-%{pkg_libdir}raries/releases/download/%{pkg_module}.%{rocm_patch}/%{name}.tar.gz#/%{name}-%{version}.tar.gz
%else
%endif
%global nanobind_version 2.9.2
%global nanobind_giturl https://github.com/wjakob/nanobind
Source1:        %{nanobind_giturl}/archive/v%{nanobind_version}/nanobind-%{nanobind_version}.tar.gz
%global robinmap_version 1.3.0
%global robinmap_giturl https://github.com/Tessil/robin-map
Source2:        %{robinmap_giturl}/archive/v%{robinmap_version}/robin-map-%{robinmap_version}.tar.gz
Patch1:         0001-hipblaslt-tensilelite-remove-yappi-dependency.patch
Patch2:         0001-hipblaslt-tensilelite-use-fedora-paths.patch
Patch3:         0001-hipblaslt-find-origami-package.patch
Patch4:         0001-hipblaslt-tensilelite-use-nanobind-tarball.patch
Patch5:         0001-hipblaslt-cmake-compile-and-link-pools.patch
%if 0%{?suse_version}
%else
%endif
%if 0%{?suse_version}
%global tensile_verbose 2
%else
%if %{with nanobind}
%endif
%global tensile_verbose 1
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
Provides:       hipblaslt%{pkg_suffix} = %{version}-%{release}
Provides:       bundled(python-tensile) = %{tensile_version}
%if %{without nanobind}
Provides:       bundled(nanobind) = %{nanobind_version}
Provides:       bundled(robin-map) = %{robinmap_version}
%endif
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  blis-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  hipblas-devel
BuildRequires:  hipcc
BuildRequires:  lapack-devel
BuildRequires:  libzstd-devel
BuildRequires:  msgpack-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-llvm-devel
BuildRequires:  rocm-origami-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-smi-devel
BuildRequires:  rocminfo
BuildRequires:  zlib-devel
# /oreon:deps
%description
hipBLASLt is a library that provides general matrix-matrix
operations. It has a flexible API that extends functionalities
beyond a traditional BLAS library, such as adding flexibility
to matrix data layouts, input types, compute types, and
algorithmic implementations and heuristics.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       hipblaslt%{pkg_suffix}-devel = %{version}-%{release}
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

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/hipblaslt
%patch -P1 -p1
%patch -P2 -p1
%else
%autosetup -p1 -n %{upstreamname}
%endif

# Use PATH to find where TensileGetPath and other tensile bins are
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g'            tensilelite/Tensile/cmake/TensileConfig.cmake

# defer to cmdline
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt

# Do not use virtualenv_install
sed -i -e 's@virtualenv_install@#virtualenv_install@'                          CMakeLists.txt

# Disable trying to download rocm-cmake
sed -i -e 's@if(NOT ROCmCMakeBuildTools_FOUND)@if(FALSE)@' cmake/dependencies.cmake

%if %{with nanobind}
# Disable download of nanobind
sed -i -e 's@FetchContent_MakeAvailable(nanobind)@find_package(nanobind)@' tensilelite/rocisa/CMakeLists.txt
%else
# Use bundled nanobind
tar xf %{SOURCE1}
mv nanobind-* nanobind
cd nanobind
tar xf %{SOURCE2}
cp -r robin-map-*/* ext/robin_map/
cd ..
tar czf nanobind.tar.gz nanobind
%endif

# As of 6.4, there is a long poll
# compile_code_object.sh gfx90a,gfx1100,gfx1101,gfx1151,gfx1200,gfx1201 RelWithDebInfo sha1 hipblasltTransform.hsaco
# This compiles a large file with multiple gpus.
GPUS=`echo %{gpu_list} | grep -o 'gfx' | wc -l`

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
if [ "$GPUS" -lt "$HIP_JOBS" ]; then
    HIP_JOBS=$GPUS
fi

# HIPBLASLT_ENABLE_OPENMP is OFF yet it is still being used
# https://github.com/ROCm/rocm-libraries/issues/3201
sed -i -e '/OpenMP::OpenMP_CXX/d' clients/CMakeLists.txt
sed -i -e '/omp/d'                clients/common/src/blis_interface.cpp
sed -i -e '/#include <omp.h>/d'   clients/common/include/testing_matmul.hpp
sed -i -e '/#include <omp.h>/d'   clients/common/include/hipblaslt_init.hpp
sed -i -e '/#include <omp.h>/d'   clients/common/src/cblas_interface.cpp

# We are building from a tarball, not a git repo
sed -i -e 's@find_package(Git REQUIRED)@#find_package(Git REQUIRED)@' cmake/dependencies.cmake

%build

%if %{with gitcommit}
cd projects/hipblaslt
%endif
cd tensilelite
TL=$PWD
%python_exec setup.py install --root $TL
cd ..
export PATH=%{pkg_prefix}/bin:$PATH
CLANG_PATH=`hipconfig --hipclangpath`
ROCM_CLANG=${CLANG_PATH}/clang
RESOURCE_DIR=`${ROCM_CLANG} -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode
export TENSILE_ROCM_ASSEMBLER_PATH=${CLANG_PATH}/clang++
export TENSILE_ROCM_OFFLOAD_BUNDLER_PATH=${CLANG_PATH}/clang-offload-bundler
export PATH=${TL}/%{_bindir}:$PATH
%if 0%{?suse_version}
%{python_expand} export PYTHONPATH=${TL}%{python_sitelib}:$PYTHONPATH
%{python_expand} export Tensile_DIR=${TL}%{python_sitelib}/Tensile
%else
export PYTHONPATH=${TL}%{python3_sitelib}:$PYTHONPATH
export Tensile_DIR=${TL}%{python3_sitelib}/Tensile
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
       -DGPU_TARGETS=%{gpu_list} \
       -DBLIS_INCLUDE_DIR=%{_includedir}/blis \
       -DBLIS_LIB=%{_libdir}/libblis.so \
       -DBUILD_CLIENTS_TESTS=%{build_test} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DBUILD_VERBOSE=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/amdclang \
       -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/amdclang++ \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DCMAKE_PREFIX_PATH=%{python3_sitelib}/nanobind \
       -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DHIP_PLATFORM=amd \
       -DHIPBLASLT_ENABLE_CLIENT=%{build_test} \
       -DHIPBLASLT_ENABLE_MARKER=OFF \
       -DHIPBLASLT_ENABLE_OPENMP=OFF \
       -DHIPBLASLT_ENABLE_ROCROLLER=OFF \
       -DHIPBLASLT_ENABLE_SAMPLES=OFF \
       -DROCM_SYMLINK_LIBS=OFF \
       -DTensile_LIBRARY_FORMAT=msgpack \
       -DTensile_VERBOSE=%{tensile_verbose} \
       -DVIRTUALENV_BIN_DIR=%{_bindir} \
       -DHIPBLASLT_PARALLEL_COMPILE_JOBS=${COMPILE_JOBS} \
       -DHIPBLASLT_PARALLEL_LINK_JOBS=${LINK_JOBS} \
       %{nil}
%cmake_build
%install
%if %{with gitcommit}
cd projects/hipblaslt
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipblaslt/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n hipblaslt-devel -f %{oreon_filedir}/hipblaslt-devel.list
%files -n hipblaslt-test -f %{oreon_filedir}/hipblaslt-test.list

%changelog

%autochangelog
