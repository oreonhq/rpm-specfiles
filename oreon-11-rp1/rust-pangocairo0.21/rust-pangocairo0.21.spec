%global source0_hash b36c5c84304072939d860595d9bda2a797d3bd6f7215e20b8ccd0e72d84da8c8
%bcond check 1
%global debug_package %{nil}
%global crate pangocairo
Name:           rust-pangocairo0.21
Version:        0.21.5
Release:        1%{?dist}
Summary:        Rust bindings for the PangoCairo library
License:        MIT
URL:            https://crates.io/crates/pangocairo
Source0:        https://static.crates.io/crates/pangocairo/pangocairo-%{version}.crate
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
Summary:        Rust bindings for the PangoCairo library
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
%files -n rust-pangocairo0.21-devel -f %{oreon_filedir}/rust-pangocairo0.21-devel.list

%changelog

%autochangelog
