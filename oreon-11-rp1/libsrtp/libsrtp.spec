# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ef5569220749529d778013aae1178391d972570a2b4f7288dda22effa875b07c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:		libsrtp
Version:	2.8.1
Release:	1%{?dist}
Summary:	An implementation of the Secure Real-time Transport Protocol (SRTP)
License:	BSD-3-Clause
URL:		https://github.com/cisco/libsrtp
Source0:	https://github.com/cisco/libsrtp/archive/v%{version}.tar.gz
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:	doxygen
BuildRequires:	meson
BuildRequires:	procps-ng
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libpcap)
Provides:	libsrtp-tools = %{version}-%{release}
Obsoletes:	libsrtp-tools < 2.6.0-1

%description
This package provides an implementation of the Secure Real-time
Transport Protocol (SRTP), the Universal Security Transform (UST), and
a supporting cryptographic kernel.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%setup -q -n %{name}-%{version}

%build
%meson -Dcrypto-library=openssl -Dcrypto-library-kdf=disabled
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc CHANGES README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/srtp2/
%{_libdir}/pkgconfig/libsrtp2.pc
%{_libdir}/*.so

%changelog
%autochangelog
