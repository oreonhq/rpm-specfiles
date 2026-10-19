%global source0_hash 73225868fc1cd84eef2c3c230ddb91273bf1de46aeb8a4248da76d32a0924a1c
%bcond check 0
%global debug_package %{nil}
%global crate pyo3-macros
Name:           rust-pyo3-macros
Version:        0.29.2
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

%package     -n %{name}+experimental-async-devel
Summary:        Proc macros for PyO3 package
BuildArch:      noarch
%description -n %{name}+experimental-async-devel

This package contains library source intended for building other packages which
use the "experimental-async" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-inspect-devel
Summary:        Proc macros for PyO3 package
BuildArch:      noarch
%description -n %{name}+experimental-inspect-devel

This package contains library source intended for building other packages which
use the "experimental-inspect" feature of the "%{crate}" crate.

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
%files -n rust-pyo3-macros-devel -f %{oreon_filedir}/rust-pyo3-macros-devel.list

%changelog

%autochangelog
