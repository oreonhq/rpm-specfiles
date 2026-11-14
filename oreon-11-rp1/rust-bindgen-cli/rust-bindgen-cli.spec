# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8a408c0fcb20bf7bd4ceaf4bf990e223e3543a04b84d2394f3edeee29a0e87e2
%global source1_hash b991a0b4a9682e48b037cc6e8f214828270dff8bb93e436e71b4395fd84cdbcd
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

%global crate bindgen-cli

Name: rust-bindgen-cli
Version: 0.72.1
Release: 1%{?dist}
Summary: Generates Rust FFI bindings to C and C++ libraries
License: BSD-3-Clause AND Apache-2.0 AND ISC AND MIT AND Unicode-3.0 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL: https://crates.io/crates/bindgen-cli
Source0: https://crates.io/api/v1/crates/bindgen-cli/%{version}/download#/bindgen-cli-%{version}.crate
Source1: bindgen-cli-%{version}-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: rustc
BuildRequires: cargo
BuildRequires: pkgconf
BuildRequires: clang
BuildRequires: clang-devel
BuildRequires: clang-libs

%description
bindgen automatically generates Rust FFI bindings to C and C++ libraries.

%package -n %{crate}
Summary: Generates Rust FFI bindings to C and C++ libraries
Provides: bindgen = %{version}-%{release}
Obsoletes: bindgen < 0.61
Requires: clang-libs

%description -n %{crate}
bindgen automatically generates Rust FFI bindings to C and C++ libraries.
This package ships the bindgen command line tool, which loads libclang at
runtime.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n %{crate}-%{version} -p1
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
%oreon_cargo_build

%install
install -D -p -m 755 target/release/bindgen %{buildroot}%{_bindir}/bindgen

%check
%oreon_cargo_test

%files -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/bindgen

%changelog
%autochangelog
