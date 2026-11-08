# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 01a7b881bd220bfdf615f97b8718f80bdfd3f6add385b993dcf6efd14e8c0ac6
%global source1_hash 110535522396708cea37c72a802c5e7e81391139f5f7985631c93ef242b206a4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary: GNU data compression program
Name: gzip
Version:        1.14
Release:        1%{?dist}
# info pages are under GFDL license
License: GPL-3.0-or-later AND GFDL-1.3-only
Source0:        https://mirror.cs.odu.edu/gnu/gzip/gzip-%{version}.tar.xz
Source1:        fdl-1.3.txt

# downstream solution for coloured z*grep (#1034839)
Source100: colorzgrep.csh
Source101: colorzgrep.sh

Patch1:        s390_errno.patch
Patch2:        CVE-2026-41911.patch

# Fixed in upstream code.
# http://thread.gmane.org/gmane.comp.gnu.gzip.bugs/378
URL: https://www.gzip.org/
# Requires should not be added for gzip wrappers (eg. zdiff, zgrep,
# zless) of another tools, because gzip "extends" the tools by its
# wrappers much more than it "requires" them.
Requires: coreutils 
BuildRequires: texinfo, gcc, autoconf, automake, less
BuildRequires: make
BuildRequires:  oreon-rpm-macros
Conflicts: filesystem < 3
Provides: /bin/gunzip
Provides: /bin/gzip
Provides: /bin/zcat
# Gzip contains bundled Gnulib
Provides: bundled(gnulib)

%description
The gzip package contains the popular GNU gzip data compression
program. Gzipped files have a .gz extension.

Gzip should be installed on your system, because it is a
very commonly used data compression program.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -

%setup -q
%patch 1 -p1
%patch 2 -p1

cp %{SOURCE1} .
autoreconf

%build
export DEFS="NO_ASM"
export CPPFLAGS="-DHAVE_LSTAT"
export CC="%{__cc}"
export CPP="%{__cpp}"
export CXX="%{__cxx}"
%ifarch s390x

#When the otpimizations are enabled, the huft test fails as of F44/gzip1.14
#export CFLAGS="$RPM_OPT_FLAGS -Dalignas=_Alignas -DDFLTCC_LEVEL_MASK=0x7e"
#use this in the next realease after gzip 1.13 export CFLAGS="$RPM_OPT_FLAGS -DDFLTCC_LEVEL_MASK=0x7e"
#%configure --enable-dfltcc

%configure
%else
%configure
%endif
make
%check
make check
#make gzip.info

%install
%makeinstall

gzip -9nf ${RPM_BUILD_ROOT}%{_infodir}/gzip.info*

# we don't ship it, so let's remove it from ${RPM_BUILD_ROOT}
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
# uncompress is a part of ncompress package
rm -f ${RPM_BUILD_ROOT}%{_bindir}/uncompress

# coloured z*grep (#1034839)
%global profiledir %{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE100} %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE101} %{buildroot}%{profiledir}

%files
%doc NEWS README AUTHORS ChangeLog THANKS TODO
%license COPYING fdl-1.3.txt
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/gzip.info*
%{profiledir}/*

