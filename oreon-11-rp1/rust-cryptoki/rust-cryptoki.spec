%global source0_hash 625cf4599c43d69a16996ce2573fc80745a0b0300c962f0bfa11d55b6cab2b2d
%bcond check 1
%global debug_package %{nil}
%global crate cryptoki
Name:           rust-cryptoki
Version:        0.12.1
Release:        1%{?dist}
Summary:        Rust-native wrapper around the PKCS #11 API
License:        Apache-2.0
URL:            https://crates.io/crates/cryptoki
Source0:        https://static.crates.io/crates/cryptoki/cryptoki-%{version}.crate
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  kryoptic
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
Summary:        Rust-native wrapper around the PKCS #11 API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+generate-bindings-devel
Summary:        Rust-native wrapper around the PKCS #11 API
BuildArch:      noarch
%description -n %{name}+generate-bindings-devel

This package contains library source intended for building other packages which
use the "generate-bindings" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust-native wrapper around the PKCS #11 API
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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

export KRYOPTIC_CONF=/tmp/kryoptic.sql
export TEST_PKCS11_MODULE=%{_libdir}/pkcs11/libkryoptic_pkcs11.so
export RUST_BACKTRACE=1
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-cryptoki-devel -f %{oreon_filedir}/rust-cryptoki-devel.list

%changelog

%autochangelog
