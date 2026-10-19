%global source0_hash c34819042dc3d3971c46c2190835914dfbe0c3c13f61449b2997f4e9722dfa60
%bcond check 0
%global debug_package %{nil}
%global crate interpolate_name
Name:           rust-interpolate_name
Version:        0.2.4
Release:        1%{?dist}
Summary:        Simple procedural macro attribute for repetitive tests
License:        MIT
URL:            https://crates.io/crates/interpolate_name
Source0:        https://static.crates.io/crates/interpolate_name/interpolate_name-%{version}.crate
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
Summary:        Simple procedural macro attribute for repetitive tests
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
%files -n rust-interpolate_name-devel -f %{oreon_filedir}/rust-interpolate_name-devel.list

%changelog

%autochangelog
