%global source0_hash 909e307f1cc32bb8bccbd98f446e6d1bf03fa30f7b53a4337da7181ad30fa11a
%bcond check 1
%global debug_package %{nil}
%global crate asn1_derive
Name:           rust-asn1_derive
Version:        0.24.1
Release:        1%{?dist}
Summary:        #[derive] support for asn1
License:        BSD-3-Clause
URL:            https://crates.io/crates/asn1_derive
Source0:        https://static.crates.io/crates/asn1_derive/asn1_derive-%{version}.crate
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
Summary:        #[derive] support for asn1
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
%files -n rust-asn1_derive-devel -f %{oreon_filedir}/rust-asn1_derive-devel.list

%changelog

%autochangelog
