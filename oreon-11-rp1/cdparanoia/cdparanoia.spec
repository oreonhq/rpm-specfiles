%global source0_hash 005db45ef4ee017f5c32ec124f913a0546e77014266c6a1c50df902a55fe64df
Summary:        Compact Disc Digital Audio (CDDA) extraction tool (or ripper)
Name: cdparanoia
Version: 10.2
Release:        50%{?dist}
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
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n cdparanoia-III-%{version}
%patch -P0 -p3 -b .#463009
%patch -P1 -p1 -b .endian
%patch -P2 -p1 -b .install
%patch -P3 -p1 -b .fmt-sec
%patch -P4 -p1 -b .config
%patch -P5 -p1 -b .ldflags
%patch -P6 -p1 -b .pkgconfig

# Update config.guess/sub for newer architectures
cp /usr/lib/rpm/redhat/config.* .

%build

autoreconf -ifv
%configure --includedir=%{_includedir}/cdda
make OPT="$RPM_OPT_FLAGS -Wno-pointer-sign -Wno-unused" LDFLAGS="%{?__global_ldflags}"
%install
make install DESTDIR=$RPM_BUILD_ROOT
%ldconfig_scriptlets libs
%oreon_autofiles cdparanoia-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cdparanoia-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cdparanoia-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cdparanoia-static -f %{oreon_filedir}/cdparanoia-static.list
%files -n cdparanoia-libs -f %{oreon_filedir}/cdparanoia-libs.list
%files -n cdparanoia-devel -f %{oreon_filedir}/cdparanoia-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.2-50
- Prepare for Oreon 11 (RP1)
