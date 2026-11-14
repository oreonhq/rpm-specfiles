# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 01b06e2dba0e2635544fb8b301eda1105da36d63131054a42bb230b378d6d2c3

Name: annobin
Version: 13.33
Release: 1%{?dist}
Summary: Binary hardening annotation tools
License: GPL-3.0-or-later AND LGPL-2.0-or-later AND GFDL-1.3-or-later
URL: https://sourceware.org/annobin/
Source0: https://nickc.fedorapeople.org/annobin-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: elfutils-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-devel

Requires: gcc-plugin-annobin
Provides: annobin-plugin-gcc = %{version}-%{release}
Provides: annobin-annocheck = %{version}-%{release}
Provides: /usr/bin/annocheck

%description
Annobin records and checks compiler hardening information in ELF binaries.
The GCC plugin is supplied by the matching GCC build.

%prep
%oreon_sha256
%autosetup -n annobin-%{version}
touch aclocal.m4 gcc-plugin/config.h.in
touch configure */configure Makefile.in */Makefile.in doc/annobin.info

%build
%oreon_configure \
    --without-debuginfod \
    --with-gcc-plugin=no \
    --with-clang-plugin=no \
    --with-llvm-plugin=no \
    --without-tests
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
%oreon_filelist

%check
./annocheck/annocheck --version

%files -f %{_builddir}/%{name}.files
%license COPYING3 LICENSE

%changelog
%autochangelog
