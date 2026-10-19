%global source0_hash 59b9067f2e68f58e110cf8019a268057e3791cf74b0fdb1b3c7c6e49104f44e6
%bcond check 0
%global debug_package %{nil}
%global crate sval_dynamic
Name:           rust-sval_dynamic
Version:        2.20.0
Release:        1%{?dist}
Summary:        Object-safe versions of sval::Stream and sval::Value
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sval_dynamic
Source0:        https://static.crates.io/crates/sval_dynamic/sval_dynamic-%{version}.crate
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
Summary:        Object-safe versions of sval::Stream and sval::Value
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
%files -n rust-sval_dynamic-devel -f %{oreon_filedir}/rust-sval_dynamic-devel.list

%changelog

%autochangelog
