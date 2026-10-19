%global source0_hash 8a2c9ef35f3b2e11d5709d8e75dc1e7e064fd8eec5d705d56073fafca85de854
%bcond check 1
%global debug_package %{nil}
%global crate wayland-egl
Name:           rust-wayland-egl
Version:        0.32.9
Release:        1%{?dist}
Summary:        Bindings to libwayland-egl
License:        MIT
URL:            https://crates.io/crates/wayland-egl
Source0:        https://static.crates.io/crates/wayland-egl/wayland-egl-%{version}.crate
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
Summary:        Bindings to libwayland-egl
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
%files -n rust-wayland-egl-devel -f %{oreon_filedir}/rust-wayland-egl-devel.list

%changelog

%autochangelog
