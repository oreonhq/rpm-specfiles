%global source0_hash 7d4643d3d4db6b08741050c2f3afa9a892c4244c085a72fcda93c9c2c9a00f4b
%bcond check 0
%global debug_package %{nil}
%global crate pnet_sys
Name:           rust-pnet_sys
Version:        0.35.0
Release:        1%{?dist}
Summary:        Access to network related system function and calls.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pnet_sys
Source0:        https://static.crates.io/crates/pnet_sys/pnet_sys-%{version}.crate
Patch:          pnet_sys-fix-metadata-auto.diff
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
Summary:        Access to network related system function and calls.
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
%files -n rust-pnet_sys-devel -f %{oreon_filedir}/rust-pnet_sys-devel.list

%changelog

%autochangelog
