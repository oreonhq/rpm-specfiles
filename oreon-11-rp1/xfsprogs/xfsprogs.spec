# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 310c11e9e1d336064921cc123de5c84a331d5abe3c3b82aeadb89a191d34b449
%global source1_hash 85ccf3ce59cec2023c3eecf31051011a8af6e8b25ef1f21b4f7fcd92236135d1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:	Utilities for managing the XFS filesystem
Name:		xfsprogs
Version:	7.3.0
Release:	1%{?dist}
License:	GPL-1.0-or-later AND LGPL-2.1-or-later
URL:		https://xfs.wiki.kernel.org
Source0:	https://kernel.org/pub/linux/utils/fs/xfs/xfsprogs/%{name}-%{version}.tar.xz
Source1:	https://kernel.org/pub/linux/utils/fs/xfs/xfsprogs/%{name}-%{version}.tar.sign
Source2:	https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/46A7EA18AC33E108.asc

BuildRequires: oreon-rpm-macros
BuildRequires:	make
BuildRequires:	clang
BuildRequires:	libtool
BuildRequires:	gettext
BuildRequires:	libattr-devel
BuildRequires:	libuuid-devel
BuildRequires:	libedit-devel
BuildRequires:	libblkid-devel >= 2.17-0.1.git5e51568
BuildRequires:	libicu-devel >= 4.6
BuildRequires:	systemd
BuildRequires:	xz
BuildRequires:	inih-devel
BuildRequires:	liburcu-devel
BuildRequires:	openpgpverify
Provides:	xfs-cmds
Obsoletes:	xfs-cmds <= %{version}
Provides:	xfsprogs-qa-devel
Obsoletes:	xfsprogs-qa-devel <= %{version}
Conflicts:	xfsdump < 3.0.1
Suggests:	xfsprogs-xfs_scrub

%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/fsck.xfs
Provides:       /usr/sbin/mkfs.xfs
%endif

%description
A set of commands to use the XFS filesystem, including mkfs.xfs.

XFS is a high performance journaling filesystem which originated
on the SGI IRIX platform.  It is completely multi-threaded, can
support large files and large filesystems, extended attributes,
variable block sizes, is extent based, and makes extensive use of
Btrees (directories, extents, free space) to aid both performance
and scalability.

This implementation is on-disk compatible with the IRIX version
of XFS.

%package devel
Summary:	XFS filesystem-specific headers
Requires:	xfsprogs = %{version}-%{release}, libuuid-devel

%description devel
xfsprogs-devel contains the header files needed to develop XFS
filesystem-specific programs.

You should install xfsprogs-devel if you want to develop XFS
filesystem-specific programs,  If you install xfsprogs-devel, you'll
also want to install xfsprogs.

%package xfs_scrub
Summary:	XFS filesystem online scrubbing utilities
Requires:	xfsprogs = %{version}-%{release}, python3
Requires:	util-linux

%description xfs_scrub
xfs_scrub attempts to check and repair all metadata in a mounted XFS filesystem.
WARNING!  This program is EXPERIMENTAL, which means that its behavior and
interface could change at any time!

%package xfs_extras
Summary:	XFS filesystem extra utilities
Requires:	xfsprogs = %{version}-%{release}, python3
Requires:	util-linux

%description xfs_extras
Extra utilities for XFS filesystems, such as xfs_protofile, that may require
Python.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
xzcat '%{SOURCE0}' | %{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup -p1

sed -r -i 's/\$\(LIBICU_LIBS\)/\0 -licuuc/' scrub/Makefile

%build
export tagname=CC

%configure \
	--enable-editline=yes	\
	--enable-blkid=yes	\
	--enable-lto=no

%make_build

%install
make DIST_ROOT=$RPM_BUILD_ROOT install install-dev \
	PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir}

rm -f $RPM_BUILD_ROOT/{%{_lib}/*.{la,a,so},%{_libdir}/*.{la,a}}

rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/xfsprogs/

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc doc/CHANGES README
%{_libdir}/*.so.*
%dir %{_libexecdir}/xfsprogs
%{_libexecdir}/xfsprogs/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_unitdir}/*
%{_sbindir}/*
%{_datadir}/xfsprogs/mkfs/*.conf
%dir %{_datadir}/xfsprogs/
%dir %{_datadir}/xfsprogs/mkfs/
%exclude %{_datadir}/xfsprogs/xfs_scrub_all.cron
%exclude %{_sbindir}/xfs_scrub*
%exclude %{_sbindir}/xfs_protofile*
%exclude %{_mandir}/man8/xfs_scrub*
%exclude %{_mandir}/man8/xfs_protofile*
%exclude %{_libexecdir}/xfsprogs/xfs_scrub*
%exclude %{_unitdir}/*xfs_scrub*

%files xfs_scrub
%{_sbindir}/xfs_scrub*
%{_mandir}/man8/xfs_scrub*
%{_libexecdir}/xfsprogs/xfs_scrub*
%{_unitdir}/*xfs_scrub*
%{_udevrulesdir}/64-xfs.rules
%{_datadir}/xfsprogs/xfs_scrub_all.cron

%files xfs_extras
%{_sbindir}/xfs_protofile*
%{_mandir}/man8/xfs_protofile*

%files devel
%{_mandir}/man2/*
%{_mandir}/man3/*
%dir %{_includedir}/xfs
%{_includedir}/xfs/handle.h
%{_includedir}/xfs/jdm.h
%{_includedir}/xfs/linux.h
%{_includedir}/xfs/xfs.h
%{_includedir}/xfs/xfs_arch.h
%{_includedir}/xfs/xfs_fs.h
%{_includedir}/xfs/xfs_fs_compat.h
%{_includedir}/xfs/xfs_types.h
%{_includedir}/xfs/xfs_format.h
%{_includedir}/xfs/xfs_da_format.h
%{_includedir}/xfs/xfs_log_format.h
%{_includedir}/xfs/xqm.h

%{_libdir}/*.so

%changelog
%autochangelog
