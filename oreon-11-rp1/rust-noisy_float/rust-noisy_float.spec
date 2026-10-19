%global source0_hash c16843be85dd410c6a12251c4eca0dd1d3ee8c5725f746c4d5e0fdcec0a864b2
%bcond check 1
%global debug_package %{nil}
%global crate noisy_float
Name:           rust-noisy_float
Version:        0.2.1
Release:        1%{?dist}
Summary:        Rust library containing floating point types
License:        Apache-2.0
URL:            https://crates.io/crates/noisy_float
Source0:        https://static.crates.io/crates/noisy_float/noisy_float-%{version}.crate
Patch:          noisy_float-fix-metadata.diff
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
Summary:        Rust library containing floating point types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+approx-devel
Summary:        Rust library containing floating point types
BuildArch:      noarch
%description -n %{name}+approx-devel

This package contains library source intended for building other packages which
use the "approx" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust library containing floating point types
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-noisy_float-devel -f %{oreon_filedir}/rust-noisy_float-devel.list

%changelog

%autochangelog
