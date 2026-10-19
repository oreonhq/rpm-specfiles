%global source0_hash 3f6d50a57f3ed47d8234fd0ab4492634eb7c9aaf7dd902f33d3ac33564fd631d
%undefine _auto_set_build_flags
%global buildarches %{ix86} x86_64
%ifnarch %{buildarches}
%global debug_package %{nil}
%endif
Summary:        Simple kernel loader which boots from a FAT filesystem
Name: syslinux
Version: 6.04
%define tarball_version 6.04-pre1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://syslinux.zytor.com/wiki/index.php/The_Syslinux_Project
Source0:        http://www.kernel.org/pub/linux/utils/boot/%{name}/%{name}-%{tarball_version}.tar.xz
Patch0001: 0001-Add-install-all-target-to-top-side-of-HAVE_FIRMWARE.patch
Patch0002: 0002-ext4-64bit-feature.patch
Patch0003: 0003-include-sysmacros-h.patch
Patch0004: 0004-Add-RPMOPTFLAGS-to-CFLAGS-for-some-stuff.patch
Patch0005: 0005-Workaround-multiple-definition-of-symbol-errors.patch
Patch0006: 0006-Replace-builtin-strlen-that-appears-to-get-optimized.patch
Patch0007: 0007-Fix-backspace-when-editing-a-multiline-cmdline.patch
Patch0008: 0008-Fix-build-with-GCC-14.patch
Patch0009: 0009-Rewrite_Digest_SHA1_to_SHA.patch
Patch0010: 0010-Fix-reported-SAST-findings.patch
Patch0011: 0011-core-Makefile-allow-relocations-on-text-sections.patch
%define _binaries_in_noarch_packages_terminate_build 0
%ifarch %{buildarches}
Requires: syslinux-nonlinux = %{version}-%{release}
%endif
%ifarch %{ix86}
Requires: mtools, libc.so.6
%endif
%ifarch x86_64
Requires: mtools, libc.so.6()(64bit)
%endif
# oreon:deps
BuildRequires:  git
BuildRequires:  make
# /oreon:deps
%description
SYSLINUX is a suite of bootloaders, currently supporting DOS FAT
filesystems, Linux ext2/ext3 filesystems (EXTLINUX), PXE network boots
(PXELINUX), or ISO 9660 CD-ROMs (ISOLINUX).  It also includes a tool,
MEMDISK, which loads legacy operating systems from these media.

%package perl
Summary: Syslinux tools written in perl
%description perl
Syslinux tools written in perl

%package devel
Summary: Headers and libraries for syslinux development.
Provides: %{name}-static = %{version}-%{release}
%description devel
Headers and libraries for syslinux development.

%package extlinux
Summary: The EXTLINUX bootloader, for booting the local system.
Requires: syslinux
Requires: syslinux-extlinux-nonlinux = %{version}-%{release}
%description extlinux
The EXTLINUX bootloader, for booting the local system, as well as all
the SYSLINUX/PXELINUX modules in /boot.

%ifarch x86_64
%package tftpboot
Summary: SYSLINUX modules in /tftpboot, available for network booting
BuildArch: noarch
%description tftpboot
All the SYSLINUX/PXELINUX modules directly available for network
booting in the /tftpboot directory.

%package extlinux-nonlinux
Summary: The parts of the EXTLINUX bootloader which aren't run from linux.
Requires: syslinux
BuildArch: noarch
ExclusiveArch: %{ix86} x86_64
%description extlinux-nonlinux
All the EXTLINUX binaries that run from the firmware rather than
from a linux host.

%package nonlinux
Summary: SYSLINUX modules which aren't run from linux.
Requires: syslinux
BuildArch: noarch
ExclusiveArch: %{ix86} x86_64
%description nonlinux
All the SYSLINUX binaries that run from the firmware rather than from a
linux host. It also includes a tool, MEMDISK, which loads legacy operating
systems from media.
%endif

%ifarch x86_64
%package efi64
Summary: SYSLINUX binaries and modules for 64-bit UEFI systems
%description efi64
SYSLINUX binaries and modules for 64-bit UEFI systems
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am -n syslinux-%{tarball_version}

%build

%ifarch %{buildarches}
make RPMCFLAGS='%{optflags}' RPMLDFLAGS='%{build_ldflags}' bios clean all
%endif
%ifarch x86_64
make RPMCFLAGS='%{optflags}' RPMLDFLAGS='%{build_ldflags}' efi64 clean all
%endif
%install
%ifarch %{buildarches}
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_prefix}/lib/syslinux
mkdir -p %{buildroot}%{_includedir}
make bios install-all \
	INSTALLROOT=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_sbindir} \
	LIBDIR=%{_prefix}/lib DATADIR=%{_datadir} \
	MANDIR=%{_mandir} INCDIR=%{_includedir} \
	TFTPBOOT=/tftpboot EXTLINUXDIR=/boot/extlinux \
	LDLINUX=ldlinux.c32
%ifarch x86_64
make efi64 install netinstall \
	INSTALLROOT=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_sbindir} \
	LIBDIR=%{_prefix}/lib DATADIR=%{_datadir} \
	MANDIR=%{_mandir} INCDIR=%{_includedir} \
	TFTPBOOT=/tftpboot EXTLINUXDIR=/boot/extlinux \
	LDLINUX=ldlinux.c32
%endif
mkdir -p %{buildroot}%{_pkgdocdir}/sample
install -m 644 sample/sample.* %{buildroot}%{_pkgdocdir}/sample/
mkdir -p %{buildroot}/etc
( cd %{buildroot}/etc && ln -s ../boot/extlinux/extlinux.conf . )
rm -f %{buildroot}%{_prefix}/lib/libsyslinux*
rm -f %{buildroot}%{_includedir}/syslinux.h
%endif
%ifarch %{buildarches}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post extlinux

if [ -f /boot/extlinux/extlinux.conf ]; then \
	extlinux --update /boot/extlinux ; \
elif [ -f /boot/extlinux.conf ]; then \
	mkdir -p /boot/extlinux && \
	mv /boot/extlinux.conf /boot/extlinux/extlinux.conf && \
	extlinux --update /boot/extlinux ; \
fi
%endif
%files -f %{oreon_filedir}/main.list
%files -n syslinux-perl -f %{oreon_filedir}/syslinux-perl.list
%files -n syslinux-devel -f %{oreon_filedir}/syslinux-devel.list
%files -n syslinux-extlinux -f %{oreon_filedir}/syslinux-extlinux.list

%changelog

* Thu Apr 2 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.04-0.35
- Source0 path Testing/6.04 on cdn.kernel.org (6.04-pre1 moved)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.04-0.35
- Prepare for Oreon 11 (RP1)
