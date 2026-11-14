# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9ea75af35c512f7e09e61c8c3af3997f13b4d43bb099cf43fcec470126b4041e
%global majmin 6.11

Name: qt6-linguist
Version: 6.11.2
Release: 1%{?dist}
Summary: Qt6 translation tools
License: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL: https://www.qt.io/
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/qttools-everywhere-src-%{version}.tar.xz
Patch0: qttools-linguist-only.patch

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel = %{version}
BuildRequires: qt6-srpm-macros

Provides: qt6-qttools-linguist = %{version}-%{release}

%description
Qt Linguist command-line tools for extracting, updating and compiling
translations used by Qt6 applications.

%prep
%oreon_sha256
%autosetup -n qttools-everywhere-src-%{version} -p1

%build
%cmake \
  -G Ninja \
  -DQT_BUILD_TESTS=OFF \
  -DQT_BUILD_EXAMPLES=OFF \
  -DQT_FEATURE_linguist=ON \
  -DQT_FEATURE_assistant=OFF \
  -DQT_FEATURE_designer=OFF \
  -DQT_FEATURE_distancefieldgenerator=OFF \
  -DQT_FEATURE_kmap2qmap=OFF \
  -DQT_FEATURE_pixeltool=OFF \
  -DQT_FEATURE_qdbus=OFF \
  -DQT_FEATURE_qdoc=OFF \
  -DQT_FEATURE_qtattributionsscanner=OFF \
  -DQT_FEATURE_qtdiag=OFF \
  -DQT_FEATURE_qtplugininfo=OFF
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{_libdir}
%{buildroot}%{_libdir}/qt6/bin/lrelease -version
%{buildroot}%{_libdir}/qt6/bin/lupdate -version

%files
%license LICENSES/*
%doc README.md
%{_includedir}/qt6/
%{_libdir}/cmake/Qt6*/
%{_libdir}/qt6/

%changelog
%autochangelog
