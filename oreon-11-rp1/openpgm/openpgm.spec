# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8d707ef8dda45f4a7bc91016d7f2fed6a418637185d76c7ab30b306499c6d393
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:          openpgm
Version:       5.3.128
%global name_alias        pgm
%global version_main      5.3
%global version_dash_main 5-3
%global version_dash      %{version_dash_main}-128
Release:        %{autorelease}
Summary:       An implementation of the PGM reliable multicast protocol

License:       LGPL-2.1-or-later
URL:           https://github.com/steve-o/%{name}
Source0:       https://github.com/steve-o/%{name}/archive/release-%{version_dash}.tar.gz#/%{name}-%{version}.tar.gz

Patch2:        openpgm-02-checksum-arch.patch
Patch3:        openpgm-03-pkgconfig.patch
Patch6:        openpgm-configure-c99.patch
Patch7:        openpgm-c99.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: python3
BuildRequires: dos2unix
BuildRequires: perl-interpreter

%description
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.

%package devel
Summary:       Development files for openpgm
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains OpenPGM related development libraries and header files.

%prep
%oreon_sha256
%setup -q -n %{name}-release-%{version_dash}/%{name}/%{name_alias}
%patch -P2 -p3
%patch -P3 -p3
%patch -P6 -p3
%patch -P7 -p3
dos2unix examples/getopt.c examples/getopt.h
mv openpgm-5.2.pc.in openpgm-5.3.pc.in

%build
libtoolize --force --copy
aclocal
autoheader
automake --copy --add-missing
autoconf
%configure

%define _lto_cflags -flto=auto -ffat-lto-objects

%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/lib%{name_alias}.{a,la}

mv -f %{buildroot}%{_includedir}/%{name_alias}-%{version_main}/%{name_alias} %{buildroot}%{_includedir}/

%files
%doc COPYING
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc examples/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/openpgm-5.3.pc

%changelog
%autochangelog
