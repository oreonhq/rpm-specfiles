%global source0_hash 2332234f8b67dd95e63ed7caf21042a4d2792729a9a7f1f5cd52c1040550b353
Name:    skrooge
Summary:        Personal finances manager
Version: 26.8.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     http://skrooge.org
Source0:        https://download.kde.org/stable/skrooge/skrooge-%{version}.tar.xz
ExclusiveArch: %{qt6_qtwebengine_arches}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes: skrooge-devel < 2.0.0
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6NewStuffCore)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libofx)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%{name} is a personal finances manager,
aiming at being simple and intuitive.
It allows you to keep track of your expenses and incomes,
categorize them, and build reports of them.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
%oreon_prep
%build

%cmake_kf6 \
  -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.skrooge.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.skrooge.desktop
%files -f %{oreon_filedir}/main.list
%files -n skrooge-libs -f %{oreon_filedir}/skrooge-libs.list

%changelog

%autochangelog
