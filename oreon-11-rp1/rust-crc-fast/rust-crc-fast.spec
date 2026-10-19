%global source0_hash e75b2483e97a5a7da73ac68a05b629f9c53cff58d8ed1c77866079e18b00dba5
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate crc-fast
Name:           rust-crc-fast
Version:        1.10.0
Release:        1%{?dist}
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
License:        (MIT OR Apache-2.0) AND Zlib
URL:            https://crates.io/crates/crc-fast
Source0:        https://static.crates.io/crates/crc-fast/crc-fast-%{version}.crate
Patch:          crc-fast-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+cache-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+cache-devel

This package contains library source intended for building other packages which
use the "cache" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+ffi-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+ffi-devel

This package contains library source intended for building other packages which
use the "ffi" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+optimize_crc32_auto-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+optimize_crc32_auto-devel

This package contains library source intended for building other packages which
use the "optimize_crc32_auto" feature of the "%{crate}" crate.

%package     -n %{name}+optimize_crc32_avx512_v4s3x3-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+optimize_crc32_avx512_v4s3x3-devel

This package contains library source intended for building other packages which
use the "optimize_crc32_avx512_v4s3x3" feature of the "%{crate}" crate.

%package     -n %{name}+optimize_crc32_avx512_vpclmulqdq_v3x2-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+optimize_crc32_avx512_vpclmulqdq_v3x2-devel

This package contains library source intended for building other packages which
use the "optimize_crc32_avx512_vpclmulqdq_v3x2" feature of the "%{crate}" crate.

%package     -n %{name}+optimize_crc32_neon_blended-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+optimize_crc32_neon_blended-devel

This package contains library source intended for building other packages which
use the "optimize_crc32_neon_blended" feature of the "%{crate}" crate.

%package     -n %{name}+optimize_crc32_neon_eor3_v9s3x2e_s3-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+optimize_crc32_neon_eor3_v9s3x2e_s3-devel

This package contains library source intended for building other packages which
use the "optimize_crc32_neon_eor3_v9s3x2e_s3" feature of the "%{crate}" crate.

%package     -n %{name}+optimize_crc32_neon_v12e_v1-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+optimize_crc32_neon_v12e_v1-devel

This package contains library source intended for building other packages which
use the "optimize_crc32_neon_v12e_v1" feature of the "%{crate}" crate.

%package     -n %{name}+optimize_crc32_neon_v3s4x2e_v2-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+optimize_crc32_neon_v3s4x2e_v2-devel

This package contains library source intended for building other packages which
use the "optimize_crc32_neon_v3s4x2e_v2" feature of the "%{crate}" crate.

%package     -n %{name}+optimize_crc32_sse_v4s3x3-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+optimize_crc32_sse_v4s3x3-devel

This package contains library source intended for building other packages which
use the "optimize_crc32_sse_v4s3x3" feature of the "%{crate}" crate.

%package     -n %{name}+panic-handler-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+panic-handler-devel

This package contains library source intended for building other packages which
use the "panic-handler" feature of the "%{crate}" crate.

%package     -n %{name}+spin-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+spin-devel

This package contains library source intended for building other packages which
use the "spin" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+vpclmulqdq-devel
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD
BuildArch:      noarch
%description -n %{name}+vpclmulqdq-devel

This package contains library source intended for building other packages which
use the "vpclmulqdq" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f cli
%install
%cargo_install -f cli
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -f cli -- -- %{shrink:
    --skip lib::test_ffi_header
    --skip test_benchmark_
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-crc-fast-devel -f %{oreon_filedir}/rust-crc-fast-devel.list

%changelog

%autochangelog
