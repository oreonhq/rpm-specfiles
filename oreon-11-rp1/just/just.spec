# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7e46c1911c9c129f5b4f05edb3cd9aa75bba81e0198bbdbcf6181f7bcc21d74e
%global source1_hash e470466246527f5ab1b3a48028261f9ec59b8d2898d0bc991d4bef94e70ae2ab
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

%global crate just

Name: just
Version: 1.59.0
Release: 1%{?dist}
Summary: Command runner for project-specific tasks
License: CC0-1.0
URL: https://crates.io/crates/just
Source0: https://crates.io/api/v1/crates/just/%{version}/download#/just-%{version}.crate
Source1: just-%{version}-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: rustc
BuildRequires: cargo

%description
just is a command runner. It saves and runs project-specific commands
from a file called a justfile.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n %{crate}-%{version} -p1
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
%oreon_cargo_build

%install
install -D -p -m 755 target/release/just %{buildroot}%{_bindir}/just

%check
export XDG_RUNTIME_DIR="$(mktemp -d)"
chmod 700 "$XDG_RUNTIME_DIR"
%oreon_cargo_test

%files
%license LICENSE
%doc README.md CHANGELOG.md GRAMMAR.md
%{_bindir}/just

%changelog
%autochangelog
