%global source0_hash 61c1bbe46f51c63bc08a1fac0ee0c530a77c961613a86ecf828ab1b0ffc6687a
%bcond check 1
%global debug_package %{nil}
%global crate gungraun
Name:           rust-gungraun
Version:        0.17.2
Release:        1%{?dist}
Summary:        High-precision, one-shot and consistent benchmarking framework/harness for Rust
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/gungraun
Source0:        https://static.crates.io/crates/gungraun/gungraun-%{version}.crate
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
Summary:        High-precision, one-shot and consistent benchmarking framework/harness for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+benchmark-devel
Summary:        High-precision, one-shot and consistent benchmarking framework/harness for Rust
BuildArch:      noarch
%description -n %{name}+benchmark-devel

This package contains library source intended for building other packages which
use the "benchmark" feature of the "%{crate}" crate.

%package     -n %{name}+cachegrind-devel
Summary:        High-precision, one-shot and consistent benchmarking framework/harness for Rust
BuildArch:      noarch
%description -n %{name}+cachegrind-devel

This package contains library source intended for building other packages which
use the "cachegrind" feature of the "%{crate}" crate.

%package     -n %{name}+client_requests-devel
Summary:        High-precision, one-shot and consistent benchmarking framework/harness for Rust
BuildArch:      noarch
%description -n %{name}+client_requests-devel

This package contains library source intended for building other packages which
use the "client_requests" feature of the "%{crate}" crate.

%package     -n %{name}+client_requests_defs-devel
Summary:        High-precision, one-shot and consistent benchmarking framework/harness for Rust
BuildArch:      noarch
%description -n %{name}+client_requests_defs-devel

This package contains library source intended for building other packages which
use the "client_requests_defs" feature of the "%{crate}" crate.

%package     -n %{name}+gungraun-runner-devel
Summary:        High-precision, one-shot and consistent benchmarking framework/harness for Rust
BuildArch:      noarch
%description -n %{name}+gungraun-runner-devel

This package contains library source intended for building other packages which
use the "gungraun-runner" feature of the "%{crate}" crate.

%package     -n %{name}+ui_tests-devel
Summary:        High-precision, one-shot and consistent benchmarking framework/harness for Rust
BuildArch:      noarch
%description -n %{name}+ui_tests-devel

This package contains library source intended for building other packages which
use the "ui_tests" feature of the "%{crate}" crate.

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
%files -n rust-gungraun-devel -f %{oreon_filedir}/rust-gungraun-devel.list

%changelog

%autochangelog
