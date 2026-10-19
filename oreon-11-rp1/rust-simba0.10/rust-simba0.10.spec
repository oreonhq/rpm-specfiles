%global source0_hash f1a7200d82ff1c7b4235efd12f11e2537a402c91cf83a5cb97ce80eef787fde7
%bcond check 1
%global debug_package %{nil}
%global crate simba
Name:           rust-simba0.10
Version:        0.10.2
Release:        1%{?dist}
Summary:        SIMD algebra for Rust
License:        Apache-2.0
URL:            https://crates.io/crates/simba
Source0:        https://static.crates.io/crates/simba/simba-%{version}.crate
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
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cordic-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+cordic-devel

This package contains library source intended for building other packages which
use the "cordic" feature of the "%{crate}" crate.

%package     -n %{name}+decimal-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+decimal-devel

This package contains library source intended for building other packages which
use the "decimal" feature of the "%{crate}" crate.

%package     -n %{name}+fixed-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+fixed-devel

This package contains library source intended for building other packages which
use the "fixed" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+libm_force-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+libm_force-devel

This package contains library source intended for building other packages which
use the "libm_force" feature of the "%{crate}" crate.

%package     -n %{name}+partial_fixed_point_support-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+partial_fixed_point_support-devel

This package contains library source intended for building other packages which
use the "partial_fixed_point_support" feature of the "%{crate}" crate.

%package     -n %{name}+portable_simd-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+portable_simd-devel

This package contains library source intended for building other packages which
use the "portable_simd" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+rkyv-devel

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-serialize-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+rkyv-serialize-devel

This package contains library source intended for building other packages which
use the "rkyv-serialize" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_serialize-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+serde_serialize-devel

This package contains library source intended for building other packages which
use the "serde_serialize" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+wide-devel
Summary:        SIMD algebra for Rust
BuildArch:      noarch
%description -n %{name}+wide-devel

This package contains library source intended for building other packages which
use the "wide" feature of the "%{crate}" crate.

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
%files -n rust-simba0.10-devel -f %{oreon_filedir}/rust-simba0.10-devel.list

%changelog

%autochangelog
