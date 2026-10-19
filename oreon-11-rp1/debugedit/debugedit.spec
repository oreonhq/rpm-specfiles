%global source1_hash 00a69f0982e0cbc6172ca01a4486229d0b13322a7402cf852b14a1b119439284
%global source0_hash 3b8c6396fe235e0270c9b9c0d244cfd0e86c284fc27e820acc58360e7cfa08c2
Name: debugedit
Version: 5.3
Release:        1%{?dist}
Summary:        Tools and scripts for creating debuginfo and source file distributions, collect build-ids and rewrite source paths in DWARF data for debugging, tracing and profiling.
License: GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL: https://sourceware.org/debugedit/
Suggests: gdb-minimal
Source0:        https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Source1:        https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-CBA20376A15C6FFC11CD.gpg
Requires: elfutils
Requires: binutils, gawk, coreutils, xz
Requires: findutils
Requires: /usr/bin/gdb-add-index
Requires: sed
Requires: dwz
Requires: grep
%global _hardened_build 1
Patch1: debugedit-5.3-elflint-test.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dwz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  gnupg2
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  xxhash-devel
BuildRequires:  xxhash-static
# /oreon:deps
%description
The debugedit project provides programs and scripts for creating
debuginfo and source file distributions, collect build-ids and rewrite
source paths in DWARF data for debugging, tracing and profiling.

It is based on code originally from the rpm project plus libiberty and
binutils.  It depends on the elfutils libelf and libdw libraries to
read and write ELF files, DWARF data and build-ids.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -f -v -i
%configure
%make_build
%install
%make_install
cd %{buildroot}%{_bindir}
ln -s find-debuginfo find-debuginfo.sh
%oreon_autofiles main

%check

make check %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.3-2
- Import
