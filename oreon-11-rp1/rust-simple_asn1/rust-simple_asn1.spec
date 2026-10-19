%global source0_hash 0d585997b0ac10be3c5ee635f1bab02d512760d14b7c468801ac8a01d9ae5f1d
%bcond check 1
%global debug_package %{nil}
%global crate simple_asn1
Name:           rust-simple_asn1
Version:        0.6.4
Release:        1%{?dist}
Summary:        Simple DER/ASN.1 encoding/decoding library
License:        ISC
URL:            https://crates.io/crates/simple_asn1
Source0:        https://static.crates.io/crates/simple_asn1/simple_asn1-%{version}.crate
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
Summary:        Simple DER/ASN.1 encoding/decoding library
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
%files -n rust-simple_asn1-devel -f %{oreon_filedir}/rust-simple_asn1-devel.list

%changelog

%autochangelog
