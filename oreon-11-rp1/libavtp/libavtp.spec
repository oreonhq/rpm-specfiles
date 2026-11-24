# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 631f5e704a1b7c8f953ca017a382ad945e75c2952c81813ff355e9ab8071b70e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:		libavtp
Version:	0.2.0
Release:        %{autorelease}
Summary:	An AVTP protocol implementation

License:	BSD-3-Clause
URL:		https://github.com/Avnu/libavtp
Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:	libcmocka-devel
BuildRequires:	meson

%description
An open source implementation of Audio Video Transport
Protocol (AVTP) specified in IEEE 1722-2016 spec.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%{_libdir}/libavtp.so.*

%files devel
%doc CONTRIBUTING.md HACKING.md
%{_includedir}/avtp*
%{_libdir}/libavtp.so
%{_libdir}/pkgconfig/avtp.pc

%changelog
%autochangelog
