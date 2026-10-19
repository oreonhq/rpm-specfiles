%global source2_hash 27e0387973d6b8507cb15f825f6f26e0278d4d5857082c1f56b49a7b39a90183
%global source0_hash 3560a7b1951efe814fcd721938313adc56753ca39f4b23847d7e9a2402f5dbff
%bcond check 1
%global debug_package %{nil}
%global crate blake2b_simd
Name:           rust-blake2b_simd
Version:        1.0.5
Release:        1%{?dist}
Summary:        Pure Rust BLAKE2b implementation with dynamic SIMD
License:        MIT
URL:            https://crates.io/crates/blake2b_simd
Source0:        https://static.crates.io/crates/blake2b_simd/blake2b_simd-%{version}.crate
Source2:        https://github.com/oconnor663/blake2_simd/raw/refs/tags/1.0.3/LICENSE
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
Summary:        Pure Rust BLAKE2b implementation with dynamic SIMD
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust BLAKE2b implementation with dynamic SIMD
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+uninline_portable-devel
Summary:        Pure Rust BLAKE2b implementation with dynamic SIMD
BuildArch:      noarch
%description -n %{name}+uninline_portable-devel

This package contains library source intended for building other packages which
use the "uninline_portable" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE2} .
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
%files -n rust-blake2b_simd-devel -f %{oreon_filedir}/rust-blake2b_simd-devel.list

%changelog

%autochangelog
