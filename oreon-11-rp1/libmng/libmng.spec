# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cf112a1fb02f5b1c0fce5cab11ea8243852c139e669c44014125874b14b7dfaa
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libmng
Version: 2.0.3
Release: 1%{?dist}
URL: http://www.libmng.com/
Summary: Library for Multiple-image Network Graphics support
License: Zlib
Source0: http://download.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: zlib-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: lcms2-devel
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: make

%package devel
Summary: Development files for the Multiple-image Network Graphics library
Requires: %{name} = %{version}-%{release}
Requires: zlib-devel
Requires: libjpeg-devel

%description
LibMNG is a library for accessing graphics in MNG (Multi-image Network
Graphics) and JNG (JPEG Network Graphics) formats.  MNG graphics are
basically animated PNGs.  JNG graphics are basically JPEG streams
integrated into a PNG chunk.

%description devel
LibMNG is a library for accessing MNG and JNG format graphics.  The
libmng-devel package contains files needed for developing or compiling
applications which use MNG graphics.

%prep
%oreon_sha256
%setup -q

%build
cp makefiles/Makefile.am .
autoreconf -if
%configure --enable-shared --disable-static --with-zlib --with-jpeg \
	--with-gnu-ld --with-lcms2
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc CHANGES LICENSE README*
%{_libdir}/*.so.*

%files devel
%doc doc/*
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_libdir}/pkgconfig/libmng.pc

%changelog
%autochangelog
