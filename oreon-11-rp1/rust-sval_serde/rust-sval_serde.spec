%global source0_hash b983833a8a2390f89ebcf9b9acd06883017014b4ffd72ee28e0c9de6852039f5
%bcond check 0
%global debug_package %{nil}
%global crate sval_serde
Name:           rust-sval_serde
Version:        2.20.0
Release:        1%{?dist}
Summary:        Integration between serde::Serialize and sval::Value
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sval_serde
Source0:        https://static.crates.io/crates/sval_serde/sval_serde-%{version}.crate
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
Summary:        Integration between serde::Serialize and sval::Value
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Integration between serde::Serialize and sval::Value
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
%files -n rust-sval_serde-devel -f %{oreon_filedir}/rust-sval_serde-devel.list

%changelog

%autochangelog
