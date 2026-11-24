# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 173a822efd207d72cda7d7f4e951c5000f31b10209366ff7f0f5972f7f9ff137
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           liblqr-1
Version:        0.4.2
Release:        1%{?dist}
Summary:        LiquidRescale library
License:        GPL-3.0-only
URL:            http://liquidrescale.wikidot.com/
Source0:        http://liblqr.wikidot.com/local--files/en:download-page/%{name}-%{version}.tar.bz2
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  glib2-devel
BuildRequires:  make

%description
The LiquidRescale (lqr) library provides a C/C++ API for
performing non-uniform resizing of images by the seam-carving
technique.

%package devel
Summary:        LiquidRescale library development kit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel, pkgconfig

%description devel
The libqr-devel package contains the header files
needed to develop applications with liblqr

%prep
%oreon_sha256
%autosetup

%build
%set_build_flags
export CFLAGS="$CFLAGS -std=gnu11"
export LDFLAGS="%{build_ldflags} `pkg-config --libs glib-2.0` -lm"
%configure
%make_build

%install
%make_install

find $RPM_BUILD_ROOT -name \*.la -exec %{__rm} -f {} \;

%files
%doc README ChangeLog COPYING
%{_libdir}/liblqr-1.so.0.3.2
%{_libdir}/liblqr-1.so.0

%files devel
%doc docs/liblqr_manual.docbook
%{_libdir}/liblqr-1.so
%{_includedir}/lqr-1/
%{_libdir}/pkgconfig/lqr-1.pc

%changelog
%autochangelog
