# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a0d47876548bec806774bbf8dbf20bb19ba139464383156b32eb8e59915b90a9
%global source1_hash 790566ac910c8f05ce38f4100619b6a90f8508af4ef86407c1952fb45c7abfca
%global source2_hash 44323ffc2f7fdf7a4d7d7cff940d5961a2436abc86e5cfa309644bae0a203b2f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global abi 8

Name:           libdvdread
Version:        7.1.1
Release:        1%{?dist}
Summary:        A library for reading DVD video discs based on Ogle code
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Fedora-Public-Domain
URL:            https://www.videolan.org/developers/libdvdnav.html
Source0:        https://download.videolan.org/pub/videolan/libdvdread/%{version}/libdvdread-%{version}.tar.xz
Source1:        https://download.videolan.org/pub/videolan/libdvdread/%{version}/libdvdread-%{version}.tar.xz.asc
Source2:        https://download.videolan.org/pub/keys/7180713BE58D1ADC.asc

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  doxygen
BuildRequires:  gnupg2
BuildRequires:  meson
Provides:       bundled(md5-gcc)

%description
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.

%package        devel
Summary:        Development files for libdvdread
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.

This package contains development files for libdvdread.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

%build
%meson \
  -Ddefault_library=shared \
  -Denable_docs=true \
  -Dlibdvdcss=disabled
%meson_build

%install
%meson_install
mv %{buildroot}%{_pkgdocdir}/ docdir/

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libdvdread.so.%{abi}*

%files devel
%doc docdir/*
%{_includedir}/dvdread
%{_libdir}/libdvdread.so
%{_libdir}/pkgconfig/dvdread.pc

%changelog
%autochangelog
