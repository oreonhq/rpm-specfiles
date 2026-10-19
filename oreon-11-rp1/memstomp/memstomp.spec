%global source0_hash bf37b2f695b314ad2148c555f4d9ebe91ba7a34b224ae62d7aa2079c4ecbb847
%global	githash 38573e7d
Name:		memstomp
Version:	0.1.4
Release:        44%{?dist}
Summary:        Warns of memory argument overlaps to various functions
License:	LGPL-3.0-or-later AND GPL-2.0-or-later
URL:		git://fedorapeople.org/home/fedora/wcohen/public_git/memstomp
Source0:        %{name}-%{version}-%{githash}.tar.gz
Requires:	util-linux
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
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  dejagnu
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
make %{?_smp_mflags} CFLAGS+="-O0 -fno-strict-aliasing"
make -k check
%install
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
