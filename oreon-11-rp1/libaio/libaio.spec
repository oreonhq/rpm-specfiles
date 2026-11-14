# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2c44d1c5fd0d43752287c9ae1eb9c023f04ef848ea8d4aafa46e9aedb678200b

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libaio
Version:        0.3.113
Release:        1%{?dist}
Summary:        Linux-native asynchronous I/O access library
License:        LGPL-2.1-or-later
URL:            https://pagure.io/libaio
Source0:        http://ftp.de.debian.org/debian/pool/main/liba/libaio/libaio_%{version}.orig.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  glibc-devel

%description
The Linux-native asynchronous I/O facility (aio) interface lets
userspace apps submit multiple I/O operations without waiting for
completion.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for building against %{name}.

%prep
%oreon_sha256
%autosetup -n libaio-%{version} -p1

%build
%make_build -C src CFLAGS="%{optflags} -fPIC"

%install
%make_install -C src prefix=%{_prefix} includedir=%{_includedir} libdir=%{_libdir}

%check
%make_build -C harness partcheck

%files
%license COPYING
%doc ChangeLog
%{_libdir}/libaio.so.*

%files devel
%{_includedir}/libaio.h
%{_libdir}/libaio.so
%{_libdir}/libaio.a

%changelog
%autochangelog
