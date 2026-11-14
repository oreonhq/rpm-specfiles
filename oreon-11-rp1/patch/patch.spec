# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3240c7959c5347c8ed347e3c4201c0337bf4240d5cf09d68889e58eeaba30e17

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global gnulib_ver 20180203

Summary: Utility for modifying/upgrading files
Name: patch
Version:        2.8.1
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://savannah.gnu.org/projects/patch/
Source0:        https://mirror.cs.odu.edu/gnu/patch/patch-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: libselinux-devel
BuildRequires: libattr-devel
BuildRequires: ed
BuildRequires: autoconf automake
Requires: ed

Provides: bundled(gnulib) = %{gnulib_ver}

%description
The patch program applies diff files to originals.  The diff command
is used to compare an original to a changed file.  Diff lists the
changes made to the file.  A person who has the original file can then
use the patch command with the diff file to add the changes to their
original file (patching the file).

Patch should be installed because it is a common way of upgrading
applications.

%prep
echo "%{source0_hash}  %{SOURCE0}" | sha256sum -c -

%autosetup -p1

%build
autoreconf
%configure --disable-silent-rules
%make_build

%check
make check

%install
%makeinstall

%files
%license COPYING
%doc NEWS README
%{_bindir}/*
%{_mandir}/*/*

