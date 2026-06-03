%global source0_hash 3b8c6396fe235e0270c9b9c0d244cfd0e86c284fc27e820acc58360e7cfa08c2

Name: debugedit
Version: 5.3
Release: 2%{?dist}
Summary: Tools and scripts for creating debuginfo and source file distributions, collect build-ids and rewrite source paths in DWARF data for debugging, tracing and profiling.
License: GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL: https://sourceware.org/debugedit/

Suggests: gdb-minimal

Source0:        https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Source1:        https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-CBA20376A15C6FFC11CD.gpg

BuildRequires: make gcc gcc-c++
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libdw)
BuildRequires: help2man
BuildRequires: gnupg2

# For configure checking -j support
BuildRequires: dwz

# For debugedit build-id recomputation
BuildRequires: xxhash-devel
# debugedit builds with XXH_INLINE_ALL, so depend on (virtual) xxhash-static
BuildRequires: xxhash-static

# For the testsuite.
BuildRequires: autoconf
BuildRequires: automake

# For configure checks we need full gdb, otherwise gdb-add-index is fine.
# Older gdb-add-index unfortunately don't support --version.
BuildRequires: gdb

# The find-debuginfo.sh script has a couple of tools it needs at runtime.
# For strip_to_debug, eu-strip
Requires: elfutils
# For ar, add_minidebug, readelf, awk, nm, sort, comm, objcopy, xz
Requires: binutils, gawk, coreutils, xz
# For find and xargs
Requires: findutils
# For do_file, gdb_add_index
# We only need gdb-add-index, so suggest gdb-minimal (full gdb is also ok)
Requires: /usr/bin/gdb-add-index
# For run_job, sed
Requires: sed
# For dwz
Requires: dwz
# For append_uniq, grep
Requires: grep

%global _hardened_build 1

Patch1: debugedit-5.3-elflint-test.patch

%description
The debugedit project provides programs and scripts for creating
debuginfo and source file distributions, collect build-ids and rewrite
source paths in DWARF data for debugging, tracing and profiling.

It is based on code originally from the rpm project plus libiberty and
binutils.  It depends on the elfutils libelf and libdw libraries to
read and write ELF files, DWARF data and build-ids.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -f -v -i
%configure
%make_build

%install
%make_install
# Temp symlink to make sure things don't break.
cd %{buildroot}%{_bindir}
ln -s find-debuginfo find-debuginfo.sh

%check
# The testsuite should be zero fail.
make check %{?_smp_mflags}

%files
%license COPYING COPYING3 COPYING.LIB
%doc README
%{_bindir}/debugedit
%{_bindir}/sepdebugcrcfix
%{_bindir}/debugedit-classify-ar
%{_bindir}/find-debuginfo
%{_bindir}/find-debuginfo.sh
%{_mandir}/man1/debugedit.1*
%{_mandir}/man1/sepdebugcrcfix.1*
%{_mandir}/man1/debugedit-classify-ar.1*
%{_mandir}/man1/find-debuginfo.1*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.3-2
- Import
