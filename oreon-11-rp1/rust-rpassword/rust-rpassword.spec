%global source0_hash 2da316a15f47e3d053de9cb2c439650bd8fa4aaeb9365f2e5f27f492ff73c196
%bcond check 0
%global debug_package %{nil}
%global crate rpassword
Name:           rust-rpassword
Version:        7.5.4
Release:        1%{?dist}
Summary:        Read passwords in console applications (unix, windows, macos, wasm).
License:        Apache-2.0
URL:            https://crates.io/crates/rpassword
Source0:        https://static.crates.io/crates/rpassword/rpassword-%{version}.crate
Patch:          rpassword-fix-metadata-auto.diff
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
Summary:        Read passwords in console applications (unix, windows, macos, wasm).
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
%files -n rust-rpassword-devel -f %{oreon_filedir}/rust-rpassword-devel.list

%changelog

%autochangelog
