%global source0_hash none

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           minuet
Version:        25.12.3
Release:        1%{?dist}
Summary:        A KDE Software for Music Education
#OFL license for bundled Bravura.otf font
#and BSD license for cmake/FindFluidSynth.cmake
License:        GPL-2.0-or-later AND OFL-1.1
URL:            http://www.kde.org
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= 5.15.0
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-filesystem
BuildRequires:  desktop-file-utils

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

BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  libappstream-glib
# Runtime requirement
Requires:       hicolor-icon-theme
Requires:       %{name}-data

Provides:       bundled(font(bravura))

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

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README*
%license COPYING*
%{_datadir}/applications/org.kde.%name.desktop
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_libdir}/libminuetinterfaces.so.*
%{_qt6_plugindir}/%{name}

%files devel
%doc README*
%license COPYING*
%{_includedir}/%{name}
%{_kf6_libdir}/libminuetinterfaces.so

%files data
%{_kf6_datadir}/%{name}

%changelog
%autochangelog
