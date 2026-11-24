# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fee6aee6b4933f01ba8b7e18d5d9e4896ad604053fdad2ac55df4a4f1561f30a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global rc %{nil}

Name:           srt
Version:        1.5.7
Release:        1%{?dist}
Summary:        Secure Reliable Transport protocol tools

License:        MPL-2.0
URL:            https://www.srtalliance.org
Source0:        https://github.com/Haivision/srt/archive/v%{version}%{rc}/%{name}-%{version}%{rc}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  gmock-devel
BuildRequires:  gnutls-devel
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  nettle3.10-devel

Requires: srt-libs%{?_isa} = %{version}-%{release}

%description
Secure Reliable Transport (SRT) is an open source transport technology that
optimizes streaming performance across unpredictable networks, such as 
the Internet.

%package libs
Summary: Secure Reliable Transport protocol libraries

%description libs
Secure Reliable Transport protocol libraries

%package devel
Summary: Secure Reliable Transport protocol development libraries and headers
Requires: srt-libs%{?_isa} = %{version}-%{release}

%description devel
Secure Reliable Transport protocol development libraries and header files

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{version}%{rc}

%build
%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_UNITTESTS=ON \
  -DENABLE_GETNAMEINFO=ON \
  -DENABLE_BONDING=ON \
  -DENABLE_PKTINFO=ON \
  -DUSE_ENCLIB=gnutls

%cmake_build

%install
%cmake_install
rm -f %{buildroot}/%{_libdir}/pkgconfig/haisrt.pc

%check
%ctest -j1 -E TestIPv6

%ldconfig_scriptlets libs

%files
%license LICENSE
%doc README.md docs
%{_bindir}/srt-ffplay
%{_bindir}/srt-file-transmit
%{_bindir}/srt-live-transmit
%{_bindir}/srt-tunnel

%files libs
%license LICENSE
%{_libdir}/libsrt.so.1.5*

%files devel
%doc examples
%{_includedir}/srt
%{_libdir}/libsrt.so
%{_libdir}/pkgconfig/srt.pc

%changelog
%autochangelog
