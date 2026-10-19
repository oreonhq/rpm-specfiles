%global source0_hash 2eecf2d5dc9b66b732b97707a0210906b1d30523eb773193ab777c0c84b3e8d5
%bcond check 0
%global debug_package %{nil}
%global crate ghash
Name:           rust-ghash
Version:        0.6.0
Release:        1%{?dist}
Summary:        Universal hash over GF(2^128) useful for constructing a Message Authe...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ghash
Source0:        https://static.crates.io/crates/ghash/ghash-%{version}.crate
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

%package     -n %{name}+zeroize-devel
Summary:        Universal hash over GF(2^128) useful for constructing a Message Authe...
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-ghash-devel -f %{oreon_filedir}/rust-ghash-devel.list

%changelog

%autochangelog
