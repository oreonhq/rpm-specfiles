%global source0_hash 1d8f70e07b9c3962945a74e59ca1c511bba65b6419468acc217c457d93f3c740
%bcond check 0
%global debug_package %{nil}
%global crate pulp-wasm-simd-flag
Name:           rust-pulp-wasm-simd-flag
Version:        0.1.1
Release:        1%{?dist}
Summary:        safe generic simd
License:        MIT
URL:            https://crates.io/crates/pulp-wasm-simd-flag
Source0:        https://static.crates.io/crates/pulp-wasm-simd-flag/pulp-wasm-simd-flag-%{version}.crate
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
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+relaxed-simd-devel
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+relaxed-simd-devel

This package contains library source intended for building other packages which
use the "relaxed-simd" feature of the "%{crate}" crate.

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
%files -n rust-pulp-wasm-simd-flag-devel -f %{oreon_filedir}/rust-pulp-wasm-simd-flag-devel.list

%changelog

%autochangelog
