%global source0_hash 77739c880e00693faef3d65ea3aad725f196da38b22fdc7ea6ded6e1ce4d3add
%bcond check 0
%global debug_package %{nil}
%global crate typed-builder
Name:           rust-typed-builder
Version:        0.18.2
Release:        1%{?dist}
Summary:        Compile-time type-checked builder derive
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/typed-builder
Source0:        https://static.crates.io/crates/typed-builder/typed-builder-%{version}.crate
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
Summary:        Compile-time type-checked builder derive
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
%files -n rust-typed-builder-devel -f %{oreon_filedir}/rust-typed-builder-devel.list

%changelog

%autochangelog
