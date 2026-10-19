%global source0_hash d42dfc31cc629360cc84cb05446649fcd1eddd1a2e9e49d532a8f43ee91c327a
%global commit b4c9189bcba7ed9a1189d6a2c27edc3d9a3d5277
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           spirv-llvm-translator
Version:        22.1.7
Release:        1%{?dist}
Summary:        LLVM to SPIRV Translator
License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  libxml2-devel
BuildRequires:  llvm-devel
BuildRequires:  llvm-static
BuildRequires:  ninja-build
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  zlib-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n SPIRV-LLVM-Translator-%{commit} -p1

%build

%cmake -GNinja \
       -DLLVM_BUILD_TOOLS=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_RPATH:BOOL=";" \
       -DLLVM_DIR="/usr/lib64/cmake/llvm/" \
%if 0%{?__isa_bits} == 64
       -DLLVM_LIBDIR_SUFFIX=64 \
%else
       -DLLVM_LIBDIR_SUFFIX= \
%endif
       -DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers" \
       -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="/usr/include/spirv/"
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n spirv-llvm-translator-devel -f %{oreon_filedir}/spirv-llvm-translator-devel.list
%files -n spirv-llvm-translator-tools -f %{oreon_filedir}/spirv-llvm-translator-tools.list

%changelog

%autochangelog
