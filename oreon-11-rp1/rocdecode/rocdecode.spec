%global source0_hash ccd8d7fe8010214a00d75ac0299747ad9ebf25849f2575cb096b814ec071d952
%global upstreamname rocDecode
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
%global rocdecode_name librocdecode1%{pkg_suffix}
%else
%global rocdecode_name rocdecode%{pkg_suffix}
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%bcond check 1
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%bcond_with ninja
%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif
Name:           %{rocdecode_name}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        High-performance video decode SDK for AMD GPUs
Url:            https://github.com/ROCm/rocDecode
License:        MIT
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%if 0%{?suse_version}
%else 
%endif
%if %{with ninja}
%if 0%{?suse_version}
%define __builder ninja
%endif
%endif
Requires:     mesa-va-drivers
Provides:     rocdecode%{pkg_suffix} = %{version}-%{release}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  ffmpeg-free
BuildRequires:  gcc-c++
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  mesa-va-drivers
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocprofiler-register-devel
# /oreon:deps
%description
rocDecode is a high-performance video decode SDK for AMD GPUs. Using the
rocDecode API, you can access the video decoding features available on your GPU.

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%package devel
Summary: The rocDecode development package
Requires:     %{name}%{?_isa} = %{version}-%{release}
Provides:     rocdecode%{pkg_suffix}-devel = %{version}-%{release}
%description devel
The rocDecode development package.

%prep

%autosetup -p1 -n %{upstreamname}-rocm-%{version}
# Allow overriding CMAKE_CXX_COMPILER: 
# https://github.com/ROCm/rocDecode/pull/436
sed -i -e 's@set(CMAKE_C_COMPILER ${ROCM_PATH}/lib/llvm/bin/amdclang)@set(CMAKE_C_COMPILER "%rocmllvm_bindir/amdclang")@' {,test/,samples/*/}CMakeLists.txt
sed -i -e 's@set(CMAKE_CXX_COMPILER ${ROCM_PATH}/lib/llvm/bin/amdclang++)@set(CMAKE_CXX_COMPILER "%rocmllvm_bindir/amdclang++")@' {,test/,samples/*/}CMakeLists.txt

# Problems finding va.h
# https://github.com/ROCm/rocDecode/issues/477
sed -i "s|/opt/amdgpu/include NO_DEFAULT_PATH|/usr/include|" cmake/FindLibva.cmake

# cpack cruft in the middle of the configure, this breaks TW and is only used for ubuntu
sed -i -e 's@file(READ "/etc/os-release" OS_RELEASE)@#file(READ "/etc/os-release" OS_RELEASE)@'  CMakeLists.txt
sed -i -e 's@string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@#string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@'  CMakeLists.txt

# Need to add libdrm_amdgpu to link
# https://github.com/ROCm/rocDecode/issues/571
sed -i -e 's@${LINK_LIBRARY_LIST} ${LIBVA_DRM_LIBRARY}@${LINK_LIBRARY_LIST} ${LIBVA_DRM_LIBRARY} -ldrm_amdgpu@' CMakeLists.txt

%build

%cmake \
    %{cmake_generator} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DROCM_PATH=%{pkg_prefix}
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocdecode/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocdecode-asan/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/%{name}/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/%{name}-asan/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n rocdecode-7.1-devel -f %{oreon_filedir}/rocdecode-7.1-devel.list

%changelog

%autochangelog
