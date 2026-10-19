%global source0_hash cf3432d9f609fbede9f624d1dbefcce77985a9322de1d0e6d460ec05502b7fd0
%bcond check 1
%global debug_package %{nil}
%global crate kvm-bindings
%global supported_arches aarch64 riscv64 x86_64
Name:           rust-kvm-bindings
Version:        0.13.0
Release:        1%{?dist}
Summary:        Rust FFI bindings to KVM generated using bindgen
License:        Apache-2.0
URL:            https://crates.io/crates/kvm-bindings
Source0:        https://static.crates.io/crates/kvm-bindings/kvm-bindings-%{version}.crate
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
Summary:        Rust FFI bindings to KVM generated using bindgen
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+fam-wrappers-devel
Summary:        Rust FFI bindings to KVM generated using bindgen
BuildArch:      noarch
%description -n %{name}+fam-wrappers-devel

This package contains library source intended for building other packages which
use the "fam-wrappers" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust FFI bindings to KVM generated using bindgen
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+vmm-sys-util-devel
Summary:        Rust FFI bindings to KVM generated using bindgen
BuildArch:      noarch
%description -n %{name}+vmm-sys-util-devel

This package contains library source intended for building other packages which
use the "vmm-sys-util" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifarch %{supported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifarch %{supported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-kvm-bindings-devel -f %{oreon_filedir}/rust-kvm-bindings-devel.list

%changelog

%autochangelog
