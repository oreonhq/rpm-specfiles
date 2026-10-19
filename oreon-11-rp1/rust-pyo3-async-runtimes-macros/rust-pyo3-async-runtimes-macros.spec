%global source0_hash bcd7d70ee0ca1661c40407e6f84e4463ef2658c90a9e2fbbd4515b2bcdfcaeca
%bcond check 1
%global debug_package %{nil}
%global crate pyo3-async-runtimes-macros
Name:           rust-pyo3-async-runtimes-macros
Version:        0.27.0
Release:        1%{?dist}
Summary:        Proc Macro Attributes for pyo3-async-runtimes
License:        Apache-2.0
URL:            https://crates.io/crates/pyo3-async-runtimes-macros
Source0:        https://static.crates.io/crates/pyo3-async-runtimes-macros/pyo3-async-runtimes-macros-%{version}.crate
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
Summary:        Proc Macro Attributes for pyo3-async-runtimes
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
%files -n rust-pyo3-async-runtimes-macros-devel -f %{oreon_filedir}/rust-pyo3-async-runtimes-macros-devel.list

%changelog

%autochangelog
