%global source0_hash 59600e2c2d636fde9b65e99cc6445ac770c63d3628195ff39932b8d6d7409903
%bcond check 0
%global debug_package %{nil}
%global crate der_derive
Name:           rust-der_derive
Version:        0.8.0
Release:        1%{?dist}
Summary:        Custom derive support for the `der` crate's `Choice` and `Sequence` t...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/der_derive
Source0:        https://static.crates.io/crates/der_derive/der_derive-%{version}.crate
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
Summary:        Custom derive support for the `der` crate's `Choice` and `Sequence` t...
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
%files -n rust-der_derive-devel -f %{oreon_filedir}/rust-der_derive-devel.list

%changelog

%autochangelog
