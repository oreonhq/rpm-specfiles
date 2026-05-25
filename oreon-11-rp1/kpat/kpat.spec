

# 
ExcludeArch: %{ix86}

Name:    kpat
Summary: A selection of solitaire card games
Version: 26.04.1
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/games/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel

BuildRequires: pkgconfig(libblack-hole-solver)
BuildRequires: pkgconfig(libfreecell-solver)
BuildRequires: pkgconfig(phonon4qt6)

BuildRequires: pkgconfig(Qt6Widgets) pkgconfig(Qt6Qml) pkgconfig(Qt6Quick) pkgconfig(Qt6QuickWidgets) pkgconfig(Qt6Svg) pkgconfig(Qt6Test)
BuildRequires: libappstream-glib
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}

BuildRequires: shared-mime-info

%description
%{summary}.
To play patience you need, as the name suggests, patience. For simple
games, where the way the game goes depends only upon how the cards fall,
your patience might be the only thing you need.  There are also patience
games where you must plan your strategy and think ahead in order to win.
A theme common to all the games is the player must put the cards in a
special order — moving, turning and reordering them.


%prep
%autosetup


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING*
#doc README
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/knsrcfiles/*.knsrc
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/%{name}/
#{_kf6_datadir}/kconf_update/%{name}*
#{_kf6_datadir}/kxmlgui5/%{name}/
#{_kf6_datadir}/sounds/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_libdir}/libkcardgame.so
%{_datadir}/mime/packages/kpatience.xml
%{_mandir}/man6/kpat.6*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
