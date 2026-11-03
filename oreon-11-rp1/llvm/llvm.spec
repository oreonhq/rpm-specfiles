%global source0_hash 819ecf7351f1a66f76b2d701d8942faaf5faeb324cb90c9d5b090de142434bb2
%if "%{_lib}" == "lib64"
%global oreon_libsuffix 64
%else
%global oreon_libsuffix %{nil}
%endif
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

%global maj %(echo %{version} | cut -d. -f1)

Name: llvm
Version: 23.1.4
Release: 3%{?dist}
Summary: LLVM compiler infrastructure
License: Apache-2.0 WITH LLVM-exception
URL: https://llvm.org/
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/llvm-project-%{version}.src.tar.xz
Source1: llvm-project-%{version}.src.tar.xz.sig
Source2: llvm-release-keys.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: python3
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
BuildRequires: libffi-devel
BuildRequires: ncurses-devel
BuildRequires: pkgconf
Requires: llvm-libs%{?_isa} = %{version}-%{release}

%description
LLVM is a collection of modular compiler and toolchain components. This
source package also builds the Clang compiler and the LLD linker.

%package libs
Summary: LLVM shared libraries

%description libs
Shared libraries for the LLVM compiler infrastructure.

%package devel
Summary: Development files for LLVM
Requires: llvm%{?_isa} = %{version}-%{release}
Requires: llvm-libs%{?_isa} = %{version}-%{release}
Requires: llvm-static%{?_isa} = %{version}-%{release}

%description devel
Headers, CMake modules and the llvm-config tool for LLVM.

%package static
Summary: LLVM static libraries
Requires: llvm-devel%{?_isa} = %{version}-%{release}

%description static
Static libraries for the LLVM compiler infrastructure.

%package -n clang
Summary: C language family frontend for LLVM
Requires: clang-libs%{?_isa} = %{version}-%{release}
Requires: llvm-libs%{?_isa} = %{version}-%{release}
Requires: gcc
Requires: python3

%description -n clang
Clang is a C, C++ and Objective-C compiler built on LLVM.

%package -n clang-libs
Summary: Runtime libraries and headers for Clang
Requires: llvm-libs%{?_isa} = %{version}-%{release}

%description -n clang-libs
Shared libraries and compiler resource headers for Clang.

%package -n clang-devel
Summary: Development files for Clang
Requires: clang%{?_isa} = %{version}-%{release}
Requires: clang-libs%{?_isa} = %{version}-%{release}
Requires: llvm-devel%{?_isa} = %{version}-%{release}

%description -n clang-devel
Headers, static libraries and CMake modules for Clang.

%package -n lld
Summary: The LLVM linker
Requires: llvm-libs%{?_isa} = %{version}-%{release}

%description -n lld
LLD is the LLVM linker, supporting ELF, COFF, Mach-O and WebAssembly.

%package -n lld-devel
Summary: Development files for LLD
Requires: lld%{?_isa} = %{version}-%{release}
Requires: llvm-devel%{?_isa} = %{version}-%{release}

%description -n lld-devel
Headers, static libraries and CMake modules for LLD.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n llvm-project-%{version}.src -p1

%build
cd llvm
%oreon_cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DLLVM_ENABLE_PROJECTS="clang;lld" \
  -DLLVM_TARGETS_TO_BUILD="X86;AArch64;AMDGPU;NVPTX;BPF;WebAssembly" \
  -DLLVM_LIBDIR_SUFFIX=%{oreon_libsuffix} \
  -DLLVM_BUILD_LLVM_DYLIB=ON -DLLVM_LINK_LLVM_DYLIB=ON -DCLANG_LINK_CLANG_DYLIB=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DLLVM_ENABLE_RTTI=ON -DLLVM_ENABLE_EH=ON -DLLVM_ENABLE_FFI=ON \
  -DLLVM_ENABLE_ZLIB=FORCE_ON -DLLVM_ENABLE_ZSTD=FORCE_ON -DLLVM_ENABLE_LIBXML2=OFF \
  -DLLVM_INCLUDE_TESTS=OFF -DLLVM_BUILD_TESTS=OFF -DCLANG_INCLUDE_TESTS=OFF -DLLVM_INCLUDE_BENCHMARKS=OFF \
  -DLLVM_INCLUDE_EXAMPLES=OFF -DLLVM_INCLUDE_DOCS=OFF -DCLANG_INCLUDE_DOCS=OFF -DLLD_INCLUDE_DOCS=OFF \
  -DLLVM_ENABLE_SPHINX=OFF -DLLVM_ENABLE_DOXYGEN=OFF -DLLVM_INSTALL_UTILS=ON \
  -DLLVM_DEFAULT_TARGET_TRIPLE=%{_arch}-oreon-linux-gnu \
  -DCLANG_VENDOR="Oreon" -DLLVM_PARALLEL_LINK_JOBS=2 \
  -DLLVM_USE_PERF=OFF -DLLVM_ENABLE_ASSERTIONS=OFF
