# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ccad8ee5dadb1271fd4727ad14d9bd77a64e505608766c4e98267d9aede40d3d

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: xcb-util-image
Version: 0.4.1
Release: 1%{?dist}
Summary: Port of Xlib's XImage and XShmImage functions on top of libxcb
License: X11-distribute-modifications-variant
URL: https://xcb.freedesktop.org
Source0: https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: m4
BuildRequires: pkgconfig(xcb-util) >= 0.3.8

%description
XCB util-image module provides the following library:

  - image: Port of Xlib's XImage and XShmImage functions.

%package devel
Summary: Development and header files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: pkgconfig(xcb)
Requires: pkgconfig(xcb-shm)
Provides: pkgconfig(xcb-image) = %{version}

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
