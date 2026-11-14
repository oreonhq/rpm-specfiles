# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3e15d4f0e22d8ddbfbb9f5d77db43eacd7a304029bf25a6166cc63caa96d04ba

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: xcb-util-renderutil
Version: 0.3.10
Release: 1%{?dist}
Summary: Convenience functions for the Render extension
License: X11-distribute-modifications-variant AND HPND-sell-variant
URL: https://xcb.freedesktop.org
Source0: https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: m4
BuildRequires: pkgconfig(xcb-util) >= 0.3.8

%description
XCB util-renderutil module provides the following library:

  - renderutil: Convenience functions for the Render extension.

%package devel
Summary: Development and header files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: pkgconfig(xcb)
Requires: pkgconfig(xcb-render)
Provides: pkgconfig(xcb-renderutil) = %{version}

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
