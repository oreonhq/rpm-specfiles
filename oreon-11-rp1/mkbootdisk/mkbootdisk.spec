%global source0_hash d4656089d8e9e9f92dd79c4901fb77c333c9193d2cdcc61b6791c8797493cf0e

Summary: Creates a boot floppy disk for booting a system
Name: mkbootdisk
Version:  1.5.5
Release: 39%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: mkbootdisk-%{version}.tar.xz
Patch0: mkbootdisk-1.5.5-fix-long-volid.patch
Patch1: mkbootdisk-1.5.5-man-dracut.patch
Patch2: mkbootdisk-1.5.5-syslinux-5-fix.patch
BuildArch: noarch
ExclusiveOs: Linux
ExclusiveArch: %{ix86} sparc sparc64 x86_64
BuildRequires: make
Requires: genisoimage
%ifnarch sparc sparc64
Requires: syslinux
%else
Requires: silo genromfs
%endif

%description
The mkbootdisk program creates a standalone boot floppy disk for
booting the running system.  The created boot disk will look for the
root filesystem on the device mentioned in /etc/fstab and includes an
initial ramdisk image which will load any necessary SCSI modules for
the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fix-long-volid
%patch -P1 -p1 -b .man-dracut
%patch -P2 -p1 -b .syslinux-5-fix

%install
rm -rf $RPM_BUILD_ROOT
make BUILDROOT=$RPM_BUILD_ROOT mandir=%{_mandir} install

%files
%doc COPYING
%attr(755,root,root) /sbin/mkbootdisk
%attr(644,root,root) %{_mandir}/man8/mkbootdisk.8*

%changelog
%autochangelog
