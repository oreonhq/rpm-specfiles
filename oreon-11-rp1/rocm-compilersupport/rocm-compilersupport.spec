%global source0_hash none

#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

# For building earlier snapshots of the compiler
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 1b0eada6b0ee93e2e694c8c146d23fca90bc11c5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20251024

# The package follows LLVM's major version, but API version is still important:
%global comgr_maj_api_ver 3
# Upstream tags are based on rocm releases:
%global rocm_release 7.1
%global rocm_patch 0
# What LLVM is upstream using (use LLVM_VERSION_MAJOR from llvm/CMakeLists.txt):
%global llvm_maj_ver 20
%global llvm_version_suffix .rocm

%else
# Normal release

# The package follows LLVM's major version, but API version is still important:
%global comgr_maj_api_ver 3
# Upstream tags are based on rocm releases:
%global rocm_release 7.1
%global rocm_patch 1
# What LLVM is upstream using (use LLVM_VERSION_MAJOR from llvm/CMakeLists.txt):
%global llvm_maj_ver 20
%global llvm_version_suffix .rocm

%endif
# local, fedora
%global _comgr_full_api_ver %{comgr_maj_api_ver}.0
# mock, suse
%global comgr_full_api_ver %{comgr_maj_api_ver}.0.0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname llvm-project

%global toolchain clang

%global _smp_mflags %{nil}
%global _lto_cflags %{nil}
%global llvm_triple %{_target_platform}

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

%bcond_with compat
%if %{with compat}
%global amd_device_libs_prefix %{_libdir}/rocm/rocm-%{rocm_release}/llvm/lib/clang/%{llvm_maj_ver}/lib
%global bundle_prefix %{_libdir}/rocm/rocm-%{rocm_release}/llvm
%global pkg_libdir lib
%global pkg_libdir_suffix %{nil}
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%else
%global amd_device_libs_prefix %{_libdir}/rocm/llvm/lib/clang/%{llvm_maj_ver}/lib
%global bundle_prefix %{_libdir}/rocm/llvm
%global pkg_libdir %{_lib}
%global pkg_libdir_suffix %{nil}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%global device_libs_name rocm-device-libs%{pkg_suffix}
%global hipcc_name hipcc%{pkg_suffix}
%global pkg_name rocm-compilersupport%{pkg_suffix}
%global rocm_clang_analyzer_name rocm-clang-analyzer%{pkg_suffix}
%global rocm_clang_name rocm-clang%{pkg_suffix}
%global rocm_clang_tools_extra_name rocm-clang-tools-extra%{pkg_suffix}
%global rocm_libcxx_name rocm-libc++%{pkg_suffix}
%global rocm_lld_name rocm-lld%{pkg_suffix}
%global rocm_llvm_name rocm-llvm%{pkg_suffix}
%if 0%{?suse_version}
# 15.6
# rocm-comgr.x86_64: E: shlib-policy-name-error (Badness: 10000) libamd_comgr2
# Your package contains a single shared library but is not named after its SONAME.
%global comgr_name libamd_comgr3%{pkg_suffix}
%else
%global comgr_name rocm-comgr%{pkg_suffix}
%endif

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Enable ppc and aarch64 builds
%bcond_with alt_arch

# buid the static analyzer
%bcond_without sa
%if %{with sa}
%global build_sa ON
%else
%global build_sa OFF
%endif

# build gold plugin
%bcond_without gold
%if %{with gold}
%global build_gold ON
%else
%global build_gold OFF
%endif

Name:           %{pkg_name}
Version:        %{llvm_maj_ver}
%if %{with gitcommit}
Release:        0.rocm%{rocm_version}^git%{date0}.%{shortcommit0}%{?dist}.1
%else
Release:        13.rocm%{rocm_version}%{?dist}
%endif

Summary:        Various AMD ROCm LLVM related services
%if 0%{?suse_version}
Group:          Development/Languages/Other
%endif

Url:            https://github.com/ROCm/llvm-project
# llvm is Apache-2.0 WITH LLVM-exception OR NCSA
# hipcc is MIT, comgr and device-libs are NCSA:
License:        (Apache-2.0 WITH LLVM-exception OR NCSA) AND NCSA AND MIT
%if %{with gitcommit}
Source0:        %{url}/archive/%{commit0}/llvm-project-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/rocm-compilersupport-%{rocm_version}.tar.gz
%endif
Source1:        rocm-compilersupport.prep.in

# Subject: [PATCH] [gold] Fix compilation (#130334)
Patch1:         %{url}/commit/b0baa1d8bd68a2ce2f7c5f2b62333e410e9122a1.patch
# Link comgr with static versions of llvm's libraries
Patch2:         0001-comgr-link-with-static-llvm.patch
# On Fedora the assert came in gcc 15, on RHEL 10.2 gcc 14
# Reduce the gcc version check below
Patch3:         0001-rocm-llvm-work-around-new-assert-in-array.patch
# https://github.com/ROCm/llvm-project/issues/301
Patch4:         0001-rocm-compilersupport-force-hip-runtime-detection.patch
Patch5:         0001-rocm-compilersupport-simplify-use-runtime-wrapper-ch.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2415065
Patch6:         0001-lld-workaround-.gnu.version-change.patch

BuildRequires:  cmake
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  libffi-devel
BuildRequires:  libzstd-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  zlib-devel
%if %{with gold}
BuildRequires:  binutils-devel
%endif
BuildRequires:  gcc-c++
Provides:       bundled(llvm-project) = %{llvm_maj_ver}

