%global source0_hash 7ddc01a7afcd49d4ec7fa9bf94df20852db44fcda629a9763086a8c541e5da1e
%undefine _include_frame_pointers
%global llvm_ver 21
Name: pocl
Version: 7.2
Release:        1%{?dist}
License: MIT AND BSD-1-Clause AND (GPL-3.0-or-later OR LGPL-3.0-or-later)
Summary:        Portable Computing Language - an OpenCL implementation
URL: https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Provides: bundled(STC)
Requires: libstdc++-devel%{?_isa}
Requires: glibc-devel%{?_isa}
# oreon:deps
BuildRequires:  clang(major)
BuildRequires:  clang-devel(major)
BuildRequires:  cmake
BuildRequires:  compiler-rt(major)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  hwloc-devel
BuildRequires:  libedit-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  llvm-devel(major)
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  uthash-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
PoCL is a portable open source (MIT-licensed) implementation of the OpenCL
standard. In addition to being an easily portable/layered multi-device
open-source OpenCL implementation, a major goal of this project is improving
interoperability of diversity of OpenCL-capable devices by integrating them to
a single centrally orchestrated platform. Also one of the key goals is to
enhance performance portability of OpenCL programs across device types
utilizing runtime and compiler techniques.

PoCL uses Clang as an OpenCL C frontend and LLVM for kernel compiler
implementation, and as a portability layer. Thus, if your desired target has an
LLVM backend, it should be able to get OpenCL support easily by using PoCL.

%package devel
Summary: Portable Computing Language development files
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: clang(major) = %{llvm_ver}
Requires: ocl-icd-devel%{?_isa}
Requires: opencl-filesystem
Requires: uthash-devel
%description devel
Portable Computing Language development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Unbundle uthash
rm include/uthash.h
rm include/utlist.h

# TODO: Unbundle the STC headers
# Copy the STC license
cp thirdparty/STC/LICENSE STC-LICENSE

%build

%global __cc_clang clang-%{llvm_ver}
%global __cxx_clang clang++-%{llvm_ver}
%global __cpp_clang clang-cpp-%{llvm_ver}
%cmake -G Ninja \
    -DENABLE_ICD:BOOL=ON \
    -DPOCL_ICD_ABSOLUTE_PATH:BOOL=OFF \
    -DPOCL_INSTALL_ICD_VENDORDIR=%{_sysconfdir}/OpenCL/vendors \
    -DENABLE_TESTS:BOOL=ON \
    -DENABLE_EXAMPLES:BOOL=OFF \
    -DENABLE_POCLCC:BOOL=ON \
    -DEXTRA_KERNEL_CXX_FLAGS="%{optflags}" \
    -DENABLE_CONFORMANCE:BOOL=ON \
    -DENABLE_HOST_CPU_DEVICES:BOOL=ON \
    -DENABLE_HOST_CPU_DEVICES_OPENMP:BOOL=ON \
%ifarch %{ix86} x86_64 ppc64le
    -DKERNELLIB_HOST_CPU_VARIANTS=distro \
%endif
%ifarch aarch64
    -DLLC_HOST_CPU="cortex-a53" \
%endif
%ifarch riscv64
    -DLLC_HOST_CPU="generic-rv64" \
%endif
    -DWITH_LLVM_CONFIG="llvm-config-%{llvm_ver}"
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch s390x
%ctest -LE 'cpu_fail'
%endif
%files -f %{oreon_filedir}/main.list
%files -n pocl-devel -f %{oreon_filedir}/pocl-devel.list

%changelog

%autochangelog
