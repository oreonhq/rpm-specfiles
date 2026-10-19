%global source0_hash a84b605a2453f2096645b2bc81182e9df2a9a5f6c6f8927ad9141521c5f1d9f4
%bcond check 0
%global debug_package %{nil}
%global crate ossl-sys
Name:           rust-ossl-sys
Version:        1.5.2
Release:        1%{?dist}
Summary:        Low-level OpenSSL version 3+ bindings
License:        Apache-2.0
URL:            https://crates.io/crates/ossl-sys
Source0:        https://static.crates.io/crates/ossl-sys/ossl-sys-%{version}.crate
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

%package     -n %{name}+dynamic-devel
Summary:        Low-level OpenSSL version 3+ bindings
BuildArch:      noarch
%description -n %{name}+dynamic-devel

This package contains library source intended for building other packages which
use the "dynamic" feature of the "%{crate}" crate.

%package     -n %{name}+fips-devel
Summary:        Low-level OpenSSL version 3+ bindings
BuildArch:      noarch
%description -n %{name}+fips-devel

This package contains library source intended for building other packages which
use the "fips" feature of the "%{crate}" crate.

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
%files -n rust-ossl-sys-devel -f %{oreon_filedir}/rust-ossl-sys-devel.list

%changelog

%autochangelog
