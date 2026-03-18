%define efivar_version 35-2

Name: efibootmgr
Version: 18
Release: 12%{?dist}
Summary: EFI Boot Manager
License: GPL-2.0-or-later
URL: https://github.com/rhboot/%{name}/

BuildRequires: efi-srpm-macros >= 3-2
BuildRequires: efi-filesystem
BuildRequires: git popt-devel
BuildRequires: efivar-libs >= %{efivar_version}
BuildRequires: efivar-devel >= %{efivar_version}
BuildRequires: gcc
BuildRequires: make
Requires: efi-filesystem
ExclusiveArch: %{efi}

Source0: https://github.com/rhboot/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1: efibootmgr.patches

%include %{SOURCE1}

%description
%{name} displays and allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables.  Additional
information about EFI can be found at https://uefi.org/.

%prep
%autosetup -S git
git config --local --add efibootmgr.efidir %{efi_vendor}

%build
%make_build CFLAGS='%{optflags}' LDFLAGS='%{build_ldflags}'

%install
%make_install libdir=%{_libdir} \
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 18-12
- Prepare for Oreon 11 (RP1)