%if 0%{?rhel} || 0%{?suse_version}
ExclusiveArch:  x86_64
%global targets_to_build "X86;AMDGPU"
%else
%if %{with alt_arch}
ExclusiveArch:  x86_64 aarch64 ppc64le
%else
ExclusiveArch:  x86_64
%endif

%ifarch x86_64
%global targets_to_build "X86;AMDGPU"
%endif
%ifarch aarch64
%global targets_to_build "AArch64;AMDGPU"
%endif
%ifarch ppc64le
%global targets_to_build "PowerPC;AMDGPU"
%endif
%endif

%description
%{summary}

%package macros
Summary:        ROCm Compiler RPM macros
BuildArch:      noarch

%description macros
This package contains ROCm compiler related RPM macros.

%package -n %{device_libs_name}
Summary:        AMD ROCm LLVM bit code libraries
Requires:       %{rocm_clang_name}-devel
Requires:       %{rocm_llvm_name}-static
Requires:       rocm-lld%{pkg_suffix}

%description -n %{device_libs_name}
This package contains a set of AMD specific device-side language runtime
libraries in the form of bit code. Specifically:
 - Open Compute library controls
 - Open Compute Math library
 - Open Compute Kernel library
 - OpenCL built-in library
 - HIP built-in library
 - Heterogeneous Compute built-in library
 
%package -n %{comgr_name}
Summary:        AMD ROCm LLVM Code Object Manager
Provides:       comgr%{pkg_suffix}(major) = %{comgr_maj_api_ver}
Provides:       rocm-comgr%{pkg_suffix} = %{comgr_full_api_ver}-%{release}

%description -n %{comgr_name}
The AMD Code Object Manager (Comgr) is a shared library which provides
operations for creating and inspecting code objects.

%post -n %{comgr_name}  -p /sbin/ldconfig
%postun -n %{comgr_name} -p /sbin/ldconfig

%package -n %{comgr_name}-devel
Summary:        AMD ROCm LLVM Code Object Manager
Requires:       %{comgr_name}%{?_isa} = %{version}-%{release}
Requires:       %{device_libs_name}
%if 0%{?suse_version}
Provides:       rocm-comgr%{pkg_suffix}-devel = %{version}-%{release}
%endif

%description -n %{comgr_name}-devel
The AMD Code Object Manager (Comgr) development package.

%package -n %{hipcc_name}
Summary:        HIP compiler driver
Requires:       %{device_libs_name} = %{version}-%{release}
Suggests:       rocminfo%{pkg_suffix}
%if 0%{?suse_version}
Provides:       hip = %{version}-%{release}
Obsoletes:      hip <= %{version}-%{release}
%endif

%description -n %{hipcc_name}
hipcc is a compiler driver utility that will call clang or nvcc, depending on
target, and pass the appropriate include and library options for the target
compiler and HIP infrastructure.

hipcc will pass-through options to the target compiler. The tools calling hipcc
must ensure the compiler options are appropriate for the target compiler.

# ROCM LLVM
%package -n %{rocm_llvm_name}-filesystem
Summary: Filesystem package that owns the rocm llvm directory

%description -n %{rocm_llvm_name}-filesystem
This package owns the rocm llvm directory : %{bundle_prefix}

%package -n %{rocm_llvm_name}-libs
Summary: The ROCm LLVM lib
Requires:      %{rocm_llvm_name}-filesystem%{?_isa} = %{version}-%{release}
Requires:      %{rocm_libcxx_name}%{?_isa} = %{version}-%{release}

%description -n %{rocm_llvm_name}-libs
%{summary}

%package -n %{rocm_llvm_name}
Summary:       The ROCm LLVM
Requires:      %{rocm_llvm_name}-libs%{?_isa} = %{version}-%{release}
# https://bugzilla.redhat.com/show_bug.cgi?id=2362780
#  /usr/lib64/rocm/llvm/bin/amdgpu-arch 
#  Failed to 'dlopen' libhsa-runtime64.so
Recommends:      rocm-runtime%{pkg_suffix}-devel

%description -n %{rocm_llvm_name}
%{summary}

%package -n %{rocm_llvm_name}-devel
Summary:       Libraries and header files for ROCm LLVM
Requires:      %{rocm_llvm_name}%{?_isa} = %{version}-%{release}
Requires:      zlib-devel

%description -n %{rocm_llvm_name}-devel
%{summary}

%post -n %{rocm_llvm_name}-devel -p /sbin/ldconfig
%postun -n %{rocm_llvm_name}-devel -p /sbin/ldconfig

%package -n %{rocm_llvm_name}-static
Summary:       Static libraries for ROCm LLVM
Requires:      %{rocm_llvm_name}-devel%{?_isa} = %{version}-%{release}

%description -n %{rocm_llvm_name}-static
%{summary}

# ROCM CLANG
%package -n %{rocm_clang_name}-libs
Summary:       The ROCm compiler libs
Requires:      %{rocm_llvm_name}-libs%{?_isa} = %{version}-%{release}

%description -n %{rocm_clang_name}-libs
%{summary}

%post -n %{rocm_clang_name}-libs -p /sbin/ldconfig
%postun -n %{rocm_clang_name}-libs -p /sbin/ldconfig

%package -n %{rocm_clang_name}-runtime-devel
Summary:       The ROCm compiler runtime

%description -n %{rocm_clang_name}-runtime-devel
%{summary}

%package -n %{rocm_clang_name}
Summary:       The ROCm compiler
Requires:      git
Requires:      python3
Requires:      %{rocm_clang_name}-libs%{?_isa} = %{version}-%{release}
Requires:      %{rocm_clang_name}-runtime-devel%{?_isa} = %{version}-%{release}
Requires:      %{rocm_libcxx_name}-devel%{?_isa} = %{version}-%{release}

