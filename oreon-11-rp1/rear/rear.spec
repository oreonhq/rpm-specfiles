# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 04dd1d06d2c38908935199a8f74499f107dce3dbdc19122b9286bc22dcc78ea3
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# this is purely a shell script, so no debug packages
%global debug_package %{nil}

Name: rear
Version: 2.9
Release: 7%{?dist}
Summary: Relax-and-Recover is a Linux disaster recovery and system migration tool
URL: https://relax-and-recover.org

License: GPL-3.0-or-later AND LGPL-2.1-or-later

Source0: https://github.com/rear/rear/archive/%{version}/rear-%{version}.tar.gz
# Add cronjob and systemd timer as documentation
Source1: rear.cron
Source2: rear.service
Source3: rear.timer

# Required for HTML user guide
BuildRequires: asciidoctor
BuildRequires: efi-srpm-macros
# Needed for %%autosetup -S git
BuildRequires: git-core
BuildRequires: make

######################
# upstream backports #
######################
# Patch101 - Patch121 Reserved
# skip longhorn iscsi devices in disklayout.conf
# https://github.com/rear/rear/commit/d765abff976a8346ce6afa432c9a09d67ed63482
Patch122: rear-skip-longhorn-iscsi-RHEL-83551.patch

# fix PPC PReP Boot detection on GPT layouts
# https://github.com/rear/rear/commit/1ca518c2a0e675ace956ef71bc79d67e4990562b
Patch123: rear-detect-prep-boot-on-gpt-RHEL-82098.patch

# fix recovery of LUKS encrypted systems with multiple keyslots
# https://github.com/rear/rear/commit/e9ce93f096e505968cc728a7eb5a06e25dc8d88b
Patch124: rear-support-multi-keyslot-luks-RHEL-83776.patch

# support generation of ed25519 SSH host keys in the rescue image
# https://github.com/rear/rear/commit/62d9a744ff710de34035ce15bd1b1bf810b6934a
Patch125: rear-rescue-ed25519-hostkey-support-RHEL-83479.patch

# enhance the 300_map_disks.sh script to also print the disk sizes
# https://github.com/rear/rear/commit/43d62fdfcac50b35be4f99d45bac3b5340525a7a
Patch126: rear-print-disk-mapping-with-sizes-RHEL-83241.patch

# add initial support for arm/aarch64 machines with UEFI
# https://github.com/rear/rear/commit/9b28f14fad26ff00a6f90b13c3e4906d85f3ae3c
Patch127: rear-support-aarch64-uefi-RHEL-56045.patch

# Copy a sshd helper to the rescue ramdisk, necessary on EL10
# https://github.com/rear/rear/commit/8497de2d8a029460b0e47119b0664f0d254c97ac
Patch128: rear-sshd-el10-RHEL-109270.patch

# fix support for PowerNV machines without PPC PReP partitions
# https://github.com/rear/rear/commit/79a3b50a0effcf4c1a43e9dfe1b8d0427ee0bf02
Patch129: rear-fix-powerNV-support-RHEL-134218.patch

# fix duplicate execution of automated recovery
# https://github.com/rear/rear/commit/8a122cb5cfc28ce8c83baa963ad12f1c42e1c908
# https://github.com/rear/rear/commit/fe5397d9da7ab95abfa93533c2cb3efd61f6ca05
Patch130: rear-fix-duplicate-auto-recovery-RHEL-110659.patch

# fix sorting of stage scripts
# https://github.com/rear/rear/commit/95ecb7e024aa187ea6babd49eac1b4c9c3aba106
Patch131: rear-fix-script-sorting-RHEL-132181.patch

# add support for dbus broker
# https://github.com/rear/rear/commit/61d294b9635b3c71bd58409e810bccb705b1220c
Patch132: rear-dbus-broker-RHEL-134213.patch

# EL9-only
# Patch133:
# Patch134:
# Patch135:
# Patch136:

######################
# downstream patches #
######################
# No-longer applicable
# Patch201: rear-bz1492177-warning.patch

# avoid vgcfgrestore on unsupported volume types
# https://github.com/pcahyna/rear/commit/5d5d1db3ca621eb80b9481924d1fc470571cfc09
Patch202: rear-bz1747468.patch

# No-longer applicable
# Patch203: rear-bz2119501.patch

# additional fixes for NBU support
Patch204: rear-bz2120736.patch
Patch205: rear-bz2188593-nbu-systemd.patch
Patch206: rear-nbu-RHEL-17390-RHEL-17393.patch

# rear contains only bash scripts plus documentation so that on first glance it could be "BuildArch: noarch"
# but actually it is not "noarch" because it only works on those architectures that are explicitly supported.
# Of course the rear bash scripts can be installed on any architecture just as any binaries can be installed on any architecture.
# But the meaning of architecture dependent packages should be on what architectures they will work.
# Therefore only those architectures that are actually supported are explicitly listed.
# This avoids that rear can be "just installed" on architectures that are actually not supported:
ExclusiveArch: %ix86 x86_64 ppc ppc64 ppc64le ia64 s390x %arm aarch64
# Furthermore for some architectures it requires architecture dependent packages (like syslinux for x86 and x86_64)
# so that rear must be architecture dependent because ifarch conditions never match in case of "BuildArch: noarch"
# see the GitHub issue https://github.com/rear/rear/issues/629
%ifarch %ix86 x86_64
Requires: syslinux-extlinux
%endif
%ifarch ppc ppc64 ppc64le
# ofpathname called by grub2-install (except on PowerNV)
# bootlist needed to make PowerVM LPARs bootable
%if "%{_sbindir}" == "%{_bindir}"
Requires:   /usr/bin/ofpathname
Requires:   /usr/bin/bootlist
%else
Requires:   /usr/sbin/ofpathname
Requires:   /usr/sbin/bootlist
%endif
%endif
%ifarch s390x
# Contain many utilities for working with DASDs
Requires:   s390utils-base
Requires:   s390utils-core
%endif

# See https://github.com/rhboot/efi-rpm-macros/blob/main/README
%ifarch %{efi}
# We need mkfs.vfat for recreating EFI System Partition
Requires: dosfstools
# Needed for ISO image creation
Requires: grub2-efi-%{efi_arch}-modules
Requires: grub2-tools-extra
%endif


### Mandatory dependencies:
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
# No ISO image support on s390x (may change when we add support for LPARs)
%ifnarch s390x
Requires: xorriso
%endif
%if 0%{?rhel}
Requires: util-linux
%endif

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
%oreon_verify_sources
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
# build HTML user guide
# asciidoc writes a timestamp to files it produces, based on the last
# modified date of the source file, but is sensitive to the timezone.
# This makes the results differ according to the timezone of the build machine
# and spurious changes will be seen.
# Set the timezone to UTC as a workaround.
# https://wiki.debian.org/ReproducibleBuilds/TimestampsInDocumentationGeneratedByAsciidoc
TZ=UTC %make_build doc

%install
%make_install sbindir=%{_sbindir}
install -p -d %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE3} %{buildroot}%{_docdir}/%{name}/

#-- FILES ---------------------------------------------------------------------#
%files
%license COPYING
%doc MAINTAINERS README.md doc/user-guide doc/*.txt
%dir %{_sysconfdir}/rear/
%config(noreplace) %{_sysconfdir}/rear/local.conf
%{_datadir}/rear/
%{_docdir}/%{name}/rear.*
%{_mandir}/man8/rear.8*
%{_sbindir}/rear
%{_sharedstatedir}/rear/

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9-7
- Prepare for Oreon 11 (RP1)
