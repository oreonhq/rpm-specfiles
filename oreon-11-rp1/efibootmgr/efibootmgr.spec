# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2b195f912aa353f0d11f21f207684c91460fbc37f9a4f2673e63e5e32d108b10
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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

# Tag is 18, not efibootmgr-18 (asset at .../download/18/...)
Source0: https://github.com/rhboot/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

# Was efibootmgr.patches (%%include needs SOURCES at parse time for spectool)
Patch0001: 0001-Update-efibootmgr.c.patch

%description
%{name} displays and allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables.  Additional
information about EFI can be found at https://uefi.org/.

%prep
%oreon_verify_sources
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
* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 18-12
- Fix Source0 GitHub release path (tag is 18, not efibootmgr-18)
- Inline patch list, drop %%include efibootmgr.patches for spectool

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 18-12
- Prepare for Oreon 11 (RP1)
