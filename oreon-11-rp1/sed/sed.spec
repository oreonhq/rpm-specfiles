# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b8e72182b2ec96a3574e2998c47b7aaa64cc20ce000d8e9ac313cc07cecf28c7

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
# -*- coding: utf-8 -*-

Summary: A GNU stream text editor
Name: sed
Version:        4.10
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: http://sed.sourceforge.net/
Source0:        https://mirror.cs.odu.edu/gnu/sed/sed-%{version}.tar.xz
Patch0:        sed-b-flag.patch
Patch1:        sed-c-flag.patch
#Patch2: sed-covscan-annotations.patch
Patch3:        sed-regexp-cache-size.patch
BuildRequires: make
BuildRequires: glibc-devel, libselinux-devel, libacl-devel, automake, autoconf, gcc
BuildRequires: perl-Getopt-Long
BuildRequires: perl(FileHandle)

# for tests.  More tests require a ja_JP locale, but glibc-langpack-ja gives:
#   invalid-mb-seq-UMR.sh: skipped test: locale 'ja_JP' is buggy
#   mb-charclass-non-utf8.sh: skipped test: ja_JP shift-jis locale not found
BuildRequires: glibc-langpack-el, glibc-langpack-en
BuildRequires: glibc-langpack-ru

%ifarch %{valgrind_arches}
BuildRequires: valgrind
BuildRequires:  oreon-rpm-macros
%endif

Provides: /bin/sed

#copylib
Provides: bundled(gnulib)

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%prep
%oreon_sha256

%autosetup -p1

%build
#%configure --without-included-regex
%configure 
%make_build

#rhbz#2396649
sed -i s/"SELinux is enabled on this system."// ./doc/sed.1
sed -i s/"SELinux is disabled on this system."// ./doc/sed.1


%check
echo ====================TESTING=========================
make check
echo ====================TESTING END=====================

%install
rm -rf ${RPM_BUILD_ROOT}
%make_install
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

%find_lang %{name}

%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING 
%doc BUGS NEWS THANKS README AUTHORS
%{_bindir}/sed
%{_infodir}/sed.info*
%{_mandir}/man1/sed.1*

