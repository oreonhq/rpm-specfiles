%global source0_hash 16abd0c1b639e9eb4d7c50c0b8100b0d0f849be2349829c740fe8e6eb4816429
%bcond check 1
%global debug_package %{nil}
%global crate rand_pcg
Name:           rust-rand_pcg0.2
Version:        0.2.1
Release:        1%{?dist}
Summary:        Selected PCG random number generators
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_pcg
Source0:        https://static.crates.io/crates/rand_pcg/rand_pcg-%{version}.crate
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
Summary:        Selected PCG random number generators
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde1-devel
Summary:        Selected PCG random number generators
BuildArch:      noarch
%description -n %{name}+serde1-devel

This package contains library source intended for building other packages which
use the "serde1" feature of the "%{crate}" crate.

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
%files -n rust-rand_pcg0.2-devel -f %{oreon_filedir}/rust-rand_pcg0.2-devel.list

%changelog

%autochangelog
