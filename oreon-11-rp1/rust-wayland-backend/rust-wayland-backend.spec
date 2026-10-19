%global source0_hash 38a91b4eaddff87b1cd1074985e3713da4af2c49742d1b356b2c01670a67a078
%bcond check 0
%global debug_package %{nil}
%global crate wayland-backend
Name:           rust-wayland-backend
Version:        0.3.17
Release:        1%{?dist}
Summary:        Low-level bindings to the Wayland protocol
License:        MIT
URL:            https://crates.io/crates/wayland-backend
Source0:        https://static.crates.io/crates/wayland-backend/wayland-backend-%{version}.crate
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
Summary:        Low-level bindings to the Wayland protocol
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+client_system-devel
Summary:        Low-level bindings to the Wayland protocol
BuildArch:      noarch
%description -n %{name}+client_system-devel

This package contains library source intended for building other packages which
use the "client_system" feature of the "%{crate}" crate.

%package     -n %{name}+dlopen-devel
Summary:        Low-level bindings to the Wayland protocol
BuildArch:      noarch
%description -n %{name}+dlopen-devel

This package contains library source intended for building other packages which
use the "dlopen" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Low-level bindings to the Wayland protocol
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+raw-window-handle-devel
Summary:        Low-level bindings to the Wayland protocol
BuildArch:      noarch
%description -n %{name}+raw-window-handle-devel

This package contains library source intended for building other packages which
use the "raw-window-handle" feature of the "%{crate}" crate.

%package     -n %{name}+rwh_06-devel
Summary:        Low-level bindings to the Wayland protocol
BuildArch:      noarch
%description -n %{name}+rwh_06-devel

This package contains library source intended for building other packages which
use the "rwh_06" feature of the "%{crate}" crate.

%package     -n %{name}+server_system-devel
Summary:        Low-level bindings to the Wayland protocol
BuildArch:      noarch
%description -n %{name}+server_system-devel

This package contains library source intended for building other packages which
use the "server_system" feature of the "%{crate}" crate.

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
%files -n rust-wayland-backend-devel -f %{oreon_filedir}/rust-wayland-backend-devel.list

%changelog

%autochangelog
