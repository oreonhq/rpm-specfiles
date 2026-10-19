%global source0_hash db10030528f3365c03755969619dd6789147d34fc588db8107364351085aebad
Name: dwz
Version: 0.17
Release:        1%{?dist}
Summary:        DWARF optimization and duplicate removal tool
License: GPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND GPL-2.0-or-later AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND LGPL-2.0-or-later
URL: https://sourceware.org/dwz/
Source0:        https://sourceware.org/ftp/dwz/releases/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  dejagnu
BuildRequires:  elfutils
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  make
BuildRequires:  xxhash-devel
BuildRequires:  xxhash-static
# /oreon:deps
%description
The dwz package contains a program that attempts to optimize DWARF
debugging information contained in ELF shared libraries and ELF executables
for size, by replacing DWARF information representation with equivalent
smaller representation where possible and by reducing the amount of
duplication using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir dwz
%oreon_prep
%build

%make_build CFLAGS='%{optflags}' LDFLAGS='%{build_ldflags}' \
  prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}
%install
rm -rf %{buildroot}
%make_install prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}
%oreon_autofiles main

%check

CFLAGS="" LDFLAGS="" srcdir=$(pwd) make check
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16-3
- Import
