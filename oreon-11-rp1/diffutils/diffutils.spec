# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7c8b7f9fc8609141fdea9cece85249d308624391ff61dedaf528fcb337727dfd

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary: GNU collection of diff utilities
Name: diffutils
Version:        3.12
Release:        1%{?dist}
URL: https://www.gnu.org/software/diffutils/diffutils.html
Source0:        https://mirror.cs.odu.edu/gnu/diffutils/diffutils-%{version}.tar.xz
# upstream fixes
# cross compile build of 3.12 diffutils fails
Patch:        diffutils-3.12-cross-compiler-build-fail.patch
# sdiff: continue → break
Patch:        diffutils-3.12-sdiff-continue-break.patch
# sdiff: pacify gcc -flto -Wmaybe-uninitialized
Patch:        0001-sdiff-pacify-gcc-flto-Wmaybe-uninitialized.patch
# sdiff: port back to C17
Patch:        0001-sdiff-port-back-to-C17.patch
License: GPL-3.0-or-later
Provides: bundled(gnulib)
BuildRequires: gcc
BuildRequires: help2man
BuildRequires: autoconf, automake, texinfo
BuildRequires: make
BuildRequires:  oreon-rpm-macros

%description
Diffutils includes four utilities: diff, cmp, diff3 and sdiff. Diff
compares two files and shows the differences, line by line.  The cmp
command shows the offset and line numbers where two files differ, or
cmp can show the characters that differ between the two files.  The
diff3 command shows the differences between three files.  Diff3 can be
used when two people have made independent changes to a common
original; diff3 can produce a merged file that contains both sets of
changes and warnings about conflicts.  The sdiff command can be used
to merge two files interactively.

Install diffutils if you need to compare text files.

%prep
%oreon_sha256

%autosetup -p1

# Run autoreconf for aarch64 support (bug #925256).
autoreconf

%build
%configure
make PR_PROGRAM=%{_bindir}/pr

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%find_lang %{name}

%check
# Disable update-copyright gnulib test (bug #1239428).
>gnulib-tests/test-update-copyright.sh
make check

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/diffutils.info*

