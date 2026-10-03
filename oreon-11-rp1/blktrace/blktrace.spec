%global source0_hash d6deda03862de2bd1b1b9fba729bbb862d9bca795e6aa7f7ca86b656811a70d6
%global source1_hash 01fab96a513dda62adecde5c799cdf9547d2680c28f0b0d764eca01e0830e5a5
%global source2_hash 64be8e2d3f07a7e9b98c830af5500dc2eac123ebfae48cf5f7d0e960e64469b2

Summary: Utilities for performing block layer IO tracing in the Linux kernel
Name: blktrace
Version: 1.3.0
Release: %autorelease
License: GPL-2.0-or-later
Source0: http://brick.kernel.dk/snaps/blktrace-%{version}.tar.bz2
Source1: https://brick.kernel.dk/snaps/blktrace-%{version}.tar.bz2.asc
Source2: https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/F7D358FB2971E0A6.asc

Url: http://brick.kernel.dk/snaps

BuildRequires: python3-devel
BuildRequires: gcc, libaio-devel

BuildRequires: make
BuildRequires: gnupg2

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations to user space.  This package
includes both blktrace, a utility which gathers event traces from the kernel;
and blkparse, a utility which formats trace data collected by blktrace.

You should install the blktrace package if you need to gather detailed
information about IO patterns.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -pn \
 btt/bno_plot.py \
 btt/btt_plot.py

sed -i '1s=^#!/usr/bin/python3=#!%{__python3}=' \
	btt/{btt_plot.py,bno_plot.py}

%build
%{make_build} CFLAGS="%{optflags} %{build_ldflags}" all

%install
rm -rf %{buildroot}
make dest=%{buildroot} prefix=%{buildroot}/%{_prefix} mandir=%{buildroot}/%{_mandir} install

%files
%doc README COPYING
%{_bindir}/blkparse
%{_bindir}/blkrawverify
%{_bindir}/bno_plot.py
%{_bindir}/btt
%{_bindir}/verify_blkparse
%{_bindir}/blkiomon
%{_bindir}/blktrace
%{_bindir}/btrace
%{_bindir}/btrecord
%{_bindir}/btreplay
%{_mandir}/man1/blkparse.*
%{_mandir}/man1/blkrawverify.*
%{_mandir}/man1/bno_plot.*
%{_mandir}/man1/btt.*
%{_mandir}/man1/verify_blkparse.*
%{_mandir}/man8/blkiomon.*
%{_mandir}/man8/blktrace.*
%{_mandir}/man8/btrace.*
%{_mandir}/man8/btrecord.*
%{_mandir}/man8/btreplay.*

%package -n iowatcher
Summary: Utility for visualizing block layer IO patterns and performance
Requires: blktrace sysstat theora-tools librsvg2-tools

%description -n iowatcher
iowatcher generates graphs from blktrace runs to help visualize IO patterns and
performance as SVG images or movies. It can plot multiple blktrace runs
together, making it easy to compare the differences between different benchmark
runs.

You should install the iowatcher package if you need to visualize detailed
information about IO patterns.

%files -n iowatcher
%doc README iowatcher/COPYING
%{_bindir}/iowatcher
%{_mandir}/man1/iowatcher.*

%changelog
%autochangelog
