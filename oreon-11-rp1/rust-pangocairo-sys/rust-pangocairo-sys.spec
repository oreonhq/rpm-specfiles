%global source0_hash d95cb73468373b9e568abb1afbaf5b42fe6ab9128fc41b5f2adbf69451c3c77f
%bcond check 1
%global debug_package %{nil}
%global crate pangocairo-sys
Name:           rust-pangocairo-sys
Version:        0.22.0
Release:        1%{?dist}
Summary:        FFI bindings to PangoCairo
License:        MIT
URL:            https://crates.io/crates/pangocairo-sys
Source0:        https://static.crates.io/crates/pangocairo-sys/pangocairo-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pangocairo) >= 1.40
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to PangoCairo
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
%files -n rust-pangocairo-sys-devel -f %{oreon_filedir}/rust-pangocairo-sys-devel.list

%changelog

%autochangelog
