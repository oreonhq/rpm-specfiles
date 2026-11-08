# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cbeb34628e5c180cde497d43b738e8cb44d385bba028af30b1467e521698e187
%global debug_package %{nil}

Name: rust-srpm-macros
Version: 28.5
Release: 1%{?dist}
Summary: SRPM macros for Rust packages
License: MIT
URL: https://pagure.io/fedora-rust/rust-packaging
BuildArch: noarch
Source0: macros.rust-srpm
Source1: macros.rust
Source2: LICENSE

BuildRequires: oreon-rpm-macros

%description
SRPM macros for Rust crates. The compiler is not part of this package.

%prep
%oreon_sha256
cp %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.rust-srpm
install -m 644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.rust

%files
%license LICENSE
%{_rpmmacrodir}/macros.rust-srpm
%{_rpmmacrodir}/macros.rust
