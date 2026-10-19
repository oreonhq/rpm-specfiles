%global source0_hash 37d53ac171c92a39e4769491c4b4dde7022c60042254b5fc044ae409d34a24d4
%bcond check 0
%global debug_package %{nil}
%global crate test-log
Name:           rust-test-log
Version:        0.2.19
Release:        1%{?dist}
Summary:        Attribute for initializing logging and/or tracing before running tests
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/test-log
Source0:        https://static.crates.io/crates/test-log/test-log-%{version}.crate
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
Summary:        Attribute for initializing logging and/or tracing before running tests
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        Attribute for initializing logging and/or tracing before running tests
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Attribute for initializing logging and/or tracing before running tests
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+trace-devel
Summary:        Attribute for initializing logging and/or tracing before running tests
BuildArch:      noarch
%description -n %{name}+trace-devel

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Attribute for initializing logging and/or tracing before running tests
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-test-log-devel -f %{oreon_filedir}/rust-test-log-devel.list

%changelog

%autochangelog
