%global source0_hash 96ebdbf0e4b175884aa587fcf551c16dabe245ea04235abdd8cbbd160b27ed5a
%bcond check 0
%global debug_package %{nil}
%global crate sval_fmt
Name:           rust-sval_fmt
Version:        2.20.0
Release:        1%{?dist}
Summary:        Integration between std::fmt::Debug and sval::Value
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sval_fmt
Source0:        https://static.crates.io/crates/sval_fmt/sval_fmt-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Integration between std::fmt::Debug and sval::Value
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Integration between std::fmt::Debug and sval::Value
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-sval_fmt-devel -f %{oreon_filedir}/rust-sval_fmt-devel.list

%changelog

%autochangelog
