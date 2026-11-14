# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: LGPL-2.0-or-later

%global source0_hash 54ecc2eeefc0ccbba225e6e57ef1cde9df78e55b315e71fd95ebebc5bd1dbbb6
%global source1_hash a8375cee500459f2664a9a138d239bd519222413f33cc3148df13f6c434c2a23

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: sequoia-policy-config
Version: 0.8.2
Release: 1%{?dist}
Summary: Configure Sequoia using a configuration file
License: LGPL-2.0-or-later
URL: https://gitlab.com/sequoia-pgp/sequoia-policy-config
Source0: https://crates.io/api/v1/crates/sequoia-policy-config/%{version}/download#/sequoia-policy-config-%{version}.crate
Source1: sequoia-policy-config-%{version}-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: rustc
BuildRequires: cargo
BuildRequires: openssl-devel
BuildRequires: clang-devel
BuildRequires: pkgconfig(nettle)
Provides: sequoia-policy-config-check = %{version}-%{release}

%description
Helpers and the sequoia-policy-config-check tool used to validate
crypto-policies Sequoia backends.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n sequoia-policy-config-%{version} -p1
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
%oreon_cargo_build --no-default-features --features sequoia-openpgp/crypto-openssl

%install
install -Dpm0755 target/release/sequoia-policy-config-check %{buildroot}%{_bindir}/sequoia-policy-config-check

%check
%oreon_cargo_test --no-default-features --features sequoia-openpgp/crypto-openssl

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/sequoia-policy-config-check

%changelog
%autochangelog
