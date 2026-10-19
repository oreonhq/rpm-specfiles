%global source0_hash aefc127fad829eb36edd748660d3ee55490889bc54005cef71d2cd6e25ca2bb2
%bcond check 1
%global debug_package %{nil}
%global crate cool_asserts
Name:           rust-cool_asserts
Version:        2.0.4
Release:        1%{?dist}
Summary:        Collection of useful testing assertions and utilities
License:        MPL-2.0
URL:            https://crates.io/crates/cool_asserts
Source0:        https://static.crates.io/crates/cool_asserts/cool_asserts-%{version}.crate
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
Summary:        Collection of useful testing assertions and utilities
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
%files -n rust-cool_asserts-devel -f %{oreon_filedir}/rust-cool_asserts-devel.list

%changelog

%autochangelog
