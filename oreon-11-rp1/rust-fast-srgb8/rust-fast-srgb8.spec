%global source0_hash dd2e7510819d6fbf51a5545c8f922716ecfb14df168a3242f7d33e0239efe6a1
%bcond check 0
%global debug_package %{nil}
%global crate fast-srgb8
Name:           rust-fast-srgb8
Version:        1.0.0
Release:        1%{?dist}
Summary:        Very fast conversions between linear float and 8-bit sRGB (with no_st...
License:        MIT OR Apache-2.0 OR CC0-1.0
URL:            https://crates.io/crates/fast-srgb8
Source0:        https://static.crates.io/crates/fast-srgb8/fast-srgb8-%{version}.crate
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
Summary:        Very fast conversions between linear float and 8-bit sRGB (with no_st...
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
%files -n rust-fast-srgb8-devel -f %{oreon_filedir}/rust-fast-srgb8-devel.list

%changelog

%autochangelog
