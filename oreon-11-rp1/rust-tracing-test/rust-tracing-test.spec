%global source0_hash 557b891436fe0d5e0e363427fc7f217abf9ccd510d5136549847bdcbcd011d68
%bcond check 0
%global debug_package %{nil}
%global crate tracing-test
Name:           rust-tracing-test
Version:        0.2.5
Release:        1%{?dist}
Summary:        Helpers for easier testing of crates that use tracing
License:        MIT
URL:            https://crates.io/crates/tracing-test
Source0:        https://static.crates.io/crates/tracing-test/tracing-test-%{version}.crate
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
Summary:        Helpers for easier testing of crates that use tracing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no-env-filter-devel
Summary:        Helpers for easier testing of crates that use tracing
BuildArch:      noarch
%description -n %{name}+no-env-filter-devel

This package contains library source intended for building other packages which
use the "no-env-filter" feature of the "%{crate}" crate.

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
%files -n rust-tracing-test-devel -f %{oreon_filedir}/rust-tracing-test-devel.list

%changelog

%autochangelog
