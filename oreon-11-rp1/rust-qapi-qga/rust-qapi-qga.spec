%global source1_hash 92d82b247046525130b278df9c1d3d985f78cce81eb93722bd3d9dd9094185c2
%global source0_hash 2945a1829999b7e600b98c8326615ece10df20bc9e9ab12ec057a6aa29b7317d
%bcond check 1
%global debug_package %{nil}
%global crate qapi-qga
Name:           rust-qapi-qga
Version:        0.13.0
Release:        1%{?dist}
Summary:        QEMU Guest Agent protocol types
License:        MIT AND GPL-2.0-or-later
URL:            https://crates.io/crates/qapi-qga
Source0:        https://static.crates.io/crates/qapi-qga/qapi-qga-%{version}.crate
Source1:        https://raw.githubusercontent.com/arcnmx/qapi-rs/refs/heads/main/COPYING
Source2:        COPYING.GPLv2
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
Summary:        QEMU Guest Agent protocol types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
cp -pav %{SOURCE2} .
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
%files -n rust-qapi-qga-devel -f %{oreon_filedir}/rust-qapi-qga-devel.list

%changelog

%autochangelog
