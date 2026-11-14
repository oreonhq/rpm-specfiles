# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7c260a5294412aed429df1da2f8afd3bd07b7cba3fec772fba15a613a6d5c638

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: xcb-util-keysyms
Version: 0.4.1
Release: 1%{?dist}
Summary: Standard X key constants and keycodes conversion on top of libxcb
License: X11-distribute-modifications-variant
URL: https://xcb.freedesktop.org
Source0: https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: m4
BuildRequires: pkgconfig(xcb-util) >= 0.3.8

%description
XCB util-keysyms module provides the following library:

  - keysyms: Standard X key constants and conversion to/from keycodes.

%package devel
Summary: Development and header files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: pkgconfig(xcb)
Provides: pkgconfig(xcb-keysyms) = %{version}

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
