%global source0_hash a2658621297f2cf68762a6f7dc0bb7e1ff2cfd6583daef8ee0fed6f7ec468ec0
%bcond check 0
%global debug_package %{nil}
%global crate derive_builder
Name:           rust-derive_builder0.9
Version:        0.9.0
Release:        1%{?dist}
Summary:        Rust macro to automatically implement the builder pattern for arbitra...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/derive_builder
Source0:        https://static.crates.io/crates/derive_builder/derive_builder-%{version}.crate
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

%package     -n %{name}+compiletest_rs-devel
Summary:        Rust macro to automatically implement the builder pattern for arbitra...
BuildArch:      noarch
%description -n %{name}+compiletest_rs-devel

This package contains library source intended for building other packages which
use the "compiletest_rs" feature of the "%{crate}" crate.

%package     -n %{name}+env_logger-devel
Summary:        Rust macro to automatically implement the builder pattern for arbitra...
BuildArch:      noarch
%description -n %{name}+env_logger-devel

This package contains library source intended for building other packages which
use the "env_logger" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Rust macro to automatically implement the builder pattern for arbitra...
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Rust macro to automatically implement the builder pattern for arbitra...
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+nightlytests-devel
Summary:        Rust macro to automatically implement the builder pattern for arbitra...
BuildArch:      noarch
%description -n %{name}+nightlytests-devel

This package contains library source intended for building other packages which
use the "nightlytests" feature of the "%{crate}" crate.

%package     -n %{name}+skeptic-devel
Summary:        Rust macro to automatically implement the builder pattern for arbitra...
BuildArch:      noarch
%description -n %{name}+skeptic-devel

This package contains library source intended for building other packages which
use the "skeptic" feature of the "%{crate}" crate.

%package     -n %{name}+skeptic_tests-devel
Summary:        Rust macro to automatically implement the builder pattern for arbitra...
BuildArch:      noarch
%description -n %{name}+skeptic_tests-devel

This package contains library source intended for building other packages which
use the "skeptic_tests" feature of the "%{crate}" crate.

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
%files -n rust-derive_builder0.9-devel -f %{oreon_filedir}/rust-derive_builder0.9-devel.list

%changelog

%autochangelog
