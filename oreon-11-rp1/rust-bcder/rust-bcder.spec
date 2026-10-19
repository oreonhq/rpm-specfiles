%global source0_hash 1f7c42c9913f68cf9390a225e81ad56a5c515347287eb98baa710090ca1de86d
%bcond check 1
%global debug_package %{nil}
%global crate bcder
Name:           rust-bcder
Version:        0.7.6
Release:        1%{?dist}
Summary:        Handling of data encoded in BER, CER, and DER
License:        BSD-3-Clause
URL:            https://crates.io/crates/bcder
Source0:        https://static.crates.io/crates/bcder/bcder-%{version}.crate
Patch:          bcder-fix-metadata.diff
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
Summary:        Handling of data encoded in BER, CER, and DER
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
%files -n rust-bcder-devel -f %{oreon_filedir}/rust-bcder-devel.list

%changelog

%autochangelog
