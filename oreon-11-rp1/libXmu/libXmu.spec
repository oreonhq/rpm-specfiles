# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fcb27793248a39e5fcc5b9c4aec40cc0734b3ca76aac3d7d1c264e7f7e14e8b2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: X.Org X11 libXmu/libXmuu runtime libraries
Name: libXmu
Version: 1.2.1
Release: %{autorelease}
License: MIT-open-group AND SMLNJ AND X11 AND ISC
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: xorg-x11-util-macros
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXt-devel

%description
X.Org X11 libXmu/libXmuu runtime libraries

%package devel
Summary: X.Org X11 libXmu development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXmu development package

%prep
%oreon_sha256
%setup -q

%build
autoreconf -v --install --force
%configure --disable-static
make  %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -rf $RPM_BUILD_ROOT%{_docdir}

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING README.md ChangeLog
%{_libdir}/libXmu.so.6
%{_libdir}/libXmu.so.6.2.0
%{_libdir}/libXmuu.so.1
%{_libdir}/libXmuu.so.1.0.0

%files devel
%dir %{_includedir}/X11/Xmu
%{_includedir}/X11/Xmu/Atoms.h
%{_includedir}/X11/Xmu/CharSet.h
%{_includedir}/X11/Xmu/CloseHook.h
%{_includedir}/X11/Xmu/Converters.h
%{_includedir}/X11/Xmu/CurUtil.h
%{_includedir}/X11/Xmu/CvtCache.h
%{_includedir}/X11/Xmu/DisplayQue.h
%{_includedir}/X11/Xmu/Drawing.h
%{_includedir}/X11/Xmu/Editres.h
%{_includedir}/X11/Xmu/EditresP.h
%{_includedir}/X11/Xmu/Error.h
%{_includedir}/X11/Xmu/ExtAgent.h
%{_includedir}/X11/Xmu/Initer.h
%{_includedir}/X11/Xmu/Lookup.h
%{_includedir}/X11/Xmu/Misc.h
%{_includedir}/X11/Xmu/StdCmap.h
%{_includedir}/X11/Xmu/StdSel.h
%{_includedir}/X11/Xmu/SysUtil.h
%{_includedir}/X11/Xmu/WhitePoint.h
%{_includedir}/X11/Xmu/WidgetNode.h
%{_includedir}/X11/Xmu/WinUtil.h
%{_includedir}/X11/Xmu/Xct.h
%{_includedir}/X11/Xmu/Xmu.h
%{_libdir}/libXmu.so
%{_libdir}/libXmuu.so
%{_libdir}/pkgconfig/xmu.pc
%{_libdir}/pkgconfig/xmuu.pc

%changelog
%autochangelog
