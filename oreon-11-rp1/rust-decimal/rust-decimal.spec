%global source0_hash 5a8ab77e91baeb15034c3be91e87bff4665c9036216148e4996d9a9f5792114d
%bcond check 0
%global debug_package %{nil}
%global crate decimal
Name:           rust-decimal
Version:        2.1.0
Release:        1%{?dist}
Summary:        Decimal floating point arithmetic for Rust
License:        Apache-2.0
URL:            https://crates.io/crates/decimal
Source0:        https://static.crates.io/crates/decimal/decimal-%{version}.crate
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
Summary:        Decimal floating point arithmetic for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ord_subset-devel
Summary:        Decimal floating point arithmetic for Rust
BuildArch:      noarch
%description -n %{name}+ord_subset-devel

This package contains library source intended for building other packages which
use the "ord_subset" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-serialize-devel
Summary:        Decimal floating point arithmetic for Rust
BuildArch:      noarch
%description -n %{name}+rustc-serialize-devel

This package contains library source intended for building other packages which
use the "rustc-serialize" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Decimal floating point arithmetic for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-decimal-devel -f %{oreon_filedir}/rust-decimal-devel.list

%changelog

%autochangelog
