%global source0_hash 65d815f4957b27c1f994d4d905a107536fe90ffa4c229c015c241687f11fe2c0
%global upstreamname rpp
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
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%global gpu_list "gfx900;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack+;gfx90a:xnack-;gfx942;gfx950;gfx1010;gfx1012;gfx1030;gfx1100;gfx1101;gfx1102;gfx1103;gfx1150;gfx1151;gfx1152;gfx1153;gfx1200;gfx1201"
%global _gpu_list gfx1100
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%bcond_with test
Name:           rocm-rpp%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Performace Primatives for computer vision
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  half-devel
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-omp-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
# /oreon:deps
%description
AMD ROCm Performance Primitives (RPP) library is a comprehensive,
high-performance computer vision library for AMD processors that
have HIP, OpenCL, or CPU backends.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# hip compiler
sed -i -e 's@set(COMPILER_FOR_HIP ${ROCM_PATH}/llvm/bin/clang++)@set(COMPILER_FOR_HIP hipcc)@' CMakeLists.txt
# remove clang++
sed -i -e '/set(CMAKE_CXX_COMPILER clang++)/d' CMakeLists.txt

# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.cpp' -o -name '*.h' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done

# Remove search for HALF, ours is installed in the usual place
sed -i -e '/HALF/d' CMakeLists.txt

%if %{without test}
# Some things that are not used
sed -i -e '/COMPONENT test/d' CMakeLists.txt
%endif

# Remove third_party libs
# https://github.com/ROCm/rpp/issues/602
rm -rf libs/third_party

# Problems building mivsionx
# CMake Error at /usr/lib64/cmake/rpp/rpp-config.cmake:28 (message):
#  File or directory //include referenced by variable rpp_INCLUDE_DIR does not
#
# Adjust the cmake install locations
sed -i -e 's|@PACKAGE_INCLUDE_INSTALL_DIR@|%{pkg_prefix}/include|' cmake_modules/rpp-config.cmake.in
sed -i -e 's|@PACKAGE_LIB_INSTALL_DIR@|%{pkg_prefix}/%{pkg_libdir}|' cmake_modules/rpp-config.cmake.in

%build

%cmake \
    -G Ninja \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DGPU_TARGETS=%{gpu_list} \
    -DBACKEND=HIP \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DHIP_PLATFORM=amd \
    -DROCM_SYMLINK_LIBS=OFF \
    -DRPP_AUDIO_SUPPORT=OFF \
    -DROCM_PATH=%{pkg_prefix} \
    -DHIP_PATH=%{pkg_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_prefix}/%{pkg_libdir}
%cmake_build
%install
%cmake_install
chrpath -r %{rocmllvm_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/librpp.so.2.*.*
rm -f %{buildroot}%{pkg_prefix}/share/doc/rpp-asan/FFTS_LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rpp-asan/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rpp/FFTS_LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rpp/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rocm-rpp-7.1-devel -f %{oreon_filedir}/rocm-rpp-7.1-devel.list
%files -n rocm-rpp-7.1-test -f %{oreon_filedir}/rocm-rpp-7.1-test.list

%changelog

%autochangelog
