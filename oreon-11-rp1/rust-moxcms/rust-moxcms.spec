%global source0_hash bb85c154ba489f01b25c0d36ae69a87e4a1c73a72631fc6c0eb6dde34a73e44b
%bcond check 0
%global debug_package %{nil}
%global crate moxcms
Name:           rust-moxcms
Version:        0.8.1
Release:        1%{?dist}
Summary:        Simple Color Management in Rust
License:        BSD-3-Clause OR Apache-2.0
URL:            https://crates.io/crates/moxcms
Source0:        https://static.crates.io/crates/moxcms/moxcms-%{version}.crate
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
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+any_to_any-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+any_to_any-devel

This package contains library source intended for building other packages which
use the "any_to_any" feature of the "%{crate}" crate.

%package     -n %{name}+avx-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+avx-devel

This package contains library source intended for building other packages which
use the "avx" feature of the "%{crate}" crate.

%package     -n %{name}+avx512-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+avx512-devel

This package contains library source intended for building other packages which
use the "avx512" feature of the "%{crate}" crate.

%package     -n %{name}+avx512_shaper_fixed_point_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+avx512_shaper_fixed_point_paths-devel

This package contains library source intended for building other packages which
use the "avx512_shaper_fixed_point_paths" feature of the "%{crate}" crate.

%package     -n %{name}+avx512_shaper_optimized_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+avx512_shaper_optimized_paths-devel

This package contains library source intended for building other packages which
use the "avx512_shaper_optimized_paths" feature of the "%{crate}" crate.

%package     -n %{name}+avx_luts-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+avx_luts-devel

This package contains library source intended for building other packages which
use the "avx_luts" feature of the "%{crate}" crate.

%package     -n %{name}+avx_shaper_fixed_point_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+avx_shaper_fixed_point_paths-devel

This package contains library source intended for building other packages which
use the "avx_shaper_fixed_point_paths" feature of the "%{crate}" crate.

%package     -n %{name}+avx_shaper_optimized_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+avx_shaper_optimized_paths-devel

This package contains library source intended for building other packages which
use the "avx_shaper_optimized_paths" feature of the "%{crate}" crate.

%package     -n %{name}+avx_shaper_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+avx_shaper_paths-devel

This package contains library source intended for building other packages which
use the "avx_shaper_paths" feature of the "%{crate}" crate.

%package     -n %{name}+extended_range-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+extended_range-devel

This package contains library source intended for building other packages which
use the "extended_range" feature of the "%{crate}" crate.

%package     -n %{name}+in_place-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+in_place-devel

This package contains library source intended for building other packages which
use the "in_place" feature of the "%{crate}" crate.

%package     -n %{name}+lut-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+lut-devel

This package contains library source intended for building other packages which
use the "lut" feature of the "%{crate}" crate.

%package     -n %{name}+neon-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+neon-devel

This package contains library source intended for building other packages which
use the "neon" feature of the "%{crate}" crate.

%package     -n %{name}+neon_luts-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+neon_luts-devel

This package contains library source intended for building other packages which
use the "neon_luts" feature of the "%{crate}" crate.

%package     -n %{name}+neon_shaper_fixed_point_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+neon_shaper_fixed_point_paths-devel

This package contains library source intended for building other packages which
use the "neon_shaper_fixed_point_paths" feature of the "%{crate}" crate.

%package     -n %{name}+neon_shaper_optimized_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+neon_shaper_optimized_paths-devel

This package contains library source intended for building other packages which
use the "neon_shaper_optimized_paths" feature of the "%{crate}" crate.

%package     -n %{name}+neon_shaper_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+neon_shaper_paths-devel

This package contains library source intended for building other packages which
use the "neon_shaper_paths" feature of the "%{crate}" crate.

%package     -n %{name}+options-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+options-devel

This package contains library source intended for building other packages which
use the "options" feature of the "%{crate}" crate.

%package     -n %{name}+sse-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+sse-devel

This package contains library source intended for building other packages which
use the "sse" feature of the "%{crate}" crate.

%package     -n %{name}+sse_luts-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+sse_luts-devel

This package contains library source intended for building other packages which
use the "sse_luts" feature of the "%{crate}" crate.

%package     -n %{name}+sse_shaper_fixed_point_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+sse_shaper_fixed_point_paths-devel

This package contains library source intended for building other packages which
use the "sse_shaper_fixed_point_paths" feature of the "%{crate}" crate.

%package     -n %{name}+sse_shaper_optimized_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+sse_shaper_optimized_paths-devel

This package contains library source intended for building other packages which
use the "sse_shaper_optimized_paths" feature of the "%{crate}" crate.

%package     -n %{name}+sse_shaper_paths-devel
Summary:        Simple Color Management in Rust
BuildArch:      noarch
%description -n %{name}+sse_shaper_paths-devel

This package contains library source intended for building other packages which
use the "sse_shaper_paths" feature of the "%{crate}" crate.

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
%files -n rust-moxcms-devel -f %{oreon_filedir}/rust-moxcms-devel.list

%changelog

%autochangelog
