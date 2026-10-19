%global source0_hash 167ce5e579f6bcf889c4f7175a8a5a585de84e8ff93976ce393efa5f2837aab1
%bcond check 0
%global debug_package %{nil}
%global crate wasm-bindgen-macro
Name:           rust-wasm-bindgen-macro
Version:        0.2.126
Release:        1%{?dist}
Summary:        Definition of the `#[wasm_bindgen]` attribute, an internal dependency
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/wasm-bindgen-macro
Source0:        https://static.crates.io/crates/wasm-bindgen-macro/wasm-bindgen-macro-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(%{crate}/default) = %{version}
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+strict-macro-devel
Summary:        Definition of the `#[wasm_bindgen]` attribute, an internal dependency
BuildArch:      noarch
%description -n %{name}+strict-macro-devel

This package contains library source intended for building other packages which
use the "strict-macro" feature of the "%{crate}" crate.

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
%files -n rust-wasm-bindgen-macro-devel -f %{oreon_filedir}/rust-wasm-bindgen-macro-devel.list

%changelog

%autochangelog
