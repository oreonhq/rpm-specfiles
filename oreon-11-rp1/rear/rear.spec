%global source0_hash 04dd1d06d2c38908935199a8f74499f107dce3dbdc19122b9286bc22dcc78ea3
%global debug_package %{nil}
Name: rear
Version: 2.9
Release:        1%{?dist}
Summary:        Relax-and-Recover is a Linux disaster recovery and system migration tool
URL: https://relax-and-recover.org
License: GPL-3.0-or-later AND LGPL-2.1-or-later
Source0:        https://github.com/rear/rear/archive/refs/tags/%{version}.tar.gz#/rear-%{version}.tar.gz
Source1: rear.cron
Source2: rear.service
Source3: rear.timer
Patch122: rear-skip-longhorn-iscsi-RHEL-83551.patch
Patch123: rear-detect-prep-boot-on-gpt-RHEL-82098.patch
Patch124: rear-support-multi-keyslot-luks-RHEL-83776.patch
Patch125: rear-rescue-ed25519-hostkey-support-RHEL-83479.patch
Patch126: rear-print-disk-mapping-with-sizes-RHEL-83241.patch
Patch127: rear-support-aarch64-uefi-RHEL-56045.patch
Patch128: rear-sshd-el10-RHEL-109270.patch
Patch129: rear-fix-powerNV-support-RHEL-134218.patch
Patch130: rear-fix-duplicate-auto-recovery-RHEL-110659.patch
Patch131: rear-fix-script-sorting-RHEL-132181.patch
Patch132: rear-dbus-broker-RHEL-134213.patch
Patch202: rear-bz1747468.patch
Patch204: rear-bz2120736.patch
Patch205: rear-bz2188593-nbu-systemd.patch
Patch206: rear-nbu-RHEL-17390-RHEL-17393.patch
ExclusiveArch: %ix86 x86_64 ppc ppc64 ppc64le ia64 s390x %arm aarch64
%ifarch %ix86 x86_64
Requires: syslinux-extlinux
%endif
%ifarch ppc ppc64 ppc64le
%if "%{_sbindir}" == "%{_bindir}"
Requires:   /usr/bin/ofpathname
Requires:   /usr/bin/bootlist
%else
Requires:   /usr/sbin/ofpathname
Requires:   /usr/sbin/bootlist
%endif
%endif
%ifarch s390x
Requires:   s390utils-base
Requires:   s390utils-core
%endif
%ifarch %{efi}
Requires: dosfstools
Requires: grub2-efi-%{efi_arch}-modules
Requires: grub2-tools-extra
%endif
Requires: attr
Requires: bc
Requires: binutils
Requires: dhcpcd
Requires: ethtool
Requires: file
Requires: gawk
Requires: gzip
Requires: iproute
Requires: iputils
Requires: openssl
Requires: parted
Requires: tar
%ifnarch s390x
Requires: xorriso
%endif
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  efi-srpm-macros
BuildRequires:  git-core
BuildRequires:  make
# /oreon:deps
%description
Relax-and-Recover is the leading Open Source disaster recovery and system
migration solution. It comprises of a modular
frame-work and ready-to-go workflows for many common situations to produce
a bootable image and restore from backup using this image. As a benefit,
it allows to restore to different hardware and can therefore be used as
a migration tool as well.

Currently Relax-and-Recover supports various boot media (incl. ISO, PXE,
OBDR tape, USB or eSATA storage), a variety of network protocols (incl.
sftp, ftp, http, nfs, cifs) as well as a multitude of backup strategies
(incl.  IBM TSM, MircroFocus Data Protector, Symantec NetBackup, EMC NetWorker,
Bacula, Bareos, BORG, Duplicity, rsync).

Relax-and-Recover was designed to be easy to set up, requires no maintenance
and is there to assist when disaster strikes. Its setup-and-forget nature
removes any excuse for not having a disaster recovery solution implemented.

Professional services and support are available.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -S git

# Change /lib to /usr/lib for COPY_AS_IS
sed -E -e "s:([\"' ])/lib:\1/usr/lib:g" \
    -i usr/share/rear/prep/GNU/Linux/*include*.sh

# Same for Linux.conf
sed -e 's:/lib/:/usr/lib/:g' \
    -e 's:/lib\*/:/usr/lib\*/:g' \
    -e 's:/usr/usr/lib:/usr/lib:g' \
    -i 'usr/share/rear/conf/GNU/Linux.conf'

%build

TZ=UTC %make_build doc
%install
%make_install sbindir=%{_sbindir}
install -p -d %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE3} %{buildroot}%{_docdir}/%{name}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9-7
- Prepare for Oreon 11 (RP1)
