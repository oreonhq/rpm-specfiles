%global source0_hash 290f856f96eeca6f3686ac9704824bf5c84b5c1b58bdbf89708f622b3a44978a
%bcond check 0
%global debug_package %{nil}
%global crate sval_test
Name:           rust-sval_test
Version:        2.20.0
Release:        1%{?dist}
Summary:        Utilities for testing sval::Value implementations
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sval_test
Source0:        https://static.crates.io/crates/sval_test/sval_test-%{version}.crate
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
Summary:        Utilities for testing sval::Value implementations
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
%files -n rust-sval_test-devel -f %{oreon_filedir}/rust-sval_test-devel.list

%changelog

%autochangelog
