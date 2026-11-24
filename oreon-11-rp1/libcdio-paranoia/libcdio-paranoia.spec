# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 186892539dedd661276014d71318c8c8f97ecb1250a86625256abd4defbf0d0c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libcdio-paranoia
Version: 10.2+2.0.2
Release: 1%{?dist}
Summary: CD paranoia on top of libcdio
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/libcdio/
Source0: https://github.com/libcdio/libcdio-paranoia/releases/download/release-%{version}/libcdio-paranoia-%{version}.tar.bz2
Patch0: 2334834.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: gettext-devel
BuildRequires: chrpath
BuildRequires: libcdio-devel
BuildRequires: make

%description
This CDDA reader distribution ('libcdio-cdparanoia') reads audio from the
CDROM directly as data, with no analog step between, and writes the
data to a file or pipe as .wav, .aifc or as raw 16 bit linear PCM.

Split off from libcdio to allow more flexible licensing and to be compatible
with cdparanoia-III-10.2's license. And also, libcdio is just too large.

%package devel
Summary: Header files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files and libraries for %{name}.

%prep
%oreon_sha256
%setup -q
%patch -P 0 -p 1

sed -i -e 's,-I${includedir},-I${includedir}/cdio,g' libcdio_paranoia.pc.in
sed -i -e 's,-I${includedir},-I${includedir}/cdio,g' libcdio_cdda.pc.in

f=doc/ja/cd-paranoia.1.in
iconv -f euc-jp -t utf-8 -o $f.utf8 $f && mv $f.utf8 $f
iconv -f ISO88591 -t utf-8 -o THANKS.utf8 THANKS && mv THANKS.utf8 THANKS

%build
%configure \
	--disable-dependency-tracking \
	--disable-static \
	--disable-rpath
%make_build

%install
%make_install

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

cp -a $RPM_BUILD_ROOT%{_includedir}/cdio/paranoia/*.h $RPM_BUILD_ROOT%{_includedir}/cdio/

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/*.so.*

%files
%license COPYING
%doc AUTHORS NEWS.md README.md THANKS
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*

%files devel
%doc doc/overlapdef.txt
%{_includedir}/cdio/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
