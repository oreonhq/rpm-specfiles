# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9e1443a40a72a30272cbc3196d020a6b2e26937111c83e59e101e82e1e3b4fef

Name: bind
Version: 9.20.30
Release: 1%{?dist}
Summary: DNS server and utilities
License: MPL-2.0
URL: https://www.isc.org/bind/
Source0: https://ftp.isc.org/isc/bind9/%{version}/bind-%{version}.tar.xz
Source1: bind-%{version}.tar.xz.asc
Source2: gpgkey-D99CCEAF879747014F038D63182E23579462EFAA.gpg

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: liburcu-devel >= 0.13.0
BuildRequires: libuv-devel >= 1.37.0
BuildRequires: openssl-devel
BuildRequires: libcap-devel
BuildRequires: libxml2-devel
BuildRequires: json-c-devel
BuildRequires: zlib-devel
BuildRequires: readline-devel
BuildRequires: libidn2-devel
BuildRequires: nghttp2-devel
BuildRequires: krb5-devel
BuildRequires: cmocka-devel
BuildRequires: python3-sphinx
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-dns >= 2.8.0
BuildRequires: python3-cryptography
BuildRequires: python3-gssapi
BuildRequires: python3-h2
BuildRequires: python3-hypothesis
BuildRequires: python3-jinja2
BuildRequires: python3-pyyaml
BuildRequires: python3-requests
BuildRequires: perl-interpreter

%description
BIND is an implementation of the Domain Name System protocols. This package
contains the authoritative DNS server, resolver libraries, and DNS utilities.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup

%build
%oreon_configure \
    --disable-static \
    --enable-doh \
    --with-cmocka \
    --with-gssapi \
    --with-json-c \
    --with-libidn2 \
    --with-libnghttp2 \
    --with-libxml2 \
    --with-readline=readline \
    --with-zlib
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
%oreon_filelist

%check
%oreon_make check

%files -f %{_builddir}/%{name}.files
%license LICENSE
%doc README.md

%changelog
%autochangelog
