%global source0_hash 1b43ede17f21864e81be2fa654110bf1e793774238d86ef8555c37e6519c0403
%bcond check 0
%global debug_package %{nil}
%global crate half
Name:           rust-half1
Version:        1.8.3
Release:        1%{?dist}
Summary:        Half-precision floating point f16 and bf16 types for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/half
Source0:        https://static.crates.io/crates/half/half-%{version}.crate
Patch:          half-fix-metadata.diff
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
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+num-traits-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+num-traits-devel

This package contains library source intended for building other packages which
use the "num-traits" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+use-intrinsics-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+use-intrinsics-devel

This package contains library source intended for building other packages which
use the "use-intrinsics" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip bfloat::test::test_nan_conversion_to_larger --skip bfloat::test::test_nan_conversion_to_smaller --skip binary16::test::test_nan_conversion_to_larger --skip binary16::test::test_nan_conversion_to_smaller
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-half1-devel -f %{oreon_filedir}/rust-half1-devel.list

%changelog

%autochangelog
