%global source0_hash aa98634619300a535a9a97f338aed9a5ff1e01a461943e8346ff4ae26007306b
%bcond check 1
%global debug_package %{nil}
%global crate wayland-protocols-plasma
Name:           rust-wayland-protocols-plasma
Version:        0.3.10
Release:        1%{?dist}
Summary:        Generated API for the Plasma wayland protocol extensions
License:        MIT AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT-CMU
URL:            https://crates.io/crates/wayland-protocols-plasma
Source0:        https://static.crates.io/crates/wayland-protocols-plasma/wayland-protocols-plasma-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       bundled(plasma-wayland-protocols) = 1.16.0
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Generated API for the Plasma wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+client-devel
Summary:        Generated API for the Plasma wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+client-devel

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        Generated API for the Plasma wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-client-devel
Summary:        Generated API for the Plasma wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+wayland-client-devel

This package contains library source intended for building other packages which
use the "wayland-client" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-server-devel
Summary:        Generated API for the Plasma wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+wayland-server-devel

This package contains library source intended for building other packages which
use the "wayland-server" feature of the "%{crate}" crate.

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
%files -n rust-wayland-protocols-plasma-devel -f %{oreon_filedir}/rust-wayland-protocols-plasma-devel.list

%changelog

%autochangelog
