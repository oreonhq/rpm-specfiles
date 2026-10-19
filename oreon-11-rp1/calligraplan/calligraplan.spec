%global stable_kf6 stable
%global source0_hash 9267ea174c04466014343927f73757bb3047dab36a74fc8f38b891e8d8833a39
%bcond mpxj 0
%global app_id org.kde.calligraplan
Name:    calligraplan
Version: 4.0.1
Release:        3%{?dist}
Summary:        A Project Planner
License: GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://www.calligra-suite.org/
Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{name}-%{version}.tar.xz
ExcludeArch:   %{ix86}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if %{with mpxj}
Requires: apache-poi
%endif
# oreon:deps
BuildRequires:  cmake(KChart6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KGantt6)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(cups)
# /oreon:deps
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
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
find  %{buildroot}%{_kf6_libdir}/  -maxdepth 1 -name lib*.so -type l -delete
%if %{without mpxj}
rm -f %{buildroot}%{_kf6_datadir}/mime/packages/plan_mpxj_mimetype.xml
%endif
%find_lang %{name} --all-name --with-html
%oreon_autofiles calligraplan-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligraplan-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}*.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{app_id}*.desktop
%files -f %{oreon_filedir}/main.list
%files -n calligraplan-libs -f %{oreon_filedir}/calligraplan-libs.list
%files -n calligraplan-data -f %{oreon_filedir}/calligraplan-data.list

%changelog

%autochangelog
