%global source0_hash 0ed0a176c0b8c5c95fa0523177530364c5b68a8895d9745730dbfa692a7412d0
%bcond check 0
%global debug_package %{nil}
%global crate cordic
Name:           rust-cordic
Version:        0.1.5
Release:        1%{?dist}
Summary:        Special functions for fixed-point numbers using the CORDIC method.
License:        BSD-3-Clause
URL:            https://crates.io/crates/cordic
Source0:        https://static.crates.io/crates/cordic/cordic-%{version}.crate
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
Summary:        Special functions for fixed-point numbers using the CORDIC method.
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
%files -n rust-cordic-devel -f %{oreon_filedir}/rust-cordic-devel.list

%changelog

%autochangelog
