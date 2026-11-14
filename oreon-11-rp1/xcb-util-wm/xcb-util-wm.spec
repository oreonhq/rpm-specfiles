# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 62c34e21d06264687faea7edbf63632c9f04d55e72114aa4a57bb95e4f888a0b

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: xcb-util-wm
Version: 0.4.2
Release: 1%{?dist}
Summary: Client and window-manager helper library on top of libxcb
License: X11-distribute-modifications-variant
URL: https://xcb.freedesktop.org
Source0: https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: m4
BuildRequires: pkgconfig(xcb-util) >= 0.3.8

%description
XCB util-wm module provides the following libraries:

  - ewmh: Both client and window-manager helpers for EWMH.
  - icccm: Both client and window-manager helpers for ICCCM.

%package devel
Summary: Development and header files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: pkgconfig(xcb)
Provides: pkgconfig(xcb-ewmh) = %{version}
Provides: pkgconfig(xcb-icccm) = %{version}

%description devel
Development files for %{name}.

%prep
%oreon_sha256

%autosetup -p1

%build
%configure --with-pic --disable-static --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/*.so.*

%files devel
%doc NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h

%changelog
%autochangelog
