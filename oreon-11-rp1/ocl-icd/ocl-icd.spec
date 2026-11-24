# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cdd7984425fa92d37273eee4180b5f57b047eda6dd8fd623e58498f844b09b75
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           ocl-icd
Version:        2.3.5
Release:        1%{?dist}
Summary:        OpenCL Library (Installable Client Library) Bindings
License:        BSD-2-Clause
URL:            https://github.com/OCL-dev/%{name}/

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires:  asciidoc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  clang
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  opencl-headers
BuildRequires:  ruby
BuildRequires:  rubygems
BuildRequires:  xmlto

%description
%{summary}.

%package devel
Summary:        OpenCL Library Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opencl-headers

%description devel
This package contains the development files for the OpenCL ICD bindings.

%prep
%oreon_sha256
%autosetup

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install
rm -vrf %{buildroot}%{_defaultdocdir}

%check
make check

%files
%license COPYING
%doc NEWS README
%{_libdir}/libOpenCL.so.1
%{_libdir}/libOpenCL.so.1.0.0
%{_mandir}/man7/libOpenCL.7*
%{_mandir}/man7/libOpenCL.so.7*

%files devel
%doc ocl_icd_loader_gen.map ocl_icd_bindings.c
%{_includedir}/ocl_icd.h
%{_bindir}/cllayerinfo
%{_libdir}/libOpenCL.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/OpenCL.pc

%changelog
%autochangelog
