%global source1_hash fa4ecfc3e18b8f5a3091434f5b52d62e107a6aa56e7a7567d7d9c4069b0fa9cc
%global source0_hash 47e41a3a1d5138024da7fac5dd6a80fc220971172909de952db85b8afaf1a9c7
%global vc_commit db261bc52c26b716f6ac8a5fe70659a6d7e66858
%global vc_shortcommit %(c=%{vc_commit}; echo ${c:0:7})
%global optflags %{optflags} -w
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%global llvm_compat 15
%endif
%global igc_patch 8
Name: intel-igc
Version: 2.24.%{igc_patch}
Release:        1%{?dist}
Summary:        Intel Graphics Compiler for OpenCL
License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0:        https://github.com/intel/intel-graphics-compiler/archive/v%{version}/v%{version}.tar.gz
Source1: https://github.com/intel/vc-intrinsics/archive/%{vc_commit}/vc-intrinsics-%{vc_shortcommit}.tar.gz
ExclusiveArch:  x86_64
%if %{?llvm_compat} == 15
%else
%endif
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Provides: bundled(intel-vc-intrinsics)
# oreon:deps
BuildRequires:  bison
BuildRequires:  clang15
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  intel-opencl-clang-devel
BuildRequires:  libffi-devel
BuildRequires:  libunwind-devel
BuildRequires:  lld15-devel
BuildRequires:  llvm15-devel
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  python3
BuildRequires:  python3-mako
BuildRequires:  python3-pyyaml
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-llvm15.0-translator-devel
BuildRequires:  spirv-llvm15.0-translator-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Intel Graphics Compiler for OpenCL is an LLVM based compiler for OpenCL targeting Intel Gen graphics hardware architecture.

%package       devel
Summary:       Intel Graphics Compiler Frontend - Devel Files
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
%description   devel
Devel files for Intel Graphics Compiler for OpenCL.

%package       libs
Summary:       Intel Graphics Compiler Frontend - Library Files
Requires:      %{name} = %{version}-%{release}
%description   libs
Library files for Intel Graphics Compiler for OpenCL.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

tar -xf %{SOURCE1}

%autosetup -n intel-graphics-compiler-%{version} -p1

%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DIGC_OPTION__LLVM_PREFERRED_VERSION='%(rpm -q --qf '%%{version}' llvm%{?llvm_compat}-devel | cut -d. -f1 | sed "s/$/.0.0/")' \
    -DVC_INTRINSICS_SRC="%{_builddir}/vc-intrinsics-%{vc_commit}" \
    -DIGC_API_PATCH_VERSION=%{igc_patch} \
%ifarch x86_64
    -DIGC_OPTION__ARCHITECTURE_TARGET='Linux64' \
%endif
%ifarch i686
    -DIGC_OPTION__ARCHITECTURE_TARGET='Linux32' \
%endif
    -DIGC_OPTION__LINK_KHRONOS_SPIRV_TRANSLATOR=ON \
    -DIGC_BUILD__VC_ENABLED=ON \
    -DIGC_OPTION__SPIRV_TRANSLATOR_MODE=Prebuilds \
    -DIGC_OPTION__CLANG_MODE=Prebuilds \
    -DIGC_OPTION__LLD_MODE=Prebuilds \
    -DIGC_OPTION__LLVM_MODE=Prebuilds \
    -DLLVM_ROOT=%{_libdir}/llvm%{?llvm_compat}/ \
    -DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds \
    -DIGC_OPTION__USE_PREINSTALLED_SPIRV_HEADERS=ON \
    -DIGC_OPTION__VC_INTRINSICS_MODE=Source \
    -DINSTALL_GENX_IR=ON \
    -Wno-dev \
    -G Ninja
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n intel-igc-devel -f %{oreon_filedir}/intel-igc-devel.list
%files -n intel-igc-libs -f %{oreon_filedir}/intel-igc-libs.list

%changelog

%autochangelog
