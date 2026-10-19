%global source0_hash 4a52d18780be9b1314328a3de5f930b73d2200112e3849ca6cb11822793fb34d
%bcond check 1
%global debug_package %{nil}
%global crate wayland-cursor
Name:           rust-wayland-cursor
Version:        0.31.14
Release:        1%{?dist}
Summary:        Bindings to libwayland-cursor
License:        MIT
URL:            https://crates.io/crates/wayland-cursor
Source0:        https://static.crates.io/crates/wayland-cursor/wayland-cursor-%{version}.crate
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
Summary:        Bindings to libwayland-cursor
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
%files -n rust-wayland-cursor-devel -f %{oreon_filedir}/rust-wayland-cursor-devel.list

%changelog

%autochangelog
