%global source0_hash 28dea519a9695b9977216879a3ebfddf92f1c08c05d984f8996aecd6ecdc811d
%bcond check 0
%global debug_package %{nil}
%global crate fiat-crypto
Name:           rust-fiat-crypto0.2
Version:        0.2.9
Release:        1%{?dist}
Summary:        Fiat-crypto generated Rust
License:        MIT OR Apache-2.0 OR BSD-1-Clause
URL:            https://crates.io/crates/fiat-crypto
Source0:        https://static.crates.io/crates/fiat-crypto/fiat-crypto-%{version}.crate
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
Summary:        Fiat-crypto generated Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fiat-crypto generated Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-fiat-crypto0.2-devel -f %{oreon_filedir}/rust-fiat-crypto0.2-devel.list

%changelog

%autochangelog
