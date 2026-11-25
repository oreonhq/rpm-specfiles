# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ad235437a6e8813a581d4163a8461655208b2c47ff808a01241aa957f051f016
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: cosmic-randr
Version: 1.12.0
Release: 1%{?dist}
Summary: Display and output configuration tool for the COSMIC desktop
License: MPL-2.0
URL: https://github.com/pop-os/cosmic-randr
Source0: https://github.com/pop-os/cosmic-randr/archive/refs/tags/epoch-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: rustc
BuildRequires: cargo

%description
cosmic-randr is a command line tool for listing and configuring display
outputs on COSMIC and other Wayland compositors that support the
COSMIC output management protocol.

%prep
%oreon_sha256
%autosetup -n cosmic-randr-epoch-%{version} -p1

%build
%oreon_cargo_prep fetch
%oreon_cargo_build

%install
install -D -p -m 755 target/release/cosmic-randr %{buildroot}%{_bindir}/cosmic-randr

%check
%oreon_cargo_test

%files
%license LICENSE
%{_bindir}/cosmic-randr

%changelog
%autochangelog
