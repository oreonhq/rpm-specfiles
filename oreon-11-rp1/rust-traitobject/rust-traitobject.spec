%global source0_hash 04a79e25382e2e852e8da874249358d382ebaf259d0d34e75d8db16a7efabbc7
%bcond check 0
%global debug_package %{nil}
%global crate traitobject
Name:           rust-traitobject
Version:        0.1.1
Release:        1%{?dist}
Summary:        Unsafe helpers for working with raw trait objects.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/traitobject
Source0:        https://static.crates.io/crates/traitobject/traitobject-%{version}.crate
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
Summary:        Unsafe helpers for working with raw trait objects.
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
%files -n rust-traitobject-devel -f %{oreon_filedir}/rust-traitobject-devel.list

%changelog

%autochangelog
