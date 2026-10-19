%global source0_hash e97ca2c89572ae41bbec1c99498251f87dd5a94e500c5ec19c382dd593dd5ce9
%bcond check 1
%global debug_package %{nil}
%global crate polonius-the-crab
Name:           rust-polonius-the-crab
Version:        0.4.2
Release:        1%{?dist}
Summary:        Tools to feature more lenient Polonius-based borrow-checker patterns in stable Rust
License:        Zlib OR MIT OR Apache-2.0
URL:            https://crates.io/crates/polonius-the-crab
Source0:        https://static.crates.io/crates/polonius-the-crab/polonius-the-crab-%{version}.crate
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
Summary:        Tools to feature more lenient Polonius-based borrow-checker patterns in stable Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+better-docs-devel
Summary:        Tools to feature more lenient Polonius-based borrow-checker patterns in stable Rust
BuildArch:      noarch
%description -n %{name}+better-docs-devel

This package contains library source intended for building other packages which
use the "better-docs" feature of the "%{crate}" crate.

%package     -n %{name}+polonius-devel
Summary:        Tools to feature more lenient Polonius-based borrow-checker patterns in stable Rust
BuildArch:      noarch
%description -n %{name}+polonius-devel

This package contains library source intended for building other packages which
use the "polonius" feature of the "%{crate}" crate.

%package     -n %{name}+ui-tests-devel
Summary:        Tools to feature more lenient Polonius-based borrow-checker patterns in stable Rust
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
%files -n rust-polonius-the-crab-devel -f %{oreon_filedir}/rust-polonius-the-crab-devel.list

%changelog

%autochangelog
