%global source0_hash dc1b4cb0cc549fcf58d7dfc081778139b3d283a081644e833e84682ad71cea24
%bcond check 0
%global debug_package %{nil}
%global crate wasm-bindgen-shared
Name:           rust-wasm-bindgen-shared
Version:        0.2.126
Release:        1%{?dist}
Summary:        Shared support between wasm-bindgen and wasm-bindgen cli, an internal
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/wasm-bindgen-shared
Source0:        https://static.crates.io/crates/wasm-bindgen-shared/wasm-bindgen-shared-%{version}.crate
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
Summary:        Shared support between wasm-bindgen and wasm-bindgen cli, an internal
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-wasm-bindgen-shared-devel -f %{oreon_filedir}/rust-wasm-bindgen-shared-devel.list

%changelog

%autochangelog
