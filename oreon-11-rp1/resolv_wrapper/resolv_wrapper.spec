# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fbc30f77da3e12ecd4ef66ccf5ab77e0b744930ccd89062404082f928a8ec2e0

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           resolv_wrapper
Version:        1.1.8
Release:        1%{?dist}
Summary:        A wrapper for dns name resolving or dns faking
License:        BSD-3-Clause
URL:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        resolv_wrapper-1.1.8.tar.gz.asc
Source2:        resolv_wrapper.keyring
Patch0:         resolv_wrapper-fix-cmocka-1.1.6+-support.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel
BuildRequires:  socket_wrapper

Recommends:     cmake
Recommends:     pkgconfig

%description
It is likely that if you have a server/client architecture, you need to do DNS
queries or a third party library, like Kerberos needs to be able to do queries.
In the case of Kerberos the client needs to look the address of the KDC up via a
SRV record. resolv_wrapper is able to either redirect all DNS queries to your
DNS server implementation, or fake DNS replies!

To use it set the following environment variables:

LD_PRELOAD=libresolv_wrapper.so
RESOLV_WRAPPER_CONF=./my_resolv.conf

This package doesn't have a devel package because this project is for
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
LD_PRELOAD=%{__cmake_builddir}/src/libresolv_wrapper.so bash -c '>/dev/null'

%ldconfig_scriptlets

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libresolv_wrapper.so*
%dir %{_libdir}/cmake/resolv_wrapper
%{_libdir}/cmake/resolv_wrapper/resolv_wrapper-config-version.cmake
%{_libdir}/cmake/resolv_wrapper/resolv_wrapper-config.cmake
%{_libdir}/pkgconfig/resolv_wrapper.pc
%{_mandir}/man1/resolv_wrapper.1*

%changelog
%autochangelog
