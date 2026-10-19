%global source0_hash 7a0e87cdf78571d9fbeff16861c37a006cd718d2433dc6d5b80beaae367d899a
%bcond check 0
%global debug_package %{nil}
%global crate cint
Name:           rust-cint
Version:        0.3.1
Release:        1%{?dist}
Summary:        Lean, minimal, and stable set of types for color interoperation between crates in Rust
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/cint
Source0:        https://static.crates.io/crates/cint/cint-%{version}.crate
Patch:          https://github.com/fu5ha/cint/pull/3.patch
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
Summary:        Lean, minimal, and stable set of types for color interoperation between crates in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Lean, minimal, and stable set of types for color interoperation between crates in Rust
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

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
%files -n rust-cint-devel -f %{oreon_filedir}/rust-cint-devel.list

%changelog

%autochangelog
