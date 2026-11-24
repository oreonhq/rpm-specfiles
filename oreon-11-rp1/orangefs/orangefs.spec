# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a945e33b824220b6b97d3d036dabea7c56a1392155b86d741d75a55427814d42
%global source1_hash 5d605129e4dcf7619b0a211d3405ac54404e8cb855d99416125103daf41fcf91
%global source2_hash 2dee68cafa712781386cd24cc254664b2bb60e5011e59683e11d0be7f979804e
%global source3_hash 7de9fac0aac82100be2a2275706f311b1904b2ceec1d66a6f2ad7ff5354b231b
%global source4_hash ee587be720866b64b7610a9a0c6c0a35e8c63acce8dceb758d7e69416401eed9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define         _legacy_common_support 1

%global         _hardened_build 1

Name:           orangefs
Version:        2.10.1
Release:        1%{?dist}
Summary:        Parallel network file system client
URL:            https://www.orangefs.org/
License:       LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND Zlib
Source0:       https://github.com/waltligon/orangefs/archive/refs/tags/2.10.1.tar.gz
Source1:       orangefs-server.service
Source2:       orangefs-client.service
Source3:       orangefs.conf
Source4:       pvfs2tab

Patch:         orangefs-genconfig.patch

Patch:         orangefs-lmdb.patch

Patch:         orangefs-no-start-stop.patch

Patch:         orangefs-configure-c99.patch

Patch:         orangefs-2.10.1-disable-ib-exp.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: automake
BuildRequires: bison
BuildRequires: flex
BuildRequires: fuse-devel
BuildRequires: libattr-devel
BuildRequires: libselinux-devel
BuildRequires: lmdb-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Math::BigInt)
BuildRequires: perl(Term::ReadLine)
BuildRequires: systemd
%ifnarch armv7hl
BuildRequires: libibverbs-devel
%endif
%if ! 0%{?oreon}
BuildRequires: ghostscript-tools-dvipdf
BuildRequires: latex2html
BuildRequires: texlive
BuildRequires: texlive-dvips
BuildRequires: texlive-charter
BuildRequires: texlive-courier
BuildRequires: texlive-times
%endif
%description
OrangeFS (formerly PVFS2) is a high-performance parallel
network file system designed for use on high performance computing
systems.  It provides very high performance access to disk storage for
parallel applications.  It is accessible through a variety of
interfaces, including the native OrangeFS library, the kernel, FUSE,
and MPI-IO.

This package provides the pvfs2-client-core which is required to use
he kernel module.

%package       server
Summary:       Parallel network file system server
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      perl(Math::BigInt)
%description   server
This package contains the Parallel network file system server

%package       fuse
Summary:       Parallel network file system FUSE client
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   fuse
This package contains the Parallel network file system FUSE client

%package       devel
Summary:       Parallel network file system development libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   devel
This package contains the headers and libraries necessary for client
development of the Parallel network file system

%if ! 0%{?oreon}
%package       docs
Summary:       Documentation for the  Parallel network file system
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   docs
This package contains documentation of the Parallel network file system
%endif

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
%autosetup -p1 -n orangefs-%{version}
rm -r src/apps/devel/lmdb
rm -r src/common/lmdb
mv doc/man/pvfs2.conf.5 doc/man/orangefs.conf.5

autoupdate -I maint/config
autoreconf -vif -I maint/config

%build
export LDFLAGS="%{optflags} -Wl,--as-needed"
%configure --enable-external-lmdb \
           --enable-shared        \
           --disable-static       \
           --enable-fuse          \
           --disable-usrint-cwd   \
           --with-db-backend=lmdb \
%ifnarch armv7hl
           --with-openib=/usr     \
%endif
           --disable-olib         \
           --with-ib=no           \
           --with-experimental-ib=no
%make_build V=1
%if ! 0%{?oreon}
make docs V=1
%endif

%install
%make_install

