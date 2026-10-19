%global source0_hash bfcaedb62e0475a6898988138995ec7b1e5d116167a72bb12c7b59d0649fbbc2
%bcond check 1
%global debug_package %{nil}
%global crate smol-macros
Name:           rust-smol-macros
Version:        0.1.1
Release:        1%{?dist}
Summary:        Macros for setting up a smol runtime
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/smol-macros
Source0:        https://static.crates.io/crates/smol-macros/smol-macros-%{version}.crate
Patch:          smol-macros-fix-metadata.diff
Patch2:         smol-macros-remove-unsend-from-tests.patch
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
Summary:        Macros for setting up a smol runtime
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
%files -n rust-smol-macros-devel -f %{oreon_filedir}/rust-smol-macros-devel.list

%changelog

%autochangelog
