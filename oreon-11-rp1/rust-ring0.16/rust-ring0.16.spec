%global source0_hash 3053cf52e236a3ed746dfc745aa9cacf1b791d846bdaf412f60a8d7d6e17c8fc
%bcond check 0
%global debug_package %{nil}
%global crate ring
Name:           rust-ring0.16
Version:        0.16.20
Release:        1%{?dist}
Summary:        Safe, fast, small crypto using Rust.
License:        MIT OR Apache-2.0
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
Summary:        Safe, fast, small crypto using Rust.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Safe, fast, small crypto using Rust.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+dev_urandom_fallback-devel
Summary:        Safe, fast, small crypto using Rust.
BuildArch:      noarch
%description -n %{name}+dev_urandom_fallback-devel

This package contains library source intended for building other packages which
use the "dev_urandom_fallback" feature of the "%{crate}" crate.

%package     -n %{name}+internal_benches-devel
Summary:        Safe, fast, small crypto using Rust.
BuildArch:      noarch
%description -n %{name}+internal_benches-devel

This package contains library source intended for building other packages which
use the "internal_benches" feature of the "%{crate}" crate.

%package     -n %{name}+slow_tests-devel
Summary:        Safe, fast, small crypto using Rust.
BuildArch:      noarch
%description -n %{name}+slow_tests-devel

This package contains library source intended for building other packages which
use the "slow_tests" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Safe, fast, small crypto using Rust.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+test_logging-devel
Summary:        Safe, fast, small crypto using Rust.
BuildArch:      noarch
%description -n %{name}+test_logging-devel

This package contains library source intended for building other packages which
use the "test_logging" feature of the "%{crate}" crate.

%package     -n %{name}+wasm32_c-devel
Summary:        Safe, fast, small crypto using Rust.
BuildArch:      noarch
%description -n %{name}+wasm32_c-devel

This package contains library source intended for building other packages which
use the "wasm32_c" feature of the "%{crate}" crate.

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
%files -n rust-ring0.16-devel -f %{oreon_filedir}/rust-ring0.16-devel.list

%changelog

%autochangelog
