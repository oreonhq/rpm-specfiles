%global source0_hash 025474d3928738efb38ac36d4744a74a400c901c7596199e20e45d98eb194105
%bcond check 1
%global debug_package %{nil}
%global crate pyo3-ffi
Name:           rust-pyo3-ffi0.26
Version:        0.26.0
Release:        1%{?dist}
Summary:        Python-API bindings for the PyO3 ecosystem
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3-ffi
Source0:        https://static.crates.io/crates/pyo3-ffi/pyo3-ffi-%{version}.crate
Patch2:         Allow-unsupported-Python-versions-in-RPM-builds.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.7
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-devel

This package contains library source intended for building other packages which
use the "abi3" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py310-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py310-devel

This package contains library source intended for building other packages which
use the "abi3-py310" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py311-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py311-devel

This package contains library source intended for building other packages which
use the "abi3-py311" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py312-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py312-devel

This package contains library source intended for building other packages which
use the "abi3-py312" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py313-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py313-devel

This package contains library source intended for building other packages which
use the "abi3-py313" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py314-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py314-devel

This package contains library source intended for building other packages which
use the "abi3-py314" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py37-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py37-devel

This package contains library source intended for building other packages which
use the "abi3-py37" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py38-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py38-devel

This package contains library source intended for building other packages which
use the "abi3-py38" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py39-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+abi3-py39-devel

This package contains library source intended for building other packages which
use the "abi3-py39" feature of the "%{crate}" crate.

%package     -n %{name}+extension-module-devel
Summary:        Python-API bindings for the PyO3 ecosystem
BuildArch:      noarch
%description -n %{name}+extension-module-devel

This package contains library source intended for building other packages which
use the "extension-module" feature of the "%{crate}" crate.

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
%files -n rust-pyo3-ffi0.26-devel -f %{oreon_filedir}/rust-pyo3-ffi0.26-devel.list

%changelog

%autochangelog
