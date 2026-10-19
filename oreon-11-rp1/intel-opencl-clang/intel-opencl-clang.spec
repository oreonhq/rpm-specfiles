%global source0_hash 8d50e6c8672fe683700af82227cbd07c764ba09c36439565be0ef3d491776a77
%global commit 202a1e6367848ca3a51fdeab3cb28fc0ad783ffa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%global llvm_compat 15
%endif
Name: intel-opencl-clang
Version: 15.0.5
Release:        1%{?dist}
Summary:        Library to compile OpenCL C kernels to SPIR-V modules
License: NCSA
URL:     https://github.com/intel/opencl-clang
Source0:        https://github.com/intel/opencl-clang/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%if %{?llvm_compat} == 15
%else
%endif
# oreon:deps
BuildRequires:  clang15
BuildRequires:  clang15-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  llvm15-devel
BuildRequires:  make
BuildRequires:  spirv-llvm15.0-translator-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
opencl-clang is a thin wrapper library around clang. The library has OpenCL-oriented API and
is capable to compile OpenCL C kernels to SPIR-V modules.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files for
developing against %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n opencl-clang-%{commit} -p1
sed -i 's/$<TARGET_FILE:clang>/$<TARGET_FILE:clang%{?llvm_compat}>/' cl_headers/CMakeLists.txt

%build

%cmake \
    -DPREFERRED_LLVM_VERSION='%(rpm -q --qf '%%{version}' llvm%{?llvm_compat}-devel | cut -d. -f1 | sed "s/$/.0.0/")' \
    -DLLVM_DIR=%{_libdir}/llvm%{?llvm_compat}/lib/cmake/llvm/
%cmake_build
%install
%cmake_install
%ifnarch i686
mkdir -p %{buildroot}%{_libdir}/
cp %{buildroot}/usr/lib/libopencl-clang.so.* %{buildroot}%{_libdir}/
cp %{buildroot}/usr/lib/libopencl-clang.so %{buildroot}%{_libdir}/
rm %{buildroot}/usr/lib/libopencl-clang.so.*
rm %{buildroot}/usr/lib/libopencl-clang.so
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n intel-opencl-clang-devel -f %{oreon_filedir}/intel-opencl-clang-devel.list

%changelog

%autochangelog
