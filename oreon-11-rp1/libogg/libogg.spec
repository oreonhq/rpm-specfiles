# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5c8253428e181840cd20d41f3ca16557a9cc04bad4a3d04cce84808677fa1061
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:        The Ogg bitstream file format library
Name:           libogg
Epoch:          2
Version:        1.3.6
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://www.xiph.org/

Source0:        https://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  make
BuildRequires:  cmake

%description
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.

%package devel
Summary:        Files needed for development using libogg
Requires:       libogg = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Requires:       automake

%description devel
Libogg is a library used for manipulating Ogg bitstreams. The
libogg-devel package contains the header files and documentation
needed for development using libogg.

%package devel-docs
Summary:        Documentation for developing Ogg applications
BuildArch:      noarch

%description devel-docs
Documentation for developing applications with libogg

%prep
%oreon_sha256
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

mv $RPM_BUILD_ROOT%{_docdir}/ogg __installed_docs

mkdir -p %{buildroot}%{_datadir}/aclocal
cp -pr ogg.m4 %{buildroot}%{_datadir}/aclocal/

%ldconfig_scriptlets

%files
%doc AUTHORS CHANGES COPYING README.md
%{_libdir}/libogg.so.0*

%files devel
%dir %{_includedir}/ogg
%{_includedir}/ogg/ogg.h
%{_includedir}/ogg/os_types.h
%{_includedir}/ogg/config_types.h
%{_libdir}/libogg.so
%{_libdir}/pkgconfig/ogg.pc
%{_datadir}/aclocal/ogg.m4
%{_libdir}/cmake/Ogg/

%files devel-docs
%doc __installed_docs/*

%changelog
%autochangelog
