%global source1_hash 2d2601a82d2d3b7e143a3c8d43ef616671391034bc46891a9816b79cf2d3e7a8
%global source0_hash 670ef46f6b39311cdba7752069fd831c9146c88636a9c185dfa10cdc304b9682
%global upstreamname rocAL
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
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong//' -e 's/-fcf-protection//' -e 's/-mtls-dialect=gnu2//')
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%bcond check 1
%bcond_with test
%global _source_payload         w7T0.xzdio
%global _binary_payload         w7T0.xzdio
%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100
Name:           rocal%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Augmentation Library
Url:            https://github.com/ROCm/rocAL
License:        MIT AND BSD-3-Clause
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch1:         0001-rocal-find-mivisionx.patch
%global rapidjson_date 20241218
%global rapidjson_commit 24b5e7a8b27f42fa16b96fc70aade9106cf7102f
%global short_rapidjson_commit %(c=%{rapidjson_commit}; echo ${c:0:7})
Source1:        https://github.com/Tencent/rapidjson/archive/%{rapidjson_commit}.tar.gz
Provides:       bundled(rapidjson) = %{rapidjson_date}.g%{short_rapidjson_commit}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  half-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lmdb-devel
BuildRequires:  mivisionx-7.1-devel
BuildRequires:  protobuf-devel
BuildRequires:  pybind11-devel
BuildRequires:  rocdecode-7.1-devel
BuildRequires:  rocjpeg-7.1-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-omp-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-rpp-7.1-devel
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  turbojpeg-devel
# /oreon:deps
%description
The AMD ROCm Augmentation Library (rocAL) is designed to efficiently
decode and process images and videos from a variety of storage formats
and modify them through a processing graph programmable by the user.
rocAL currently provides C API.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rocal%{pkg_suffix}-devel = %{version}-%{release}
%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# rapidjson ToT
tar xf %{SOURCE1}

# cmake 3.5 minimum
sed -i -e 's@cmake_minimum_required(VERSION 2.8)@cmake_minimum_required(VERSION 3.5)@' rapidjson-%{rapidjson_commit}/example/CMakeLists.txt

# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.h' -o -name '*.cpp' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done
sed -i -e 's@half/half.hpp@half.hpp@' cmake/FindHALF.cmake

# We set this below
sed -i -e 's@set(COMPILER_FOR_HIP@#set(COMPILER_FOR_HIP@' rocAL/rocAL_hip/CMakeLists.txt

# https://github.com/ROCm/rocAL/issues/287
# Several rpmlint warning about missing libjpeg syms
# rocal.x86_64: E: undefined-non-weak-symbol /usr/lib64/librocal.so.2.1.0 jpeg_mem_src (/usr/lib64/librocal.so.2.1.0)
sed -i -e 's@set(LINK_LIBRARY_LIST ${LINK_LIBRARY_LIST} ${TurboJpeg_LIBRARIES})@set(LINK_LIBRARY_LIST ${LINK_LIBRARY_LIST} ${LIBJPEG_LIBRARIES} ${TurboJpeg_LIBRARIES})@' rocAL/CMakeLists.txt

# Tests use the wrong ROCM_PATH
sed -i -e 's@set(ROCM_PATH /opt/rocm@set(ROCM_PATH %{pkg_prefix}@' tests/cpp_api/CMakeLists.txt
sed -i -e 's@set(ROCM_PATH /opt/rocm@set(ROCM_PATH %{pkg_prefix}@' tests/cpp_api/*/CMakeLists.txt

# tests have wrong include
for f in `find tests -type f -name '*.cpp' `; do
    sed -i -e 's@rocal_api.h@rocal/rocal_api.h@' $f
    sed -i -e 's@rocal_api_types.h@rocal/rocal_api_types.h@' $f
done

# Remove to make license simpler
# Apache License 2.0
# ------------------
# rocal-6.3.3-build/rocAL-rocm-6.3.3/docs/examples/tf/pets_training/create_pet_tf_record.py
rm -rf docs/examples/tf/pets_training

%build

cd rapidjson-%{rapidjson_commit}
p=$PWD
mkdir build
cd build
%__cmake \
       -DBUILD_SHARED_LIBS=OFF \
       -DCMAKE_BUILD_TYPE=RELEASE \
       -DRAPIDJSON_BUILD_CXX11:BOOL=OFF \
       -DCMAKE_INSTALL_PREFIX=$p/install \
       ..
%make_build
%make_build install
cd ../..
%cmake \
    --debug-find-pkg=MIVisionX \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/amdclang \
    -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_PREFIX_PATH=$p/install/lib/cmake \
    -DCOMPILER_FOR_HIP=%rocmllvm_bindir/clang++ \
    -DGPU_TARGETS=%{gpu_list} \
    -DHIP_PLATFORM=amd \
    -DROCM_PATH=%{pkg_prefix}
%cmake_build
%if %{with check}
%check

%ctest
%endif
%install
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocal/LICENSE.txt
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocal-asan/LICENSE.txt
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocal/README.md
%if %{without test}
rm -rf %{buildroot}%{pkg_prefix}/share/rocal/test
%endif
chrpath -r %{rocmllvm_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/librocal.so.2.*.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rocal-7.1-devel -f %{oreon_filedir}/rocal-7.1-devel.list
%files -n rocal-7.1-test -f %{oreon_filedir}/rocal-7.1-test.list

%changelog

%autochangelog
