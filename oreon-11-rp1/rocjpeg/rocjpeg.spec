%global source0_hash 26ea59dd772c57ae5476a6ba3799bf86981694fbba9b87af882ed76c1b89c639
%global upstreamname rocJPEG
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
%global rocjpeg_name librocjpeg1%{pkg_suffix}
%else
%global rocjpeg_name rocjpeg%{pkg_suffix}
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
Name:           %{rocjpeg_name}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        A high-performance jpeg decode library for AMD’s GPUs
Url:            https://github.com/ROCm/rocJPEG
License:        MIT
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%if %{with check}
%if 0%{?suse_version}
%else 
%endif
%endif
%if %{with ninja}
%if 0%{?suse_version}
%define __builder ninja
%endif
%endif
%if 0%{?suse_version}
Requires:     Mesa-libva
%else
Requires:     mesa-va-drivers
%endif
Provides:     rocjpeg%{pkg_suffix} = %{version}-%{release}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  ffmpeg-free
BuildRequires:  gcc-c++
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  mesa-va-drivers
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocprofiler-register-7.1-devel
# /oreon:deps
%description
rocJPEG is a high performance JPEG decode SDK for AMD GPUs. Using
the rocJPEG API, you can access the JPEG decoding features available
on your GPU.

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%package devel
Summary: The development package for %{name}
Requires:     %{name}%{?_isa} = %{version}-%{release}
Provides:     rocjpeg%{pkg_suffix}-devel = %{version}-%{release}
%description devel
The rocJPEG development package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Fix this error:
# gmake[2]: /opt/rocm/lib/llvm/bin/clang++: No such file or directory
sed -i -e 's@set(CMAKE_C_COMPILER ${ROCM_PATH}/lib/llvm/bin/amdclang)@set(CMAKE_C_COMPILER "%rocmllvm_bindir/amdclang")@' {,test/,test/*/,samples/*/}CMakeLists.txt
sed -i -e 's@set(CMAKE_CXX_COMPILER ${ROCM_PATH}/lib/llvm/bin/amdclang++)@set(CMAKE_CXX_COMPILER "%rocmllvm_bindir/amdclang++")@' {,test/,test/*/,samples/*/}CMakeLists.txt

# There is no /opt/amgpu/include, just use the normal path.
sed -i "s|/opt/amdgpu/include NO_DEFAULT_PATH|%{pkg_prefix}/include|" cmake/FindLibva.cmake

# Fix up sample
sed -i -e 's@${ROCM_PATH}/lib/llvm/bin/clang++@%{pkg_prefix}/bin/hipcc@' samples/*/CMakeLists.txt
sed -i -e 's@${ROCM_PATH}/lib@%{pkg_prefix}/lib64@' samples/*/CMakeLists.txt test/CMakeLists.txt
sed -i -e 's@${ROCM_PATH}/include/rocjpeg@%{pkg_prefix}/include/rocjpeg@' samples/*/CMakeLists.txt test/CMakeLists.txt
sed -i -e 's@set(ROCM_PATH /opt/rocm@set(__ROCM_PATH /opt/rocm@' samples/*/CMakeLists.txt test/CMakeLists.txt
# Fix up test
sed -i -e 's@${ROCM_PATH}/share@%{pkg_prefix}/share@' test/CMakeLists.txt

# cpack cruft in the middle of the configure, this breaks TW 
sed -i -e 's@file(READ "/etc/os-release" OS_RELEASE)@#file(READ "/etc/os-release" OS_RELEASE)@'  CMakeLists.txt
sed -i -e 's@string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@#string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@'  CMakeLists.txt
sed -i -e 's@string(REGEX MATCH "SLES" SLES_FOUND ${OS_RELEASE})@#string(REGEX MATCH "SLES" SLES_FOUND ${OS_RELEASE})@' CMakeLists.txt
sed -i -e 's@string(REGEX MATCH "Mariner" MARINER_FOUND ${OS_RELEASE})@#string(REGEX MATCH "Mariner" MARINER_FOUND ${OS_RELEASE})@' CMakeLists.txt

# Need to add libdrm_amdgpu to link
# https://github.com/ROCm/rocJPEG/issues/146
sed -i -e 's@${LINK_LIBRARY_LIST} ${LIBVA_DRM_LIBRARY}@${LINK_LIBRARY_LIST} ${LIBVA_DRM_LIBRARY} -ldrm_amdgpu@' CMakeLists.txt

%build

%cmake \
    %{cmake_generator} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocjpeg/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocjpeg-asan/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocjpeg-dev/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocjpeg-test/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/rocjpeg/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/rocjpeg-dev/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/rocjpeg-test/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/rocjpeg-asan/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n rocjpeg-7.1-devel -f %{oreon_filedir}/rocjpeg-7.1-devel.list

%changelog

%autochangelog
