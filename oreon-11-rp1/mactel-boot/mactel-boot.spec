%global source0_hash 0305aeddc171078848cb562caf2f095a61c4dd73f12cbe617dcbcd84077de506
Name:		mactel-boot
Version:	0.9
Release:        37%{?dist}
Summary:        Intel Mac boot files
License:	GPL-2.0-or-later
URL:		http://www.codon.org.uk/~mjg59/mactel-boot/
Source0:        http://www.codon.org.uk/~mjg59/mactel-boot/%{name}-%{version}.tar.bz2
Source1:	mactel-boot-setup
Patch0:		mactel-boot-c99.patch
ExclusiveArch:	%{x86_64}
Requires:	coreutils
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Files for booting Fedora on Intel-based Apple hardware using EFI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build PRODUCTVERSION="Fedora %{fedora}"
%install
%make_install
install -Dpm 644 SystemVersion.plist %{buildroot}/boot/efi/System/Library/CoreServices/SystemVersion.plist
echo "This file is required for booting" >%{buildroot}/boot/efi/mach_kernel
touch %{buildroot}/boot/efi/System/Library/CoreServices/boot.efi
touch %{buildroot}/boot/efi/.VolumeIcon.icns
install -D %{SOURCE1} %{buildroot}%{_libexecdir}/mactel-boot-setup
%if "%{_sbindir}" != "/usr/sbin"
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_prefix}/sbin/* %{buildroot}%{_sbindir}
rmdir %{buildroot}%{_prefix}/sbin
%oreon_autofiles main
%endif
%triggerin -- grub-efi grub2-efi fedora-logos generic-logos

%{_libexecdir}/mactel-boot-setup
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
