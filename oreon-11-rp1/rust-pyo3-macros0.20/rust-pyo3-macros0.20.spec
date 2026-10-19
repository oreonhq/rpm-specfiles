%global source0_hash 7305c720fa01b8055ec95e484a6eca7a83c841267f0dd5280f0c8b8551d2c158
%bcond check 0
%global debug_package %{nil}
%global crate pyo3-macros
Name:           rust-pyo3-macros0.20
Version:        0.20.3
Release:        1%{?dist}
Summary:        Proc macros for PyO3 package
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3-macros
Source0:        https://static.crates.io/crates/pyo3-macros/pyo3-macros-%{version}.crate
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

%package     -n %{name}+multiple-pymethods-devel
Summary:        Proc macros for PyO3 package
BuildArch:      noarch
%description -n %{name}+multiple-pymethods-devel

This package contains library source intended for building other packages which
use the "multiple-pymethods" feature of the "%{crate}" crate.

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
%files -n rust-pyo3-macros0.20-devel -f %{oreon_filedir}/rust-pyo3-macros0.20-devel.list

%changelog

%autochangelog
