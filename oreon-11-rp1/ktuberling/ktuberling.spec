%global source0_hash 0d2962a37c51b7317c9c5cf2b49c7977c3ddfc7e598556ebcd17e06c44587c53
%undefine __cmake_in_source_build
ExcludeArch: %{ix86}
Name:    ktuberling
Summary:        Picture game for children
Version: 25.12.3
Release:        1%{?dist}
License: GPL-2.0-or-later AND GFDL-1.2-or-later
URL:     https://invent.kde.org/games/%{name}/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
# oreon:deps
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-knewstuff-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-knotifyconfig-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(phonon4qt6)
# /oreon:deps
%description
KTuberling a simple constructor game suitable for children and adults
alike. The idea of the game is based around a once popular doll making
concept. A potato was decorated with various small artifacts to make it
look more like a tiny person. KTuberling however, goes much further in
terms of content and adds a surprising variety of different themes.

%prep
%oreon_prep
%build

%{cmake_kf6}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
