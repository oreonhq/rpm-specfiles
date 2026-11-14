# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3f55cd3670f1ff1a439d5a40071870b9e4ca2be8877a0eb80e24783cb532b380

Name: teckit
Version: 2.5.13
Release: 1%{?dist}
Summary: Encoding conversion library and mapping compiler
License: (LGPL-2.1-or-later OR CPL-1.0) AND (LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-2.0)
URL: https://software.sil.org/teckit/
Source0: https://github.com/silnrsi/teckit/releases/download/v%{version}/teckit-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: expat-devel
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: zlib-devel

%description
TECkit provides a library and tools for converting legacy encodings to and
from Unicode using compiled mapping tables.

%package devel
Summary: Development files for TECkit
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for developing software with TECkit.

%prep
%oreon_sha256
%autosetup -n teckit-%{version}
rm -rf SFconv/expat perl_binaries
find zlib-* -type f \( -name '*.c' -o -name '*.h' \) -delete

%build
autoreconf -fi
%oreon_configure \
    --disable-static \
    --disable-debug \
    --without-old-lib-names \
    --with-system-zlib \
    --disable-tetex-build
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete

%check
%oreon_make check

%files
%license license/*
%doc AUTHORS NEWS README
%{_bindir}/sfconv
%{_bindir}/teckit_compile
%{_bindir}/txtconv
%{_libdir}/libTECkit.so.0*
%{_libdir}/libTECkit_Compiler.so.0*
%{_mandir}/man1/sfconv.*
%{_mandir}/man1/teckit_compile.*
%{_mandir}/man1/txtconv.*

%files devel
%doc docs/*.pdf
%{_includedir}/teckit
%{_libdir}/libTECkit.so
%{_libdir}/libTECkit_Compiler.so
%{_libdir}/pkgconfig/teckit.pc

%changelog
%autochangelog
