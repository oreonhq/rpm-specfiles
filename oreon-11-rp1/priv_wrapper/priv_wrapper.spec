# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b10bff1672640e9e0dc92a821e8173bd0d727a148b5939f01e95abc89621e3c1

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           priv_wrapper
Version:        1.0.1
Release:        1%{?dist}
Summary:        A library to disable resource limits and other privilege dropping
License:        GPL-3.0-or-later
URL:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        priv_wrapper-1.0.1.tar.gz.asc
Source2:        priv_wrapper.keyring
Patch0:         priv_wrapper-fix-cmocka-1.1.6+-support.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel >= 1.1.0

Recommends:     cmake
Recommends:     pkgconfig

%description
priv_wrapper aims to help running processes which are dropping privileges or
are restricting resources in test environments.
It can disable chroot, prctl, pledge and setrlmit system calls. A disabled call
always succeeds (i.e. returns 0) and does nothing.
The system call pledge exists only on OpenBSD.

To use it, set the following environment variables:

LD_PRELOAD=libpriv_wrapper.so
PRIV_WRAPPER_CHROOT_DISABLE=1

This package does not have a devel package, because this project is for
development/testing.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%cmake -DUNIT_TESTING=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets

%files
%doc AUTHORS README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libpriv_wrapper.so*
%dir %{_libdir}/cmake/priv_wrapper
%{_libdir}/cmake/priv_wrapper/priv_wrapper-config-version.cmake
%{_libdir}/cmake/priv_wrapper/priv_wrapper-config.cmake
%{_libdir}/pkgconfig/priv_wrapper.pc
%{_mandir}/man1/priv_wrapper.1*

%changelog
%autochangelog
