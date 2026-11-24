# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 769d3eaf57fa4fbdb05dd12873b6cb9a5be7844d8937e222b647381d44284820
%global source1_hash 8fb7bfa4d9e0104249f331dddbd975930740cc7b2e59a2d760a0966aa7ce0abb
%global source2_hash 961f5e8d3dcffab4c04c891a3f26e27bedf49301e53cbf83660001de3d9390c8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libnetfilter_conntrack
Version:        1.1.1
Release:        %{autorelease}
Summary:        Netfilter conntrack userspace library
License:        GPL-2.0-or-later
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/libnetfilter_conntrack/files/%{name}-%{version}.tar.xz
Source1:        http://netfilter.org/projects/libnetfilter_conntrack/files/%{name}-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  kernel-headers
BuildRequires:  libmnl-devel >= 1.0.3
BuildRequires:  libnfnetlink-devel >= 1.0.1
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
libnetfilter_conntrack is a userspace library providing a programming 
interface (API) to the in-kernel connection tracking state table.

%package        devel
Summary:        Netfilter conntrack userspace library
Requires:       %{name} = %{version}-%{release}, libnfnetlink-devel >= 1.0.1
Requires:       kernel-headers

%description    devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -vi
%configure --disable-static --disable-rpath

%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_conntrack
%{_includedir}/libnetfilter_conntrack/*.h

%changelog
%autochangelog
