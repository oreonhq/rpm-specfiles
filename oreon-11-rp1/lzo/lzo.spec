# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c0f892943208266f9b6543b3ae308fab6284c5c90e627931446fb49b4221a072

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: lzo
Version: 2.10
Release: 1%{?dist}
Summary: Data compression library with very fast compression and decompression
License: GPL-2.0-or-later
URL: https://www.oberhumer.com/opensource/lzo/
Source0: https://www.oberhumer.com/opensource/lzo/download/lzo-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make

%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

%package devel
Summary: Development files for the lzo library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Provides: pkgconfig(lzo2) = %{version}

%description devel
LZO is a portable lossless data compression library written in ANSI C.
This package contains development files needed for lzo.

%prep
%oreon_sha256

%autosetup -p1

%build
%configure --disable-static --enable-shared
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}/lzo

%check
make check

%ldconfig_post
%ldconfig_postun

%files
%license COPYING
%doc AUTHORS NEWS README THANKS
%{_libdir}/liblzo2.so.2*

%files devel
%doc doc/LZOAPI.TXT doc/LZO.FAQ doc/LZO.TXT
%{_includedir}/lzo/
%{_libdir}/liblzo2.so
%{_libdir}/pkgconfig/lzo2.pc

%changelog
%autochangelog
