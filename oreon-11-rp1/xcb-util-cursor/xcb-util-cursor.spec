# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fdeb8bd127873519be5cc70dcd0d3b5d33b667877200f9925a59fdcad8f7a933

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: xcb-util-cursor
Version: 0.1.6
Release: 1%{?dist}
Summary: Cursor library on top of libxcb
License: X11-distribute-modifications-variant
URL: https://xcb.freedesktop.org
Source0: https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: m4
BuildRequires: pkgconfig(xcb-util) >= 0.3.8
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-image)

%description
XCB util-cursor module provides the following libraries:

  - cursor: port of libxcursor

%package devel
Summary: Development and header files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: pkgconfig(xcb)
Provides: pkgconfig(xcb-cursor) = %{version}

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
