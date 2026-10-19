%global source0_hash f8c6fd2f0b9338b6d298dbcee4b4ec2a6ec2e88dc0a5f6f92d5cecd65afdf445
%bcond check 0
%global debug_package %{nil}
%global crate linreg
Name:           rust-linreg
Version:        0.2.0
Release:        1%{?dist}
Summary:        Calculates linear regresssions of two-dimensional data
License:        MIT
URL:            https://crates.io/crates/linreg
Source0:        https://static.crates.io/crates/linreg/linreg-%{version}.crate
Patch:         linreg-update-displaydoc.patch
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
Summary:        Calculates linear regresssions of two-dimensional data
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
%files -n rust-linreg-devel -f %{oreon_filedir}/rust-linreg-devel.list

%changelog

%autochangelog
