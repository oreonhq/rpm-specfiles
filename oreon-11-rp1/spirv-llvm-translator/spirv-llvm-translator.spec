# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ecfd7112b14a0a6e6168bf78d1fc2ef1ca35e2ad7eaff6410288b248dc3a3bb8

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global commit 19a29d4376ab470909ba43ca014ae668fb1156c9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           spirv-llvm-translator
Version:        23.1.0
Release:        1%{?dist}
Summary:        LLVM to SPIRV Translator

License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  libxml2-devel
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  llvm-static
BuildRequires:  ninja-build
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  zlib-devel

%description
Khronos LLVM to SPIRV Translator. This is a library
to be used by Mesa for OpenCL support. It translate
LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package devel
Summary: Development files for LLVM to SPIRV Translator
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{name}

%package tools
Summary: Standalone llvm to spirv translator tool
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains the standalone llvm to spirv tool.

%prep
%oreon_sha256

%autosetup -n SPIRV-LLVM-Translator-%{commit} -p1

%build
%cmake -GNinja \
       -DLLVM_BUILD_TOOLS=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_RPATH:BOOL=";" \
       -DLLVM_DIR="%{_libdir}/cmake/llvm/" \
%if 0%{?__isa_bits} == 64
       -DLLVM_LIBDIR_SUFFIX=64 \
%else
       -DLLVM_LIBDIR_SUFFIX= \
%endif
       -DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers" \
       -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="%{_includedir}/spirv/"

%cmake_build

%install
%cmake_install

%check
# upstream lit suite needs clang and llvm test tools, so just a roundtrip
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
cat > check.ll <<'EOT'
target datalayout = "e-i64:64-v16:16-v24:32-v32:32-v48:64-v96:128-v192:256-v256:256-v512:512-v1024:1024-n8:16:32:64"
target triple = "spir64-unknown-unknown"

define spir_kernel void @check() {
  ret void
}
EOT
llvm-as check.ll -o check.bc
%{buildroot}%{_bindir}/llvm-spirv check.bc -o check.spv
spirv-val check.spv
%{buildroot}%{_bindir}/llvm-spirv -r check.spv -o check-rev.bc
llvm-dis check-rev.bc -o - | grep -q '@check'

%files
%doc README.md
%license LICENSE.TXT
%{_libdir}/libLLVMSPIRVLib.so.*

%files tools
%{_bindir}/llvm-spirv

%files devel
%dir %{_includedir}/LLVMSPIRVLib/
%{_includedir}/LLVMSPIRVLib/*
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
%autochangelog
