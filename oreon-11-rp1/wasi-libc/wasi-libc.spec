%global source0_hash d511de1f556521041b0811c6fb9c3e175d9a527bce5ade9ca31ab79b0941823c
Name:       wasi-libc
Summary:        C library implementation for WebAssembly System Interface
Version:    29
Release:        1%{?dist}
License:    Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND BSD-2-Clause
URL:        https://github.com/WebAssembly/wasi-libc/
Source0:        https://github.com/WebAssembly/%{name}//archive/refs/tags/wasi-sdk-%{version}.tar.gz#/%{name}-wasi-sdk-%{version}.tar.gz
Source1:    smoke-test.c
Patch:      0001-make-don-t-rebuild-files-on-make-install.patch
Patch:      0002-Disable-linking-compiler-rt-builtins-library.patch
Patch:      wasi-libc-clang-wasip1-expected.patch
%global     musl_version 1.2.5
%global     _binaries_in_noarch_packages_terminate_build 0
BuildArch:  noarch
%global     toolchain clang
%global     __brp_llvm_compile_lto_elf %{nil}
%global __brp_strip_static_archive %{nil}
%global __brp_strip_lto %{nil}
%global     build_cflags --target=wasm32-wasip1 -fstack-protector
%global     wasi_prefix %{_prefix}/wasm32-wasi
%global     wasi_datadir %{wasi_prefix}/share
%global     wasi_includedir %{wasi_prefix}/include
%global     wasi_libdir %{wasi_prefix}/lib
%global     wasi_make_flags TARGET_TRIPLE=wasm32-wasip1 MALLOC_IMPL=emmalloc INSTALL_DIR='%{buildroot}%{wasi_prefix}' SYSROOT='%{_builddir}/sysroot'
# oreon:deps
BuildRequires:  clang
BuildRequires:  git-core
BuildRequires:  llvm
BuildRequires:  make
# /oreon:deps
%description

%package static
Provides: bundled(musl) = %{musl_version}
Summary:  C library for WASI - static libraries
%description static

%package devel
Requires: %{name}-static  = %{version}-%{release}
Provides: bundled(musl) = %{musl_version}
Summary:  C library for WASI - headers and development files
%description devel

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-wasi-sdk-%{version} -S git_am
# Pull additional license text
cp -p libc-bottom-half/cloudlibc/LICENSE LICENSE-cloudlibc

%build

%make_build %{wasi_make_flags}
make %{?_smp_mflags} %{wasi_make_flags} check-symbols
%install
%make_install %{wasi_make_flags}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

xargs test '%{musl_version}' = <libc-top-half/musl/VERSION
%files -f %{oreon_filedir}/main.list
%files -n wasi-libc-static -f %{oreon_filedir}/wasi-libc-static.list
%files -n wasi-libc-devel -f %{oreon_filedir}/wasi-libc-devel.list

%changelog

%autochangelog
