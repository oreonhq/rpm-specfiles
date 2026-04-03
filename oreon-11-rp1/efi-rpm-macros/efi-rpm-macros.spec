Summary: Common RPM Macros for building EFI-related packages
Name: efi-rpm-macros
Version: 6
Release: 6%{?dist}
License: GPL-3.0-or-later
URL: https://github.com/rhboot/%{name}/
BuildRequires: git sed
BuildRequires: make
BuildArch: noarch

# Tag 6 has no GitHub release asset (releases/download/...tar.bz2 404). Use tag archive.
Source0: https://github.com/rhboot/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Not upstream, but trivial and posted upstream as a PR:
# https://github.com/rhboot/efi-rpm-macros/pull/3
Patch0001: 0001-add-riscv64-support.patch
Patch0002: 0002-Re-enable-ia32-as-an-alt-for-x86_64.patch

%global debug_package %{nil}
%global _efi_vendor_ %(eval echo $(sed -n -e 's/rhel/redhat/' -e 's/^ID=//p' /etc/os-release))

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
%autosetup -S git_am -n %{name}-6
git config --local --add efi.vendor "%{_efi_vendor_}"
git config --local --add efi.esp-root /boot/efi
git config --local --add efi.arches "x86_64 aarch64 %{arm} %{ix86} riscv64"

%build
%make_build clean all

%install
%make_install

#%%files
#%%{!?_licensedir:%%global license %%%%doc}
#%%license LICENSE
#%%doc README
#%%{_rpmmacrodir}/macros.efi

%files -n efi-srpm-macros
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README
%{_rpmmacrodir}/macros.efi-srpm
%{_rpmconfigdir}/brp-boot-efi-times

%files -n efi-filesystem
%defattr(0700,root,root,-)
%dir /boot/efi
%dir /boot/efi/EFI
%dir /boot/efi/EFI/BOOT
%dir /boot/efi/EFI/%{_efi_vendor_}

%changelog
* Thu Apr 2 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6-6
- Source0: use GitHub tag archive (no uploaded release tarball for v6)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6-6
- Prepare for Oreon 11 (RP1)
