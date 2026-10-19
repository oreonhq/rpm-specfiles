%global source0_hash 575d32d7ec1a9770108c879fc7c47815a80073f96ca07ff9525a94fcede1dd46
%bcond check 0
%global debug_package %{nil}
%global crate rocket_codegen
Name:           rust-rocket_codegen
Version:        0.5.1
Release:        1%{?dist}
Summary:        Procedural macros for the Rocket web framework.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rocket_codegen
Source0:        https://static.crates.io/crates/rocket_codegen/rocket_codegen-%{version}.crate
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
Summary:        Procedural macros for the Rocket web framework.
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
%files -n rust-rocket_codegen-devel -f %{oreon_filedir}/rust-rocket_codegen-devel.list

%changelog

%autochangelog
