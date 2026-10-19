%global source0_hash 0c74e146e96aa56c4ce832cf299e4ae38b80953cbdb9f47ae72ab85b1965cb9f
Summary:        Common RPM Macros for building EFI-related packages
Name: efi-rpm-macros
Version: 6
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://github.com/rhboot/%{name}/
BuildArch: noarch
Source0:        https://github.com/rhboot/efi-rpm-macros/archive/refs/tags/%{version}.tar.gz#/efi-rpm-macros-%{version}.tar.gz
Patch0001:        0001-add-riscv64-support.patch
Patch0002:        0002-Re-enable-ia32-as-an-alt-for-x86_64.patch
%global debug_package %{nil}
%global _efi_vendor_ %(eval echo $(sed -n -e 's/rhel/redhat/' -e 's/^ID=//p' /etc/os-release))
# oreon:deps
BuildRequires:  git
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
%{name} provides a set of RPM macros for use in EFI-related packages.

%package -n efi-srpm-macros
Summary: Common SRPM Macros for building EFI-related packages
BuildArch: noarch
Requires: rpm
%description -n efi-srpm-macros
efi-srpm-macros provides a set of SRPM macros for use in EFI-related packages.

%package -n efi-filesystem
Summary: The basic directory layout for EFI machines
BuildArch: noarch
Requires: filesystem
%description -n efi-filesystem
The efi-filesystem package contains the basic directory layout for EFI
machine bootloaders and tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am -n %{name}-6
git config --local --add efi.vendor "%{_efi_vendor_}"
git config --local --add efi.esp-root /boot/efi
git config --local --add efi.arches "x86_64 aarch64 %{arm} %{ix86} riscv64"

%build

%make_build clean all
%install
%make_install
%oreon_autofiles efi-srpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles efi-filesystem usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n efi-srpm-macros -f %{oreon_filedir}/efi-srpm-macros.list
%files -n efi-filesystem -f %{oreon_filedir}/efi-filesystem.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6-6
- Import
