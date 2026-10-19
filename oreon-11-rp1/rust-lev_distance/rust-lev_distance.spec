%global source0_hash 72d9d1bd215936bc8647ad92986bb56f3f216550b53c44ab785e3217ae33625e
%bcond check 0
%global debug_package %{nil}
%global crate lev_distance
Name:           rust-lev_distance
Version:        0.1.1
Release:        1%{?dist}
Summary:        Copy of Levenshtein distance implementation from Rust Compiler
License:        MIT
URL:            https://crates.io/crates/lev_distance
Source0:        https://static.crates.io/crates/lev_distance/lev_distance-%{version}.crate
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
Summary:        Copy of Levenshtein distance implementation from Rust Compiler
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
%files -n rust-lev_distance-devel -f %{oreon_filedir}/rust-lev_distance-devel.list

%changelog

%autochangelog
