%global source0_hash 0c0a6e355560527dd2d1cf7890652f4f09bb3433b6aadade4c9b5ed76de5f3ec
%bcond check 0
%global debug_package %{nil}
%global crate wezterm-bidi
Name:           rust-wezterm-bidi
Version:        0.2.3
Release:        1%{?dist}
Summary:        The Unicode Bidi Algorithm (UBA)
License:        MIT AND Unicode-DFS-2016
URL:            https://crates.io/crates/wezterm-bidi
Source0:        https://static.crates.io/crates/wezterm-bidi/wezterm-bidi-%{version}.crate
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
Summary:        The Unicode Bidi Algorithm (UBA)
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
%files -n rust-wezterm-bidi-devel -f %{oreon_filedir}/rust-wezterm-bidi-devel.list

%changelog

%autochangelog
