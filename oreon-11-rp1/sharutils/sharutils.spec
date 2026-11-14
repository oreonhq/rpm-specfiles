# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2b05cff7de5d7b646dc1669bc36c35fdac02ac6ae4b6c19cb3340d87ec553a9a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: sharutils
Version: 4.15.2
Release: 1%{?dist}
Summary: GNU shar utilities for shell archives
License: GPL-3.0-or-later AND BSD-4-Clause AND (LGPL-3.0-or-later OR BSD-3-Clause) AND LGPL-2.0-or-later AND GFDL-1.3-or-later
URL: https://www.gnu.org/software/sharutils/
Source0: https://ftp.gnu.org/gnu/sharutils/sharutils-%{version}.tar.xz
Source1: sharutils-4.15.2.tar.xz.sig
Source2: gpgkey-1F967B15DEB2349CACDF3D71D9204CB5BFBF0221.gpg
Patch0: sharutils-4.14.2-Pass-compilation-with-Werror-format-security.patch
Patch1: sharutils-4.15.2-Fix-a-heap-buffer-overflow-in-find_archive.patch
Patch2: sharutils-4.15.2-fflush-adjust-to-glibc-2.28-libio.h-removal.patch
Patch3: sharutils-4.15.2-Fix-building-with-GCC-10.patch
Patch4: sharutils-4.15.2-Do-not-include-lib-md5.c-into-src-shar.c.patch
Patch5: sharutils-4.15.2-ISO-C23-Backport-stdbool.m4-from-gnulib-devel-0-52.2.patch
Patch6: sharutils-4.15.2-ISO-C23-Port-getcwd.m4-to-ISO-C23.patch
Patch7: sharutils-4.15.2-ISO-C23-Port-the-code-to-ISO-C23.patch

BuildRequires: oreon-rpm-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: glibc-common
BuildRequires: make
BuildRequires: sed
BuildRequires: diffutils
BuildRequires: gnupg2

Provides: bundled(gnulib)
Provides: bundled(libopts) = 41.1

%description
GNU shar utilities for encoding and decoding shell archives.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1
for i in TODO THANKS; do
  iconv -f iso-8859-1 -t utf-8 -o $i{.utf8,}
  mv $i{.utf8,}
done

%build
autoreconf
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%check
%make_build check

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
