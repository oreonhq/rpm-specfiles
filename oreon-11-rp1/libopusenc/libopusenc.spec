# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f616d3aff9b2034547894ccb8ab56c36cf1a4acb0d922c5d7119f97bbe58642c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:     libopusenc
Version:  0.3
Release:        %{autorelease}
Summary:  A library that provides an easy way to encode Ogg Opus files
License:  LicenseRef-Callaway-BSD
URL:      https://opus-codec.org/

Source0:  https://archive.mozilla.org/pub/opus/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: doxygen
BuildRequires: opus-devel
BuildRequires: make

%description
A library that provides an easy way to encode Ogg Opus files.

%package  devel
Summary:  Development package for libopusenc
Requires: opus-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with libopusenc.

%prep
%oreon_sha256
%setup -q

%build
%configure --disable-static

%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete
rm -rf %{buildroot}%{_datadir}/doc/libopusenc/

%check
make check %{?_smp_mflags} V=1

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libopusenc.so.*

%files devel
%doc doc/html
%{_includedir}/opus/opusenc.h
%{_libdir}/libopusenc.so
%{_libdir}/pkgconfig/libopusenc.pc

%changelog
%autochangelog
