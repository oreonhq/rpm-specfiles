%global source0_hash 4d9d9089bb0ce62f4b5d52a0be0f4acfb35738b979380670d3dea85fe38d6ddd
%bcond check 0
%global debug_package %{nil}
%global crate postgres-derive
Name:           rust-postgres-derive
Version:        0.4.9
Release:        1%{?dist}
Summary:        An internal crate used by postgres-types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/postgres-derive
Source0:        https://static.crates.io/crates/postgres-derive/postgres-derive-%{version}.crate
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
Summary:        An internal crate used by postgres-types
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
%files -n rust-postgres-derive-devel -f %{oreon_filedir}/rust-postgres-derive-devel.list

%changelog

%autochangelog
