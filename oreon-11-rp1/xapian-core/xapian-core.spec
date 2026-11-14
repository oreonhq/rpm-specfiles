# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c55c9bc8613ad3ec2c218eafca088c218ab7cddcba7ef08f3af0e542f4e521bc

Name: xapian-core
Version: 1.4.29
Release: 1%{?dist}
Summary: Search engine library
License: GPL-2.0-or-later
URL: https://xapian.org/
Source0: https://oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(zlib)

%description
Xapian is a highly adaptable search engine library with support for
probabilistic ranking and boolean query operators.

%package devel
Summary: Development files for Xapian
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and build metadata for applications using Xapian.

%prep
%oreon_sha256
%autosetup

%build
%configure \
  --disable-static \
  --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
rm -rf %{buildroot}%{_docdir}/xapian-core

%check
%make_build check

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/copydatabase
%{_bindir}/quest
%{_bindir}/simpleexpand
%{_bindir}/simpleindex
%{_bindir}/simplesearch
%{_bindir}/xapian-check
%{_bindir}/xapian-compact
%{_bindir}/xapian-delve
%{_bindir}/xapian-metadata
%{_bindir}/xapian-progsrv
%{_bindir}/xapian-replicate
%{_bindir}/xapian-replicate-server
%{_bindir}/xapian-tcpsrv
%{_libdir}/libxapian.so.*
%{_mandir}/man1/copydatabase.1*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/xapian-*.1*

%files devel
%{_bindir}/xapian-config
%{_includedir}/xapian/
%{_includedir}/xapian.h
%{_libdir}/libxapian.so
%{_libdir}/pkgconfig/xapian-core.pc
%{_libdir}/cmake/xapian/
%{_datadir}/aclocal/xapian.m4

%changelog
%autochangelog
