%global source0_hash none

%bcond mpxj 0

%global app_id org.kde.calligraplan

Name:    calligraplan
Version: 4.0.1
Release: 3%{?dist}
Summary: A Project Planner 

License: GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://www.calligra-suite.org/
Source:  https://download.kde.org/%{stable_kf6}/%{name}/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

## downstream patches

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

BuildRequires: gcc-c++
BuildRequires: perl-interpreter
# kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6ThreadWeaver)
BuildRequires: cmake(PlasmaActivities)
# qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6DBus)
# optional
BuildRequires: cmake(KChart6)
BuildRequires: cmake(KGantt6)
BuildRequires: cmake(Qca-qt6)
BuildRequires: pkgconfig(cups)
# %%check validation
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%if %{with mpxj}
BuildRequires: java-devel
Requires: apache-poi
#Requires: apache-mpxj
%endif

%description
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package  libs
Summary:  Runtime libraries for %{name}
Requires: %{name}-data = %{version}-%{release}
%description libs
%{summary}.

%package data
Summary:   Runtime support files for %{name}
BuildArch: noarch
Requires:  hicolor-icon-theme
%description data
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

## unpackaged files
# no need to package lib*.so symlinks
find  %{buildroot}%{_kf6_libdir}/  -maxdepth 1 -name lib*.so -type l -delete

%if %{without mpxj}
rm -f %{buildroot}%{_kf6_datadir}/mime/packages/plan_mpxj_mimetype.xml
%endif

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}*.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{app_id}*.desktop

%files
%{_kf6_bindir}/calligraplan
%{_kf6_bindir}/calligraplanportfolio
%{_kf6_bindir}/calligraplanwork
%{_kf6_datadir}/applications/%{app_id}.desktop
%{_kf6_datadir}/applications/%{app_id}portfolio.desktop
%{_kf6_datadir}/applications/%{app_id}work.desktop
%{_kf6_metainfodir}/%{app_id}.appdata.xml
%{_kf6_metainfodir}/%{app_id}portfolio.appdata.xml
%{_kf6_metainfodir}/%{app_id}work.appdata.xml

%files libs
%{_kf6_libdir}/lib%{name}*.so.4{,.*}
%{_kf6_qtplugindir}/%{name}/

%files data -f %{name}.lang
%license LICENSES/*
%{_kf6_sysconfdir}/xdg/calligraplanrc
%{_kf6_sysconfdir}/xdg/calligraplanworkrc
%{_kf6_datadir}/calligraplan/
%{_kf6_datadir}/calligraplanwork/
%{_kf6_datadir}/config.kcfg/calligraplansettings.kcfg
%{_kf6_datadir}/config.kcfg/calligraplanworksettings.kcfg
%{_kf6_datadir}/kxmlgui5/calligraplan/
%{_kf6_datadir}/kxmlgui5/calligraplanportfolio/
%{_kf6_datadir}/kxmlgui5/calligraplanwork/
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}portfolio.*
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}work.*
%{_kf6_datadir}/icons/hicolor/*/mimetypes/application-x-vnd.kde.{kplato,plan}.*
%{_kf6_datadir}/mime/packages/calligraplanportfolio_mimetype.xml
%if %{with mpxj}
%{_kf6_datadir}/mime/packages/plan_mpxj_mimetype.xml
%endif

%changelog
%autochangelog
