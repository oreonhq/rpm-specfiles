%global source0_hash 9462104f987d8d0f6625f0c7764f1c8b890bd1dc8584d8293e031f25c5a0d242
%bcond check 0
%global debug_package %{nil}
%global crate plotlib
Name:           rust-plotlib
Version:        0.5.1
Release:        1%{?dist}
Summary:        Pure Rust plotting library
License:        MIT
URL:            https://crates.io/crates/plotlib
Source0:        https://static.crates.io/crates/plotlib/plotlib-%{version}.crate
Patch:          plotlib-fix-metadata.diff
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
Summary:        Pure Rust plotting library
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
%files -n rust-plotlib-devel -f %{oreon_filedir}/rust-plotlib-devel.list

%changelog

%autochangelog
