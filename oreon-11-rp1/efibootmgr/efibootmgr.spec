# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2b195f912aa353f0d11f21f207684c91460fbc37f9a4f2673e63e5e32d108b10
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define efivar_version 35-2

Name: efibootmgr
Version: 18
Release: 1%{?dist}
Summary: EFI Boot Manager
License: GPL-2.0-or-later
URL: https://github.com/rhboot/%{name}/

BuildRequires: oreon-rpm-macros
BuildRequires: efi-srpm-macros >= 3-2
BuildRequires: efi-filesystem
BuildRequires: git
BuildRequires: popt-devel
BuildRequires: efivar-libs >= %{efivar_version}
BuildRequires: efivar-devel >= %{efivar_version}
BuildRequires: clang
BuildRequires: make
Requires: efi-filesystem
ExclusiveArch: %{efi}

Source0: https://github.com/rhboot/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

Patch0001: 0001-Update-efibootmgr.c.patch

%description
%{name} displays and allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables.  Additional
information about EFI can be found at https://uefi.org/.

%prep
%oreon_sha256
%autosetup -S git
git config --local --add efibootmgr.efidir %{efi_vendor}

%build
%make_build CC=%{__cc} CFLAGS='%{optflags}' LDFLAGS='%{build_ldflags}'

%install
%make_install CC=%{__cc} libdir=%{_libdir} \
              bindir=%{_bindir} \
              sbindir=%{_sbindir} \
              mandir=%{_mandir} \
	      localedir=%{_datadir}/locale/ \
              includedir=%{_includedir} \
	      libexecdir=%{_libexecdir} \
              datadir=%{_datadir}

%files
%license COPYING
%{_sbindir}/*
%{_mandir}/*/*.?.gz
%doc README

%changelog
%autochangelog
