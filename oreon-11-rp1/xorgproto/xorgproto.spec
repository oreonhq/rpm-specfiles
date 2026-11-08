# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 56898c716c0578df8a2d828c9c3e5c528277705c0484381a81960fe1a67668e8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: xorgproto
Version: 2025.1
Release: 1%{?dist}
Summary: X.Org protocol headers
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/releases/individual/proto/xorgproto-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: meson
BuildRequires: ninja-build

Obsoletes: xorg-x11-proto-devel < 2025.2
Provides: xorg-x11-proto-devel = %{version}-%{release}

%description
X.Org protocol headers.

%prep
%oreon_sha256
%autosetup -n xorgproto-%{version} -p1

%build
%oreon_meson
%oreon_meson_build

%install
%oreon_meson_install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING-x11proto
