# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b7febc6c05af412d0dac20039a76438739986be9b22f8451a4babe69e06a2543
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libudfread
Version:        1.2.0
Release:        1%{?dist}
Summary:        UDF reader library
License:        LGPL-2.0-or-later
URL:            https://code.videolan.org/videolan/libudfread
Source0:        https://code.videolan.org/videolan/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  libtool
BuildRequires:  meson

%description
This library allows reading UDF filesystems, like raw devices and image files.
The library is created and maintained by VideoLAN Project and is used by
projects like VLC and Kodi.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%meson -Ddefault_library=shared
%meson_build

%install
%meson_install

%files
%doc ChangeLog
%license COPYING
%{_libdir}/libudfread.so.3*

%files devel
%{_includedir}/udfread/
%{_libdir}/libudfread.so
%{_libdir}/pkgconfig/libudfread.pc

%changelog
%autochangelog
