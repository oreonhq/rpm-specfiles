# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f590407fc51badb351973fc1333ee33111f05ec83a8f954fd8cf0c5e30439806
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:       recode
Version:    3.7.15
Release:    1%{?dist}
Summary:    Conversion between character sets and surfaces
License:    GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-2-Clause AND LicenseRef-OFSFDL
URL:        https://github.com/rrthomas/recode
Source0:        %{url}/releases/download/v%{version}/recode-%{version}.tar.gz
Patch:      recode-3.7.13-Rename-coliding-hash-functions.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  python3-Cython
BuildRequires:  python3-devel >= 3.7.5
BuildRequires:  python3-setuptools

%description
The recode tool and library convert files between character sets and surfaces.
It recognizes or produces over 200 different character sets (or about 300 if
combined with an iconv library) and transliterates files between almost any
pair. When exact transliteration is not possible, it gets rid of the offending
character or falls back on an approximations.

%package devel
Summary:    Header files for development using recode library
License:    LGPL-3.0-or-later
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the header files for a recode library.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{version}
autoreconf -fi

%build
export PYTHON=%{__python3}
%configure \
    --without-dmalloc \
    --disable-gcc-warnings \
    --enable-largefile \
    --enable-nls \
    --disable-rpath \
    --enable-shared \
    --disable-static
%{make_build}

%check
make check

%install
%{make_install}
%find_lang %{name}

rm -r $RPM_BUILD_ROOT%{_infodir}/dir

rm $RPM_BUILD_ROOT%{_libdir}/*.la

%files -f %{name}.lang
%license COPYING COPYING-LIB
%doc AUTHORS NEWS README THANKS TODO
%{_mandir}/*/*
%{_infodir}/recode.info*
%{_bindir}/*
%{_libdir}/librecode.so.3
%{_libdir}/librecode.so.3.*

%files devel
%{_libdir}/*.so
%{_includedir}/*

%changelog
%autochangelog
