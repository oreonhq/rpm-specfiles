%global source0_hash 1bdcb0d86235d26251ce2c254d9d1e3cd73e7cc49ccfba6d44539781c91a3818
%bcond check 1
%global debug_package %{nil}
%global crate libglycin-gtk4-rebind-sys
Name:           rust-libglycin-gtk4-rebind-sys
Version:        0.2.0
Release:        1%{?dist}
Summary:        FFI bindings for libglycin-gtk4
License:        MIT
URL:            https://crates.io/crates/libglycin-gtk4-rebind-sys
Source0:        https://static.crates.io/crates/%{crate}/%{crate}-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(glycin-gtk4-2)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(glycin-gtk4-2)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings for libglycin-gtk4
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
%files -n rust-libglycin-gtk4-rebind-sys-devel -f %{oreon_filedir}/rust-libglycin-gtk4-rebind-sys-devel.list

%changelog

%autochangelog
