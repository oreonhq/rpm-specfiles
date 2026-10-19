%global source0_hash bad9c72e7ca2137e0dc3813245a0d282fd6daad32fd800af018306a9169b5fe8
%bcond check 0
%global debug_package %{nil}
%global crate defmt-macros
Name:           rust-defmt-macros
Version:        1.1.1
Release:        1%{?dist}
Summary:        defmt macros
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/defmt-macros
Source0:        https://static.crates.io/crates/defmt-macros/defmt-macros-%{version}.crate
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

%package     -n %{name}+unstable-test-devel
Summary:        defmt macros
BuildArch:      noarch
%description -n %{name}+unstable-test-devel

This package contains library source intended for building other packages which
use the "unstable-test" feature of the "%{crate}" crate.

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
%files -n rust-defmt-macros-devel -f %{oreon_filedir}/rust-defmt-macros-devel.list

%changelog

%autochangelog
