# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: MIT

%global source0_hash 52733c1f5262fca35f64e7d5060c6fcd81a880ba8e1e65c9621cf0727afb5d11

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libXdamage
Version: 1.1.6
Release: 1%{?dist}
Summary: X Damage extension library
License: MIT
URL: https://www.x.org
Source0: https://www.x.org/releases/individual/lib/libXdamage-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(damageproto)
BuildRequires: pkgconfig(xproto)

%description
X Damage extension library.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(xdamage) = %{version}

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
%{_libdir}/libXdamage.so.1
%{_libdir}/libXdamage.so.1.*

%files devel
%{_libdir}/libXdamage.so
%{_includedir}/X11/extensions/Xdamage.h
%{_libdir}/pkgconfig/xdamage.pc

%changelog
%autochangelog
