%global source0_hash 4ac009e3a58bc24c58710aa53d9788761f7fa6230f20c5816744bc17e6d45d9a
%global stable_kf6 stable
Name:    baloo-widgets
Summary:        Widgets for Baloo
Version: 26.08.0
Release:        1%{?dist}
License: LGPL-2.0-only OR LGPL-3.0-only
URL:     https://invent.kde.org/libraries/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
Requires: kf6-kcoreaddons-devel
Requires: kf6-kio-devel
%description devel
%{summary}.

%prep
%oreon_prep
%build

%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
%oreon_autofiles baloo-widgets-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n baloo-widgets-devel -f %{oreon_filedir}/baloo-widgets-devel.list

%changelog

%autochangelog
