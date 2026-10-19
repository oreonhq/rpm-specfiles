%global source0_hash fb39b166781f92d482534ef4b4b1b2568f42613b53e5b6c160e24cfbfa30926d
%bcond check 1
%global debug_package %{nil}
%global crate rayon
Name:           rust-rayon
Version:        1.12.0
Release:        1%{?dist}
Summary:        Simple work-stealing parallelism for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rayon
Source0:        https://static.crates.io/crates/rayon/rayon-%{version}.crate
Patch:          rayon-fix-metadata.diff
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
Summary:        Simple work-stealing parallelism for Rust
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

%cargo_test -- -- --exact --skip par_bridge_recursion
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rayon-devel -f %{oreon_filedir}/rust-rayon-devel.list

%changelog

%autochangelog
