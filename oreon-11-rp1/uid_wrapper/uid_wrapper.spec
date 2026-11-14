# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ae4bf3b8f0a748f470531a650436b39182c8217ee9269a9c7e925c64380a9bda

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           uid_wrapper
Version:        1.3.2
Release:        1%{?dist}
Summary:        A wrapper for privilege separation
License:        GPL-3.0-or-later
URL:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        uid_wrapper-1.3.2.tar.gz.asc
Source2:        uid_wrapper.keyring

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel >= 1.1.0

Recommends:     cmake
Recommends:     pkgconfig

%description
Some projects like a file server need privilege separation to be able to switch
to the connection user and do file operations. uid_wrapper convincingly lies
to the application letting it believe it is operating as root and even
switching between UIDs and GIDs as needed.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
UID_WRAPPER=1

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

%ldconfig_scriptlets

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libuid_wrapper.so*
%dir %{_libdir}/cmake/uid_wrapper
%{_libdir}/cmake/uid_wrapper/uid_wrapper-config-version.cmake
%{_libdir}/cmake/uid_wrapper/uid_wrapper-config.cmake
%{_libdir}/pkgconfig/uid_wrapper.pc
%{_mandir}/man1/uid_wrapper.1*

%changelog
%autochangelog
