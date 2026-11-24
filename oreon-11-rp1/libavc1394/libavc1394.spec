# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7cb1ff09506ae911ca9860bef4af08c2403f3e131f6c913a2cbd6ddca4215b53
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:        Audio/Video Control library for IEEE-1394 devices
Name:           libavc1394
Version:        0.5.4
Release:        1%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://sourceforge.net/projects/libavc1394/
Source0:        https://sourceforge.net/projects/libavc1394/files/libavc1394/libavc1394-%{version}.tar.gz
Patch1:         libavc1394-%{version}-librom.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  libraw1394-devel
BuildRequires:  chrpath
BuildRequires:  make

ExcludeArch:    s390 s390x

%description
The libavc1394 library allows utilities to control IEEE-1394 devices
using the AV/C specification.  Audio/Video Control allows applications
to control devices like the tape on a VCR or camcorder.

%package devel
Summary: Development libs for libavc1394

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libraw1394-devel%{?_isa}

%description devel
Development libraries required to build applications using libavc1394.

%prep
%oreon_sha256
%autosetup -N
%patch -P 1 -p1 -b .librom
chmod -x test/dvcont.c

%build
%configure
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{la,a}

chrpath -d $RPM_BUILD_ROOT%{_libdir}/lib*
chrpath -d $RPM_BUILD_ROOT%{_bindir}/*

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README ChangeLog TODO
%license COPYING
%{_bindir}/dvcont
%{_bindir}/mkrfc2734
%{_bindir}/panelctl
%{_mandir}/man1/dvcont.1*
%{_mandir}/man1/panelctl.1*
%{_mandir}/man1/mkrfc2734.1*
%{_libdir}/libavc1394.so.*
%{_libdir}/librom1394.so.*

%files devel
%{_includedir}/libavc1394/
%{_libdir}/pkgconfig/libavc1394.pc
%{_libdir}/libavc1394.so
%{_libdir}/librom1394.so

%changelog
%autochangelog
