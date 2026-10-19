%global source0_hash eed67a952585d509dd0003049b1fc56b982ac665c8299b124b90ea2bdb3134ab
%bcond check 1
%global debug_package %{nil}
%global crate pnet_macros_support
Name:           rust-pnet_macros_support
Version:        0.35.0
Release:        1%{?dist}
Summary:        Support library for libpnet_macros
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pnet_macros_support
Source0:        https://static.crates.io/crates/pnet_macros_support/pnet_macros_support-%{version}.crate
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
Summary:        Support library for libpnet_macros
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
%files -n rust-pnet_macros_support-devel -f %{oreon_filedir}/rust-pnet_macros_support-devel.list

%changelog

%autochangelog
