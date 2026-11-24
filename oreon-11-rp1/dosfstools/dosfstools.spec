# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 64926eebf90092dca21b14259a5301b7b98e7b1943e8a201c7d726084809b527
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: dosfstools
Version: 4.2
Release: 1%{?dist}
Summary: Utilities for making and checking MS-DOS FAT filesystems on Linux
License: GPL-3.0-or-later
Source0: https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:  8da7bc93315c.patch
URL: https://github.com/dosfstools/dosfstools

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: xxd
Recommends: glibc-gconv-extra

%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/mkfs.vfat
%endif

%description
The dosfstools package includes the mkdosfs and dosfsck utilities,
which respectively make and check MS-DOS FAT filesystems on hard
drives or on floppies.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --enable-compat-symlinks
%make_build CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing"

%install
%make_install PREFIX=%{_prefix}

rm -f %{buildroot}%{_docdir}/%{name}/*

%check
make check

%files
%license COPYING
%doc NEWS README
%{_sbindir}/*
%{_mandir}/man8/*

%changelog
%autochangelog
