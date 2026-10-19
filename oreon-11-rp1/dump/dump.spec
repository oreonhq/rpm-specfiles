%global source0_hash 4042997bdfed463c7a0bf8788229718b9c692ce2cfafe46ea54d478bcd663591
%define PREVER b52
%define DUMP_VERSION 0.4%{PREVER}
Summary:        Programs for backing up and restoring ext2/ext3/ext4 filesystems
Name:          dump
Epoch:         1
Version:       0.4
Release:        1%{?dist}
License:       BSD-3-Clause
URL:           https://sourceforge.net/projects/dump/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{DUMP_VERSION}.tar.gz
Requires:      setup
Requires:      rmt
Patch101:      dump-replacement.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  device-mapper-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  libblkid-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  lzo-devel
BuildRequires:  lzo-minilzo
BuildRequires:  make
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n dump-%{DUMP_VERSION}

%build

autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS -Wall -Wpointer-arith -Wstrict-prototypes \
-Wmissing-prototypes -Wno-char-subscripts -fno-strict-aliasing"
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
    ln -sf restore .%{_sbindir}/rrestore
    mkdir -p .%{_sysconfdir}
    > .%{_sysconfdir}/dumpdates
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4-0.62.
- Prepare for Oreon 11 (RP1)
