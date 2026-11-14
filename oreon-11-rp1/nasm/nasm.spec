# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b7324cbe86e767b65f26f467ed8b12ad80e124e3ccb89076855c98e43a9eddd4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           nasm
Version:        3.01
Release:        1%{?dist}
Summary:        The Netwide Assembler
License:        BSD-2-Clause
URL:            https://www.nasm.us/
Source0:        https://www.nasm.us/pub/nasm/releasebuilds/%{version}/nasm-%{version}.tar.xz

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make

%description
NASM is the Netwide Assembler, an 80x86 and x86-64 assembler.

%prep
%oreon_sha256
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
%make_build test

%files
%license LICENSE
%doc AUTHORS CHANGES README.md
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_mandir}/man1/nasm.1*
%{_mandir}/man1/ndisasm.1*

%changelog
%autochangelog
