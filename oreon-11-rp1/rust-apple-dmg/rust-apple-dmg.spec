%global source0_hash 548e20a18d979fc2a6690823070feee65e207c5cf363d0d8aa2bcd02b5dbc5e1
%bcond check 1
%global debug_package %{nil}
%global crate apple-dmg
Name:           rust-apple-dmg
Version:        0.4.0
Release:        1%{?dist}
Summary:        Library for reading and writing dmg images
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/apple-dmg
Source0:        https://static.crates.io/crates/apple-dmg/apple-dmg-%{version}.crate
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
Summary:        Library for reading and writing dmg images
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -r assets
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
%files -n rust-apple-dmg-devel -f %{oreon_filedir}/rust-apple-dmg-devel.list

%changelog

%autochangelog
