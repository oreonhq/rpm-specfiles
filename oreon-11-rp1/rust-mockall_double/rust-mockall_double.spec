%global source0_hash f1ca96e5ac35256ae3e13536edd39b172b88f41615e1d7b653c8ad24524113e8
%bcond check 0
%global debug_package %{nil}
%global crate mockall_double
Name:           rust-mockall_double
Version:        0.3.1
Release:        1%{?dist}
Summary:        Test double adapter for Mockall
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/mockall_double
Source0:        https://static.crates.io/crates/mockall_double/mockall_double-%{version}.crate
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
Summary:        Test double adapter for Mockall
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
%files -n rust-mockall_double-devel -f %{oreon_filedir}/rust-mockall_double-devel.list

%changelog

%autochangelog
