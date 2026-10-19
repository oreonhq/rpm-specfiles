%global source0_hash 6ea2d84b969582b4b1864a92dc5d27cd2b77b622a8d79306834f1be5ba20d84b
%bcond check 0
%global debug_package %{nil}
%global crate half
Name:           rust-half
Version:        2.7.1
Release:        1%{?dist}
Summary:        Half-precision floating point f16 and bf16 types for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/half
Source0:        https://static.crates.io/crates/half/half-%{version}.crate
Patch:          half-fix-metadata-auto.diff
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

%package     -n %{name}+nightly-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+rand_distr-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+rand_distr-devel

This package contains library source intended for building other packages which
use the "rand_distr" feature of the "%{crate}" crate.

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

%package     -n %{name}+zerocopy-devel
Summary:        Half-precision floating point f16 and bf16 types for Rust
BuildArch:      noarch
%description -n %{name}+zerocopy-devel

This package contains library source intended for building other packages which
use the "zerocopy" feature of the "%{crate}" crate.

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
%files -n rust-half-devel -f %{oreon_filedir}/rust-half-devel.list

%changelog

%autochangelog
