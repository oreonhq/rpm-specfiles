# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e8cc2e3ad0c28dca89ee540a22bcc939fd65e8fd55657a5b6b5b8a784703a58c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: cargo-rpm-macros
Version: 28.4
Release: 1%{?dist}
Summary: RPM macros for building Rust packages with cargo
License: MIT
URL: https://codeberg.org/rust2rpm/cargo-rpm-macros
Source0: https://codeberg.org/rust2rpm/cargo-rpm-macros/archive/v%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
Requires: cargo2rpm >= 0.3.2
Requires: cargo
Requires: gawk
Requires: grep
Requires: rust-srpm-macros

%description
Macros and file attributes used to package cargo projects.

%prep
%oreon_sha256
%autosetup -n cargo-rpm-macros -p1

%build

%install
install -D -p -m 0644 macros.d/macros.cargo %{buildroot}%{_rpmmacrodir}/macros.cargo
install -D -p -m 0644 macros.d/macros.cargo-buildsys %{buildroot}%{_rpmmacrodir}/macros.cargo-buildsys
install -D -p -m 0644 fileattrs/cargo.attr %{buildroot}%{_fileattrsdir}/cargo.attr
install -D -p -m 0644 fileattrs/cargo_vendor.attr %{buildroot}%{_fileattrsdir}/cargo_vendor.attr

%files
%license LICENSE
%{_rpmmacrodir}/macros.cargo
%{_rpmmacrodir}/macros.cargo-buildsys
%{_fileattrsdir}/cargo.attr
%{_fileattrsdir}/cargo_vendor.attr
