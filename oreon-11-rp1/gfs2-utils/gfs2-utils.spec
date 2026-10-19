%global source0_hash e776f8d20191ef3e7742d5eb71f66f39a7af0ce025de614a8952eb7820596d7b
Name: gfs2-utils
Version: 3.6.1
Release:        3%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:        Utilities for managing the global file system (GFS2)
%ifnarch %{arm}
%{?fedora:Recommends: kmod(gfs2.ko) kmod(dlm.ko)}
%endif
ExcludeArch: %{ix86}
Source0:        https://deb.debian.org/debian/pool/main/g/gfs2-utils/gfs2-utils_%{version}.orig.tar.xz#/gfs2-utils-%{version}.tar.gz
URL: https://pagure.io/gfs2-utils
# oreon:deps
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  check-devel
BuildRequires:  flex
BuildRequires:  gettext-devel
BuildRequires:  kernel-headers
BuildRequires:  libblkid-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
# /oreon:deps
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure
%make_build
%check

make check || { cat tests/testsuite.log; exit 1; }
%install
%make_install
rm -f %{buildroot}%{_sbindir}/gfs2_trace
rm -f %{buildroot}%{_sbindir}/gfs2_lockcapture
rm -f %{buildroot}%{_mandir}/man8/gfs2_trace.8
rm -f %{buildroot}%{_mandir}/man8/gfs2_lockcapture.8
%oreon_autofiles main

%description
The gfs2-utils package contains a number of utilities for creating, checking,
modifying, and correcting inconsistencies in GFS2 file systems.

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.1-3
- Prepare for Oreon 11 (RP1)
