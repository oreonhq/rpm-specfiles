# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5abe3bbbd8e54f0fa3ec945291b7e8fa8cfd3cccc43718f8758430f94126e512

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           xcb-util
Version:        0.4.1
Release:        1%{?dist}
Summary:        Convenience libraries sitting on top of libxcb
License:        X11-distribute-modifications-variant
URL:            https://xcb.freedesktop.org
Source0:        https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  m4
BuildRequires:  pkgconfig(xcb)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       pkgconfig(xcb)
Provides:       pkgconfig(xcb-util) = %{version}
Provides:       pkgconfig(xcb-atom) = %{version}
Provides:       pkgconfig(xcb-aux) = %{version}
Provides:       pkgconfig(xcb-event) = %{version}

%description devel
Headers and pkgconfig files for %{name}.

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
%{_libdir}/libxcb-util.so.*

%files devel
%{_includedir}/xcb/*.h
%{_libdir}/libxcb-util.so
%{_libdir}/pkgconfig/xcb-util.pc
%{_libdir}/pkgconfig/xcb-atom.pc
%{_libdir}/pkgconfig/xcb-aux.pc
%{_libdir}/pkgconfig/xcb-event.pc

%changelog
%autochangelog
