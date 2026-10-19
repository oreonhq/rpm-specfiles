%global source0_hash dd122633e4bef06db27737f21d3738fb89c8f6d5360d6d9d7635dda142a7757e
%bcond check 0
%global debug_package %{nil}
%global crate dsl_auto_type
Name:           rust-dsl_auto_type
Version:        0.2.0
Release:        1%{?dist}
Summary:        Automatically expand query fragment types for factoring as functions
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dsl_auto_type
Source0:        https://static.crates.io/crates/dsl_auto_type/dsl_auto_type-%{version}.crate
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
Summary:        Automatically expand query fragment types for factoring as functions
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
%files -n rust-dsl_auto_type-devel -f %{oreon_filedir}/rust-dsl_auto_type-devel.list

%changelog

%autochangelog
