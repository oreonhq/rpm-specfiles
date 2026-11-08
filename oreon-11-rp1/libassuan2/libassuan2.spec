# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0103081ffc27838a2e50479153ca105e873d3d65d8a9593282e9c94c7e6afb76
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libassuan2
Version: 2.5.7
Release: 1%{?dist}
Summary: IPC library for GnuPG components, 2.x ABI
License: LGPL-2.1-or-later
URL: https://gnupg.org/software/libassuan/
Source0: https://www.gnupg.org/ftp/gcrypt/libassuan/libassuan-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: libgpg-error-devel

%description
IPC library for GnuPG components, 2.x ABI

%prep
%oreon_sha256
%autosetup -n libassuan-%{version} -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
find %{buildroot} -mindepth 1 -not -path '%{buildroot}%{_libdir}/libassuan.so.0*' -not -type d -delete
find %{buildroot} -depth -mindepth 1 -type d -empty -delete
for f in %{buildroot}%{_libdir}/libassuan.so.0.*; do
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%files
%license COPYING.LIB
%{_libdir}/libassuan.so.0
%{_libdir}/libassuan.so.0.*
