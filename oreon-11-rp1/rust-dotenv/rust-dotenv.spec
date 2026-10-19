%global source1_hash d7366187540d9ec714de6402f3f2adbaa029f5ecb92612f27544e67b99b96739
%global source0_hash 77c90badedccf4105eca100756a0b1289e191f6fcbdadd3cee1d2f614f97da8f
%bcond check 0
%global debug_package %{nil}
%global crate dotenv
Name:           rust-dotenv
Version:        0.15.0
Release:        1%{?dist}
Summary:        Dotenv implementation for Rust
License:        MIT
URL:            https://crates.io/crates/dotenv
Source0:        https://static.crates.io/crates/dotenv/dotenv-%{version}.crate
Source1:        https://github.com/dotenv-rs/dotenv/raw/v%{version}/LICENSE.md
Patch:          dotenv-fix-metadata.diff
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
Summary:        Dotenv implementation for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-dotenv-devel -f %{oreon_filedir}/rust-dotenv-devel.list

%changelog

%autochangelog
