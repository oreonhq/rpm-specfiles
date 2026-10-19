%global source0_hash a4f0c30c76f2f4ccee3fe55a2435f691ca00c0e4bd87abe4f4a851b1d4dac39b
%bcond check 0
%global debug_package %{nil}
%global crate inventory
Name:           rust-inventory
Version:        0.3.24
Release:        1%{?dist}
Summary:        Typed distributed plugin registration
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/inventory
Source0:        https://static.crates.io/crates/inventory/inventory-%{version}.crate
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
Summary:        Typed distributed plugin registration
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
%files -n rust-inventory-devel -f %{oreon_filedir}/rust-inventory-devel.list

%changelog

%autochangelog
