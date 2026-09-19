%global source0_hash ef619b49efb9f792d80c777fdd2d639ed2839da98bffe8b4754c8e5ce61592fb

Name: squashfs-tools-ng
Version: 1.3.2
Summary: A new set of tools and libraries for working with SquashFS images
URL:	 https://github.com/AgentD/squashfs-tools-ng
Source0: https://infraroot.at/pub/squashfs/squashfs-tools-ng-%{version}.tar.gz
Release: %autorelease
License: LGPL-3.0-or-later AND GPL-3.0-or-later AND BSD-2-Clause AND MIT

BuildRequires: make
BuildRequires: gcc
BuildRequires: zlib-devel
BuildRequires: xz-devel
BuildRequires: lzo-devel
BuildRequires: libattr-devel
BuildRequires: lz4-devel
BuildRequires: libzstd-devel
BuildRequires: libselinux-devel
BuildRequires: help2man

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains modified utilities for manipulating squashfs filesystems.

%package libs
Summary: The squashfs-tools-ng libsquashfs library

%description libs
The squashfs-tools-ng-libs package contains the libsquashfs
library provided and used by squashfs-tools-ng.

%package devel
Summary: Header files for squashfs-tools-ng development
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The squashfs-tools-ng-devel package contains the header files needed to
develop programs that use the squashfs-tools-ng libsquashfs library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install

%check
make check

%files
%license COPYING*
%doc README* CHANGELOG*
%{_bindir}/gensquashfs
%{_bindir}/rdsquashfs
%{_bindir}/sqfs2tar
%{_bindir}/sqfsdiff
%{_bindir}/tar2sqfs
%{_mandir}/man1/gensquashfs.1.*
%{_mandir}/man1/rdsquashfs.1.*
%{_mandir}/man1/sqfs2tar.1.*
%{_mandir}/man1/sqfsdiff.1.*
%{_mandir}/man1/tar2sqfs.1.*

%files libs
%license COPYING*
%{_libdir}/libsquashfs.so.1{,.*}

%files devel
%license COPYING*
%doc doc/architecture.md doc/benchmark.txt doc/format.adoc doc/parallelism.txt
%{_libdir}/libsquashfs.so
%{_includedir}/sqfs/
%{_libdir}/pkgconfig/libsquashfs1.pc

%changelog
%autochangelog
