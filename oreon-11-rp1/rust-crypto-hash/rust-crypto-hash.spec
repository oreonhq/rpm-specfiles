%global source0_hash 8a77162240fd97248d19a564a565eb563a3f592b386e4136fb300909e67dddca
%bcond check 0
%global debug_package %{nil}
%global crate crypto-hash
Name:           rust-crypto-hash
Version:        0.3.4
Release:        1%{?dist}
Summary:        Wrapper for OS-level cryptographic hash functions
License:        MIT
URL:            https://crates.io/crates/crypto-hash
Source0:        https://static.crates.io/crates/crypto-hash/crypto-hash-%{version}.crate
Patch:          crypto-hash-fix-metadata-auto.diff
Patch:          crypto-hash-fix-metadata.diff
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
Summary:        Wrapper for OS-level cryptographic hash functions
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
%files -n rust-crypto-hash-devel -f %{oreon_filedir}/rust-crypto-hash-devel.list

%changelog

%autochangelog
