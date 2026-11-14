# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d2931cdad266e633510f9970e1a2f346055e351bb19f9b78912475b8074c36f6

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:    libassuan
Summary: GnuPG IPC library
Version:        3.0.2
Release:        1%{?dist}

# The library is LGPLv2+, the documentation GPLv3+
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Source0:        https://gnupg.org/ftp/gcrypt/libassuan/libassuan-%{version}.tar.bz2
Source1:        libassuan-3.0.2.tar.bz2.sig
URL:     https://www.gnupg.org/

Patch1:        libassuan-2.5.2-multilib.patch

BuildRequires: gcc
BuildRequires: gawk
BuildRequires: libgpg-error-devel >= 1.8
BuildRequires: make
BuildRequires:  oreon-rpm-macros

%description
This is the IPC library used by GnuPG 2, GPGME and a few other
packages.

%package devel 
Summary: GnuPG IPC library 
Provides: libassuan2-devel = %{version}-%{release}
Provides: libassuan2-devel%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel 
This is the IPC static library used by GnuPG 2, GPGME and a few other
packages.

This package contains files needed to develop applications using %{name}.


%prep
%oreon_sha256

%setup -q

%patch 1 -p1 -b .multilib


%build
%configure \
  --includedir=%{_includedir}/libassuan2

%make_build


%install
%make_install

## Unpackaged files
rm -fv %{buildroot}%{_infodir}/dir
rm -fv %{buildroot}%{_libdir}/lib*.la


%check
make check


%ldconfig_scriptlets

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/libassuan.so.9*

%files devel 
%{_bindir}/libassuan-config
%{_includedir}/libassuan2/
%{_libdir}/libassuan.so
%{_libdir}/pkgconfig/libassuan.pc
%{_datadir}/aclocal/libassuan.m4
%{_infodir}/assuan.info*


