# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9364b70a12eb59a06830fb488d9357f90100dff0d98b23ea3593a183d43e6f2f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: c-ares
Version: 1.34.9
Release: 1%{?dist}
Summary: Library for asynchronous DNS requests
License: MIT
URL: https://c-ares.org/
Source0: https://github.com/c-ares/c-ares/releases/download/v%{version}/c-ares-%{version}.tar.gz
Source1: cares-test-dns.c
Patch0: c-ares-cmake-cxx.patch
Patch1: c-ares-live-resolv.patch

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: gmock-devel
BuildRequires: make
BuildRequires: glibc-devel

%description
c-ares is a C library for asynchronous DNS requests.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: c-ares-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libcares) = %{version}

%description devel
Headers and libraries for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake \
  -DCARES_SHARED=ON \
  -DCARES_STATIC=OFF \
  -DCARES_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
gcc -O2 -o cares-test-dns %{SOURCE1}
./cares-test-dns 15353 > cares-test-dns.log 2>&1 &
echo $! > cares-test-dns.pid
ready=0
for _ in 1 2 3 4 5 6 7 8 9 10; do
  if grep -q ready cares-test-dns.log; then
    ready=1
    break
  fi
  sleep 0.1
done
if test "$ready" != 1; then
  cat cares-test-dns.log
  exit 1
fi
printf 'nameserver 127.0.0.1:15353\noptions timeout:1 attempts:1\n' > cares-test-resolv.conf
export CARES_TEST_RESOLV="$PWD/cares-test-resolv.conf"
%ctest
kill "$(cat cares-test-dns.pid)" || :

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libcares.so.*
%{_bindir}/adig
%{_bindir}/ahost
%{_mandir}/man1/adig.1*
%{_mandir}/man1/ahost.1*

%files devel
%{_libdir}/libcares.so
%{_includedir}/ares*.h
%{_libdir}/pkgconfig/libcares.pc
%{_libdir}/cmake/c-ares/
%{_mandir}/man3/ares_*.3*

%changelog
%autochangelog
