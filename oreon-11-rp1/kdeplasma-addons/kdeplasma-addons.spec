Name:    kdeplasma-addons
Summary: Additional Plasmoids for Plasma 6
Version: 6.6.2
Release:	2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/plasma/%{name}

Source0: http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

ExcludeArch: %{ix86}

%ifarch %{qt6_qtwebengine_arches}
BuildRequires:  cmake(Qt6WebEngineQuick)
%endif

## upstream patches

Obsoletes: kdeplasma-addons-libs < 5.0.0

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  kf6-rpm-macros >= 5.25.0-2
BuildRequires:  libicu-devel
BuildRequires:  libxcb-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  plasma-workspace-devel
BuildRequires:  libksysguard-devel
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)

# for notes.svgz
Requires:       kf6-plasma

# Quickshare applet runtime dep
BuildRequires:  cmake(KF6Purpose)
Recommends:     kf6-purpose%{?_isa}

# Cube effect
Requires:       qt6-qtquick3d%{?_isa}

Requires:       kf6-kitemmodels%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}

%description
%{summary}.

%package -n kate-krunner-plugin
Summary: KRunner plugin for searching Kate sessions
Requires: kate
Supplements: kate
# Before the split
Conflicts: kdeplasma-addons < 5.92.0-3
%description -n kate-krunner-plugin
%{summary}.

%package devel
Summary:        Development files for %{name}
# headers only: fixme: confirm need for dep on main pkg? -- rdieter
Requires: %{name} = %{version}-%{release}
#find_dependency(Qt5Gui "5.12.0")
#find_dependency(KF5CoreAddons "5.58.0")
Requires: cmake(Qt6Gui)
Requires: cmake(KF6CoreAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang kdeplasmaaddons5_qt --with-qt --all-name

%files -f kdeplasmaaddons5_qt.lang
%license LICENSES/*.txt
%{_kf6_datadir}/kwin/effects/cube/
%{_kf6_datadir}/plasma/plasmoids/*
%{_kf6_datadir}/plasma/desktoptheme/default/widgets/*
%{_kf6_datadir}/plasma/desktoptheme/default/weather/
%{_kf6_datadir}/plasma/wallpapers/*
%{_kf6_datadir}/qlogging-categories6/kdeplasma-addons.categories
%{_kf6_datadir}/qlogging-categories6/kdeplasma-addons.renamecategories
%{_kf6_qtplugindir}/plasma/applets/*.so
%{_kf6_plugindir}/krunner/kcms/kcm_krunner_charrunner.so
%{_kf6_plugindir}/krunner/kcms/kcm_krunner_dictionary.so
%{_kf6_plugindir}/krunner/kcms/kcm_krunner_spellcheck.so
%{_kf6_plugindir}/krunner/krunner_charrunner.so
%{_kf6_plugindir}/krunner/krunner_dictionary.so
%{_kf6_plugindir}/krunner/krunner_konsoleprofiles.so
%{_kf6_plugindir}/krunner/krunner_spellcheck.so
%{_kf6_plugindir}/krunner/org.kde.datetime.so
%{_kf6_plugindir}/krunner/unitconverter.so
%{_kf6_plugindir}/packagestructure/*.so
%{_kf6_qtplugindir}/plasmacalendarplugins/
%{_kf6_qtplugindir}/kwin/effects/configs/kwin_cube_config.so
%{_kf6_qtplugindir}/potd/
%{_kf6_qmldir}/org/kde/plasma/*
%{_kf6_datadir}/knotifications6/plasma_applet_timer.notifyrc
%{_datadir}/kwin/tabbox/
%{_datadir}/icons/hicolor/scalable/apps/accessories-dictionary.svgz
%{_datadir}/knsrcfiles/comic.knsrc
%{_kf6_libdir}/libplasmapotdprovidercore.so.*
%{_libdir}/qt6/qml/org/kde/plasmacalendar/astronomicaleventsconfig/*
%{_kf6_plugindir}/kded/kameleon.so
%{_kf6_plugindir}/krunner/krunner_colors.so
%{_kf6_libexecdir}/kauth/kameleonhelper
%{_kf6_datadir}/dbus-1/system-services/org.kde.kameleonhelper.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.kameleonhelper.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.kameleonhelper.policy
%{_libdir}/libplasmaweatherdata.so.*
%{_libdir}/libplasmaweatherion.so.*
%{_kf6_qtplugindir}/plasma/weather_ions/bbcukmet.so
%{_kf6_qtplugindir}/plasma/weather_ions/dwd.so
%{_kf6_qtplugindir}/plasma/weather_ions/envcan.so
%{_kf6_qtplugindir}/plasma/weather_ions/noaa.so
%{_kf6_qtplugindir}/plasma/weather_ions/wettercom.so
%{_datadir}/plasma/weather/noaa_station_list.xml
%{_datadir}/kwin/scripts/virtualdesktopsonlyonprimary/

%files -n kate-krunner-plugin
%{_kf6_plugindir}/krunner/krunner_katesessions.so

%files devel
%{_libdir}/libplasmaweatherdata.so
%{_libdir}/libplasmaweatherion.so
%{_libdir}/cmake/PlasmaPotdProvider/
%{_includedir}/plasma/potdprovider/
%{_kf6_datadir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2
%{_kf6_libdir}/libplasmapotdprovidercore.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