%description -n %{rocm_clang_name}
%{summary}

%package -n %{rocm_clang_name}-devel
Summary:       Libraries and header files for ROCm CLANG
Requires:      %{rocm_clang_name}%{?_isa} = %{version}-%{release}

%description -n %{rocm_clang_name}-devel
%{summary}

# CLANG TOOLS EXTRA
%package -n %{rocm_clang_tools_extra_name}
Summary:	Extra tools for clang
Requires:	rocm-clang%{pkg_suffix}-libs%{?_isa} = %{version}-%{release}

%description -n %{rocm_clang_tools_extra_name}
A set of extra tools built using Clang's tooling API.

%package -n %{rocm_clang_tools_extra_name}-devel
Summary: Development header files for clang tools
Requires: %{rocm_clang_tools_extra_name} = %{version}-%{release}

%description -n %{rocm_clang_tools_extra_name}-devel
Development header files for clang tools.

# ROCM LLD
%package -n %{rocm_lld_name}
Summary:        The ROCm Linker
Requires:      %{rocm_llvm_name}-libs%{?_isa} = %{version}-%{release}

%description -n %{rocm_lld_name}
%{summary}

# ROCM LIBC++
%package -n %{rocm_libcxx_name}
Summary:       The ROCm libc++
Requires:      %{rocm_llvm_name}-filesystem%{?_isa} = %{version}-%{release}

%description -n %{rocm_libcxx_name}
%{summary}

%package -n %{rocm_libcxx_name}-devel
Summary:       The ROCm libc++ libraries and headers
Requires:      %{rocm_libcxx_name}%{?_isa} = %{version}-%{release}

%description -n %{rocm_libcxx_name}-devel
%{summary}

%package -n %{rocm_libcxx_name}-static
Summary:       The ROCm libc++ static libraries
Requires:      %{rocm_libcxx_name}-devel%{?_isa} = %{version}-%{release}

%description -n %{rocm_libcxx_name}-static
%{summary}

%if %{with sa}
%package -n %{rocm_clang_analyzer_name}
Summary:       The ROCm code analysis framework
Requires:      %{rocm_clang_name} = %{version}-%{release}
# For scan-build
Requires:      perl(File::Copy)
Requires:      perl(File::Find)
Requires:      perl(FindBin)
Requires:      perl(Hash::Util)
Requires:      perl(Sys::Hostname)

%description -n %{rocm_clang_analyzer_name}
%{summary}
%endif

%prep
%if %{with gitcommit}
%autosetup -p1 -n %{upstreamname}-%{commit0}
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{rocm_version}
%endif

# rm llvm-project bits we do not need
rm -rf {bolt,flang,flang-rt,libclc,lldb,llvm-libgcc,mlir,polly}

#Force static linking of libclang in comgr
sed -i "s/TARGET clangFrontendTool/true/" amd/comgr/CMakeLists.txt

# change version check of array assert work around
%if 0%{?rhel}
sed -i -e 's@#if _GLIBCXX_RELEASE >= 15@#if _GLIBCXX_RELEASE >= 14@' clang/lib/Headers/cuda_wrappers/array
%endif

install -pm 755 %{SOURCE1} prep.sh
sed -i -e 's@%%{pkg_prefix}@%{pkg_prefix}@' prep.sh
sed -i -e 's@%%{pkg_libdir}@%{pkg_libdir}@' prep.sh
sed -i -e 's@%%{amd_device_libs_prefix}@%{amd_device_libs_prefix}@' prep.sh
sed -i -e 's@%%{bundle_prefix}@%{bundle_prefix}@' prep.sh
grep -v '%%{' prep.sh

. ./prep.sh

%build
CLANG_VERSION=%llvm_maj_ver
LLVM_BINDIR=%{bundle_prefix}/bin
LLVM_LIBDIR=%{bundle_prefix}/lib
LLVM_CMAKEDIR=%{bundle_prefix}/lib/cmake/llvm

echo "%%rocmllvm_version $CLANG_VERSION"   > macros.rocmcompiler
echo "%%rocmllvm_bindir $LLVM_BINDIR"     >> macros.rocmcompiler
echo "%%rocmllvm_libdir $LLVM_LIBDIR"     >> macros.rocmcompiler
echo "%%rocmllvm_cmakedir $LLVM_CMAKEDIR" >> macros.rocmcompiler

# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memmory usage per core, do not thrash real memory
LINK_MEM=4
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`
JOBS=${COMPILE_JOBS}
if [ "$LINK_JOBS" -lt "$JOBS" ]; then
    JOBS=$LINK_JOBS
fi

%global llvm_projects "clang;clang-tools-extra;lld"
%global llvm_runtimes "compiler-rt;libcxx;libcxxabi"
%global build_libcxx ON

p=$PWD

#
# BASE LLVM
#
%global llvmrocm_cmake_config \\\
 -DBUILD_SHARED_LIBS=OFF \\\
 -DBUILD_TESTING=OFF \\\
 -DCLANG_ENABLE_STATIC_ANALYZER=%{build_sa} \\\
 -DCLANG_ENABLE_ARCMT=OFF \\\
 -DCLANG_TOOL_CLANG_FUZZER_BUILD=OFF \\\
 -DCMAKE_BUILD_TYPE=%{build_type} \\\
 -DCMAKE_INSTALL_DO_STRIP=ON \\\
 -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \\\
 -DCOMPILER_RT_BUILD_BUILTINS=ON \\\
 -DCOMPILER_RT_BUILD_CTX_PROFILE=OFF \\\
 -DCOMPILER_RT_BUILD_GWP_ASAN=OFF \\\
 -DCOMPILER_RT_BUILD_LIBFUZZER=OFF \\\
 -DCOMPILER_RT_BUILD_MEMPROF=OFF \\\
 -DCOMPILER_RT_BUILD_ORC=OFF \\\
 -DCOMPILER_RT_BUILD_PROFILE=OFF \\\
 -DCOMPILER_RT_BUILD_SANITIZERS=OFF \\\
 -DCOMPILER_RT_BUILD_XRAY=OFF \\\
 -DENABLE_LINKER_BUILD_ID=ON \\\
 -DLIBCXX_INCLUDE_BENCHMARKS=OFF \\\
 -DLIBCXXABI_USE_LLVM_UNWINDER=OFF \\\
 -DLLVM_BINUTILS_INCDIR=%{_includedir} \\\
 -DLLVM_BUILD_RUNTIME=ON \\\
 -DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \\\
 -DLLVM_ENABLE_EH=ON \\\
 -DLLVM_ENABLE_FFI=ON \\\
 -DLLVM_ENABLE_LIBCXX=%{build_libcxx} \\\
 -DLLVM_ENABLE_OCAMLDOC=OFF \\\
 -DLLVM_ENABLE_RTTI=ON \\\
 -DLLVM_ENABLE_ZLIB=ON \\\
 -DLLVM_ENABLE_ZSTD=ON \\\
 -DLLVM_INCLUDE_BENCHMARKS=OFF \\\
 -DLLVM_INCLUDE_EXAMPLES=OFF \\\
 -DLLVM_INCLUDE_TESTS=OFF \\\
 -DLLVM_LIBDIR_SUFFIX=%{pkg_libdir_suffix} \\\
 -DLLVM_TARGETS_TO_BUILD=%{targets_to_build} \\\
 -DLLVM_TOOL_GOLD_BUILD=%{build_gold} \\\
 -DLLVM_TOOL_LLVM_AS_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_DIS_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_DLANG_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_ISEL_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_ITANIUM_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MC_ASSEMBLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MC_DISASSEMBLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MICROSOFT_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_OPT_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_RUST_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_SPECIAL_CASE_LIST_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_YAML_NUMERIC_PARSER_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_YAML_PARSER_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_VFABI_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_VERSION_SUFFIX=%{llvm_version_suffix} \\\
 -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \\\
 -DLLVM_BUILD_LLVM_DYLIB=ON \\\
 -DLLVM_LINK_LLVM_DYLIB=ON \\\
 -DLLVM_BUILD_TOOLS=ON \\\
 -DLLVM_BUILD_UTILS=ON \\\
 -DMLIR_BUILD_MLIR_C_DYLIB=ON

pushd .
%if 0%{?suse_version}
%define __sourcedir llvm
%define __builddir build-llvm
%else
%define _vpath_srcdir llvm
%define _vpath_builddir build-llvm
%endif

# Mixing use of gcc and clang in the build conflicts with rpm's setting of flags.
# Set them manually as CMAKE_<LANG>_FLAGS
export CFLAGS=""
export CXXFLAGS=""
export LDFLAGS=""

# So just built tools can find their *.so's
export LD_LIBRARY_PATH=$PWD/build-llvm/lib
export CC=/usr/bin/gcc
export CXX=/usr/bin/g++

%if 0%{?suse_version}
%cmake \
%else
%__cmake -S llvm -B build-llvm \
%endif
       %{llvmrocm_cmake_config} \
       -DCMAKE_CXX_COMPILER=/usr/bin/g++ \
       -DCMAKE_C_COMPILER=/usr/bin/gcc \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DLLVM_ENABLE_PROJECTS=%{llvm_projects}

%if 0%{?suse_version}
%cmake_build -j ${JOBS}
%else
%make_build -C build-llvm -j ${JOBS}
%endif

popd

build_stage1=$p/build-llvm

%global llvmrocm_stage1_config \\\
    -DCMAKE_AR=$build_stage1/bin/llvm-ar \\\
    -DCMAKE_C_COMPILER=$build_stage1/bin/clang \\\
    -DCMAKE_CXX_COMPILER=$build_stage1/bin/clang++ \\\
    -DCMAKE_LINKER=$build_stage1/bin/ld.lld \\\
    -DCMAKE_RANLIB=$build_stage1/bin/llvm-ranlib \\\
    -DLLVM_DIR=$build_stage1/lib/cmake/llvm \\\
    -DClang_DIR=$build_stage1/lib/cmake/clang \\\
    -DLLD_DIR=$build_stage1/lib/cmake/lld

#
# Rebuild and add libc++
#
pushd .
%if 0%{?suse_version}
%define __sourcedir llvm
%define __builddir build-llvm-2
%else
%define _vpath_srcdir llvm
%define _vpath_builddir build-llvm-2
%endif

export LD_LIBRARY_PATH=$PWD/build-llvm-2/lib

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_stage1_config} \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_RPATH=%{bundle_prefix}/lib \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DCMAKE_SKIP_INSTALL_RPATH=OFF \
       -DCLANG_DEFAULT_LINKER=lld \
       -DLLVM_ENABLE_LLD=ON \
       -DLLVM_TOOL_COMPILER_RT_BUILD=ON \
       -DLLVM_TOOL_LIBCXXABI_BUILD=%{build_libcxx} \
       -DLLVM_TOOL_LIBCXX_BUILD=%{build_libcxx} \
       -DLLVM_ENABLE_PROJECTS=%{llvm_projects} \
       -DLLVM_ENABLE_RUNTIMES=%{llvm_runtimes}

%cmake_build -j ${JOBS}
popd

build_stage2=$p/build-llvm-2

%global llvmrocm_tools_config \\\
       -DLLVM_DIR=$build_stage2/lib/cmake/llvm \\\
       -DClang_DIR=$build_stage2/lib/cmake/clang \\\
       -DLLD_DIR=$build_stage2/lib/cmake/lld

export CC=$build_stage2/bin/clang
export CXX=$build_stage2/bin/clang++
export LD=$build_stage2/bin/ld.lld

#
# DEVICE LIBS
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/device-libs
%define __builddir build-devicelibs
%else
%define _vpath_srcdir amd/device-libs
%define _vpath_builddir build-devicelibs
%endif

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{amd_device_libs_prefix}

%cmake_build -j ${JOBS}
popd

build_devicelibs=$p/build-devicelibs
%global llvmrocm_devicelibs_config \\\
	-DAMDDeviceLibs_DIR=$build_devicelibs/%{pkg_libdir}/cmake/AMDDeviceLibs

#
# HIPCC
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/hipcc
%define __builddir build-hipcc
%else
%define _vpath_srcdir amd/hipcc
%define _vpath_builddir build-hipcc
%endif

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       %{llvmrocm_devicelibs_config} \
       -DCMAKE_INSTALL_RPATH=%{bundle_prefix}/lib \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_SKIP_INSTALL_RPATH=OFF

%cmake_build -j ${JOBS}
popd

#
# COMGR
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/comgr
%define __builddir build-comgr
%else
%define _vpath_srcdir amd/comgr
%define _vpath_builddir build-comgr
%endif

%cmake -G "Unix Makefiles" \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       %{llvmrocm_devicelibs_config} \
       -DBUILD_SHARED_LIBS=ON \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir}

# cmake produces a link.txt that includes libLLVM*.so, hack it out
%if 0%{?suse_version}
sed -i -e 's@libLLVM.so.%{llvm_maj_ver}.0%{llvm_version_suffix}@libLLVMCore.a@' CMakeFiles/amd_comgr.dir/link.txt
# Order of link is wrong include some missing libs
sed -i -e 's@-lrt -lm@-lLLVMCoverage -lLLVMFrontendDriver -lLLVMFrontendHLSL -lLLVMLTO -lLLVMOption -lLLVMSymbolize -lLLVMWindowsDriver -lrt -lm@' CMakeFiles/amd_comgr.dir/link.txt
%else
sed -i -e 's@libLLVM.so.%{llvm_maj_ver}.0%{llvm_version_suffix}@libLLVMCore.a@' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
# Order of link is wrong include some missing libs
sed -i -e 's@-lrt -lm@-lLLVMCoverage -lLLVMFrontendDriver -lLLVMFrontendHLSL -lLLVMLTO -lLLVMOption -lLLVMSymbolize -lLLVMWindowsDriver -lrt -lm@' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
%endif

%cmake_build -j ${JOBS}

# Check that static linking happened
# ldd build-comgr/libamd_comgr.so
# fail

popd

%check
%if 0%{?suse_version}
%define __sourcedir amd/device-libs
%define __builddir build-devicelibs
%else
%define _vpath_srcdir amd/device-libs
%define _vpath_builddir build-devicelibs
%endif
pushd .
# Workaround for bug in cmake tests not finding amdgcn:
ln -s %{amd_device_libs_prefix}/amdgcn build-devicelibs/amdgcn
%if %{with broken_tests}
%ctest
%endif
popd

%install
install -Dpm 644 macros.rocmcompiler \
    %{buildroot}%{_rpmmacrodir}/macros.rocmcompiler

#
# BASE LLVM
#
pushd .
%if 0%{?suse_version}
%define __builddir build-llvm-2
%else
%define _vpath_builddir build-llvm-2
%endif

%cmake_install

popd

#
# DEVICE LIBS
#
pushd .
%if 0%{?suse_version}
%define __builddir build-devicelibs
%else
%define _vpath_builddir build-devicelibs
%endif

%cmake_install

# move cmake bits to where the others are
mkdir -p %{buildroot}%{pkg_prefix}/%{pkg_libdir}/cmake
mv %{buildroot}%{amd_device_libs_prefix}/%{pkg_libdir}/cmake/* %{buildroot}%{pkg_prefix}/%{pkg_libdir}/cmake
# no extra license please
rm -rf %{buildroot}%{amd_device_libs_prefix}/share

popd

#
# COMGR
#
pushd .
%if 0%{?suse_version}
%define __builddir build-comgr
%else
%define _vpath_builddir build-comgr
%endif

%cmake_install
popd

#
# HIPCC
#
pushd .
%if 0%{?suse_version}
%define __builddir build-hipcc
%else
%define _vpath_builddir build-hipcc
%endif

%cmake_install
popd

%if %{without compat}
# Make directories users of rocm-rpm-modules will install to
%global modules_gpu_list gfx8 gfx9 gfx10 gfx11 gfx12 gfx906 gfx908 gfx90a gfx942 gfx950 gfx1031 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103 gfx1150 gfx1151 gfx1152 gfx1153 gfx1200 gfx1201
for gpu in %{modules_gpu_list}
do
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/lib/cmake
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/bin
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/include
done
mkdir -p %{buildroot}%{_libdir}/rocm/lib/cmake
mkdir -p %{buildroot}%{_libdir}/rocm/bin
mkdir -p %{buildroot}%{_libdir}/rocm/include
%endif

rm -rf %{buildroot}%{pkg_prefix}/hip
rm -rf %{buildroot}%{pkg_prefix}/share/doc/packages/*

%if 0%{?suse_version}
find %{buildroot}%{bundle_prefix}/bin -type f -executable -exec strip {} \;
find %{buildroot}%{pkg_prefix}/bin -type f -executable -exec strip {} \;
find %{buildroot}%{bundle_prefix}/lib -type f -name '*.so*' -exec strip {} \;
find %{buildroot}%{pkg_prefix}/lib64 -type f -name '*.so*' -exec strip {} \;
%endif

# Remove lld's libs
rm -rf %{buildroot}%{bundle_prefix}/include/lld
rm -rf %{buildroot}%{bundle_prefix}/lib/cmake/lld
rm -rf %{buildroot}%{bundle_prefix}/lib/liblld*
# rm wasm-ld
rm -rf %{buildroot}%{bundle_prefix}/bin/wasm-ld

# Remove exec perm
chmod a-x %{buildroot}%{bundle_prefix}/share/opt-viewer/optpmap.py
chmod a-x %{buildroot}%{bundle_prefix}/share/opt-viewer/style.css

# Lingering perl
rm -f %{buildroot}%{pkg_prefix}/bin/hipvars.pm

# Extra docs
rm -rf %{buildroot}%{pkg_prefix}/share/doc/ROCm-Device-Libs/LICENSE.TXT
rm -rf %{buildroot}%{pkg_prefix}/share/doc/amd_comgr/LICENSE.txt
rm -rf %{buildroot}%{pkg_prefix}/share/doc/amd_comgr/NOTICES.txt
rm -rf %{buildroot}%{pkg_prefix}/share/doc/amd_comgr/README.md
rm -rf %{buildroot}%{pkg_prefix}/share/doc/hipcc/LICENSE.txt
rm -rf %{buildroot}%{pkg_prefix}/share/doc/hipcc/README.md

#Clean up dupes:
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{_prefix}
%endif

%files macros
%{_rpmmacrodir}/macros.rocmcompiler

%files -n %{device_libs_name}
%license amd/device-libs/LICENSE.TXT
%doc amd/device-libs/README.md amd/device-libs/doc/*.md
%{pkg_prefix}/%{pkg_libdir}/cmake/AMDDeviceLibs/
%{amd_device_libs_prefix}/amdgcn

%files -n %{comgr_name}
%license amd/comgr/LICENSE.txt amd/comgr/NOTICES.txt
%doc amd/comgr/README.md
%{pkg_prefix}/%{pkg_libdir}/libamd_comgr.so.*

%files -n %{comgr_name}-devel
%{pkg_prefix}/include/amd_comgr/
%{pkg_prefix}/%{pkg_libdir}/cmake/amd_comgr/
%{pkg_prefix}/%{pkg_libdir}/libamd_comgr.so

%files -n %{hipcc_name}
%license amd/hipcc/LICENSE.txt
%doc amd/hipcc/README.md
%{pkg_prefix}/bin/hipcc
%{pkg_prefix}/bin/hipconfig

# ROCM LLVM
%files -n %{rocm_llvm_name}-filesystem
%dir %{_libdir}/rocm
%if %{without compat}
# For rocm-rpm-modules
%dir %{_libdir}/rocm/bin
%dir %{_libdir}/rocm/include
%dir %{_libdir}/rocm/lib
%dir %{_libdir}/rocm/gfx8
%dir %{_libdir}/rocm/gfx8/bin
%dir %{_libdir}/rocm/gfx8/include
%dir %{_libdir}/rocm/gfx8/lib
%dir %{_libdir}/rocm/gfx8/lib/cmake
%dir %{_libdir}/rocm/gfx9
%dir %{_libdir}/rocm/gfx9/bin
%dir %{_libdir}/rocm/gfx9/include
%dir %{_libdir}/rocm/gfx9/lib
%dir %{_libdir}/rocm/gfx9/lib/cmake
%dir %{_libdir}/rocm/gfx10
%dir %{_libdir}/rocm/gfx10/bin
%dir %{_libdir}/rocm/gfx10/include
%dir %{_libdir}/rocm/gfx10/lib
%dir %{_libdir}/rocm/gfx10/lib/cmake
%dir %{_libdir}/rocm/gfx11
%dir %{_libdir}/rocm/gfx11/bin
%dir %{_libdir}/rocm/gfx11/include
%dir %{_libdir}/rocm/gfx11/lib
%dir %{_libdir}/rocm/gfx11/lib/cmake
%dir %{_libdir}/rocm/gfx12
%dir %{_libdir}/rocm/gfx12/bin
%dir %{_libdir}/rocm/gfx12/include
%dir %{_libdir}/rocm/gfx12/lib
%dir %{_libdir}/rocm/gfx12/lib/cmake
%dir %{_libdir}/rocm/gfx906
%dir %{_libdir}/rocm/gfx906/bin
%dir %{_libdir}/rocm/gfx906/include
%dir %{_libdir}/rocm/gfx906/lib
%dir %{_libdir}/rocm/gfx906/lib/cmake
%dir %{_libdir}/rocm/gfx908
%dir %{_libdir}/rocm/gfx908/bin
%dir %{_libdir}/rocm/gfx908/include
%dir %{_libdir}/rocm/gfx908/lib
%dir %{_libdir}/rocm/gfx908/lib/cmake
%dir %{_libdir}/rocm/gfx90a
%dir %{_libdir}/rocm/gfx90a/bin
%dir %{_libdir}/rocm/gfx90a/include
%dir %{_libdir}/rocm/gfx90a/lib
%dir %{_libdir}/rocm/gfx90a/lib/cmake
%dir %{_libdir}/rocm/gfx942
%dir %{_libdir}/rocm/gfx942/bin
%dir %{_libdir}/rocm/gfx942/include
%dir %{_libdir}/rocm/gfx942/lib
%dir %{_libdir}/rocm/gfx942/lib/cmake
%dir %{_libdir}/rocm/gfx950
%dir %{_libdir}/rocm/gfx950/bin
%dir %{_libdir}/rocm/gfx950/include
%dir %{_libdir}/rocm/gfx950/lib
%dir %{_libdir}/rocm/gfx950/lib/cmake
%dir %{_libdir}/rocm/gfx1031
%dir %{_libdir}/rocm/gfx1031/bin
%dir %{_libdir}/rocm/gfx1031/include
%dir %{_libdir}/rocm/gfx1031/lib
%dir %{_libdir}/rocm/gfx1031/lib/cmake
%dir %{_libdir}/rocm/gfx1036
%dir %{_libdir}/rocm/gfx1036/bin
%dir %{_libdir}/rocm/gfx1036/include
%dir %{_libdir}/rocm/gfx1036/lib
%dir %{_libdir}/rocm/gfx1036/lib/cmake
%dir %{_libdir}/rocm/gfx1100
%dir %{_libdir}/rocm/gfx1100/bin
%dir %{_libdir}/rocm/gfx1100/include
%dir %{_libdir}/rocm/gfx1100/lib
%dir %{_libdir}/rocm/gfx1100/lib/cmake
%dir %{_libdir}/rocm/gfx1101
%dir %{_libdir}/rocm/gfx1101/bin
%dir %{_libdir}/rocm/gfx1101/include
%dir %{_libdir}/rocm/gfx1101/lib
%dir %{_libdir}/rocm/gfx1101/lib/cmake
%dir %{_libdir}/rocm/gfx1102
%dir %{_libdir}/rocm/gfx1102/bin
%dir %{_libdir}/rocm/gfx1102/include
%dir %{_libdir}/rocm/gfx1102/lib
%dir %{_libdir}/rocm/gfx1102/lib/cmake
%dir %{_libdir}/rocm/gfx1103
%dir %{_libdir}/rocm/gfx1103/bin
%dir %{_libdir}/rocm/gfx1103/include
%dir %{_libdir}/rocm/gfx1103/lib
%dir %{_libdir}/rocm/gfx1103/lib/cmake
%dir %{_libdir}/rocm/gfx1150
%dir %{_libdir}/rocm/gfx1150/bin
%dir %{_libdir}/rocm/gfx1150/include
%dir %{_libdir}/rocm/gfx1150/lib
%dir %{_libdir}/rocm/gfx1150/lib/cmake
%dir %{_libdir}/rocm/gfx1151
%dir %{_libdir}/rocm/gfx1151/bin
%dir %{_libdir}/rocm/gfx1151/include
%dir %{_libdir}/rocm/gfx1151/lib
%dir %{_libdir}/rocm/gfx1151/lib/cmake
%dir %{_libdir}/rocm/gfx1152
%dir %{_libdir}/rocm/gfx1152/bin
%dir %{_libdir}/rocm/gfx1152/include
%dir %{_libdir}/rocm/gfx1152/lib
%dir %{_libdir}/rocm/gfx1152/lib/cmake
%dir %{_libdir}/rocm/gfx1153
%dir %{_libdir}/rocm/gfx1153/bin
%dir %{_libdir}/rocm/gfx1153/include
%dir %{_libdir}/rocm/gfx1153/lib
%dir %{_libdir}/rocm/gfx1153/lib/cmake
%dir %{_libdir}/rocm/gfx1200
%dir %{_libdir}/rocm/gfx1200/bin
%dir %{_libdir}/rocm/gfx1200/include
%dir %{_libdir}/rocm/gfx1200/lib
%dir %{_libdir}/rocm/gfx1200/lib/cmake
%dir %{_libdir}/rocm/gfx1201
%dir %{_libdir}/rocm/gfx1201/bin
%dir %{_libdir}/rocm/gfx1201/include
%dir %{_libdir}/rocm/gfx1201/lib
%dir %{_libdir}/rocm/gfx1201/lib/cmake
%endif
# For llvm
%dir %{bundle_prefix}
%dir %{bundle_prefix}/bin
%dir %{bundle_prefix}/include
%dir %{bundle_prefix}/include/clang
%dir %{bundle_prefix}/include/clang-c
%dir %{bundle_prefix}/include/llvm
%dir %{bundle_prefix}/include/llvm-c
%dir %{bundle_prefix}/lib
%dir %{bundle_prefix}/lib/clang
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/cuda_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/llvm_libc_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/openmp_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/ppc_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux
%dir %{bundle_prefix}/lib/cmake
%dir %{bundle_prefix}/lib/cmake/clang
%dir %{bundle_prefix}/lib/cmake/llvm
%dir %{bundle_prefix}/share
%dir %{bundle_prefix}/share/clang
%dir %{bundle_prefix}/share/opt-viewer

%files -n %{rocm_llvm_name}-libs
%{bundle_prefix}/lib/libLLVM-*.so
%{bundle_prefix}/lib/libLLVM.so.*
%{bundle_prefix}/lib/libLTO.so.*
%{bundle_prefix}/lib/libRemarks.so.*

%post -n %{rocm_llvm_name}-libs -p /sbin/ldconfig
%postun -n %{rocm_llvm_name}-libs -p /sbin/ldconfig

%files -n %{rocm_llvm_name}
%license llvm/LICENSE.TXT
%{bundle_prefix}/bin/bugpoint
%{bundle_prefix}/bin/llc
%{bundle_prefix}/bin/lli
%{bundle_prefix}/bin/amdgpu-arch
%{bundle_prefix}/bin/dsymutil
%{bundle_prefix}/bin/llvm*
%{bundle_prefix}/bin/opt
%{bundle_prefix}/bin/reduce-chunk-list
%{bundle_prefix}/bin/sancov
%{bundle_prefix}/bin/sanstats
%{bundle_prefix}/bin/verify-uselistorder
%{bundle_prefix}/share/opt-viewer/*

%files -n %{rocm_llvm_name}-devel
%license llvm/LICENSE.TXT
%{bundle_prefix}/include/llvm/*
%{bundle_prefix}/include/llvm-c/*
%{bundle_prefix}/lib/cmake/llvm/*
%{bundle_prefix}/lib/libLLVM.so
%{bundle_prefix}/lib/libLTO.so
%{bundle_prefix}/lib/libRemarks.so
%if %{with gold}
%{bundle_prefix}/lib/LLVMgold.so
%endif

%files -n %{rocm_llvm_name}-static
%license llvm/LICENSE.TXT
%{bundle_prefix}/lib/libLLVM*.a

# ROCM CLANG
%files -n %{rocm_clang_name}-libs
%{bundle_prefix}/lib/libclang*.so.*

%files -n %{rocm_clang_name}-runtime-devel
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/*
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux/clang_rt.*
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux/libclang_rt.*

%files -n %{rocm_clang_name}
%license clang/LICENSE.TXT
%{bundle_prefix}/bin/c-index-test
%{bundle_prefix}/bin/clang*
%{bundle_prefix}/bin/diagtool
%{bundle_prefix}/bin/find-all-symbols
%{bundle_prefix}/bin/flang
%{bundle_prefix}/bin/git-clang-format
%{bundle_prefix}/bin/hmaptool
%{bundle_prefix}/bin/modularize
%{bundle_prefix}/bin/nvptx-arch
%{bundle_prefix}/bin/pp-trace
%{bundle_prefix}/share/clang/*
%{bundle_prefix}/share/clang-doc
%{bundle_prefix}/bin/amdclang*
%{bundle_prefix}/bin/amdflang*
%{bundle_prefix}/bin/amdllvm

%files -n %{rocm_clang_name}-devel
%license clang/LICENSE.TXT
%{bundle_prefix}/include/clang/*
%{bundle_prefix}/include/clang-c/*
%{bundle_prefix}/lib/cmake/clang/*
%{bundle_prefix}/lib/libclang*.so

# ROCM CLANG TOOLS EXTRA
%files -n %{rocm_clang_tools_extra_name}
%license clang-tools-extra/LICENSE.TXT
%{bundle_prefix}/bin/run-clang-tidy

%files -n %{rocm_clang_tools_extra_name}-devel
%dir %{bundle_prefix}/include/clang-tidy
%license clang-tools-extra/LICENSE.TXT
%{bundle_prefix}/include/clang-tidy/*

# ROCM LLD
%files -n %{rocm_lld_name}
%license lld/LICENSE.TXT
%{bundle_prefix}/bin/ld.lld
%{bundle_prefix}/bin/ld64.lld
%{bundle_prefix}/bin/lld
%{bundle_prefix}/bin/lld-link
%{bundle_prefix}/bin/amdlld

# ROCM LIBC++
%files -n %{rocm_libcxx_name}
%license libcxx/LICENSE.TXT
%{bundle_prefix}/lib/libc++.so.*
%{bundle_prefix}/lib/libc++abi.so.*
%{bundle_prefix}/lib/libc++.modules.json

%post -n %{rocm_libcxx_name} -p /sbin/ldconfig
%postun -n %{rocm_libcxx_name} -p /sbin/ldconfig

%files -n %{rocm_libcxx_name}-devel
%dir %{bundle_prefix}/share/libc++
%{bundle_prefix}/include/c++/
%{bundle_prefix}/share/libc++/
%{bundle_prefix}/lib/libc++.so
%{bundle_prefix}/lib/libc++abi.so

%files -n %{rocm_libcxx_name}-static
%{bundle_prefix}/lib/libc++.a
%{bundle_prefix}/lib/libc++abi.a
%{bundle_prefix}/lib/libc++experimental.a

%if %{with sa}
%files -n %{rocm_clang_analyzer_name}
%{bundle_prefix}/bin/analyze-build
%{bundle_prefix}/bin/intercept-build
%{bundle_prefix}/bin/scan-build
%{bundle_prefix}/bin/scan-build-py
%{bundle_prefix}/bin/scan-view
%{bundle_prefix}/lib/libear/*
%{bundle_prefix}/lib/libscanbuild/*
%{bundle_prefix}/libexec/analyze-c++
%{bundle_prefix}/libexec/analyze-cc
%{bundle_prefix}/libexec/c++-analyzer
%{bundle_prefix}/libexec/ccc-analyzer
%{bundle_prefix}/libexec/intercept-c++
%{bundle_prefix}/libexec/intercept-cc
%{bundle_prefix}/share/man/man1/scan-build.1
%{bundle_prefix}/share/scan-build/*
%{bundle_prefix}/share/scan-view/*
%endif

%changelog
%autochangelog
