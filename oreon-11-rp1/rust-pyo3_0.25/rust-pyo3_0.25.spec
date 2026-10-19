%global source0_hash 4688ddedf473e32662b9b067670129a8afb8c18e351482c70d62ba4a88171e8b
%bcond check 1
%global debug_package %{nil}
%global crate pyo3
Name:           rust-pyo3_0.25
Version:        0.29.2
Release:        1%{?dist}
Summary:        Bindings to Python interpreter
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3
Source0:        https://static.crates.io/crates/pyo3/pyo3-%{version}.crate
Patch:          pyo3-fix-metadata-auto.diff
Patch:          pyo3-fix-metadata.diff
Patch2:         0001-Make-unsafe-subinterpreter-support-available-via-cfg.patch
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
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+abi3-devel

This package contains library source intended for building other packages which
use the "abi3" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py310-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+abi3-py310-devel

This package contains library source intended for building other packages which
use the "abi3-py310" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py311-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+abi3-py311-devel

This package contains library source intended for building other packages which
use the "abi3-py311" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py312-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+abi3-py312-devel

This package contains library source intended for building other packages which
use the "abi3-py312" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py313-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+abi3-py313-devel

This package contains library source intended for building other packages which
use the "abi3-py313" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py314-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+abi3-py314-devel

This package contains library source intended for building other packages which
use the "abi3-py314" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py37-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+abi3-py37-devel

This package contains library source intended for building other packages which
use the "abi3-py37" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py38-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+abi3-py38-devel

This package contains library source intended for building other packages which
use the "abi3-py38" feature of the "%{crate}" crate.

%package     -n %{name}+abi3-py39-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+abi3-py39-devel

This package contains library source intended for building other packages which
use the "abi3-py39" feature of the "%{crate}" crate.

%package     -n %{name}+anyhow-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+anyhow-devel

This package contains library source intended for building other packages which
use the "anyhow" feature of the "%{crate}" crate.

%package     -n %{name}+arc_lock-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+arc_lock-devel

This package contains library source intended for building other packages which
use the "arc_lock" feature of the "%{crate}" crate.

%package     -n %{name}+auto-initialize-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+auto-initialize-devel

This package contains library source intended for building other packages which
use the "auto-initialize" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-local-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+chrono-local-devel

This package contains library source intended for building other packages which
use the "chrono-local" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-tz-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+chrono-tz-devel

This package contains library source intended for building other packages which
use the "chrono-tz" feature of the "%{crate}" crate.

%package     -n %{name}+either-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+either-devel

This package contains library source intended for building other packages which
use the "either" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-async-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+experimental-async-devel

This package contains library source intended for building other packages which
use the "experimental-async" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-inspect-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+experimental-inspect-devel

This package contains library source intended for building other packages which
use the "experimental-inspect" feature of the "%{crate}" crate.

%package     -n %{name}+extension-module-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+extension-module-devel

This package contains library source intended for building other packages which
use the "extension-module" feature of the "%{crate}" crate.

%package     -n %{name}+eyre-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+eyre-devel

This package contains library source intended for building other packages which
use the "eyre" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+indoc-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+indoc-devel

This package contains library source intended for building other packages which
use the "indoc" feature of the "%{crate}" crate.

%package     -n %{name}+inventory-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+inventory-devel

This package contains library source intended for building other packages which
use the "inventory" feature of the "%{crate}" crate.

%package     -n %{name}+jiff-02-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+jiff-02-devel

This package contains library source intended for building other packages which
use the "jiff-02" feature of the "%{crate}" crate.

%package     -n %{name}+lock_api-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+lock_api-devel

This package contains library source intended for building other packages which
use the "lock_api" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+multiple-pymethods-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+multiple-pymethods-devel

This package contains library source intended for building other packages which
use the "multiple-pymethods" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+num-complex-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+num-complex-devel

This package contains library source intended for building other packages which
use the "num-complex" feature of the "%{crate}" crate.

%package     -n %{name}+num-rational-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+num-rational-devel

This package contains library source intended for building other packages which
use the "num-rational" feature of the "%{crate}" crate.

%package     -n %{name}+ordered-float-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+ordered-float-devel

This package contains library source intended for building other packages which
use the "ordered-float" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+py-clone-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+py-clone-devel

This package contains library source intended for building other packages which
use the "py-clone" feature of the "%{crate}" crate.

%package     -n %{name}+pyo3-macros-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+pyo3-macros-devel

This package contains library source intended for building other packages which
use the "pyo3-macros" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+unindent-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+unindent-devel

This package contains library source intended for building other packages which
use the "unindent" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Bindings to Python interpreter
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -r emscripten/ newsfragments/
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

export LANG=C.utf8
%cargo_test -f auto-initialize,full
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-pyo3_0.25-devel -f %{oreon_filedir}/rust-pyo3_0.25-devel.list

%changelog

%autochangelog
