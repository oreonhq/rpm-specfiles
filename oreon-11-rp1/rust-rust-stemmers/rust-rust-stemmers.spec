%global source0_hash e46a2036019fdb888131db7a4c847a1063a7493f971ed94ea82c67eada63ca54
%bcond check 0
%global debug_package %{nil}
%global crate rust-stemmers
Name:           rust-rust-stemmers
Version:        1.2.0
Release:        1%{?dist}
Summary:        Rust implementation of some popular snowball stemming algorithms
License:        (MIT OR BSD-3-Clause) AND GPL-3.0-or-later
URL:            https://crates.io/crates/rust-stemmers
Source0:        https://static.crates.io/crates/rust-stemmers/rust-stemmers-%{version}.crate
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
Summary:        Rust implementation of some popular snowball stemming algorithms
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
%files -n rust-rust-stemmers-devel -f %{oreon_filedir}/rust-rust-stemmers-devel.list

%changelog

%autochangelog
