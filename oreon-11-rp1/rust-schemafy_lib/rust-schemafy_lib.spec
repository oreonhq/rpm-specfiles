%global source0_hash af3d87f1df246a9b7e2bfd1f4ee5f88e48b11ef9cfc62e63f0dead255b1a6f5f
%bcond check 0
%global debug_package %{nil}
%global crate schemafy_lib
Name:           rust-schemafy_lib
Version:        0.6.0
Release:        1%{?dist}
Summary:        Generates serializeable Rust types from a json schema
License:        MIT
URL:            https://crates.io/crates/schemafy_lib
Source0:        https://static.crates.io/crates/schemafy_lib/schemafy_lib-%{version}.crate
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
Summary:        Generates serializeable Rust types from a json schema
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
%files -n rust-schemafy_lib-devel -f %{oreon_filedir}/rust-schemafy_lib-devel.list

%changelog

%autochangelog
