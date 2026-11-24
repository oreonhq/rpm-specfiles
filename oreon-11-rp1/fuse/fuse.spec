# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d0e69d5d608cc22ff4843791ad097f554dd32540ddc9bed7638cc6fea7c1b4b5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:		fuse
Version:	2.9.9
Release:	1%{?dist}
Summary:	File System in Userspace (FUSE) v2 utilities
License:	GPL-1.0-or-later
URL:		https://github.com/libfuse/libfuse/
Source0:	https://github.com/libfuse/libfuse/releases/download/%{name}-%{version}.tar.gz

Patch1: fuse2-0001-More-parentheses.patch
Patch2: fuse2-0002-add-fix-for-namespace-conflict-in-fuse_kernel.h.patch
Patch3: fuse2-0003-make-buffer-size-match-kernel-max-transfer-size.patch
Patch4: fuse2-0004-Whitelist-SMB2-found-on-some-NAS-devices.patch
Patch5:	fuse2-0005-Whitelist-UFSD-backport-to-2.9-branch-452.patch
Patch6: fuse2-0006-Correct-errno-comparison-571.patch
Patch7: fuse2-0007-util-ulockmgr_server.c-conditionally-define-closefro.patch

Requires:	which
Conflicts:	filesystem < 3
BuildRequires: oreon-rpm-macros
BuildRequires:	libselinux-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	make
BuildRequires:  systemd-udev
Requires:       fuse-common >= 3.4.2-4

%description
With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains the FUSE v2 userspace tools to
mount a FUSE filesystem.

%package libs
Summary:	File System in Userspace (FUSE) v2 libraries
License:	LGPL-2.1-or-later
Conflicts:	filesystem < 3

%description libs
Devel With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains the FUSE v2 libraries.

%package devel
Summary:	File System in Userspace (FUSE) v2 devel files
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pkgconfig
License:	LGPL-2.1-or-later
Conflicts:	filesystem < 3

%description devel
With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains development files (headers,
pgk-config) to develop FUSE v2 based applications/filesystems.

%prep
%oreon_sha256
%autosetup -p 1

export ACLOCAL_PATH=/usr/share/gettext/m4/
sed -i 's|mknod|echo Disabled: mknod |g' util/Makefile.in
autoreconf -ivf

%build
export MOUNT_FUSE_PATH="%{_sbindir}"
CFLAGS="%{optflags} -D_GNU_SOURCE" %configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
install -m 0755 lib/.libs/libfuse.so.%{version} %{buildroot}/%{_libdir}
install -m 0755 lib/.libs/libulockmgr.so.1.0.1 %{buildroot}/%{_libdir}
install -p fuse.pc %{buildroot}/%{_libdir}/pkgconfig/
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 util/fusermount %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 util/mount.fuse %{buildroot}/%{_sbindir}
install -m 0755 util/ulockmgr_server %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_includedir}/fuse
install -p include/old/fuse.h %{buildroot}/%{_includedir}/
install -p include/ulockmgr.h %{buildroot}/%{_includedir}/
for i in cuse_lowlevel.h fuse_common_compat.h fuse_common.h fuse_compat.h fuse.h fuse_lowlevel_compat.h fuse_lowlevel.h fuse_opt.h; do
	install -p include/$i %{buildroot}/%{_includedir}/fuse/
done
mkdir -p %{buildroot}/%{_mandir}/man1/
cp -a doc/fusermount.1 doc/ulockmgr_server.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{_mandir}/man8/
cp -a doc/mount.fuse.8 %{buildroot}/%{_mandir}/man8/
pushd %{buildroot}/%{_libdir}
ln -s libfuse.so.%{version} libfuse.so.2
ln -s libfuse.so.%{version} libfuse.so
ln -s libulockmgr.so.1.0.1 libulockmgr.so.1
ln -s libulockmgr.so.1.0.1 libulockmgr.so
popd

rm -f %{buildroot}/%{_libdir}/*.a

%ldconfig_scriptlets libs

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md README.NFS
%{_sbindir}/mount.fuse
%attr(4755,root,root) %{_bindir}/fusermount
%{_bindir}/ulockmgr_server
%{_mandir}/man1/*
%{_mandir}/man8/*

%files libs
%license COPYING.LIB
%{_libdir}/libfuse.so.*
%{_libdir}/libulockmgr.so.*

%files devel
%{_libdir}/libfuse.so
%{_libdir}/libulockmgr.so
%{_libdir}/pkgconfig/fuse.pc
%{_includedir}/fuse.h
%{_includedir}/ulockmgr.h
%{_includedir}/fuse

%changelog
%autochangelog
