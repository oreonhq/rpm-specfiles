%global source0_hash dc05a5d33db20c784f873e84934ad94bb209a090987ac5f62fede2c178234f23
%bcond check 1
%global debug_package %{nil}
%global crate derive_utils
Name:           rust-derive_utils
Version:        0.16.0
Release:        1%{?dist}
Summary:        Procedural macro helper for easily writing derive macros for enums
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/derive_utils
Source0:        https://static.crates.io/crates/derive_utils/derive_utils-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Procedural macro helper for easily writing derive macros for enums
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli set Cargo.toml arrays delitem --key path test tests/compiletest.rs
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
%files -n rust-derive_utils-devel -f %{oreon_filedir}/rust-derive_utils-devel.list

%changelog

%autochangelog
