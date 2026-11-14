# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash dc79ab072779be4403b45b60cd044dd13780d4bb9675d27abf1932ada7c8a88d

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           nss_wrapper
Version:        1.1.16
Release:        1%{?dist}
Summary:        A wrapper for the user, group and hosts NSS API
License:        BSD-3-Clause
URL:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        nss_wrapper-1.1.16.tar.gz.asc
Source2:        nss_wrapper.keyring
Patch0:         nwrap-fix-tests.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel
BuildRequires:  perl-generators

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     cmake
Recommends:     pkgconfig

%description
There are projects which provide daemons needing to be able to create, modify
and delete Unix users. Or just switch user ids to interact with the system e.g.
a user space file server. To be able to test that you need the privilege to
modify the passwd and groups file. With nss_wrapper it is possible to define
your own passwd and groups file which will be used by software to act correctly
while under test.

If you have a client and server under test they normally use functions to
resolve network names to addresses (dns) or vice versa. The nss_wrappers allow
you to create a hosts file to setup name resolution for the addresses you use
with socket_wrapper.

To use it set the following environment variables:

LD_PRELOAD=libnss_wrapper.so
NSS_WRAPPER_PASSWD=/path/to/passwd
NSS_WRAPPER_GROUP=/path/to/group
NSS_WRAPPER_HOSTS=/path/to/host

This package doesn't have a devel package because this project is for
development/testing.

%package libs
Summary:        Shared library for nss_wrapper

%description libs
The %{name}-libs package provides only the shared library.
For a minimal footprint, install just this package.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%cmake -DUNIT_TESTING=ON
%cmake_build

%install
%cmake_install
sed -i '1 s|/usr/bin/env perl|/usr/bin/perl|' %{buildroot}%{_bindir}/nss_wrapper.pl

%check
%ctest

%ldconfig_scriptlets libs

%files
%{_bindir}/nss_wrapper.pl
%dir %{_libdir}/cmake/nss_wrapper
%{_libdir}/cmake/nss_wrapper/nss_wrapper-config-version.cmake
%{_libdir}/cmake/nss_wrapper/nss_wrapper-config.cmake
%{_libdir}/pkgconfig/nss_wrapper.pc
%{_mandir}/man1/nss_wrapper.1*

%files libs
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libnss_wrapper.so*

%changelog
%autochangelog
