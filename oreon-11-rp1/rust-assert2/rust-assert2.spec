%global source0_hash 0d6c710e60d14b07d8f42d0e702b16120865eea39edb751e75cd6bf401d18f14
%bcond check 1
%global debug_package %{nil}
%global crate assert2
Name:           rust-assert2
Version:        0.3.16
Release:        1%{?dist}
Summary:        Assert!(...) and check!(...) macros inspired by Catch2, now with diffs!
License:        BSD-2-Clause
URL:            https://crates.io/crates/assert2
Source0:        https://static.crates.io/crates/assert2/assert2-%{version}.crate
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
Summary:        Assert!(...) and check!(...) macros inspired by Catch2, now with diffs!
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
%files -n rust-assert2-devel -f %{oreon_filedir}/rust-assert2-devel.list

%changelog

%autochangelog
