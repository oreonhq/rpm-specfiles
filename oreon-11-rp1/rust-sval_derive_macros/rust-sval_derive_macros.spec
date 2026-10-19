%global source0_hash 9aad212d014dac439257cc7417810f10d629b4f36c6bb68f69260c29b8f62cd5
%bcond check 0
%global debug_package %{nil}
%global crate sval_derive_macros
Name:           rust-sval_derive_macros
Version:        2.20.0
Release:        1%{?dist}
Summary:        Minimal derive support for `sval`
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sval_derive_macros
Source0:        https://static.crates.io/crates/sval_derive_macros/sval_derive_macros-%{version}.crate
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

%package     -n %{name}+flatten-devel
Summary:        Minimal derive support for `sval`
BuildArch:      noarch
%description -n %{name}+flatten-devel

This package contains library source intended for building other packages which
use the "flatten" feature of the "%{crate}" crate.

%package     -n %{name}+ref-devel
Summary:        Minimal derive support for `sval`
BuildArch:      noarch
%description -n %{name}+ref-devel

This package contains library source intended for building other packages which
use the "ref" feature of the "%{crate}" crate.

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
%files -n rust-sval_derive_macros-devel -f %{oreon_filedir}/rust-sval_derive_macros-devel.list

%changelog

%autochangelog
