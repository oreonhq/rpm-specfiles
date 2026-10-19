%global source0_hash e9597cdf02cf0c34cd5823786dce6b5ae8598f05c2daf5621b6e178d4f7345f3
%bcond check 1
%global debug_package %{nil}
%global crate wayland-protocols-wlr
Name:           rust-wayland-protocols-wlr
Version:        0.3.10
Release:        1%{?dist}
Summary:        Generated API for the WLR wayland protocol extensions
License:        MIT AND HPND-sell-variant
URL:            https://crates.io/crates/wayland-protocols-wlr
Source0:        https://static.crates.io/crates/wayland-protocols-wlr/wayland-protocols-wlr-%{version}.crate
Patch:          wayland-protocols-wlr-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       bundled(wlr-protocols) = 0^20250816gita741f0a
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Generated API for the WLR wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+client-devel
Summary:        Generated API for the WLR wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+client-devel

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        Generated API for the WLR wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-client-devel
Summary:        Generated API for the WLR wayland protocol extensions
BuildArch:      noarch
%description -n %{name}+wayland-client-devel

This package contains library source intended for building other packages which
use the "wayland-client" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-server-devel
Summary:        Generated API for the WLR wayland protocol extensions
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
%files -n rust-wayland-protocols-wlr-devel -f %{oreon_filedir}/rust-wayland-protocols-wlr-devel.list

%changelog

%autochangelog
