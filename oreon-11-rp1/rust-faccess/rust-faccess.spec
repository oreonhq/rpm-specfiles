%global source0_hash 59ae66425802d6a903e268ae1a08b8c38ba143520f227a205edf4e9c7e3e26d5
%bcond check 0
%global debug_package %{nil}
%global crate faccess
Name:           rust-faccess
Version:        0.2.4
Release:        1%{?dist}
Summary:        Simple file accessibility checks
License:        MIT
URL:            https://crates.io/crates/faccess
Source0:        https://static.crates.io/crates/faccess/faccess-%{version}.crate
Patch:          faccess-fix-metadata-auto.diff
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
Summary:        Simple file accessibility checks
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
%files -n rust-faccess-devel -f %{oreon_filedir}/rust-faccess-devel.list

%changelog

%autochangelog
