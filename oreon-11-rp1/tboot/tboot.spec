%global source0_hash 0fc184ef4c90878d183e719c6a11e77320471e1d4c0fe1a61020132553ad2a72
Summary:        Performs a verified launch using Intel TXT
Name:          tboot
Version:       1.11.7
Release:        1%{?dist}
Epoch:         1
License:       BSD-3-Clause
URL:           http://sourceforge.net/projects/tboot/
Source0:        https://sourceforge.net/projects/tboot/files/%{name}/%{name}-%{version}.tar.gz
Patch0:        tboot-gcc14.patch
Patch1:        openssl-no-engine.patch
Patch2:        tboot-sbin.patch
Patch3:        tboot-1.11.7-len.patch
Requires:      grub2-efi-x64-modules
ExclusiveArch: %{ix86} x86_64
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl
BuildRequires:  zlib-devel
# /oreon:deps
%description
Trusted Boot (tboot) is an open source, pre-kernel/VMM module that uses
Intel Trusted Execution Technology (Intel TXT) to perform a measured
and verified launch of an OS kernel/VMM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%make_build debug=y
%install
%make_install debug=y
%oreon_autofiles main

%post

grub2-mkconfig -o /boot/grub2/grub.cfg
if [ -d /sys/firmware/efi ]; then
	echo "EFI detected .."
	[ -d /boot/grub2/x86_64-efi ] || mkdir -pv /boot/grub2/x86_64-efi
	cp -vf /usr/lib/grub/x86_64-efi/relocator.mod /boot/grub2/x86_64-efi/
	cp -vf /usr/lib/grub/x86_64-efi/multiboot2.mod /boot/grub2/x86_64-efi/
fi
%postun

[ -d /boot/grub2/x86_64-efi ] && rm -rf /boot/grub2/x86_64-efi
grub2-mkconfig -o /etc/grub2.cfg
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.11.7-15
- Import
