%global source0_hash fce5b5fb86b0c57c20c834c1b412fd09c77c8a59b9473f86272709e78874cd1d
%bcond check 0
%global debug_package %{nil}
%global crate cexpr
Name:           rust-cexpr0.3
Version:        0.3.6
Release:        1%{?dist}
Summary:        A C expression parser and evaluator
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/cexpr
Source0:        https://static.crates.io/crates/cexpr/cexpr-%{version}.crate
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
Summary:        A C expression parser and evaluator
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
%files -n rust-cexpr0.3-devel -f %{oreon_filedir}/rust-cexpr0.3-devel.list

%changelog

%autochangelog
