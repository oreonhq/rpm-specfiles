# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: HPND-sell-variant

%global source0_hash d4a4df096aba96fea02c029ee3a44e11a47eb7f7213c1a729be83e85ec3fde10

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libxshmfence
Version: 1.3.3
Release: 1%{?dist}
Summary: X11 shared memory fences
License: HPND-sell-variant
URL: https://www.x.org
Source0: https://www.x.org/releases/individual/lib/libxshmfence-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xproto)

%description
Shared memory fences for X11.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(xshmfence) = %{version}

%description devel
Headers and libraries for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make check

%files
%license COPYING
%{_libdir}/libxshmfence.so.1
%{_libdir}/libxshmfence.so.1.*

%files devel
%{_libdir}/libxshmfence.so
%{_includedir}/X11/xshmfence.h
%{_libdir}/pkgconfig/xshmfence.pc

%changelog
%autochangelog
