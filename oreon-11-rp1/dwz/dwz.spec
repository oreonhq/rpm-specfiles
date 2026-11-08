# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash db10030528f3365c03755969619dd6789147d34fc588db8107364351085aebad

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary: DWARF optimization and duplicate removal tool
Name: dwz
Version:        0.17
Release:        1%{?dist}
License: GPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND GPL-2.0-or-later AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND LGPL-2.0-or-later
URL: https://sourceware.org/dwz/
Source0:        https://sourceware.org/ftp/dwz/releases/dwz-%{version}.tar.xz
BuildRequires: gcc, gcc-c++, gdb, elfutils-libelf-devel, dejagnu
# dwz builds with XXH_INLINE_ALL, so depend on (virtual) xxhash-static
BuildRequires: make elfutils xxhash-devel xxhash-static
BuildRequires:  oreon-rpm-macros

# Patches
Patch1:        0001-dwz-cleanup-allocatable-section-after-non-allocatabl.patch

%description
The dwz package contains a program that attempts to optimize DWARF
debugging information contained in ELF shared libraries and ELF executables
for size, by replacing DWARF information representation with equivalent
smaller representation where possible and by reducing the amount of
duplication using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
%oreon_sha256

%autosetup -p1 -n dwz

%build
%make_build CFLAGS='%{optflags}' LDFLAGS='%{build_ldflags}' \
  prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%install
rm -rf %{buildroot}
%make_install prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%check
CFLAGS="" LDFLAGS="" srcdir=$(pwd) make check

%files
%license COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz
%{_mandir}/man1/dwz.1*

