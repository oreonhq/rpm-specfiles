%global source0_hash f0d8a4362ccb29cb0b265253fb0a2728f592895ee6854fd9bc13f2ffda266ff1
%bcond check 1
%global debug_package %{nil}
%global crate ghash
Name:           rust-ghash0.5
Version:        0.5.1
Release:        1%{?dist}
Summary:        Universal hash over GF(2^128) useful for the AES-GCM cipher
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

%package     -n %{name}+default-devel
Summary:        Universal hash over GF(2^128) useful for the AES-GCM cipher
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Universal hash over GF(2^128) useful for the AES-GCM cipher
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Universal hash over GF(2^128) useful for the AES-GCM cipher
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
%files -n rust-ghash0.5-devel -f %{oreon_filedir}/rust-ghash0.5-devel.list

%changelog

%autochangelog
