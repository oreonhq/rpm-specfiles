%global source0_hash 781442f29170c5c93b7185ad559492601acdc71d5bb0706f5868094f45cfcd08
%bcond check 0
%global debug_package %{nil}
%global crate rustc-stable-hash
Name:           rust-rustc-stable-hash
Version:        0.1.2
Release:        1%{?dist}
Summary:        A stable hashing algorithm used by rustc
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/rustc-stable-hash
Source0:        https://static.crates.io/crates/rustc-stable-hash/rustc-stable-hash-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(%{crate}/default) = %{version}
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        A stable hashing algorithm used by rustc
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

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
%files -n rust-rustc-stable-hash-devel -f %{oreon_filedir}/rust-rustc-stable-hash-devel.list

%changelog

%autochangelog
