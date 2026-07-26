%global source0_hash none

Name:    skrooge
Summary: Personal finances manager
Version: 26.1.20
Release: 2%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://skrooge.org
Source0: https://download.kde.org/stable/skrooge/skrooge-%{version}.tar.xz

## upstream patches

ExclusiveArch: %{qt6_qtwebengine_arches}

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Designer)
BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuffCore)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(PlasmaActivities)

BuildRequires: pkgconfig(libofx)
BuildRequires: pkgconfig(sqlcipher)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# drop prior needless -devel pkg
Obsoletes: skrooge-devel < 2.0.0

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
%autosetup -p1

%build
%cmake_kf6 \
  -DQT_MAJOR_VERSION=6

%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html

## unpackaged files

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.skrooge.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.skrooge.desktop

%files -f %{name}.lang
%doc AUTHORS CHANGELOG README.md
%license COPYING
%{_kf6_datadir}/knsrcfiles/skrooge_unit.knsrc
%{_kf6_bindir}/skrooge*
%{_kf6_metainfodir}/org.kde.skrooge.appdata.xml
%{_kf6_datadir}/applications/org.kde.skrooge.desktop
%{_kf6_datadir}/skrooge/
%{_kf6_datadir}/mime/packages/x-skg.xml
%{_kf6_datadir}/icons/breeze/*/*/*
%{_kf6_datadir}/icons/breeze-dark/*/*/*
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/config.kcfg/skg*.kcfg
%{_kf6_datadir}/knotifications6/skrooge.notifyrc
%{_kf6_datadir}/knsrcfiles/skrooge_monthly.knsrc
%{_kf6_datadir}/kxmlgui5/skg*/
%{_kf6_datadir}/kxmlgui5/skrooge_*/

%files libs
%{_kf6_qtplugindir}/skg_gui/
%{_kf6_qtplugindir}/skrooge_import/
%{_kf6_qtplugindir}/kf6/ktexttemplate/
%{_kf6_qtplugindir}/sqldrivers/libskgsqlcipher.so
%{_kf6_libdir}/libskgbankgui.so.2*
%{_kf6_libdir}/libskgbankmodeler.so.2*
%{_kf6_libdir}/libskgbasegui.so.2*
%{_kf6_libdir}/libskgbasemodeler.so.2*
%{_kf6_datadir}/skrooge_import_backend/
%{_kf6_datadir}/skrooge_source/

%changelog
%autochangelog
