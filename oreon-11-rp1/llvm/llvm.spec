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

Name: llvm
Version: 23.1.4
Release: 1%{?dist}
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
BuildRequires: zstd-devel
BuildRequires: libffi-devel
BuildRequires: ncurses-devel
BuildRequires: pkgconf

%description
LLVM is a collection of modular compiler and toolchain components. This
source package also builds the Clang compiler and the LLD linker.

%package devel
Summary: Development files for LLVM
Requires: llvm%{?_isa} = %{version}-%{release}
Provides: llvm-libs = %{version}-%{release}
Provides: llvm-static = %{version}-%{release}
Provides: cmake(LLVM)

%description devel
Headers, CMake modules and the llvm-config tool for LLVM.

%package -n clang
Summary: C language family frontend for LLVM
Requires: llvm%{?_isa} = %{version}-%{release}
Requires: gcc
Provides: clang-libs = %{version}-%{release}
Provides: clang-tools-extra = %{version}-%{release}

%description -n clang
Clang is a C, C++ and Objective-C compiler built on LLVM.

%package -n clang-devel
Summary: Development files for Clang and LLD
Requires: clang%{?_isa} = %{version}-%{release}
Requires: lld%{?_isa} = %{version}-%{release}
Requires: llvm-devel%{?_isa} = %{version}-%{release}
Provides: lld-devel = %{version}-%{release}
Obsoletes: lld-devel < %{version}-%{release}
Provides: cmake(Clang)
Provides: cmake(LLD)

%description -n clang-devel
Headers and CMake modules for Clang and LLD.

%package -n lld
Summary: The LLVM linker
Requires: llvm%{?_isa} = %{version}-%{release}
Provides: lld-libs = %{version}-%{release}
Obsoletes: lld-libs < %{version}-%{release}

%description -n lld
LLD is the LLVM linker, supporting ELF, COFF, Mach-O and WebAssembly.

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
%oreon_filelist_devel
cd %{_builddir}
grep -E '/(clang|libclang|scan-build|scan-view|scan-build-py|c-index-test|git-clang|hmaptool|diagtool|amdgpu-arch|nvptx-arch|offload-arch|analyze-build|intercept-build)' %{name}.files > clang.files || :
grep -E '/(lld|ld\.lld|ld64\.lld|wasm-ld|lld-link)' %{name}.files > lld.files || :
grep -E '/(clang|libclang)' %{name}-devel.files > clang-devel.files || :
grep -E '/(lld)' %{name}-devel.files > lld-devel.files || :
cat clang.files lld.files > other.files
grep -vxF -f other.files %{name}.files > main.files || :
mv main.files %{name}.files
cat clang-devel.files lld-devel.files > other.files
grep -vxF -f other.files %{name}-devel.files > main.files || :
mv main.files %{name}-devel.files
cat lld-devel.files >> clang-devel.files
rm -f other.files lld-devel.files

%files -f %{_builddir}/%{name}.files
%license llvm/LICENSE.TXT

%files devel -f %{_builddir}/%{name}-devel.files

%files -n clang -f %{_builddir}/clang.files
%license clang/LICENSE.TXT

%files -n clang-devel -f %{_builddir}/clang-devel.files

%files -n lld -f %{_builddir}/lld.files
%license lld/LICENSE.TXT
