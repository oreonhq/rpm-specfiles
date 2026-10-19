%global source0_hash 1cb1d1f4e7328a563286d459cf348988e04df64bcff2057cef9b910a0d5950f8
%bcond check 0
%global debug_package %{nil}
%global crate assert-eq-float
Name:           rust-assert-eq-float
Version:        0.1.4
Release:        1%{?dist}
Summary:        Assert_eq_float! macros that support floats
License:        MIT
URL:            https://crates.io/crates/assert-eq-float
Source0:        https://static.crates.io/crates/assert-eq-float/assert-eq-float-%{version}.crate
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
Summary:        Assert_eq_float! macros that support floats
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
%files -n rust-assert-eq-float-devel -f %{oreon_filedir}/rust-assert-eq-float-devel.list

%changelog

%autochangelog
