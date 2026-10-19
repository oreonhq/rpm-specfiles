%global source0_hash 5f2ab60e120fd6eaa68d9567f3226e876684639d22a4219b313ff69ec0ccd5ac
%bcond check 0
%global debug_package %{nil}
%global crate wezterm-dynamic
Name:           rust-wezterm-dynamic
Version:        0.2.1
Release:        1%{?dist}
Summary:        config serialization for wezterm via dynamic json-like data values
License:        MIT
URL:            https://crates.io/crates/wezterm-dynamic
Source0:        https://static.crates.io/crates/wezterm-dynamic/wezterm-dynamic-%{version}.crate
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
Summary:        config serialization for wezterm via dynamic json-like data values
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
%files -n rust-wezterm-dynamic-devel -f %{oreon_filedir}/rust-wezterm-dynamic-devel.list

%changelog

%autochangelog
