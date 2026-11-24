# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c40062022a1963c80573d48f6070792297cecd7c6bffe3aefcac0d8b9bee8913
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_without tests

Name:    libzip
Version: 1.12.1
Release: 1%{?dist}
Summary: C library for reading, creating, and modifying zip archives

License: BSD-3-Clause
URL:     https://libzip.org/
Source0: https://libzip.org/download/libzip-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  zlib-devel >= 1.1.2
BuildRequires:  bzip2-devel
BuildRequires:  openssl-devel
BuildRequires:  xz-devel >= 5.2
BuildRequires:  libzstd-devel >= 1.4
BuildRequires:  cmake >= 3.14
BuildRequires:  mandoc
%if %{with tests}
BuildRequires:  nihtest
%endif

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from 
other zip archives. Changes made without closing the archive can be reverted. 
The API is documented by man pages.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:  Command line tools from %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package provides command line tools split off %{name}:
- zipcmp
- zipmerge
- ziptool

%prep
%oreon_sha256
%autosetup -p1

rm INSTALL.md

sed -e '/clone-fs-/d' \
    -i regress/CMakeLists.txt

%build
%cmake \
  -DENABLE_COMMONCRYPTO:BOOL=OFF \
  -DENABLE_GNUTLS:BOOL=OFF \
  -DENABLE_MBEDTLS:BOOL=OFF \
  -DENABLE_OPENSSL:BOOL=ON \
  -DENABLE_WINDOWS_CRYPTO:BOOL=OFF \
  -DENABLE_BZIP2:BOOL=ON \
  -DENABLE_LZMA:BOOL=ON \
  -DENABLE_ZSTD:BOOL=ON \
  -DBUILD_TOOLS:BOOL=ON \
  -DBUILD_REGRESS:BOOL=ON \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DBUILD_DOC:BOOL=ON

%cmake_build

%install
%cmake_install

%check
%if %{with tests}
%ctest
%else
: Test suite disabled
%endif

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libzip.so.5*

%files tools
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_bindir}/ziptool
%{_mandir}/man1/zip*

%files devel
%doc AUTHORS THANKS *.md
%{_includedir}/zip.h
%{_includedir}/zipconf*.h
%{_libdir}/libzip.so
%{_libdir}/pkgconfig/libzip.pc
%{_libdir}/cmake/libzip
%{_mandir}/man3/libzip*
%{_mandir}/man3/zip*
%{_mandir}/man3/ZIP*
%{_mandir}/man5/zip*

%changelog
%autochangelog
