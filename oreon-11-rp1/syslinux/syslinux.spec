%global source0_hash 3f6d50a57f3ed47d8234fd0ab4492634eb7c9aaf7dd902f33d3ac33564fd631d

# No, please don't break the build.  Thanks.
%undefine _auto_set_build_flags

%global buildarches %{ix86} x86_64
%ifnarch %{buildarches}
%global debug_package %{nil}
%endif

Summary: Simple kernel loader which boots from a FAT filesystem
Name: syslinux
Version: 6.04
%define tarball_version 6.04-pre1
Release: 0.35%{?dist}
License: GPL-2.0-or-later
URL: http://syslinux.zytor.com/wiki/index.php/The_Syslinux_Project
# Pre-releases live under Testing/6.04/ on kernel.org (top-level path 404)
Source0:        http://www.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{tarball_version}.tar.xz
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

# this is to keep rpmbuild from thinking the .c32 / .com / .0 / memdisk files
# in noarch packages are a reason to stop the build.
%define _binaries_in_noarch_packages_terminate_build 0

BuildRequires: make
BuildRequires: git
%ifarch %{buildarches}
BuildRequires:  gcc
BuildRequires: nasm >= 0.98.38-1, perl-interpreter, perl-generators, netpbm-progs
BuildRequires: perl(FileHandle)
BuildRequires: (glibc-devel(x86-32) or glibc32)
BuildRequires: libuuid-devel
Requires: syslinux-nonlinux = %{version}-%{release}
%endif
%ifarch %{ix86}
Requires: mtools, libc.so.6
BuildRequires: mingw32-gcc
%endif
%ifarch x86_64
Requires: mtools, libc.so.6()(64bit)
BuildRequires: mingw32-gcc mingw64-gcc
%endif

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

# don't ship libsyslinux, at least, not for now
rm -f %{buildroot}%{_prefix}/lib/libsyslinux*
rm -f %{buildroot}%{_includedir}/syslinux.h
%endif

%ifarch %{buildarches}
%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc NEWS README*
%doc doc/* 
%doc sample
%{_mandir}/man1/gethostip*
%{_mandir}/man1/syslinux*
%{_mandir}/man1/isohybrid*
%{_mandir}/man1/memdiskfind*
%{_bindir}/gethostip
%{_bindir}/isohybrid
%{_bindir}/memdiskfind
%{_bindir}/syslinux
%dir %{_datadir}/syslinux
%dir %{_datadir}/syslinux/dosutil
%{_datadir}/syslinux/dosutil/*
%dir %{_datadir}/syslinux/diag
%{_datadir}/syslinux/diag/*
%ifarch %{ix86}
%{_datadir}/syslinux/syslinux.exe
%else
%{_datadir}/syslinux/syslinux64.exe
%endif

%files perl
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_mandir}/man1/lss16toppm*
%{_mandir}/man1/ppmtolss16*
%{_mandir}/man1/syslinux2ansi*
%{_bindir}/keytab-lilo
%{_bindir}/lss16toppm
%{_bindir}/md5pass
%{_bindir}/mkdiskimage
%{_bindir}/ppmtolss16
%{_bindir}/pxelinux-options
%{_bindir}/sha1pass
%{_bindir}/syslinux2ansi
%{_bindir}/isohybrid.pl

%files devel
%{!?_licensedir:%global license %%doc}
%license COPYING
%dir %{_datadir}/syslinux/com32
%{_datadir}/syslinux/com32/*

%files extlinux
%{_sbindir}/extlinux
%{_mandir}/man1/extlinux*
%config /etc/extlinux.conf

%ifarch x86_64
%files tftpboot
/tftpboot

%files nonlinux
%{_datadir}/syslinux/*.com
%{_datadir}/syslinux/*.exe
%{_datadir}/syslinux/*.c32
%{_datadir}/syslinux/*.bin
%{_datadir}/syslinux/*.0
%{_datadir}/syslinux/memdisk

%files extlinux-nonlinux
/boot/extlinux

%else
%exclude %{_datadir}/syslinux/memdisk
%exclude %{_datadir}/syslinux/*.com
%exclude %{_datadir}/syslinux/*.exe
%exclude %{_datadir}/syslinux/*.c32
%exclude %{_datadir}/syslinux/*.bin
%exclude %{_datadir}/syslinux/*.0
%exclude /boot/extlinux
%exclude /tftpboot
%endif

%ifarch x86_64
%files efi64
%{!?_licensedir:%global license %%doc}
%license COPYING
%dir %{_datadir}/syslinux/efi64
%{_datadir}/syslinux/efi64
%endif

%post extlinux
# If we have a /boot/extlinux.conf file, assume extlinux is our bootloader
# and update it.
if [ -f /boot/extlinux/extlinux.conf ]; then \
	extlinux --update /boot/extlinux ; \
elif [ -f /boot/extlinux.conf ]; then \
	mkdir -p /boot/extlinux && \
	mv /boot/extlinux.conf /boot/extlinux/extlinux.conf && \
	extlinux --update /boot/extlinux ; \
fi
%endif

%changelog
* Thu Apr 2 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.04-0.35
- Source0 path Testing/6.04 on cdn.kernel.org (6.04-pre1 moved)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.04-0.35
- Prepare for Oreon 11 (RP1)
