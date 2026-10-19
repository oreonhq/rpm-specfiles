%global source0_hash 0aa83c34e62843d924f905e0f5c866eb1dd6545fc4d719e803d9ba6030371fce
%bcond check 0
%global debug_package %{nil}
%global crate blake3
Name:           rust-blake3
Version:        1.8.5
Release:        1%{?dist}
Summary:        the BLAKE3 hash function
License:        CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception
URL:            https://crates.io/crates/blake3
Source0:        https://static.crates.io/crates/blake3/blake3-%{version}.crate
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
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+mmap-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+mmap-devel

This package contains library source intended for building other packages which
use the "mmap" feature of the "%{crate}" crate.

%package     -n %{name}+neon-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+neon-devel

This package contains library source intended for building other packages which
use the "neon" feature of the "%{crate}" crate.

%package     -n %{name}+no_avx2-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+no_avx2-devel

This package contains library source intended for building other packages which
use the "no_avx2" feature of the "%{crate}" crate.

%package     -n %{name}+no_avx512-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+no_avx512-devel

This package contains library source intended for building other packages which
use the "no_avx512" feature of the "%{crate}" crate.

%package     -n %{name}+no_neon-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+no_neon-devel

This package contains library source intended for building other packages which
use the "no_neon" feature of the "%{crate}" crate.

%package     -n %{name}+no_sse2-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+no_sse2-devel

This package contains library source intended for building other packages which
use the "no_sse2" feature of the "%{crate}" crate.

%package     -n %{name}+no_sse41-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+no_sse41-devel

This package contains library source intended for building other packages which
use the "no_sse41" feature of the "%{crate}" crate.

%package     -n %{name}+prefer_intrinsics-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+prefer_intrinsics-devel

This package contains library source intended for building other packages which
use the "prefer_intrinsics" feature of the "%{crate}" crate.

%package     -n %{name}+pure-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+pure-devel

This package contains library source intended for building other packages which
use the "pure" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+traits-preview-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+traits-preview-devel

This package contains library source intended for building other packages which
use the "traits-preview" feature of the "%{crate}" crate.

%package     -n %{name}+wasm32_simd-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+wasm32_simd-devel

This package contains library source intended for building other packages which
use the "wasm32_simd" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        the BLAKE3 hash function
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-blake3-devel -f %{oreon_filedir}/rust-blake3-devel.list

%changelog

%autochangelog
