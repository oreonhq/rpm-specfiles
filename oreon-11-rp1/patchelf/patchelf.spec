# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 491108728f120ce05b539934b41a750235031a6df8abc6b47e57aff7de15094d

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
# hardening breaks the set-interpreter-long test on i686, x86_64, ppc64le, s390x
%undefine _hardened_build

Name:           patchelf
Version:        0.19.1
Release:        1%{?dist}
Summary:        A utility for patching ELF binaries

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://nixos.org/patchelf.html
Source0:        https://github.com/NixOS/patchelf/releases/download/%{version}/patchelf-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  oreon-rpm-macros

%description
PatchELF is a simple utility for modifying an existing ELF executable
or library.  It can change the dynamic loader ("ELF interpreter")
of an executable and change the RPATH of an executable or library.

%prep
%oreon_sha256

%autosetup -p1

# package ships elf.h - delete to use glibc-headers one
rm src/elf.h

%build
%configure
%make_build

%check
make check || (cat tests/*.log; exit 1)

%install
%make_install

# the docs get put in a funny place, so delete and include in the
# standard way in the docs section below
rm -rf %{buildroot}/usr/share/doc/%{name}

%files
%license COPYING
%doc README.md
%{_bindir}/patchelf
%{_mandir}/man1/patchelf.1*
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_patchelf

