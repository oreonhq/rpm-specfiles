%global source0_hash e01ed3140b2f8d422c68afa1ed2e85d996ea619c988ac834d255db32138655cb
%bcond check 1
%global debug_package %{nil}
%global crate actix-macros
Name:           rust-actix-macros
Version:        0.2.4
Release:        1%{?dist}
Summary:        Macros for Actix system and runtime
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-macros
Source0:        https://static.crates.io/crates/actix-macros/actix-macros-%{version}.crate
Patch:          actix-macros-doctest-ignore.patch
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
Summary:        Macros for Actix system and runtime
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm tests/trybuild.rs
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
%files -n rust-actix-macros-devel -f %{oreon_filedir}/rust-actix-macros-devel.list

%changelog

%autochangelog
