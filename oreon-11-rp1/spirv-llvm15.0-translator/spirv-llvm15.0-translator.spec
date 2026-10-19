%global source0_hash d6ffd2cf520b2608e1baa369ab3deddd0dd60e0be27d93c40a16177b55bc4e4e
%global commit 9deca7fd213e123f6a2d1deeac1d3998a1adfcd5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           spirv-llvm15.0-translator
Version:        15.0.19
Release:        1%{?dist}
Summary:        LLVM 15 to SPIRV Translator
License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{commit}/spirv-llvm-translator-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  llvm15-devel
BuildRequires:  llvm15-static
BuildRequires:  ninja-build
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools-devel
# /oreon:deps
%description
Khronos LLVM 15 to SPIRV Translator. This is a library
that is used by Mesa and compute-runtime for OpenCL support.
It translates LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package devel
Summary: Development files for LLVM 15 to SPIRV Translator
Conflicts: spirv-llvm-translator-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files for
developing against %{name}

%package tools
Summary: Standalone llvm 15 to spirv translator tool
Conflicts: spirv-llvm-translator-tools
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
This package contains the standalone llvm to spirv tool.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n SPIRV-LLVM-Translator-%{commit} -p1

%build

%cmake -GNinja \
       -DLLVM_DIR=%{_libdir}/llvm15/lib/cmake/llvm \
       -DLLVM_BUILD_TOOLS=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_RPATH:BOOL=";" \
       -DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers" \
       -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="/usr/include/spirv/" \
%if 0%{?__isa_bits} == 64
       -DLLVM_LIBDIR_SUFFIX=64
%else
       -DLLVM_LIBDIR_SUFFIX=
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n spirv-llvm15.0-translator-devel -f %{oreon_filedir}/spirv-llvm15.0-translator-devel.list
%files -n spirv-llvm15.0-translator-tools -f %{oreon_filedir}/spirv-llvm15.0-translator-tools.list

%changelog

%autochangelog
