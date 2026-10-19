%global source0_hash a4689e6c2294d81e88dc6261c768b63bc4fcdb852be6d1352498b114f61383b7
%bcond check 0
%global debug_package %{nil}
%global crate ring
Name:           rust-ring
Version:        0.17.14
Release:        1%{?dist}
Summary:        An experiment.
License:        Apache-2.0 AND ISC
URL:            https://crates.io/crates/ring
Source0:        https://static.crates.io/crates/ring/ring-%{version}.crate
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
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+dev_urandom_fallback-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+dev_urandom_fallback-devel

This package contains library source intended for building other packages which
use the "dev_urandom_fallback" feature of the "%{crate}" crate.

%package     -n %{name}+less-safe-getrandom-custom-or-rdrand-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+less-safe-getrandom-custom-or-rdrand-devel

This package contains library source intended for building other packages which
use the "less-safe-getrandom-custom-or-rdrand" feature of the "%{crate}" crate.

%package     -n %{name}+less-safe-getrandom-espidf-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+less-safe-getrandom-espidf-devel

This package contains library source intended for building other packages which
use the "less-safe-getrandom-espidf" feature of the "%{crate}" crate.

%package     -n %{name}+slow_tests-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+slow_tests-devel

This package contains library source intended for building other packages which
use the "slow_tests" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+test_logging-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+test_logging-devel

This package contains library source intended for building other packages which
use the "test_logging" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-testing-arm-no-hw-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+unstable-testing-arm-no-hw-devel

This package contains library source intended for building other packages which
use the "unstable-testing-arm-no-hw" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-testing-arm-no-neon-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+unstable-testing-arm-no-neon-devel

This package contains library source intended for building other packages which
use the "unstable-testing-arm-no-neon" feature of the "%{crate}" crate.

%package     -n %{name}+wasm32_unknown_unknown_js-devel
Summary:        An experiment.
BuildArch:      noarch
%description -n %{name}+wasm32_unknown_unknown_js-devel

This package contains library source intended for building other packages which
use the "wasm32_unknown_unknown_js" feature of the "%{crate}" crate.

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
%files -n rust-ring-devel -f %{oreon_filedir}/rust-ring-devel.list

%changelog

%autochangelog
