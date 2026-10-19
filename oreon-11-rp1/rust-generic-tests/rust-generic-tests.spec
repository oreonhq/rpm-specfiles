%global source0_hash d9ff6d6584f4f6fa911d5e07856abf1a48dc5599b3734f2eaea130f2c3baa989
%bcond check 1
%global debug_package %{nil}
%global crate generic-tests
Name:           rust-generic-tests
Version:        0.1.3
Release:        1%{?dist}
Summary:        Procedural macro to define tests and benchmarks generically
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/generic-tests
Source0:        https://static.crates.io/crates/generic-tests/generic-tests-%{version}.crate
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
Summary:        Procedural macro to define tests and benchmarks generically
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-generic-tests-devel -f %{oreon_filedir}/rust-generic-tests-devel.list

%changelog

%autochangelog
