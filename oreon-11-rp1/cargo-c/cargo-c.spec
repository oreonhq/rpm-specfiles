# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 57700786539a322a50f1848332e3465bf15efa5af2fd8b6113f36cbfce46c830
%global source1_hash d3cb865d40625de197b71fa591f1f24c0593b5a24b46b7c126eae7fecf7be315
%global source2_hash e4064d49caed5e007508e6cdb1f65754a49091f420de350885402a0c332343b2

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: cargo-c
Version: 0.10.26
Release: 1%{?dist}
Summary: Cargo subcommands for building and installing C libraries
License: MIT
URL: https://github.com/lu-zero/cargo-c
Source0: https://github.com/lu-zero/cargo-c/archive/refs/tags/v%{version}.tar.gz
Source1: https://github.com/lu-zero/cargo-c/releases/download/v%{version}/Cargo.lock
Source2: cargo-c-%{version}-vendor.tar.xz

BuildRequires: oreon-rpm-macros >= 1-14
BuildRequires: cargo
BuildRequires: rust
BuildRequires: gcc

%description
cargo-cbuild, cargo-cinstall, cargo-ctest and cargo-capi build and install
Rust cdylib crates the way a C library is built and installed.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%autosetup -n cargo-c-%{version}
cp %{SOURCE1} Cargo.lock
tar -xf %{SOURCE2}

%build
%oreon_cargo_prep vendor
%oreon_cargo_build

%install
%oreon_cargo_install

%check
%oreon_cargo_test

%files
%license LICENSE
%doc README.md
%{_bindir}/cargo-capi
%{_bindir}/cargo-cbuild
%{_bindir}/cargo-cinstall
%{_bindir}/cargo-ctest

%changelog
%autochangelog
