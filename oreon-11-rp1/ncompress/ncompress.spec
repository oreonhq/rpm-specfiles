# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 96ec931d06ab827fccad377839bfb91955274568392ddecf809e443443aead46

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: ncompress
Version: 5.0
Release: 1%{?dist}
Summary: Fast compression and decompression utilities
License: LicenseRef-Oreon-Public-Domain
URL: https://github.com/vapier/ncompress
Source0: https://github.com/vapier/ncompress/archive/refs/tags/v%{version}.tar.gz#/ncompress-%{version}.tar.gz
Patch0: ncompress-5.0-2GB.patch
Patch1: ncompress-5.0-endians.patch
Patch2: ncompress-5.0-lfs.patch
Patch3: ncompress-5.0-make.patch
Patch4: ncompress-5.0-memmove.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make

Provides: /usr/bin/compress
Provides: /usr/bin/uncompress

%description
ncompress is a fast compression and decompression package.

%prep
%oreon_sha256
%autosetup -n ncompress-%{version} -p1

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
%make_install PREFIX=%{buildroot}%{_prefix} MANPATH=%{buildroot}%{_mandir}/man1

%check
%make_build check

%files
%license LZW.INFO
%doc README.md Acknowleds
%{_bindir}/compress
%{_bindir}/uncompress
%{_mandir}/man1/compress.1*
%{_mandir}/man1/uncompress.1*

%changelog
%autochangelog
