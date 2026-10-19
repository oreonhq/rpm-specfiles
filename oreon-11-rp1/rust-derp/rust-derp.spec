%global source0_hash 071e692e5a98cc563dd1ccb9fcc1a019c92717d88d7bae0d88d7d0ca2b8e1e0c
%bcond check 1
%global debug_package %{nil}
%global crate derp
Name:           rust-derp
Version:        0.0.15
Release:        1%{?dist}
Summary:        DER Parser (and Writer)
License:        ISC
URL:            https://crates.io/crates/derp
Source0:        https://static.crates.io/crates/derp/derp-%{version}.crate
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
Summary:        DER Parser (and Writer)
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
%files -n rust-derp-devel -f %{oreon_filedir}/rust-derp-devel.list

%changelog

%autochangelog
