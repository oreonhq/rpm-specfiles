%global source0_hash 4e27ee8bb91ca0adcf0ecb116293afa12d393f9c2b9b9cd54d33e8078fe19839
%bcond check 0
%global debug_package %{nil}
%global crate robust
Name:           rust-robust
Version:        1.2.0
Release:        1%{?dist}
Summary:        Robust adaptive floating-point predicates for computational geometry
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/robust
Source0:        https://static.crates.io/crates/robust/robust-%{version}.crate
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

%package     -n %{name}+no_std-devel
Summary:        Robust adaptive floating-point predicates for computational geometry
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

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
%files -n rust-robust-devel -f %{oreon_filedir}/rust-robust-devel.list

%changelog

%autochangelog
