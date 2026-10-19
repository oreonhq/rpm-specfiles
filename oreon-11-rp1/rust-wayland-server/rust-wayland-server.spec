%global source0_hash 9297ab90f8d1f597711d36455c5b1b2290eca59b8134485e377a296b80b118c9
%bcond check 1
%global debug_package %{nil}
%global crate wayland-server
Name:           rust-wayland-server
Version:        0.31.11
Release:        1%{?dist}
Summary:        Bindings to the standard C implementation of the wayland protocol, server side
License:        MIT
URL:            https://crates.io/crates/wayland-server
Source0:        https://static.crates.io/crates/wayland-server/wayland-server-%{version}.crate
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
Summary:        Bindings to the standard C implementation of the wayland protocol, server side
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Bindings to the standard C implementation of the wayland protocol, server side
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
%files -n rust-wayland-server-devel -f %{oreon_filedir}/rust-wayland-server-devel.list

%changelog

%autochangelog
