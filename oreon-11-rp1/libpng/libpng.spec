# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d80dd2a38a37f803cb9b6ac7b14bd6e74ddc3b654780a8380bdf93523fdb4389

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libpng
Version: 1.6.59
Release: 1%{?dist}
Summary: A library of functions for manipulating PNG image format files
License: libpng-2.0
URL: http://www.libpng.org/pub/png/
Source0: https://downloads.sourceforge.net/libpng/libpng-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: zlib-devel

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files. PNG is a
bit-mapped graphics format similar to the GIF format. PNG was created to
replace the GIF format, since GIF uses a patented data compression
algorithm.

%package devel
Summary: Development tools for programs to manipulate PNG image format files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: zlib-devel
Requires: pkgconfig
Provides: pkgconfig(libpng) = %{version}
Provides: pkgconfig(libpng16) = %{version}

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.

%package tools
Summary: Tools for PNG image format file manipulation
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains tools used to fix and inspect PNG image files.

%prep
%oreon_sha256

%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la

%check
make check

%ldconfig_post
%ldconfig_postun

%files
%license LICENSE
%doc ANNOUNCE CHANGES README TODO
%{_libdir}/libpng16.so.16*
%{_mandir}/man5/png.5*

%files devel
%doc libpng-manual.txt example.c
%{_bindir}/libpng*-config
%{_includedir}/png.h
%{_includedir}/pngconf.h
%{_includedir}/pnglibconf.h
%{_includedir}/libpng16/
%{_libdir}/libpng.so
%{_libdir}/libpng16.so
%{_libdir}/pkgconfig/libpng.pc
%{_libdir}/pkgconfig/libpng16.pc
%{_mandir}/man3/libpng.3*
%{_mandir}/man3/libpngpf.3*

%files tools
%{_bindir}/png-fix-itxt
%{_bindir}/pngfix

%changelog
%autochangelog
