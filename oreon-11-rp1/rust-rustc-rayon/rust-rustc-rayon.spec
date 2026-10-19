%global source0_hash 2cd9fb077db982d7ceb42a90471e5a69a990b58f71e06f0d8340bb2cf35eb751
%bcond check 0
%global debug_package %{nil}
%global crate rustc-rayon
Name:           rust-rustc-rayon
Version:        0.5.1
Release:        1%{?dist}
Summary:        Simple work-stealing parallelism for Rust - fork for rustc
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustc-rayon
Source0:        https://static.crates.io/crates/rustc-rayon/rustc-rayon-%{version}.crate
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

%package     -n %{name}+indexmap-devel
Summary:        Simple work-stealing parallelism for Rust - fork for rustc
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

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
%files -n rust-rustc-rayon-devel -f %{oreon_filedir}/rust-rustc-rayon-devel.list

%changelog

%autochangelog
