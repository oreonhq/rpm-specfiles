%global source0_hash 353e1ca18966c16d9deb1c69278edbc5f194139612772bd9537af60ac231e1e6
%bcond check 0
%global debug_package %{nil}
%global crate primeorder
Name:           rust-primeorder
Version:        0.13.6
Release:        1%{?dist}
Summary:        Pure Rust implementation of complete addition formulas for prime orde...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/primeorder
Source0:        https://static.crates.io/crates/primeorder/primeorder-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of complete addition formulas for prime orde...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+dev-devel
Summary:        Pure Rust implementation of complete addition formulas for prime orde...
BuildArch:      noarch
%description -n %{name}+dev-devel

This package contains library source intended for building other packages which
use the "dev" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Pure Rust implementation of complete addition formulas for prime orde...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serdect-devel
Summary:        Pure Rust implementation of complete addition formulas for prime orde...
BuildArch:      noarch
%description -n %{name}+serdect-devel

This package contains library source intended for building other packages which
use the "serdect" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of complete addition formulas for prime orde...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-primeorder-devel -f %{oreon_filedir}/rust-primeorder-devel.list

%changelog

%autochangelog
