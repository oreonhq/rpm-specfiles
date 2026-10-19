%global source0_hash 8f14bc08631933f365bf937d8c2c944d2c43825bbc1fc462cc9b86173a1a8615
%bcond check 0
%global debug_package %{nil}
%global crate nu-color-config
Name:           rust-nu-color-config
Version:        0.115.1
Release:        1%{?dist}
Summary:        Color configuration code used by Nushell
License:        MIT
URL:            https://crates.io/crates/nu-color-config
Source0:        https://static.crates.io/crates/nu-color-config/nu-color-config-%{version}.crate
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
Summary:        Color configuration code used by Nushell
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

%cargo_test -- -- --exact --skip style_computer::test_computable_style_closure_basic --skip style_computer::test_computable_style_closure_errors
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nu-color-config-devel -f %{oreon_filedir}/rust-nu-color-config-devel.list

%changelog

%autochangelog
