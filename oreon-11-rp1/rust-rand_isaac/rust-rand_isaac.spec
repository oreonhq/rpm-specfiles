%global source0_hash ded997c9d5f13925be2a6fd7e66bf1872597f759fd9dd93513dd7e92e5a5ee08
%bcond check 0
%global debug_package %{nil}
%global crate rand_isaac
Name:           rust-rand_isaac
Version:        0.1.1
Release:        1%{?dist}
Summary:        ISAAC random number generator
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_isaac
Source0:        https://static.crates.io/crates/rand_isaac/rand_isaac-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        ISAAC random number generator
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde1-devel
Summary:        ISAAC random number generator
BuildArch:      noarch
%description -n %{name}+serde1-devel

This package contains library source intended for building other packages which
use the "serde1" feature of the "%{crate}" crate.

%package     -n %{name}+serde_derive-devel
Summary:        ISAAC random number generator
BuildArch:      noarch
%description -n %{name}+serde_derive-devel

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

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
%files -n rust-rand_isaac-devel -f %{oreon_filedir}/rust-rand_isaac-devel.list

%changelog

%autochangelog
