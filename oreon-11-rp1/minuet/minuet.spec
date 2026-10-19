%global stable_kf6 stable
%global source0_hash e0c9c852df80afb1738087efe6055d8402fff9e696422f186d0fec204b3cd0d3
ExcludeArch: %{ix86}
Name:           minuet
Version:        25.12.3
Release:        1%{?dist}
Summary:        A KDE Software for Music Education
License:        GPL-2.0-or-later AND OFL-1.1
URL:            http://www.kde.org
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
Requires:       %{name}-data
Provides:       bundled(font(bravura))
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-filesystem
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(fluidsynth)
# /oreon:deps
%description
Application for Music Education.

Minuet aims at supporting students and teachers in many aspects
of music education, such as ear training, first-sight reading,
solfa, scales, rhythm, harmony, and improvisation.
Minuet makes extensive use of MIDI capabilities to provide a
full-fledged set of features regarding volume, tempo, and pitch
changes, which makes Minuet a valuable tool for both novice and
experienced musicians.

%package devel
Summary:        Minuet: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers and libraries for Minuet.

%package data
Summary:        Minuet: Data files
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description data
Data files for Minuet.

%prep

%autosetup -p1
chmod -x src/app/org.kde.%{name}.desktop

%build

%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n minuet-devel -f %{oreon_filedir}/minuet-devel.list
%files -n minuet-data -f %{oreon_filedir}/minuet-data.list

%changelog

%autochangelog
