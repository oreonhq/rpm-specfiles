# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 82ad632d31ee05da13b537c124f819eb88e18851d9cb0c30ae0552084811588c

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:           hiredis
Version:        1.2.0
Release:        1%{?dist}
Summary:        Minimalistic C client library for Redis
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/redis/hiredis
Source0:        https://github.com/redis/hiredis/archive/v%{version}/hiredis-%{version}.tar.gz
# Make test.sh use REDIS_SERVER everywhere
# https://github.com/redis/hiredis/pull/1276
Patch0:        hiredis-envvar.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
%ifnarch %{ix86}
BuildRequires:  valkey
BuildRequires:  oreon-rpm-macros
%endif

%description 
Hiredis is a minimalistic C client library for the Redis database.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256

%autosetup -p1

%build
%make_build PREFIX="%{_prefix}" LIBRARY_PATH="%{_lib}"     \
            DEBUG="%{optflags}" LDFLAGS="%{?__global_ldflags}" USE_SSL=1

%install
%make_install PREFIX="%{_prefix}" LIBRARY_PATH="%{_lib}" USE_SSL=1

find %{buildroot} -name '*.a' -delete -print

%ifnarch %{ix86}
%check
make check REDIS_SERVER=valkey-server
%endif

%files
%doc COPYING
%{_libdir}/libhiredis.so.1
%{_libdir}/libhiredis.so.1.1.0
%{_libdir}/libhiredis_ssl.so.1
%{_libdir}/libhiredis_ssl.so.1.1.0

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/%{name}/
%{_libdir}/libhiredis.so
%{_libdir}/libhiredis_ssl.so
%{_libdir}/pkgconfig/hiredis.pc
%{_libdir}/pkgconfig/hiredis_ssl.pc

