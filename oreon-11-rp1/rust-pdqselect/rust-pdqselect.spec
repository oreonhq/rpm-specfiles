%global source0_hash 4ec91767ecc0a0bbe558ce8c9da33c068066c57ecc8bb8477ef8c1ad3ef77c27
%bcond check 0
%global debug_package %{nil}
%global crate pdqselect
Name:           rust-pdqselect
Version:        0.1.0
Release:        1%{?dist}
Summary:        Selects the kth smallest element of a slice, based on Orson Peters's...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/pdqselect
Source0:        https://static.crates.io/crates/pdqselect/pdqselect-%{version}.crate
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
Summary:        Selects the kth smallest element of a slice, based on Orson Peters's...
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
%files -n rust-pdqselect-devel -f %{oreon_filedir}/rust-pdqselect-devel.list

%changelog

%autochangelog
