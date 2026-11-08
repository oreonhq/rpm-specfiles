# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d4eb1f22746894dd654a8fa50576200d047f0de0e1ae2a361d7ebe263d351bc8
%global source1_hash 80c570392fa8821719b2c37c8254622e7c6fc5f7eb6efe3be3af7e60efc8030a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: sequoia-sqv
Version: 1.5.0
Release: 1%{?dist}
Summary: Simple OpenPGP signature verification program
License: LGPL-2.0-or-later
URL: https://gitlab.com/sequoia-pgp/sequoia-sqv
Source0: https://crates.io/api/v1/crates/sequoia-sqv/%{version}/download#/sequoia-sqv-%{version}.crate
Source1: sequoia-sqv-%{version}-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: rustc
BuildRequires: cargo
BuildRequires: pkgconf
BuildRequires: openssl-devel >= 1:4.0
BuildRequires: clang-devel
Requires: openssl-libs

%description
sqv verifies detached OpenPGP signatures against a set of certificates.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n sequoia-sqv-%{version} -p1
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
export ASSET_OUT_DIR=$PWD/assets
%oreon_cargo_build --no-default-features --features crypto-openssl

%install
install -D -p -m 755 target/release/sqv %{buildroot}%{_bindir}/sqv
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 assets/man-pages/*.1 %{buildroot}%{_mandir}/man1/
install -D -p -m 644 assets/shell-completions/sqv.bash %{buildroot}%{_datadir}/bash-completion/completions/sqv
install -D -p -m 644 assets/shell-completions/_sqv %{buildroot}%{_datadir}/zsh/site-functions/_sqv
install -D -p -m 644 assets/shell-completions/sqv.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sqv.fish

%files
%license LICENSE.txt
%doc README.md NEWS
%{_bindir}/sqv
%{_mandir}/man1/sqv.1*
%{_datadir}/bash-completion/completions/sqv
%{_datadir}/zsh/site-functions/_sqv
%{_datadir}/fish/vendor_completions.d/sqv.fish
