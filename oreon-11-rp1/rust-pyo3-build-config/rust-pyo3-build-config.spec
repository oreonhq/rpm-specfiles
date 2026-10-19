%global source0_hash f41027e41b4bd03f6e60f9f417fe24a6341a6bb744edd62b6f709f2a52ea30e9
%bcond check 0
%global debug_package %{nil}
%global crate pyo3-build-config
Name:           rust-pyo3-build-config
Version:        0.29.2
Release:        1%{?dist}
Summary:        Build configuration for the PyO3 ecosystem
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3-build-config
Source0:        https://static.crates.io/crates/pyo3-build-config/pyo3-build-config-%{version}.crate
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  python3
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+extension-module-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+extension-module-devel

This package contains library source intended for building other packages which
use the "extension-module" feature of the "%{crate}" crate.

%package     -n %{name}+resolve-config-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+resolve-config-devel

This package contains library source intended for building other packages which
use the "resolve-config" feature of the "%{crate}" crate.

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
%files -n rust-pyo3-build-config-devel -f %{oreon_filedir}/rust-pyo3-build-config-devel.list

%changelog

%autochangelog
