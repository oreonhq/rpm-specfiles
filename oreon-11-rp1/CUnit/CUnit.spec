# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: LGPL-2.0-or-later

%global source0_hash f5b29137f845bb08b77ec60584fdb728b4e58f1023e6f249a464efa49a40f214

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: CUnit
Version: 2.1.3
Release: 1%{?dist}
Summary: Unit testing framework for C
License: LGPL-2.0-or-later
URL: https://cunit.sourceforge.net/
Source0: https://downloads.sourceforge.net/cunit/CUnit-2.1-3.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: make

%description
CUnit is a lightweight unit testing framework for C.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: CUnit-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(cunit) = %{version}

%description devel
Headers and libraries for %{name}.

%prep
%oreon_sha256
%autosetup -n CUnit-2.1-3 -p1
libtoolize --force --copy
aclocal
autoheader
automake --add-missing --copy
autoconf

%build
%configure --enable-shared --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libcunit.so.*
%{_datadir}/CUnit/

%files devel
%{_libdir}/libcunit.so
%{_includedir}/CUnit/
%{_libdir}/pkgconfig/cunit.pc

%changelog
%autochangelog
