%global source0_hash 9008cbbba9e1d655538870b91fd93814bd82e6968f27788fc734375120ac6f57
%bcond check 1
%global debug_package %{nil}
%global crate assert2-macros
Name:           rust-assert2-macros
Version:        0.3.16
Release:        1%{?dist}
Summary:        Procedural macros for assert2
License:        BSD-2-Clause
URL:            https://crates.io/crates/assert2-macros
Source0:        https://static.crates.io/crates/assert2-macros/assert2-macros-%{version}.crate
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
Summary:        Procedural macros for assert2
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
%files -n rust-assert2-macros-devel -f %{oreon_filedir}/rust-assert2-macros-devel.list

%changelog

%autochangelog
