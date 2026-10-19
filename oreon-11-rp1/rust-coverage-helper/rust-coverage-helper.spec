%global source0_hash 435aea653a110cde24da15ca2dac9e06d17d92ce2bd6c2b9179b508abbe6f06f
%bcond check 1
%global debug_package %{nil}
%global crate coverage-helper
Name:           rust-coverage-helper
Version:        0.2.4
Release:        1%{?dist}
Summary:        Helper for <https://github.com/taiki-e/cargo-llvm-cov/issues/123>
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/coverage-helper
Source0:        https://static.crates.io/crates/coverage-helper/coverage-helper-%{version}.crate
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
Summary:        Helper for <https://github.com/taiki-e/cargo-llvm-cov/issues/123>
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
%files -n rust-coverage-helper-devel -f %{oreon_filedir}/rust-coverage-helper-devel.list

%changelog

%autochangelog
