%global source0_hash fe2444076b48641147115697648dc743c2c00b61adade0f01ce67133c7babe8c
%bcond check 0
%global debug_package %{nil}
%global crate diesel_table_macro_syntax
Name:           rust-diesel_table_macro_syntax
Version:        0.3.0
Release:        1%{?dist}
Summary:        Internal diesel crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/diesel_table_macro_syntax
Source0:        https://static.crates.io/crates/diesel_table_macro_syntax/diesel_table_macro_syntax-%{version}.crate
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
Summary:        Internal diesel crate
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
%files -n rust-diesel_table_macro_syntax-devel -f %{oreon_filedir}/rust-diesel_table_macro_syntax-devel.list

%changelog

%autochangelog
