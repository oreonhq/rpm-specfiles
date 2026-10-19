%global source101_hash 23f18e03dc49df91622fe2a76176497404e46ced8a715d9d2b67a7446571cca3
%global source100_hash 62c7a1e35f56406896d7aa7ca52d0cc0d272ac022b5d2796e7d6905db8a3636a
%global source0_hash dc19eb2373ccf3d1999967c26c3d44534ff71ae5d8b9dacf78f4b13132229e48
%bcond check 0
%global debug_package %{nil}
%global crate tracker-macros
Name:           rust-tracker-macros
Version:        0.2.2
Release:        1%{?dist}
Summary:        Macros for the tracker crate
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/tracker-macros
Source0:        https://static.crates.io/crates/tracker-macros/tracker-macros-%{version}.crate
Source100:      https://raw.githubusercontent.com/AaronErhardt/Tracker/main/LICENSE-APACHE
Source101:      https://raw.githubusercontent.com/AaronErhardt/Tracker/main/LICENSE-MIT
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
Summary:        Macros for the tracker crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE100} %{SOURCE101} .
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
%files -n rust-tracker-macros-devel -f %{oreon_filedir}/rust-tracker-macros-devel.list

%changelog

%autochangelog
