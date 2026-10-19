%global source0_hash 1fb256a02274bc6cb6b6b7f514b6cbcffbd30c2dbeee1533de6e1c573cbec72a
%bcond check 1
%global debug_package %{nil}
%global crate sequoia-openpgp-mt
Name:           rust-sequoia-openpgp-mt
Version:        0.2.0
Release:        1%{?dist}
Summary:        Multi-threaded parsing of OpenPGP data
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-openpgp-mt
Source0:        https://static.crates.io/crates/sequoia-openpgp-mt/sequoia-openpgp-mt-%{version}.crate
Patch:          sequoia-openpgp-mt-fix-metadata-auto.diff
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
Summary:        Multi-threaded parsing of OpenPGP data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f sequoia-openpgp/crypto-nettle
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-sequoia-openpgp-mt-devel -f %{oreon_filedir}/rust-sequoia-openpgp-mt-devel.list

%changelog

%autochangelog
