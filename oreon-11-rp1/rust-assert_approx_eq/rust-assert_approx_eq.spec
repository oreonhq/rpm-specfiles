%global source0_hash 3c07dab4369547dbe5114677b33fbbf724971019f3818172d59a97a61c774ffd
%bcond check 0
%global debug_package %{nil}
%global crate assert_approx_eq
Name:           rust-assert_approx_eq
Version:        1.1.0
Release:        1%{?dist}
Summary:        Assert approximately equal
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/assert_approx_eq
Source0:        https://static.crates.io/crates/assert_approx_eq/assert_approx_eq-%{version}.crate
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
Summary:        Assert approximately equal
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
%files -n rust-assert_approx_eq-devel -f %{oreon_filedir}/rust-assert_approx_eq-devel.list

%changelog

%autochangelog
