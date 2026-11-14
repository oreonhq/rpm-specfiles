# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2ecb53484c9c167ba674026b656d8a27d7657a58e6066aa902bfb1a4aa00ae20
%global source1_hash 4b40ab38a15d14b92489172c161509ad3292ed9fe97b0af52e0f389a3b12b383
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

%global crate cbindgen

Name: rust-cbindgen
Version: 0.29.4
Release: 1%{?dist}
Summary: Tool for generating C bindings to Rust code
License: MPL-2.0 AND MIT AND Unicode-3.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL: https://crates.io/crates/cbindgen
Source0: https://crates.io/api/v1/crates/cbindgen/%{version}/download#/cbindgen-%{version}.crate
Source1: cbindgen-%{version}-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: rustc
BuildRequires: cargo
BuildRequires: python3-cython

%description
A tool for generating C bindings to Rust code.

%package -n %{crate}
Summary: Tool for generating C bindings to Rust code

%description -n %{crate}
A tool for generating C bindings to Rust code.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n %{crate}-%{version} -p1
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
%oreon_cargo_build

%install
install -D -p -m 755 target/release/cbindgen %{buildroot}%{_bindir}/cbindgen

%check
%oreon_cargo_test

%files -n %{crate}
%license LICENSE
%doc README.md
%doc contributing.md
%doc docs.md
%doc internals.md
%{_bindir}/cbindgen

%changelog
%autochangelog
