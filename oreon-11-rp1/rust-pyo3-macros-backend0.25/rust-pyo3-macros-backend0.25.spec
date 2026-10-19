%global source0_hash 4109984c22491085343c05b0dbc54ddc405c3cf7b4374fc533f5c3313a572ccc
%bcond check 1
%global debug_package %{nil}
%global crate pyo3-macros-backend
Name:           rust-pyo3-macros-backend0.25
Version:        0.25.1
Release:        1%{?dist}
Summary:        Code generation for PyO3 package
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3-macros-backend
Source0:        https://static.crates.io/crates/pyo3-macros-backend/pyo3-macros-backend-%{version}.crate
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
Summary:        Code generation for PyO3 package
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-async-devel
Summary:        Code generation for PyO3 package
BuildArch:      noarch
%description -n %{name}+experimental-async-devel

This package contains library source intended for building other packages which
use the "experimental-async" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-inspect-devel
Summary:        Code generation for PyO3 package
BuildArch:      noarch
%description -n %{name}+experimental-inspect-devel

This package contains library source intended for building other packages which
use the "experimental-inspect" feature of the "%{crate}" crate.

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
%files -n rust-pyo3-macros-backend0.25-devel -f %{oreon_filedir}/rust-pyo3-macros-backend0.25-devel.list

%changelog

%autochangelog
