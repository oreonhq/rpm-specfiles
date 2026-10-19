%global source0_hash 08db1edfb05d9b3c1542e521aea074442088292f00b5f28e435c714a98f85031
%bcond check 1
%global debug_package %{nil}
%global crate wiremock
Name:           rust-wiremock
Version:        0.6.5
Release:        1%{?dist}
Summary:        HTTP mocking to test Rust applications
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/wiremock
Source0:        https://static.crates.io/crates/wiremock/wiremock-%{version}.crate
Patch:          wiremock-fix-metadata.diff
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
Summary:        HTTP mocking to test Rust applications
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

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-wiremock-devel -f %{oreon_filedir}/rust-wiremock-devel.list

%changelog

%autochangelog
