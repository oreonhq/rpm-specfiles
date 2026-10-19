%global source0_hash 9e24a010dd405bd7ed803e5253182815b41bf2e6a80cc3bfc066658e03a198aa
%bcond check 0
%global debug_package %{nil}
%global crate keccak
Name:           rust-keccak0.2
Version:        0.2.0
Release:        1%{?dist}
Summary:        Pure Rust implementation of the Keccak sponge functions
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

%package     -n %{name}+hybrid-array-devel
Summary:        Pure Rust implementation of the Keccak sponge functions
BuildArch:      noarch
%description -n %{name}+hybrid-array-devel

This package contains library source intended for building other packages which
use the "hybrid-array" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Pure Rust implementation of the Keccak sponge functions
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

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
%files -n rust-keccak0.2-devel -f %{oreon_filedir}/rust-keccak0.2-devel.list

%changelog

%autochangelog
