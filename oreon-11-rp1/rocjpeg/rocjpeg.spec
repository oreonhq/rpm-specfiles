%global source0_hash 26ea59dd772c57ae5476a6ba3799bf86981694fbba9b87af882ed76c1b89c639

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
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

# Requires actual HW, so disabled by default.
# Testing is not well behaved.
%bcond check 1

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# Use ninja if it is available
%if 0%{?fedora} || 0%{?suse_version}
%bcond_without ninja
%else
%bcond_with ninja
%endif

%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif

Name:           %{rocjpeg_name}
Version:        %{rocm_version}
Release:        5%{?dist}
Summary:        A high-performance jpeg decode library for AMD’s GPUs

Url:            https://github.com/ROCm/rocJPEG
License:        MIT
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}

%if %{with check}
%if 0%{?suse_version}
BuildRequires:  ffmpeg
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  Mesa-libva
%else 
BuildRequires:  ffmpeg-free
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  mesa-va-drivers
%endif
BuildRequires:  rocprofiler-register%{pkg_suffix}-devel
%endif

%if %{with ninja}
%if 0%{?fedora}
BuildRequires:  ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:  ninja
%define __builder ninja
%endif
%endif

# Rocjpeg isn't useful without AMD's mesa va drivers:
%if 0%{?suse_version}
Requires:     Mesa-libva
%else
Requires:     mesa-va-drivers
%endif
Provides:     rocjpeg%{pkg_suffix} = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

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

# Need to install first
%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE
%{pkg_prefix}/%{pkg_libdir}/librocjpeg.so.1{,.*}

%files devel
%{pkg_prefix}/%{pkg_libdir}/librocjpeg.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocjpeg/
%{pkg_prefix}/include/rocjpeg/
%{pkg_prefix}/share/rocjpeg/

%changelog
%autochangelog
