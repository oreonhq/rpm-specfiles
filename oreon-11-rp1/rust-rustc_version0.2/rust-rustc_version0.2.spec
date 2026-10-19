%global source0_hash 138e3e0acb6c9fb258b19b67cb8abd63c00679d2851805ea151465464fe9030a
%bcond check 1
%global debug_package %{nil}
%global crate rustc_version
Name:           rust-rustc_version0.2
Version:        0.2.3
Release:        1%{?dist}
Summary:        Library for querying the version of a installed rustc compiler
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustc_version
Source0:        https://static.crates.io/crates/rustc_version/rustc_version-%{version}.crate
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
Summary:        Library for querying the version of a installed rustc compiler
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
%files -n rust-rustc_version0.2-devel -f %{oreon_filedir}/rust-rustc_version0.2-devel.list

%changelog

%autochangelog
