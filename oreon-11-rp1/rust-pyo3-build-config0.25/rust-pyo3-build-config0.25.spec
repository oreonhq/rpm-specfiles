%global source0_hash 458eb0c55e7ece017adeba38f2248ff3ac615e53660d7c71a238d7d2a01c7598
%bcond check 1
%global debug_package %{nil}
%global crate pyo3-build-config
Name:           rust-pyo3-build-config0.25
Version:        0.25.1
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

%package     -n %{name}+abi3-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-devel

This package contains library source intended for building other packages which
use the "abi3" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py310-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py310-devel

This package contains library source intended for building other packages which
use the "abi3-py310" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py311-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py311-devel

This package contains library source intended for building other packages which
use the "abi3-py311" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py312-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py312-devel

This package contains library source intended for building other packages which
use the "abi3-py312" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py313-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py313-devel

This package contains library source intended for building other packages which
use the "abi3-py313" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py314-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py314-devel

This package contains library source intended for building other packages which
use the "abi3-py314" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py37-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py37-devel

This package contains library source intended for building other packages which
use the "abi3-py37" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py38-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py38-devel

This package contains library source intended for building other packages which
use the "abi3-py38" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py39-devel
Summary:        Build configuration for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py39-devel

This package contains library source intended for building other packages which
use the "abi3-py39" feature of the "%{crate}" crate.

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
%files -n rust-pyo3-build-config0.25-devel -f %{oreon_filedir}/rust-pyo3-build-config0.25-devel.list

%changelog

%autochangelog