%oreon_cmake_build

%install
cd llvm
%oreon_cmake_install
cd ..
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%files
%license llvm/LICENSE.TXT
%{_bindir}/*
%exclude %{_bindir}/llvm-config
%exclude %{_bindir}/clang*
%exclude %{_bindir}/c-index-test
%exclude %{_bindir}/diagtool
%exclude %{_bindir}/hmaptool
%exclude %{_bindir}/scan-build
%exclude %{_bindir}/scan-build-py
%exclude %{_bindir}/scan-view
%exclude %{_bindir}/git-clang-format
%exclude %{_bindir}/analyze-build
%exclude %{_bindir}/intercept-build
%exclude %{_bindir}/amdgpu-arch
%exclude %{_bindir}/nvptx-arch
%exclude %{_bindir}/offload-arch
%exclude %{_bindir}/ld.lld
%exclude %{_bindir}/ld64.lld
%exclude %{_bindir}/lld
%exclude %{_bindir}/lld-link
%exclude %{_bindir}/wasm-ld
%{_datadir}/opt-viewer/

%files libs
%license llvm/LICENSE.TXT
%{_libdir}/libLLVM.so.%{maj}*
%{_libdir}/libLLVM-%{maj}.so
%{_libdir}/libLTO.so.%{maj}*
%{_libdir}/libRemarks.so.%{maj}*

%files devel
%{_bindir}/llvm-config
%{_includedir}/llvm/
%{_includedir}/llvm-c/
%{_libdir}/libLLVM.so
%{_libdir}/libLTO.so
%{_libdir}/libRemarks.so
%{_libdir}/cmake/llvm/

%files static
%{_libdir}/libLLVM*.a

%files -n clang
%license clang/LICENSE.TXT
%{_bindir}/clang*
%{_bindir}/c-index-test
%{_bindir}/diagtool
%{_bindir}/hmaptool
%{_bindir}/scan-build
%{_bindir}/scan-build-py
%{_bindir}/scan-view
%{_bindir}/git-clang-format
%{_bindir}/analyze-build
%{_bindir}/intercept-build
%{_bindir}/amdgpu-arch
%{_bindir}/nvptx-arch
%{_bindir}/offload-arch
%{_libexecdir}/ccc-analyzer
%{_libexecdir}/c++-analyzer
%{_libexecdir}/analyze-c++
%{_libexecdir}/analyze-cc
%{_libexecdir}/intercept-c++
%{_libexecdir}/intercept-cc
%{_prefix}/lib/libscanbuild/
%{_prefix}/lib/libear/
%{_datadir}/clang/
%{_datadir}/scan-build/
%{_datadir}/scan-view/
%{_mandir}/man1/scan-build.1*

%files -n clang-libs
%license clang/LICENSE.TXT
%{_libdir}/libclang.so.%{maj}*
%{_libdir}/libclang-cpp.so.%{maj}*
%{_libdir}/clang/

%files -n clang-devel
%{_includedir}/clang/
%{_includedir}/clang-c/
%{_libdir}/libclang.so
%{_libdir}/libclang-cpp.so
%{_libdir}/libclang*.a
%{_libdir}/cmake/clang/

%files -n lld
%license lld/LICENSE.TXT
%{_bindir}/ld.lld
%{_bindir}/ld64.lld
%{_bindir}/lld
%{_bindir}/lld-link
%{_bindir}/wasm-ld

%files -n lld-devel
%{_includedir}/lld/
%{_libdir}/liblld*.a
%{_libdir}/cmake/lld/
