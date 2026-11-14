# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: LGPL-2.1-or-later

%global source0_hash 3f84f66e97b5f408b829060db2fedb3b6622740651a1cf646382554fc3fb1671

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: librhsm
Version: 0.0.5
Release: 1%{?dist}
Summary: Red Hat Subscription Manager library
License: LGPL-2.1-or-later
URL: https://github.com/rpm-software-management/librhsm
Source0: https://github.com/rpm-software-management/librhsm/releases/download/v%{version}/librhsm-%{version}.tar.xz
Source1: https://github.com/rpm-software-management/librhsm/releases/download/v%{version}/librhsm-%{version}.tar.xz.asc
Source2: gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: meson
BuildRequires: gnupg2
BuildRequires: pkgconfig(gio-2.0) >= 2.44
BuildRequires: pkgconfig(glib-2.0) >= 2.44
BuildRequires: pkgconfig(gobject-2.0) >= 2.44
BuildRequires: pkgconfig(json-glib-1.0) >= 1.2
BuildRequires: pkgconfig(openssl)

%description
Library helpers for Red Hat Subscription Manager style product and
entitlement certificate handling.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(librhsm) = %{version}

%description devel
Headers and pkgconfig for %{name}.

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

%files
%license COPYING
%doc README.md
%{_libdir}/librhsm.so.0*

%files devel
%{_libdir}/librhsm.so
%{_includedir}/rhsm/
%{_libdir}/pkgconfig/librhsm.pc

%changelog
%autochangelog
