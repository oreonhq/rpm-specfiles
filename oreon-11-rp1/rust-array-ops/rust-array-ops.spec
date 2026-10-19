%global source0_hash cc9118422b9f472e9f49c2775cbf92c1b2740bd74278fd66cad3dc7b5fa2c7ca
%bcond check 0
%global debug_package %{nil}
%global crate array-ops
Name:           rust-array-ops
Version:        0.1.0
Release:        1%{?dist}
Summary:        Automatic method implementations for array data types
License:        MPL-2.0+
URL:            https://crates.io/crates/array-ops
Source0:        https://static.crates.io/crates/array-ops/array-ops-%{version}.crate
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
Summary:        Automatic method implementations for array data types
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
%files -n rust-array-ops-devel -f %{oreon_filedir}/rust-array-ops-devel.list

%changelog

%autochangelog
