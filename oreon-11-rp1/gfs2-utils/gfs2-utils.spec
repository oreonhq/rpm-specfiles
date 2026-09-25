%global source0_hash none

Name: gfs2-utils
Version: 3.6.1
Release: 3%{?dist}
# Refer to doc/README.licence in the upstream tarball
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Summary: Utilities for managing the global file system (GFS2)
%ifnarch %{arm}
%{?fedora:Recommends: kmod(gfs2.ko) kmod(dlm.ko)}
%endif
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}
BuildRequires: ncurses-devel
BuildRequires: kernel-headers
BuildRequires: automake
BuildRequires: libtool
BuildRequires: zlib-devel
BuildRequires: gettext-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: libblkid-devel
BuildRequires: libuuid-devel
BuildRequires: check-devel
BuildRequires: bzip2-devel
BuildRequires: make
Source:        https://deb.debian.org/debian/pool/main/g/gfs2-utils/gfs2-utils_%{version}.orig.tar.xz#/gfs2-utils-%{version}.tar.gz
URL: https://pagure.io/gfs2-utils

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%check
make check || { cat tests/testsuite.log; exit 1; }

%install
%make_install
# Don't ship gfs2_{trace,lockcapture} in this package
rm -f %{buildroot}%{_sbindir}/gfs2_trace
rm -f %{buildroot}%{_sbindir}/gfs2_lockcapture
rm -f %{buildroot}%{_mandir}/man8/gfs2_trace.8
rm -f %{buildroot}%{_mandir}/man8/gfs2_lockcapture.8

%description
The gfs2-utils package contains a number of utilities for creating, checking,
modifying, and correcting inconsistencies in GFS2 file systems.

%files
%doc doc/COPYING.* doc/COPYRIGHT doc/*.txt
%doc doc/README.contributing doc/README.licence
%{_sbindir}/fsck.gfs2
%{_sbindir}/gfs2_grow
%{_sbindir}/gfs2_jadd
%{_sbindir}/mkfs.gfs2
%{_sbindir}/gfs2_edit
%{_sbindir}/tunegfs2
%{_sbindir}/glocktop
%{_libexecdir}/gfs2_withdraw_helper
%{_mandir}/man8/*gfs2*
%{_mandir}/man8/glocktop*
%{_mandir}/man5/*
%{_prefix}/lib/udev/rules.d/82-gfs2-withdraw.rules

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.1-3
- Prepare for Oreon 11 (RP1)
