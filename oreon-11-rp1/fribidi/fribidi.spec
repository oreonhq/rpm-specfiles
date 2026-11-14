# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1de5e8073d035388b71d0b2d452b1da1f8caeea8a7702997b401fe1b6250727f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: fribidi
Version: 1.0.18
Release: 1%{?dist}
Summary: Unicode bidirectional algorithm library
License: LGPL-2.1-or-later
URL: https://github.com/fribidi/fribidi
Source0: https://github.com/fribidi/fribidi/releases/download/v%{version}/fribidi-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: help2man
BuildRequires: meson
BuildRequires: python3

%description
FriBidi implements the Unicode bidirectional algorithm. It is used to
display right-to-left and mixed-direction text.

%package devel
Summary: Development files for FriBidi
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and development files for applications using FriBidi.

%prep
%oreon_sha256
%autosetup

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
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/fribidi
%{_libdir}/libfribidi.so.0*
%{_mandir}/man1/fribidi.1*

%files devel
%{_includedir}/fribidi/
%{_libdir}/libfribidi.so
%{_libdir}/pkgconfig/fribidi.pc

%changelog
%autochangelog
