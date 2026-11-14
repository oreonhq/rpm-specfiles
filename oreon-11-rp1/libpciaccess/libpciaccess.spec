# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3c55aa86c82e54a4e3109786f0463530d53b36b6d1cfd14616454f985dd2aa43

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libpciaccess
Version:        0.19
Release:        1%{?dist}
Summary:        PCI access library

License:        HPND AND MIT
URL:            https://www.x.org/
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

Patch2:         libpciaccess-rom-size.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-util-macros
BuildRequires:  zlib-devel
Requires:       hwdata

%description
libpciaccess is a library for portable PCI access routines across multiple
operating systems.

%package devel
Summary:        PCI access library development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development package for libpciaccess.

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libpciaccess.so.0
%{_libdir}/libpciaccess.so.0.11.*

%files devel
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc

%changelog
%autochangelog
