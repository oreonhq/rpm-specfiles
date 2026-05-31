%global source0_hash 4042997bdfed463c7a0bf8788229718b9c692ce2cfafe46ea54d478bcd663591

%define PREVER b52
%define DUMP_VERSION 0.4%{PREVER}

%if 0%{?rhel}
Summary:       Program for restoring ext2/ext3 filesystems
Name:          restore
%else
Summary:       Programs for backing up and restoring ext2/ext3/ext4 filesystems
Name:          dump
%endif
Epoch:         1
Version:       0.4
Release:       0.62.%{PREVER}%{?dist}
License:       BSD-3-Clause
URL:           https://sourceforge.net/projects/dump/
Source:        https://downloads.sourceforge.net/dump/dump-%{DUMP_VERSION}.tar.gz
BuildRequires: e2fsprogs-devel >= 1.18, readline-devel >= 4.2
BuildRequires: zlib-devel, bzip2-devel, automake, make
BuildRequires: device-mapper-devel, libselinux-devel
BuildRequires: lzo-minilzo
BuildRequires: lzo-devel, libtool
BuildRequires: libblkid-devel libuuid-devel
# This Requires is now mandatory because we need to ensure the "disk"
# group is created before installation (#60461)
Requires:      setup
Requires:      rmt
%if 0%{?fedora}
Obsoletes:     dump-static <= 0.4
Provides:      dump-static
%endif

# No dump package in RHEL (restore remains)
Patch101:      dump-replacement.patch

%if 0%{?rhel}
%description
The restore command performs the inverse function of dump; it can
restore a full backup of a filesystem. Subsequent incremental backups
can then be layered on top of the full backup. Single files and
directory subtrees may also be restored from full or partial backups.

Install restore if you need restoring filesystems after backups
made by dump.
%else
%description
The dump package contains both dump and restore. Dump examines files
in a filesystem, determines which ones need to be backed up, and
copies those files to a specified disk, tape, or other storage medium.
The restore command performs the inverse function of dump; it can
restore a full backup of a filesystem. Subsequent incremental backups
can then be layered on top of the full backup. Single files and
directory subtrees may also be restored from full or partial backups.

Install dump if you need a system for both backing up filesystems and
restoring filesystems after backups.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n dump-%{DUMP_VERSION}

%if 0%{?rhel}
rm -rf dump/*.c
%patch 101 -p1
%endif

%build
autoreconf -fiv

export CFLAGS="$RPM_OPT_FLAGS -Wall -Wpointer-arith -Wstrict-prototypes \
-Wmissing-prototypes -Wno-char-subscripts -fno-strict-aliasing"

# XXX --enable-kerberos needs krcmd
%configure --disable-static \
    --enable-transselinux \
    --enable-largefile \
    --disable-rmt \
    --enable-qfa \
    --enable-readline \
    --with-binmode=0755 \
    --with-manowner=root \
    --with-mangrp=root \
    --with-manmode=0644

%make_build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8

%make_install \
    SBINDIR=%{buildroot}%{_sbindir} \
    BINDIR=%{buildroot}%{_sbindir} \
    MANDIR=%{buildroot}%{_mandir}/man8 \
    BINOWNER=$(id -un) \
    BINGRP=$(id -gn) \
    MANOWNER=$(id -un) \
    MANGRP=$(id -gn)

pushd %{buildroot}
%if 0%{?fedora}
    ln -sf dump .%{_sbindir}/rdump
%endif
    ln -sf restore .%{_sbindir}/rrestore
    mkdir -p .%{_sysconfdir}
    > .%{_sysconfdir}/dumpdates
popd

%files
%doc AUTHORS COPYING INSTALL KNOWNBUGS MAINTAINERS NEWS README REPORTING-BUGS TODO
%doc dump.lsm
%attr(0664,root,disk) %config(noreplace) %{_sysconfdir}/dumpdates
%if 0%{?fedora}
%{_sbindir}/dump
%{_sbindir}/rdump
%{_mandir}/man8/dump.8*
%{_mandir}/man8/rdump.8*
%endif
%{_sbindir}/restore
%{_sbindir}/rrestore
%{_mandir}/man8/restore.8*
%{_mandir}/man8/rrestore.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4-0.62.
- Prepare for Oreon 11 (RP1)
