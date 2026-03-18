Name:		dvd+rw-tools
Version:	7.1
Release:	46%{?dist}
Summary:	Toolchain to master DVD+RW/+R media
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://fy.chalmers.se/~appro/linux/DVD+RW/

Source:		http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-%{version}.tar.gz
Source1:	index.html
Patch1:		dvd+rw-tools-7.0.manpatch
Patch2:		dvd+rw-tools-7.0-wexit.patch
Patch3:		dvd+rw-tools-7.0-glibc2.6.90.patch
Patch4:		dvd+rw-tools-7.0-reload.patch
Patch5:		dvd+rw-tools-7.0-wctomb.patch
Patch6:		dvd+rw-tools-7.0-dvddl.patch
Patch7:		dvd+rw-tools-7.1-noevent.patch
Patch8:		dvd+rw-tools-7.1-lastshort.patch
Patch9:		dvd+rw-tools-7.1-format.patch
Patch10:	dvd+rw-tools-7.1-bluray_srm+pow.patch
Patch11:	dvd+rw-tools-7.1-bluray_pow_freespace.patch
Patch12:	dvd+rw-tools-7.1-sysmacro-inc.patch

Requires:	genisoimage
BuildRequires:	gcc gcc-c++
BuildRequires:	kernel-headers m4
BuildRequires: make

%description
Collection of tools to master DVD+RW/+R media. For further
information see http://fy.chalmers.se/~appro/linux/DVD+RW/.

%prep
%setup -q
%patch -P1 -p1 -b .manpatch
%patch -P2 -p1 -b .wexit
%patch -P3 -p1 -b .glibc2.6.90
%patch -P4 -p1 -b .reload
%patch -P5 -p0 -b .wctomb
%patch -P6 -p0 -b .dvddl
%patch -P7 -p1 -b .noevent
%patch -P8 -p1 -b .lastshort
%patch -P9 -p1 -b .format
%patch -P10 -p1 -b .pow
%patch -P11 -p1 -b .freespace
%patch -P12 -p1 -b .sysmacro

install -m 644 %{SOURCE1} index.html

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export LDFLAGS="$RPM_LD_FLAGS"
make WARN="-DDEFAULT_BUF_SIZE_MB=16 -DRLIMIT_MEMLOCK" %{?_smp_mflags}

%install
# make install DESTDIR= does not work here
%makeinstall

%files
%license LICENSE
%doc index.html
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.1-46
- Prepare for Oreon 11 (RP1)
