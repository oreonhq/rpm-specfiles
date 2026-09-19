%global source0_hash none

%undefine __cmake_in_source_build

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ktuberling
Summary: Picture game for children
Version: 25.12.3
Release: 1%{?dist}

License: GPL-2.0-or-later AND GFDL-1.2-or-later
URL:     https://invent.kde.org/games/%{name}/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

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
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires:  libkdegames-devel >= %{majmin_ver}

BuildRequires:  pkgconfig(phonon4qt6)

BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick) pkgconfig(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Svg)

%description
KTuberling a simple constructor game suitable for children and adults
alike. The idea of the game is based around a once popular doll making
concept. A potato was decorated with various small artifacts to make it
look more like a tiny person. KTuberling however, goes much further in
terms of content and adds a surprising variety of different themes.

%prep
%autosetup

%build
%{cmake_kf6}
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/
#{_kf6_datadir}/kconf_update/%{name}*
#{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_datadir}/qlogging-categories6/%{name}*

%changelog
%autochangelog
