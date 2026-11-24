# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 651e88af3c8189d4faed538bee3affde360eb4698a70505765fc7e5653f5eb23
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global commit0 5e9be272f96e00f15a2f3c5f8ba7e124862aec38
%global date 20160216
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           aribb24
Version:        1.0.3%{!?tag:^%{date}git%{shortcommit0}}
Release:        1%{?dist}
Summary:        A library for ARIB STD-B24
License:        LGPL-3.0-only
URL:            https://github.com/nkoriyama/%{name}

%if 0%{?tag:1}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %url/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libpng-devel

%description
A library for ARIB STD-B24, decoding JIS 8 bit characters and parsing MPEG-TS
stream.

%package devel
Summary:        Development files for the ARIB STD-B24 library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and headers for the ARIB STD-B24 library.

%prep
%oreon_sha256
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{name}.la

rm -fr %{buildroot}%{_docdir}/%{name}

%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.0.0

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