mkdir -p %{buildroot}%{_docdir}/orangefs
%if ! 0%{?oreon}
install -p -m 644 doc/*.pdf %{buildroot}%{_docdir}/orangefs
mkdir -p %{buildroot}%{_docdir}/orangefs/coding
install -p -m 644 doc/coding/*.pdf %{buildroot}%{_docdir}/orangefs/coding
mkdir -p %{buildroot}%{_docdir}/orangefs/design
install -p -m 644 doc/design/*.pdf %{buildroot}%{_docdir}/orangefs/design
mkdir -p %{buildroot}%{_docdir}/orangefs/random
install -p -m 644 doc/random/*.pdf %{buildroot}%{_docdir}/orangefs/random
%endif
install -p -m 644 COPYING %{buildroot}%{_docdir}/orangefs

mkdir -p %{buildroot}%{_unitdir}
install  -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sharedstatedir}/orangefs
mkdir -p %{buildroot}%{_sysconfdir}/orangefs
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/orangefs
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}

%ldconfig_scriptlets

%files
%license %{_docdir}/orangefs/COPYING
%config(noreplace) %{_sysconfdir}/pvfs2tab
%{_bindir}/pvfs2-check-server
%{_bindir}/pvfs2-chmod
%{_bindir}/pvfs2-chown
%{_bindir}/pvfs2-cp
%{_bindir}/pvfs2-drop-caches
%{_bindir}/pvfs2-fs-dump
%{_bindir}/pvfs2-fsck
%{_bindir}/pvfs2-get-uid
%{_bindir}/pvfs2-getmattr
%{_bindir}/pvfs2-ln
%{_bindir}/pvfs2-ls
%{_bindir}/pvfs2-lsplus
%{_bindir}/pvfs2-mkdir
%{_bindir}/pvfs2-perf-mon-example
%{_bindir}/pvfs2-perf-mon-snmp
%{_bindir}/pvfs2-perror
%{_bindir}/pvfs2-ping
%{_bindir}/pvfs2-remove-object
%{_bindir}/pvfs2-set-debugmask
%{_bindir}/pvfs2-set-eventmask
%{_bindir}/pvfs2-set-mode
%{_bindir}/pvfs2-set-perf-history
%{_bindir}/pvfs2-set-perf-interval
%{_bindir}/pvfs2-set-sync
%{_bindir}/pvfs2-set-turn-off-timeouts
%{_bindir}/pvfs2-setmattr
%{_bindir}/pvfs2-stat
%{_bindir}/pvfs2-statfs
%{_bindir}/pvfs2-touch
%{_bindir}/pvfs2-validate
%{_bindir}/pvfs2-viewdist
%{_bindir}/pvfs2-write
%{_bindir}/pvfs2-xattr
%{_sbindir}/pvfs2-client
%{_sbindir}/pvfs2-client-core
%{_unitdir}/orangefs-client.service
%{_libdir}/libpvfs2.so.2
%{_libdir}/libpvfs2.so.2.*
%{_mandir}/man1/getmattr.1*
%{_mandir}/man1/pvfs2-client-core.1*
%{_mandir}/man1/pvfs2-client.1*
%{_mandir}/man1/pvfs2-cp.1*
%{_mandir}/man1/pvfs2-check-server.1*
%{_mandir}/man1/pvfs2-chmod.1*
%{_mandir}/man1/pvfs2-chown.1*
%{_mandir}/man1/pvfs2-config.1*
%{_mandir}/man1/pvfs2-drop-caches.1*
%{_mandir}/man1/pvfs2-fs-dump.1*
%{_mandir}/man1/pvfs2-fsck.1*
%{_mandir}/man1/pvfs2-get-uid.1*
%{_mandir}/man1/pvfs2-getmattr.1*
%{_mandir}/man1/pvfs2-ln.1*
%{_mandir}/man1/pvfs2-ls.1*
%{_mandir}/man1/pvfs2-lsplus.1*
%{_mandir}/man1/pvfs2-mkdir.1*
%{_mandir}/man1/pvfs2-perf-mon-example.1*
%{_mandir}/man1/pvfs2-perf-mon-snmp.1*
%{_mandir}/man1/pvfs2-perror.1*
%{_mandir}/man1/pvfs2-ping.1*
%{_mandir}/man1/pvfs2-remove-object.1*
%{_mandir}/man1/pvfs2-rm.1*
%{_mandir}/man1/pvfs2-set-debugmask.1*
%{_mandir}/man1/pvfs2-set-eventmask.1*
%{_mandir}/man1/pvfs2-set-mode.1*
%{_mandir}/man1/pvfs2-set-perf-history.1*
%{_mandir}/man1/pvfs2-set-perf-interval.1*
%{_mandir}/man1/pvfs2-set-sync.1*
%{_mandir}/man1/pvfs2-set-turn-off-timeouts.1*
%{_mandir}/man1/pvfs2-setmattr.1*
%{_mandir}/man1/pvfs2-stat.1*
%{_mandir}/man1/pvfs2-statfs.1*
%{_mandir}/man1/pvfs2-touch.1*
%{_mandir}/man1/pvfs2-validate.1*
%{_mandir}/man1/pvfs2-viewdist.1*
%{_mandir}/man1/pvfs2-write.1*
%{_mandir}/man1/pvfs2-xattr.1*
%{_mandir}/man1/pvfs2.1*
%{_mandir}/man1/setmattr.1*
%{_mandir}/man5/pvfs2tab.5*
%exclude %{_mandir}/man1/pvfs2-start-all.1*
%exclude %{_mandir}/man1/pvfs2-stop-all.1*

%files server
%dir %{_sysconfdir}/orangefs
%config(noreplace) %{_sysconfdir}/orangefs/orangefs.conf
%{_bindir}/pvfs2-genconfig
%{_bindir}/pvfs2-mkspace
%{_bindir}/pvfs2-showcoll
%{_sbindir}/pvfs2-server
%{_unitdir}/orangefs-server.service
%{_mandir}/man1/pvfs2-genconfig.1*
%{_mandir}/man1/pvfs2-mkspace.1*
%{_mandir}/man1/pvfs2-server.1*
%{_mandir}/man1/pvfs2-showcoll.1*
%{_mandir}/man5/orangefs.conf.5*
%dir %{_sharedstatedir}/orangefs

%files fuse
%{_bindir}/pvfs2fuse

%files devel
%{_bindir}/pvfs2-config
%{_includedir}/orange.h
%{_includedir}/pvfs2-compat.h
%{_includedir}/pvfs2-debug.h
%{_includedir}/pvfs2-encode-stubs.h
%{_includedir}/pvfs2-hint.h
%{_includedir}/pvfs2-mgmt.h
%{_includedir}/pvfs2-mirror.h
%{_includedir}/pvfs2-request.h
%{_includedir}/pvfs2-sysint.h
%{_includedir}/pvfs2-types.h
%{_includedir}/pvfs2-usrint.h
%{_includedir}/pvfs2-util.h
%{_includedir}/pvfs2.h
%{_libdir}/libpvfs2.so

%if ! 0%{?oreon}
%files docs
%dir %{_docdir}/orangefs
%license %{_docdir}/orangefs/COPYING
%{_docdir}/orangefs/pvfs2-guide.pdf
%dir %{_docdir}/orangefs/coding
%{_docdir}/orangefs/coding/developer-guidelines.pdf
%dir %{_docdir}/orangefs/design
%{_docdir}/orangefs/design/bmi-design.pdf
%{_docdir}/orangefs/design/concepts.pdf
%{_docdir}/orangefs/design/distributions.pdf
%{_docdir}/orangefs/design/flow-design.pdf
%{_docdir}/orangefs/design/fs-semantics.pdf
%{_docdir}/orangefs/design/handle-allocator.pdf
%{_docdir}/orangefs/design/pvfs2-client.pdf
%{_docdir}/orangefs/design/pvfs2-trove-usage.pdf
%{_docdir}/orangefs/design/trove-dbpf.pdf
%{_docdir}/orangefs/design/request-design.pdf
%{_docdir}/orangefs/design/storage-interface.pdf
%{_docdir}/orangefs/pvfs2-ha.pdf
%{_docdir}/orangefs/pvfs2-ha-heartbeat-v2.pdf
%{_docdir}/orangefs/pvfs2-faq.pdf
%{_docdir}/orangefs/pvfs2-quickstart.pdf
%{_docdir}/orangefs/pvfs2-status.pdf
%{_docdir}/orangefs/pvfs2-tuning.pdf
%dir %{_docdir}/orangefs/random
%{_docdir}/orangefs/random/SystemInterfaceTesting.pdf
%endif

%changelog
%autochangelog
