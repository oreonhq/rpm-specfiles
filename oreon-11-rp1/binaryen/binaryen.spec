%global source0_hash eb0825d6f601b81c70db41aea3c3b35848dc1de7859ecbd01ac89807f8e14891

%bcond check 0
%global wats_commit 4b24564c844e3d34bf46dfcb3c774ee5163e31cc
%global wats_shortcommit %(c=%{wats_commit}; echo ${c:0:7})

Summary:       Compiler and toolchain infrastructure library for WebAssembly
Name:          binaryen
Version:       126
Release:       1%{?dist}

URL:           https://github.com/WebAssembly/binaryen
Source0:       %{url}/archive/version_%{version}/%{name}-version_%{version}.tar.gz
Source1:       https://github.com/WebAssembly/testsuite/archive/%{wats_commit}/testsuite-%{wats_shortcommit}.tar.gz
Patch0:        %{name}-use-system-gtest.patch
Patch1:        https://github.com/WebAssembly/binaryen/pull/8362.patch
# third_party/llvm-project/MD5.cpp: bcrypt-Solar-Designer
# third_party/llvm-project/include/llvm/Support/MD5.h: bcrypt-Solar-Designer
License:       Apache-2.0 AND bcrypt-Solar-Designer

# tests fail on big-endian
# https://github.com/WebAssembly/binaryen/issues/2983
ExcludeArch:   ppc64 s390x
BuildRequires: cmake
BuildRequires: FP16-devel
BuildRequires: gcc-c++
%if %{with check}
BuildRequires: cmake(GTest)
BuildRequires: nodejs
BuildRequires: pkgconfig(gmock)
BuildRequires: python3dist(filecheck)
BuildRequires: python3dist(lit)
%endif

# filter out internal shared library
%global __provides_exclude_from ^%{_libdir}/%{name}/.*$
%global __requires_exclude ^libbinaryen\\.so.*$

%description
Binaryen is a compiler and toolchain infrastructure library for WebAssembly,
written in C++. It aims to make compiling to WebAssembly easy, fast, and
effective:

* Easy: Binaryen has a simple C API in a single header, and can also be used
  from JavaScript. It accepts input in WebAssembly-like form but also accepts
  a general control flow graph for compilers that prefer that.

* Fast: Binaryen's internal IR uses compact data structures and is designed for
  completely parallel codegen and optimization, using all available CPU cores.
  Binaryen's IR also compiles down to WebAssembly extremely easily and quickly
  because it is essentially a subset of WebAssembly.

* Effective: Binaryen's optimizer has many passes that can improve code very
  significantly (e.g. local coloring to coalesce local variables; dead code
  elimination; precomputing expressions when possible at compile time; etc.).
  These optimizations aim to make Binaryen powerful enough to be used as a
  compiler backend by itself. One specific area of focus is on
  WebAssembly-specific optimizations (that general-purpose compilers might not
  do), which you can think of as wasm minification , similar to minification for
  JavaScript, CSS, etc., all of which are language-specific (an example of such
  an optimization is block return value generation in SimplifyLocals).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-version_%{version}
%if %{with check}
rmdir test/spec/testsuite
tar xzf %{S:1} -C test/spec
mv test/spec/testsuite{-%{wats_commit},}
# v8 tests cannot be executed because we don't have v8 in Fedora
rm -rv test/lit/d8
rm -rv third_party/FP16
%endif

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}/%{name} \
    -DCMAKE_INSTALL_RPATH=\$ORIGIN/../%{_lib}/%{name} \
    -DENABLE_WERROR=OFF \

%cmake_build

%install
%cmake_install
rm -v %{buildroot}%{_bindir}/binaryen-unittests

%if %{with check}
%check
./check.py \
    --binaryen-bin %{__cmake_builddir}/bin \
    --binaryen-lib %{__cmake_builddir}/lib \

%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/wasm-as
%{_bindir}/wasm-ctor-eval
%{_bindir}/wasm-dis
%{_bindir}/wasm-emscripten-finalize
%{_bindir}/wasm-fuzz-lattices
%{_bindir}/wasm-fuzz-types
%{_bindir}/wasm-merge
%{_bindir}/wasm-metadce
%{_bindir}/wasm-opt
%{_bindir}/wasm-reduce
%{_bindir}/wasm-shell
%{_bindir}/wasm-split
%{_bindir}/wasm2js
%{_includedir}/binaryen-c.h
%{_includedir}/wasm-delegations.def
%{_libdir}/%{name}/libbinaryen.so

%changelog
%autochangelog
