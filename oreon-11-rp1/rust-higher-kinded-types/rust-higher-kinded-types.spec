%global source0_hash 561985554c8b8d4808605c90a5f1979cc6c31a5d20b78465cd59501233c6678e
%bcond check 1
%global debug_package %{nil}
%global crate higher-kinded-types
Name:           rust-higher-kinded-types
Version:        0.1.1
Release:        1%{?dist}
Summary:        "Generic generics" / higher-kinded APIs in stable Rust
License:        Zlib OR MIT OR Apache-2.0
URL:            https://crates.io/crates/higher-kinded-types
Source0:        https://static.crates.io/crates/higher-kinded-types/higher-kinded-types-%{version}.crate
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
Summary:        "Generic generics" / higher-kinded APIs in stable Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+better-docs-devel
Summary:        "Generic generics" / higher-kinded APIs in stable Rust
BuildArch:      noarch
%description -n %{name}+better-docs-devel

This package contains library source intended for building other packages which
use the "better-docs" feature of the "%{crate}" crate.

%package     -n %{name}+docs-rs-devel
Summary:        "Generic generics" / higher-kinded APIs in stable Rust
BuildArch:      noarch
%description -n %{name}+docs-rs-devel

This package contains library source intended for building other packages which
use the "docs-rs" feature of the "%{crate}" crate.

%package     -n %{name}+fn_traits-devel
Summary:        "Generic generics" / higher-kinded APIs in stable Rust
BuildArch:      noarch
%description -n %{name}+fn_traits-devel

This package contains library source intended for building other packages which
use the "fn_traits" feature of the "%{crate}" crate.

%package     -n %{name}+ui-tests-devel
Summary:        "Generic generics" / higher-kinded APIs in stable Rust
BuildArch:      noarch
%description -n %{name}+ui-tests-devel

This package contains library source intended for building other packages which
use the "ui-tests" feature of the "%{crate}" crate.

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
%files -n rust-higher-kinded-types-devel -f %{oreon_filedir}/rust-higher-kinded-types-devel.list

%changelog

%autochangelog
