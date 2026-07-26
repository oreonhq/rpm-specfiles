%global source0_hash bf37b2f695b314ad2148c555f4d9ebe91ba7a34b224ae62d7aa2079c4ecbb847

%global	githash 38573e7d

Name:		memstomp
Version:	0.1.4
Release:	44%{?dist}
Summary:	Warns of memory argument overlaps to various functions
# The entire source code is LGPLV3+ with the exception of backtrace-symbols.c which
# is GPLv2+ by way of being a hacked up old version of binutils's addr2line.
# backtrace-symbols.c is built into an independent .so to avoid license contamination
# Automatically converted from old format: LGPLv3+ and GPLv2+ - review is highly recommended.
License:	LGPL-3.0-or-later AND GPL-2.0-or-later
URL:		git://fedorapeople.org/home/fedora/wcohen/public_git/memstomp
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# git glone git://fedorapeople.org/home/fedora/wcohen/public_git/memstomp
# cd memstomp
# git archive --prefix memstomp-0.1.4-38573e7d/ master | gzip > memstomp-0.1.4-3867e37d.tar.gz
Source0:	%{name}-%{version}-%{githash}.tar.gz
Requires:	util-linux
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	binutils-devel autoconf automake dejagnu

Patch0: memstomp-testsuite.patch
Patch1: memstomp-man.patch
Patch2: memstomp-rh961495.patch
Patch3: memstomp-rh962763.patch
Patch4: memstomp-quietmode.patch
Patch5: memstomp-rh1093173.patch
Patch6: memstomp-rh1133815.patch
Patch7: memstomp-implicit-int.patch
Patch8: bfd-api-change.patch
Patch9: memstomp-PTR.patch
Patch10: memstomp-sframe.patch

%description 
memstomp is a simple program that can be used to identify
places in code which trigger undefined behavior due to
overlapping memory arguments to certain library calls.

%ldconfig_scriptlets

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-%{githash}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1

%build
autoreconf
%configure
# We force -O0 here because memstomp essentially relies on GCC
# not removing any of its checks.  GCC continues to get better
# and twarting its optimizer isn't something I have any interest
# in maintaining over time.  So just force -O0 for stupid code
# generation.
make %{?_smp_mflags} CFLAGS+="-O0 -fno-strict-aliasing"
make -k check

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README LGPL3 GPL2 GPL3
%{_bindir}/memstomp
%{_libdir}/libmemstomp.so
%{_libdir}/libmemstomp-backtrace-symbols.so
%{_mandir}/man1/memstomp.1.gz

%changelog
%autochangelog
