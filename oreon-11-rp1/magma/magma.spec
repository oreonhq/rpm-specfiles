%global source0_hash 26347adbccbe7a6693d6b3f3c0ab5620037eb3a62b5ef69d05e40289472a82a4
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' -e 's/-flto=thin//' )
%global _lto_cflags %nil
%bcond_with test
%if %{with test}
%global gpu_list gfx1201
%else
%global gpu_list %{rocm_gpu_list_default}
%endif
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
Name:           magma
Version:        2.10.0
Release:        1%{?dist}
Summary:        Matrix Algebra on GPU and Multi-core Architectures
Url:            https://icl.utk.edu/magma/
License:        BSD-3-Clause AND MIT
Source0:        https://github.com/icl-utk-edu/%{name}/archive/v%{version}.tar.gz
Patch0:         0001-Prepare-magma-cmake-for-fedora.patch
Patch1:         0001-magma-ROCm-7-changes.patch
Provides:       bundled(hipify) = 3.4.0
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  hipblas-devel
BuildRequires:  hipsparse-devel
BuildRequires:  ninja-build
BuildRequires:  python3
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
# /oreon:deps
%description
Matrix Algebra on GPU and Multi-core Architectures (MAGMA) is a collection
of next-generation linear algebra libraries for heterogeneous computing.
The MAGMA package supports interfaces for current linear algebra packages
and standards (e.g., LAPACK and BLAS) to enable computational scientists
to easily port any linear algebra–reliant software component to
heterogeneous computing systems. MAGMA enables applications to fully
exploit the power of current hybrid systems of many-core CPUs and
multi-GPUs/coprocessors to deliver the fastest possible time to accurate
solutions within given energy constraints.

MAGMA features LAPACK-compliant routines for multi-core CPUs enhanced with
NVIDIA or AMD GPUs. MAGMA 2.7.2 now includes more than 400 routines that
cover one-sided dense matrix factorizations and solvers, two-sided
factorizations, and eigen/singular-value problem solvers, as well as a
subset of highly optimized BLAS for GPUs. A MagmaDNN package has been
added and further enhanced to provide high-performance data analytics,
including functionalities for machine learning applications that use MAGMA
as their computational back end. The MAGMA Sparse and MAGMA Batched
packages have been included since MAGMA 1.6.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%if %{with test}
# Just the test gpu gfx1201
sed -i -e 's@1032 1033@1201@' Makefile
# Remove some tests,
sed -i -e '/testing_zgenerate.cpp/d' testing/Makefile.src
%else
# Add some more gfx's
# https://bitbucket.org/icl/magma/issues/76/a-few-new-rocm-gpus
sed -i -e 's@1032 1033@950 1032 1033 1100 1101 1102 1103 1150 1151 1152 1153 1200 1201@' Makefile
# Disable building tests
sed -i -e 's@include_directories( testing )@#include_directories( testing )@' CMakeLists.txt
sed -i -e 's@foreach( filename ${testing_all} )@foreach( filename ${no_testing_all} )@' CMakeLists.txt
sed -i -e 's@add_custom_target( testing DEPENDS ${testing} )@#add_custom_target( testing DEPENDS ${testing} )@' CMakeLists.txt
sed -i -e 's@foreach( TEST ${sparse_testing_all} )@foreach( TEST ${no_sparse_testing_all} )@' CMakeLists.txt
sed -i -e 's@add_custom_target( sparse-testing DEPENDS ${sparse-testing} )@#add_custom_target( sparse-testing DEPENDS ${sparse-testing} )@' CMakeLists.txt
%endif

# Change the bin,lib install locations
sed -i -e 's@DESTINATION lib@DESTINATION ${CMAKE_INSTALL_LIBDIR}@' CMakeLists.txt
sed -i -e 's@DESTINATION bin@DESTINATION ${CMAKE_INSTALL_BINDIR}@' CMakeLists.txt

# Version *.so
sed -i -e 's@magma_VERSION@"%{version}"@g' CMakeLists.txt

# python to python3, need env to find local bits like magmasubs.py
sed -i -e 's@env python@env python3@' tools/checklist_run_tests.py
sed -i -e 's@env python@env python3@' tools/check-style.py
sed -i -e 's@env python@env python3@' tools/parse-magma.py

# Remove some files we do not need to similify licenses
# GPL, results for cuda
rm -rf results/*
# ICS, Copy of strlcpy - just use strlcpy
sed -i -e '/strlcpy/d' control/Makefile.src
sed -i -e '/strlcpy/d' include/magma_auxiliary.h
sed -i -e 's@magma_strlcpy@strlcpy@' control/trace.cpp
rm control/strlcpy.cpp

# Policy CMP0037 may not be set to OLD behavior because this version of CMake
sed -i -e 's@cmake_policy( SET CMP0037 OLD)@#cmake_policy( SET CMP0037 OLD)@' CMakeLists.txt

# Add offload-compress compile flags
sed -i -e 's@-DROCM_VERSION@--offload-compress -DROCM_VERSION@' CMakeLists.txt

%build

export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
echo "BACKEND = hip"                          > make.inc
echo "FORT = false"                          >> make.inc
%if %{with test}
echo "GPU_TARGET = gfx1201" >> make.inc
%else
echo "GPU_TARGET = gfx900;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack+;gfx90a:xnack-;gfx942;gfx950;gfx1010;gfx1012;gfx1030;gfx1031;gfx1035;gfx1100;gfx1101;gfx1102;gfx1103;gfx1150;gfx1151;gfx1152;gfx1153;gfx1200;gfx1201" >> make.inc
%endif
make generate
%cmake -G Ninja \
       -DBLA_VENDOR=FlexiBLAS \
       -DCMAKE_BUILD_TYPE=%{build_type} \
       -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
       -DAMDGPU_TARGETS=%{gpu_list} \
       -DCMAKE_INSTALL_LIBDIR=%_libdir \
       -DMAGMA_ENABLE_HIP=ON \
       -DUSE_FORTRAN=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with test}
%check

%{_vpath_builddir}/testing/testing_sgemm
%endif
%files -f %{oreon_filedir}/main.list
%files -n magma-devel -f %{oreon_filedir}/magma-devel.list

%changelog

%autochangelog
