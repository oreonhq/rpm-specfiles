Name:    libkdegames
Summary: Common code and data for many KDE games
Version: 25.12.3
Release:	2%{?dist}

# libKF5KDEGames is LGPLv2, libKF5KDEGamesPrivate is GPLv2+
# Automatically converted from old format: LGPLv2 and GPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2 AND GPL-2.0-or-later
URL:     https://invent.kde.org/games/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/libkdegames-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kbookmarks-devel
BuildRequires: kf6-kcodecs-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kdnssd-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel
BuildREquires: kf6-knewstuff-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-rpm-macros

BuildRequires: pkgconfig(Qt6Widgets) pkgconfig(Qt6Qml) pkgconfig(Qt6Quick) pkgconfig(Qt6QuickWidgets) pkgconfig(Qt6Svg) pkgconfig(Qt6Test)

BuildRequires: gettext
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(sndfile)

Provides: libkdegames-kf6 = %{version}-%{release}
Provides: libkdegames-kf6%{?_isa} = %{version}-%{release}

%global __provides_exclude_from ^%{_qt6_archdatadir}/qml/.*\\.so$

%description
%{summary}.

%package devel
Summary:  Development files for %{name} 
Provides: libkdegames-kf6-devel = %{version}-%{release}
Provides: libkdegames-kf6-devel%{?_isa} = %{version}-%{release}
Provides: libkdegames-private-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig(Qt6Network) pkgconfig(Qt6Widgets) pkgconfig(Qt6Qml) pkgconfig(Qt6QuickWidgets) pkgconfig(Qt6Xml)
Requires: kf6-kconfig-devel
Requires: kf6-kconfigwidgets-devel
Requires: kf6-kcompletion-devel
Requires: kf6-ki18n-devel
Requires: kf6-kwidgetsaddons-devel
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README TODO
%license LICENSES/*
%{_datadir}/qlogging-categories6/libkdegames*
%{_kf6_libdir}/libKDEGames6.so.6*
%{_kf6_libdir}/libKDEGames6Private.so.6*
%{_qt6_archdatadir}/qml/org/kde/games/
# consider common/noarch subpkg
%{_kf6_datadir}/carddecks/

%files devel
%{_kf6_libdir}/libKDEGames6.so
%{_kf6_libdir}/libKDEGames6Private.so
%{_includedir}/KDEGames6/
%{_kf6_libdir}/cmake/KDEGames6/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
