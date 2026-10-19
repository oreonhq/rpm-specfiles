%global source0_hash 69c376a9b84afdf97bddd2628096cf3554208b2a676cf06b4532e0f433a54e02
%bcond check 1
%global debug_package %{nil}
%global crate vm-superio
Name:           rust-vm-superio
Version:        0.8.1
Release:        1%{?dist}
Summary:        Emulation for legacy devices
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/vm-superio
Source0:        https://static.crates.io/crates/vm-superio/vm-superio-%{version}.crate
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
Summary:        Emulation for legacy devices
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
%files -n rust-vm-superio-devel -f %{oreon_filedir}/rust-vm-superio-devel.list

%changelog

%autochangelog
