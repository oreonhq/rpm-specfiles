# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a2a18f5ad36d133c74bf9106b6445806fa253b09141a46392550394b647b221e
%global source1_hash a66cecca8de03524605482788c3d7734e089534b5b657e1ba6eb309a336c1588
%global source2_hash 44323ffc2f7fdf7a4d7d7cff940d5961a2436abc86e5cfa309644bae0a203b2f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global abi 4

Name:           libdvdnav
Version:        7.0.0
Release:        1%{?dist}
Summary:        A library for reading DVD video discs based on Ogle code
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://dvdnav.mplayerhq.hu/
Source0:        https://download.videolan.org/pub/videolan/libdvdnav/%{version}/libdvdnav-%{version}.tar.xz
Source1:        https://download.videolan.org/pub/videolan/libdvdnav/%{version}/libdvdnav-%{version}.tar.xz.asc
Source2:        https://download.videolan.org/pub/keys/7180713BE58D1ADC.asc

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  doxygen
BuildRequires:  gnupg2
BuildRequires:  libdvdread-devel >= 6.0.0
BuildRequires:  meson

%description
libdvdnav provides a simple library for reading DVD video discs.
The code is based on Ogle and used in, among others, the Xine dvdnav plug-in.

%package        devel
Summary:        Development files for libdvdnav
Requires:       %{name} = %{version}-%{release}
Requires:       libdvdread-devel >= 6.0.0
Requires:       pkgconfig

%description    devel
libdvdnav-devel contains the files necessary to build packages that use the
libdvdnav library.

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
  -Denable_examples=true
%meson_build

%install
%meson_install
rm %{buildroot}%{_pkgdocdir}/{COPYING,TODO,AUTHORS,ChangeLog,README.md}
mv %{buildroot}%{_pkgdocdir}/ docdir/

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_libdir}/libdvdnav.so.%{abi}*

%files devel
%doc docdir/*
%{_libdir}/libdvdnav.so
%{_includedir}/dvdnav
%{_libdir}/pkgconfig/dvdnav.pc

%changelog
%autochangelog
