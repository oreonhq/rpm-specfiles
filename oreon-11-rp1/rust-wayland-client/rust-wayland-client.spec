%global source0_hash b8e6faa537fbb6c186cb9f1d41f2f811a4120d1b57ec61f50da451a0c5122bec
%bcond check 1
%global debug_package %{nil}
%global crate wayland-client
Name:           rust-wayland-client
Version:        0.31.12
Release:        1%{?dist}
Summary:        Bindings to the standard C implementation of the wayland protocol, client side
License:        MIT
URL:            https://crates.io/crates/wayland-client
Source0:        https://static.crates.io/crates/wayland-client/wayland-client-%{version}.crate
Patch:          wayland-client-fix-metadata.diff
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
Summary:        Bindings to the standard C implementation of the wayland protocol, client side
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Bindings to the standard C implementation of the wayland protocol, client side
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

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
%files -n rust-wayland-client-devel -f %{oreon_filedir}/rust-wayland-client-devel.list

%changelog

%autochangelog
