%global source0_hash cb26cec98cce3a3d96cbb7bced3c4b16e3d13f27ec56dbd62cbc8f39cfb9d653
%bcond check 0
%global debug_package %{nil}
%global crate keccak
Name:           rust-keccak
Version:        0.1.6
Release:        1%{?dist}
Summary:        Pure Rust implementation of the Keccak sponge function including the...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/keccak
Source0:        https://static.crates.io/crates/keccak/keccak-%{version}.crate
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

%package     -n %{name}+asm-devel
Summary:        Pure Rust implementation of the Keccak sponge function including the...
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%package     -n %{name}+no_unroll-devel
Summary:        Pure Rust implementation of the Keccak sponge function including the...
BuildArch:      noarch
%description -n %{name}+no_unroll-devel

This package contains library source intended for building other packages which
use the "no_unroll" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Pure Rust implementation of the Keccak sponge function including the...
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

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
%files -n rust-keccak-devel -f %{oreon_filedir}/rust-keccak-devel.list

%changelog

%autochangelog
