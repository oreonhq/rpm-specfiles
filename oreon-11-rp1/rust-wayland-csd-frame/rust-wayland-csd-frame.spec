%global source0_hash 625c5029dbd43d25e6aa9615e88b829a5cad13b2819c4ae129fdbb7c31ab4c7e
%bcond check 0
%global debug_package %{nil}
%global crate wayland-csd-frame
Name:           rust-wayland-csd-frame
Version:        0.3.0
Release:        1%{?dist}
Summary:        Common trait and types for wayland CSD interop
License:        MIT
URL:            https://crates.io/crates/wayland-csd-frame
Source0:        https://static.crates.io/crates/wayland-csd-frame/wayland-csd-frame-%{version}.crate
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
Summary:        Common trait and types for wayland CSD interop
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
%files -n rust-wayland-csd-frame-devel -f %{oreon_filedir}/rust-wayland-csd-frame-devel.list

%changelog

%autochangelog
