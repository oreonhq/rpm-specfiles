%global source0_hash 2f2cca48d7c093a680461fc80e7ef812f383cdf6e421a718a5292fd42438960b

%undefine __cmake_in_source_build
%bcond check 0
%global commit ad75c5edcdff96d73c245b57fbc07607aaca9f95
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ts_commit d76759e746f3564a03f6106ae19679742f2a1831
%global ts_shortcommit %(c=%{ts_commit}; echo ${c:0:7})
%global wc_commit b6dd1fb658a282c64b029867845bc50ae59e1497
%global wc_shortcommit %(c=%{wc_commit}; echo ${c:0:7})

Summary: The WebAssembly Binary Toolkit
Name: wabt
Version: 1.0.39
Release: 2%{?dist}
URL: https://github.com/WebAssembly/wabt
Source0: https://github.com/WebAssembly/wabt/archive/%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/WebAssembly/testsuite/archive/%{ts_commit}/%{name}-testsuite-%{ts_shortcommit}.tar.gz
Source2: https://github.com/WebAssembly/wasm-c-api/archive/%{wc_commit}/%{name}-wasm-c-api-%{wc_shortcommit}.tar.gz
# increase test timeout to avoid failures
Patch0: %{name}-test-timeout.patch
License: Apache-2.0
BuildRequires: cmake3
BuildRequires: gcc-c++
BuildRequires: openssl-devel
%if %{with check}
BuildRequires: gtest-devel
BuildRequires: python%{python3_pkgversion}-ply
BuildRequires: simde-devel >= 0.8.2
%endif
# wasm.h from https://github.com/WebAssembly/wasm-c-api/ is used for build
Provides: bundled(wasm-c-api) = %{wc_commit}

%description
WABT (we pronounce it "wabbit") is a suite of tools for WebAssembly. These tools
are intended for use in (or for development of) toolchains or other systems that
want to manipulate WebAssembly files. Unlike the WebAssembly spec interpreter
(which is written to be as simple, declarative and "speccy" as possible), they
are written in C/C++ and designed for easier integration into other systems.
Unlike Binaryen these tools do not aim to provide an optimization platform or a
higher-level compiler target; instead they aim for full fidelity and compliance
with the spec (e.g. 1:1 round-trips with no changes to instructions).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
rmdir third_party/wasm-c-api
tar xzf %{S:2} -C third_party
mv third_party/wasm-c-api{-%{wc_commit},}
%if %{with check}
rmdir third_party/testsuite
tar xzf %{S:1} -C third_party
mv third_party/testsuite{-%{ts_commit},}
%patch 0 -p1 -b .timeout
pushd test
# https://github.com/WebAssembly/wabt/issues/1044
%ifarch i686
rm regress/empty-quoted-module.txt
rm spec/float_exprs.txt
rm spec/float_misc.txt
rm spec/local_tee.txt
rm spec/simd_f32x4_arith.txt
rm spec/simd_f32x4_pmin_pmax.txt
rm spec/simd_f64x2_arith.txt
rm spec/simd_f64x2_pmin_pmax.txt
rm wasm2c/spec/conversions.txt
rm wasm2c/spec/float_memory.txt
rm wasm2c/spec/float_misc.txt
rm wasm2c/spec/float_exprs.txt
rm wasm2c/spec/local_tee.txt
rm wasm2c/spec/memory64/float_memory64.txt
rm wasm2c/spec/multi-memory/float_memory0.txt
rm wasm2c/spec/select.txt
rm wast2json/test-invalid-quoted-modules.txt
%endif
# https://github.com/WebAssembly/wabt/issues/1045
# https://github.com/WebAssembly/wabt/issues/2240
%ifarch ppc64le
rm spec/conversions.txt
rm spec/simd_conversions.txt
rm wasm2c/spec/memory64/simd_address.txt
rm wasm2c/spec/simd_address.txt
rm wasm2c/spec/simd_f32x4_arith.txt
rm wasm2c/spec/simd_f32x4_pmin_pmax.txt
rm wasm2c/spec/simd_splat.txt
%endif
popd
%endif

%build
%cmake3 -DUSE_SYSTEM_GTEST=ON \
%ifarch i686
    -DWASM2C_CFLAGS="-msse2 -mfpmath=sse"
%endif
%cmake3_build

%install
%cmake3_install

%if %{with check}
%check
# See https://github.com/WebAssembly/wabt/blob/main/.github/workflows/build.yml#L261
cmake --build redhat-linux-build --verbose --target run-unittests %{?_smp_mflags}
cmake --build redhat-linux-build --verbose --target run-tests %{?_smp_mflags}
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/spectest-interp
%{_bindir}/wasm-decompile
%{_bindir}/wasm-interp
%{_bindir}/wasm-objdump
%{_bindir}/wasm-stats
%{_bindir}/wasm-strip
%{_bindir}/wasm-validate
%{_bindir}/wasm2c
%{_bindir}/wasm2wat
%{_bindir}/wast2json
%{_bindir}/wat-desugar
%{_bindir}/wat2wasm
%{_datadir}/wabt
%{_includedir}/wabt
%{_includedir}/wasm-rt.h
%{_includedir}/wasm-rt-exceptions.h
%{_libdir}/cmake/wabt
%{_libdir}/libwabt.a
%{_libdir}/libwasm-rt-impl.a
%{_mandir}/man1/spectest-interp.1*
%{_mandir}/man1/wasm-decompile.1*
%{_mandir}/man1/wasm-interp.1*
%{_mandir}/man1/wasm-objdump.1*
%{_mandir}/man1/wasm-stats.1*
%{_mandir}/man1/wasm-strip.1*
%{_mandir}/man1/wasm-validate.1*
%{_mandir}/man1/wasm2c.1*
%{_mandir}/man1/wasm2wat.1*
%{_mandir}/man1/wast2json.1*
%{_mandir}/man1/wat-desugar.1*
%{_mandir}/man1/wat2wasm.1*

%changelog
%autochangelog
