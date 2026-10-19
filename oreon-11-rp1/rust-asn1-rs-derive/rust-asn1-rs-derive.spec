%global source0_hash db8b7511298d5b7784b40b092d9e9dcd3a627a5707e4b5e507931ab0d44eeebf
%bcond check 0
%global debug_package %{nil}
%global crate asn1-rs-derive
Name:           rust-asn1-rs-derive
Version:        0.1.0
Release:        1%{?dist}
Summary:        Derive macros for the `asn1-rs` crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/asn1-rs-derive
Source0:        https://static.crates.io/crates/asn1-rs-derive/asn1-rs-derive-%{version}.crate
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
Summary:        Derive macros for the `asn1-rs` crate
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
%files -n rust-asn1-rs-derive-devel -f %{oreon_filedir}/rust-asn1-rs-derive-devel.list

%changelog

%autochangelog
