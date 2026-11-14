# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash eac15b82b5ba5ed0648af580221eb74657394f7fe768e966d9e9ebb27435429f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libmpdclient
Version:        2.22
Release:        1%{?dist}
Summary:        Client library for the Music Player Daemon
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://www.musicpd.org/libs/libmpdclient/
Source0:        https://www.musicpd.org/download/libmpdclient/2/libmpdclient-%{version}.tar.xz

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  check-devel

%description
A stable, documented, asynchronous API library for interfacing MPD in the C
and C++ languages.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       pkgconfig(libmpdclient) = %{version}

%description devel
Headers and libraries for building against %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%meson -Ddocumentation=false -Dtest=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSES/BSD-2-Clause.txt LICENSES/BSD-3-Clause.txt
%doc AUTHORS NEWS README.md
%{_libdir}/libmpdclient.so.*

%files devel
%{_includedir}/mpd/
%{_libdir}/libmpdclient.so
%{_libdir}/pkgconfig/libmpdclient.pc

%changelog
%autochangelog
