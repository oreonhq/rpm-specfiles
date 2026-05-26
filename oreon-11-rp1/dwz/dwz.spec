Summary: DWARF optimization and duplicate removal tool
Name: dwz
Version: 0.16
Release: 3%{?dist}
License: GPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND GPL-2.0-or-later AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND LGPL-2.0-or-later
URL: https://sourceware.org/dwz/
Source: https://sourceware.org/ftp/dwz/releases/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 3602c8221be1f31fe612d4c80226b2e6bb20e19ccfcc0ebef321d90ba74d35a1
%global source0_file dwz-0.16.tar.xz
# oreon url source checksums end
BuildRequires: gcc, gcc-c++, gdb, elfutils-libelf-devel, dejagnu
# dwz builds with XXH_INLINE_ALL, so depend on (virtual) xxhash-static
BuildRequires: make elfutils xxhash-devel xxhash-static

# Patches

%description
The dwz package contains a program that attempts to optimize DWARF
debugging information contained in ELF shared libraries and ELF executables
for size, by replacing DWARF information representation with equivalent
smaller representation where possible and by reducing the amount of
duplication using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/dwz-0.16.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3602c8221be1f31fe612d4c80226b2e6bb20e19ccfcc0ebef321d90ba74d35a1" || { echo "oreon: Source0 SHA256 mismatch for dwz-0.16.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16-3
- Import
