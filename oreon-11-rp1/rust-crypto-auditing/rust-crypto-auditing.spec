%global source0_hash e1f8cd62823adf394499bc76be4d8b8fa72964bef59bd50f6bb89316c585da1c
%bcond check 1
%global debug_package %{nil}
%global crate crypto-auditing
Name:           rust-crypto-auditing
Version:        0.3.2
Release:        1%{?dist}
Summary:        Client library for crypto-auditing project
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/crypto-auditing
Source0:        https://static.crates.io/crates/crypto-auditing/crypto-auditing-%{version}.crate
Patch:          rust-crypto-auditing-0.2.4-types32.patch
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
Summary:        Client library for crypto-auditing project
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p2
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
%files -n rust-crypto-auditing-devel -f %{oreon_filedir}/rust-crypto-auditing-devel.list

%changelog

%autochangelog
