# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 005db45ef4ee017f5c32ec124f913a0546e77014266c6a1c50df902a55fe64df
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: Compact Disc Digital Audio (CDDA) extraction tool (or ripper)
Name: cdparanoia
Version: 10.2
Release: 1%{?dist}
License: GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2
URL: http://www.xiph.org/paranoia/index.html

Source0:        http://downloads.xiph.org/releases/cdparanoia/cdparanoia-III-%{version}.src.tgz
Patch0: cdparanoia-10.2-#463009.patch
Patch1: cdparanoia-10.2-endian.patch
Patch2: cdparanoia-10.2-install.patch
Patch3: cdparanoia-10.2-format-security.patch
Patch4: cdparanoia-use-proper-gnu-config-files.patch
Patch5: cdparanoia-10.2-ldflags.patch
Patch6: cdparanoia-10.2-add-pkgconfig.patch

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires: make

%description
Cdparanoia (Paranoia III) reads digital audio directly from a CD, then
writes the data to a file or pipe in WAV, AIFC or raw 16 bit linear
PCM format.  Cdparanoia doesn't contain any extra features (like the ones
included in the cdda2wav sampling utility).  Instead, cdparanoia's strength
lies in its ability to handle a variety of hardware, including inexpensive
drives prone to misalignment, frame jitter and loss of streaming during
atomic reads.  Cdparanoia is also good at reading and repairing data from
damaged CDs.

%package static
Summary: Development tools for libcdda_paranoia (Paranoia III)
Requires: cdparanoia-devel = %{version}-%{release}
License: LicenseRef-Callaway-LGPLv2

%description static
The cdparanoia-devel package contains the static libraries needed for
developing applications to read CD Digital Audio disks.

%package libs
Summary: Libraries for libcdda_paranoia (Paranoia III)
License: LicenseRef-Callaway-LGPLv2

%description libs
The cdparanoia-libs package contains the dynamic libraries needed for
applications which read CD Digital Audio disks.

%package devel
Summary: Development tools for libcdda_paranoia (Paranoia III)
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
License: LicenseRef-Callaway-LGPLv2

%description devel
The cdparanoia-devel package contains the libraries and header files needed
for developing applications to read CD Digital Audio disks.

%prep
%oreon_sha256
%setup -q -n cdparanoia-III-%{version}
%patch -P0 -p3 -b .#463009
%patch -P1 -p1 -b .endian
%patch -P2 -p1 -b .install
%patch -P3 -p1 -b .fmt-sec
%patch -P4 -p1 -b .config
%patch -P5 -p1 -b .ldflags
%patch -P6 -p1 -b .pkgconfig

cp /usr/lib/rpm/redhat/config.* .

%build
autoreconf -ifv
%configure --includedir=%{_includedir}/cdda
make OPT="$RPM_OPT_FLAGS -Wno-pointer-sign -Wno-unused" LDFLAGS="%{?__global_ldflags}"

%install
make install DESTDIR=$RPM_BUILD_ROOT

%ldconfig_scriptlets libs

%files
%doc COPYING* README
%{_bindir}/cdparanoia
%{_mandir}/man1/cdparanoia.1*

%files libs
%{_libdir}/*.so.*

%files devel
%{_includedir}/cdda/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%files static
%{_libdir}/*.a

%changelog
%autochangelog
