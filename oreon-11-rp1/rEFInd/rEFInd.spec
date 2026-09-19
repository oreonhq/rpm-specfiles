%global source0_hash f7d93ce80da76b86c567281ea225b6a87907ce86ff77233c9357a522c115c8f0

# Local definition of arm32 if missing
%{!?arm32:%global arm32 %{arm}}

# EFI/UEFI binaries are not ELF, but PE32/PE32+/COFF
%global debug_package %{nil}

# Disable LTO because it breaks EFI binary build
%global _lto_cflags %{nil}

# GNU-EFI static libraries path from gnu-efi 3.0.18+
%global gnu_efi_libdir %{_prefix}/lib

%global _description %{expand:
A graphical boot manager for EFI- and UEFI-based computers, such as all
Intel-based Macs and recent (most 2011 and later) PCs. rEFInd presents a
boot menu showing all the EFI boot loaders on the EFI-accessible
partitions, and optionally BIOS-bootable partitions on Macs and BIOS boot
entries on UEFI PCs with CSMs. EFI-compatible OSes, including Linux,
provide boot loaders that rEFInd can detect and launch. rEFInd can launch
Linux EFI boot loaders such as ELILO, GRUB Legacy, GRUB 2, and 3.3.0 and
later kernels with EFI stub support. EFI file system drivers for ext2/3/4fs,
ReiserFS, Btrfs, NTFS, HFS+, and ISO-9660 enable rEFInd to read boot
loaders from these file systems, too. rEFInd's ability to detect boot
loaders at run time makes it very easy to use, particularly when paired with
Linux kernels that provide EFI stub support.
}

Name:		rEFInd
Version:	0.14.2
Release:	5%{?dist}
Summary:	User friendly EFI boot manager
License:	GPL-3.0-or-later

URL:		http://www.rodsbooks.com/refind/
Source0:	https://sourceforge.net/projects/refind/files/%{version}/refind-src-%{version}.tar.gz
# Replace wrong Fedora icon with correct version
Source1:	os_fedora.png
# Add --nvramonly option to refind-install
Patch0: 	install-nvram-only.patch
# Support 32-bit EFI on 64-bit OS (and vice versa)
Patch1:		detect-efi-size.patch
# Fix building on AArch64 natively
Patch2:		fix-aarch64-efi-build.patch
# Replaces outdated objcopy target option
Patch3:		fix-target-option.patch

ExclusiveArch:  %{efi}
# rEFInd doesn't work on 32-bit arm
ExcludeArch:    %{arm32}
BuildRequires:  gcc
BuildRequires:  make
# Ensure we have the correct paths
BuildRequires:	gnu-efi-devel >= 3.0.18
Requires:	efi-filesystem
Requires:	efibootmgr
Requires:	%{name}-tools = %{version}-%{release}
Requires:	%{name}-bootloader-%{efi_arch} = %{version}
Suggests:	%{name}-signed-%{efi_arch}

# These were vendored and adapted into rEFInd long ago...
## License: BSD-3-Clause
Provides:       bundled(libeg)
## License: BSD-3-Clause
Provides:       bundled(LodePNG)
## License: MIT
Provides:       bundled(NanoJPEG)

%description %{_description}

%files
# Empty metpackage

# ---------------------------------------------------------------

%package tools
Summary:	User friendly EFI boot manager (management tools)
BuildArch:	noarch

%description tools %{_description}
This package provides the tools to manage the installation
of %{name} on your system.

%files tools
%doc NEWS.txt README.txt docs/Styles docs/refind
%doc VERSION README.install
%license COPYING.txt LICENSE.txt CREDITS.txt
%{_sbindir}/mkrlconf
%{_sbindir}/mvrefind
%{_sbindir}/refind-install
%{_sbindir}/refind-mkdefault
%{_mandir}/man8/mkrlconf.8*
%{_mandir}/man8/mvrefind.8*
%{_mandir}/man8/refind-install.8*
%{_mandir}/man8/refind-mkdefault.8*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/banners/
%{_datadir}/%{name}/fonts/
%{_datadir}/%{name}/refind-install
%dir %{_datadir}/%{name}/refind
%{_datadir}/%{name}/refind/icons/
%{_datadir}/%{name}/refind/refind.conf-sample

