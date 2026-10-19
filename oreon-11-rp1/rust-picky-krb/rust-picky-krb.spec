%global source0_hash 1e78a55491723b0a10bc2c02709a8d92d74ef674fe1b569cb4a08bac3d105487
%bcond check 1
%global debug_package %{nil}
%global crate picky-krb
Name:           rust-picky-krb
Version:        0.11.1
Release:        1%{?dist}
Summary:        Encode/decode Kerberos ASN.1 DER structs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/picky-krb
Source0:        https://static.crates.io/crates/picky-krb/picky-krb-%{version}.crate
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
Summary:        Encode/decode Kerberos ASN.1 DER structs
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
%files -n rust-picky-krb-devel -f %{oreon_filedir}/rust-picky-krb-devel.list

%changelog

%autochangelog
