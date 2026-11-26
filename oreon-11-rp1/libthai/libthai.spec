# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ddba8b53dfe584c3253766030218a88825488a51a7deef041d096e715af64bdd
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:  Thai language support routines
Name: libthai
Version: 0.1.30
Release: 1%{?dist}
License: LGPL-2.1-or-later
Source0:        http://linux.thai.net/pub/thailinux/software/libthai/libthai-%{version}.tar.xz
Patch0: libthai-0.1.9-multilib.patch
URL: http://linux.thai.net

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: pkgconfig(datrie-0.2)
BuildRequires: doxygen
BuildRequires: make

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package devel
Summary:  Thai language support routines
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Provides: pkgconfig(libthai) = %{version}

%description devel
The libthai-devel package includes the header files and developer docs 
for the libthai package.

Install libthai-devel if you want to develop programs which will use
libthai.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

mkdir installed-docs
mv $RPM_BUILD_ROOT%{_docdir}/libthai/* installed-docs
rmdir $RPM_BUILD_ROOT%{_docdir}/libthai

rm $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc README AUTHORS COPYING ChangeLog
%{_libdir}/lib*.so.*
%{_datadir}/libthai

%files devel
%doc installed-docs/*
%{_includedir}/thai
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