# ---------------------------------------------------------------

%package unsigned-%{efi_arch}
Summary:	User friendly EFI boot manager (unsigned binaries)
Requires:	%{name}-tools = %{version}-%{release}
Provides:	%{name}-bootloader = %{version}
Provides:	%{name}-bootloader-%{efi_arch} = %{version}
BuildArch:	noarch

%description unsigned-%{efi_arch} %{_description}
This package provides the unsigned EFI binaries for the rEFInd bootloader.

This package is only useful if your system does not have UEFI Secure Boot
enabled.

%files unsigned-%{efi_arch}
%{_datadir}/%{name}/refind/drivers_%{efi_arch}/
%{_datadir}/%{name}/refind/refind_%{efi_arch}.efi
%{_datadir}/%{name}/refind/tools_%{efi_arch}/

# ---------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n refind-%{version} -p1
cp %{SOURCE1} icons/

%build
make GNUEFILIB=%{gnu_efi_libdir} EFILIB=%{gnu_efi_libdir} EFICRT0=%{gnu_efi_libdir}  LIBDIR=%{_libdir} GNUEFI_ARM64_TARGET_SUPPORT=y all_gnuefi

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/refind/

# Copy the rEFInd binaries (rEFInd proper and drivers)
install -Dp -m0644 refind/refind*.efi %{buildroot}%{_datadir}/%{name}/refind/
mkdir -p %{buildroot}%{_datadir}/%{name}/refind/drivers_%{efi_arch}
cp -a drivers_%{efi_arch}/* %{buildroot}%{_datadir}/%{name}/refind/drivers_%{efi_arch}/
mkdir -p %{buildroot}%{_datadir}/%{name}/refind/tools_%{efi_arch}
install -Dp -m0644 gptsync/gptsync_%{efi_arch}.efi %{buildroot}%{_datadir}/%{name}/refind/tools_%{efi_arch}/gptsync_%{efi_arch}.efi

# Copy configuration and support files
install -Dp -m0644 refind.conf-sample %{buildroot}%{_datadir}/%{name}/refind/
cp -a icons %{buildroot}%{_datadir}/%{name}/refind/
rm -rf %{buildroot}%{_datadir}/%{name}/refind/icons/svg
install -Dp -m0755 refind-install %{buildroot}%{_datadir}/%{name}/

# Copy man pages
mkdir -p %{buildroot}%{_mandir}/man8
install -Dp -m0644 docs/man/mvrefind.8 %{buildroot}%{_mandir}/man8
install -Dp -m0644 docs/man/mkrlconf.8 %{buildroot}%{_mandir}/man8
install -Dp -m0644 docs/man/refind-install.8 %{buildroot}%{_mandir}/man8
install -Dp -m0644 docs/man/refind-mkdefault.8 %{buildroot}%{_mandir}/man8

# Copy scripts
mkdir -p %{buildroot}%{_sbindir}
install -Dp -m0755 mkrlconf %{buildroot}%{_sbindir}/
install -Dp -m0755 mvrefind %{buildroot}%{_sbindir}/
install -Dp -m0755 refind-mkdefault %{buildroot}%{_sbindir}/
ln -sr %{buildroot}%{_datadir}/%{name}/refind-install %{buildroot}%{_sbindir}

# Copy banners and fonts
cp -a banners %{buildroot}%{_datadir}/%{name}/
cp -a fonts %{buildroot}%{_datadir}/%{name}/

# Create version file and install README file
echo %{version} > VERSION
echo "Version %{version} of the rEFInd boot manager is now available."   > README.install
echo "To install it in the ESP, execute the command 'refind-install'."  >> README.install
echo "If you are having no problems with booting your system, there is" >> README.install
echo "no need to install this update in the ESP."                       >> README.install

%changelog
%autochangelog
