%global source0_hash 7572660c8890448ba236b7376f27e389c6a7e1c70195622faced601f855c0ada
%bcond check 1
%global debug_package %{nil}
%global crate web_atoms
Name:           rust-web_atoms0.3
Version:        0.3.0
Release:        1%{?dist}
Summary:        Atoms for xml5ever and html5ever
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/web_atoms
Source0:        https://static.crates.io/crates/web_atoms/web_atoms-%{version}.crate
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
Summary:        Atoms for xml5ever and html5ever
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Atoms for xml5ever and html5ever
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
%files -n rust-web_atoms0.3-devel -f %{oreon_filedir}/rust-web_atoms0.3-devel.list

%changelog

%autochangelog
