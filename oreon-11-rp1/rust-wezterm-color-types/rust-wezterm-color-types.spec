%global source0_hash 7de81ef35c9010270d63772bebef2f2d6d1f2d20a983d27505ac850b8c4b4296
%bcond check 0
%global debug_package %{nil}
%global crate wezterm-color-types
Name:           rust-wezterm-color-types
Version:        0.3.0
Release:        1%{?dist}
Summary:        Types for working with colors
License:        MIT
URL:            https://crates.io/crates/wezterm-color-types
Source0:        https://static.crates.io/crates/wezterm-color-types/wezterm-color-types-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        Types for working with colors
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+use_serde-devel
Summary:        Types for working with colors
BuildArch:      noarch
%description -n %{name}+use_serde-devel

This package contains library source intended for building other packages which
use the "use_serde" feature of the "%{crate}" crate.

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
%files -n rust-wezterm-color-types-devel -f %{oreon_filedir}/rust-wezterm-color-types-devel.list

%changelog

%autochangelog
