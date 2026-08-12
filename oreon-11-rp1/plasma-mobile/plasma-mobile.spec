%global source0_hash 378085f75cb0378a46fa12cc678a0e87f2bf9f1771eb514730da8b0a617e8bec

%global stable_kf6 stable


# 
ExcludeArch: %{ix86}

Name:           plasma-mobile
Version:        6.7.4
Release: 2%{?dist}
License:        CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-only AND MIT
Summary:        General UI components for Plasma Phone including shell, containment and applets
Url:            https://invent.kde.org/plasma/plasma-mobile
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/plasma-mobile-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/plasma-mobile-%{version}.tar.xz.sig

Source15:        fedora-lookandfeel.json

## upstream patches

## downstream patches
Patch1001:      plasma-mobile-load-fedora-wallpaper.patch
Patch1002:      plasma-mobile-select-fedora-lookandfeel.patch

# Remove the 'bugfix' digit from the version for some runtime requirements
%global plasma_version %(echo %{version} | cut -d. -f1-3)

BuildRequires: extra-cmake-modules
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires: gcc-c++
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kwin-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libdrm)

BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6ModemManagerQt) >= 6.28.0
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6People)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Screen)
BuildRequires: cmake(KF6KirigamiPlatform)
BuildRequires: cmake(KPipeWire)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(QCoro6)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(LibKWorkspace)
BuildRequires: cmake(LayerShellQt)
BuildRequires: libepoxy-devel
BuildRequires: wayland-devel
BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: cmake(Plasma)
BuildRequires: cmake(KWayland)
BuildRequires: system-backgrounds-kde

Requires: feedbackd
Requires: kf6-bluez-qt
Requires: kf6-kactivities
Requires: kf6-kdeclarative
Requires: kf6-kirigami2
Requires: kpipewire
# Plasma Mobile uses kscreen to automatically set a logical scaling factor based on hardware
Requires: kscreen
Requires: kwin
Requires: plasma-milou
Requires: plasma-nano
Requires: plasma-nm
Requires: plasma-pa
Requires: plasma-workspace >= %{plasma_version}
Requires: qqc2-breeze-style
Requires: qt6-qtwayland

# Default look-and-feel theme
Requires: plasma-lookandfeel-fedora-mobile = %{version}-%{release}
Requires: system-backgrounds-kde

# This package now integrates what was plasma-nm-mobile
Obsoletes: plasma-nm-mobile < 5.27.81


BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  libxcb-devel
%description
%{summary}.

%package -n plasma-lookandfeel-fedora-mobile
Summary:  Fedora look-and-feel for Plasma Mobile
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description -n plasma-lookandfeel-fedora-mobile
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Populate initial lookandfeel package
cp -a lookandfeel lookandfeel-fedora
# Overwrite settings to configure distro wallpaper
sed -i -e 's|Image=Next$|Image=Default|' lookandfeel-fedora/contents/defaults
install -m 0644 %{SOURCE15} lookandfeel-fedora/metadata.json
cat >> CMakeLists.txt <<EOL
plasma_install_package(lookandfeel-fedora org.fedoraproject.fedora.mobile look-and-feel lookandfeel)
EOL

# RHEL 10 has .png, not .jxl
if [ -e /usr/share/wallpapers/Default/contents/images/3840x2160.png ]; then
  sed -e 's|\.jxl|.png|g' -i initialstart/qml/LandingComponent.qml
fi

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang plasma_applet_org.kde.phone.homescreen --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.plasma.mobileshell.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_{mobile_info,mobile_time,mobileshell,navigation,waydroidintegration}.desktop

%files -f plasma_applet_org.kde.phone.homescreen.lang
%license LICENSES/*
%{_kf6_datadir}/plasma-mobile-device-presets/
%{_kf6_metainfodir}/org.kde.plasma.mobileshell.metainfo.xml
%{_kf6_libexecdir}/kauth/flashlighthelper
%{_kf6_libexecdir}/kauth/waydroidhelper
%{_kf6_bindir}/startplasmamobile
%{_kf6_bindir}/plasma-mobile-envmanager
%{_kf6_bindir}/plasma-mobile-initial-start
%{_kf6_datadir}/plasma/quicksettings
%{_kf6_datadir}/wayland-sessions/plasma-mobile.desktop
%{_kf6_datadir}/plasma/shells/org.kde.plasma.mobileshell
%{_kf6_datadir}/plasma-mobile-apn-info/apns-full-conf.xml
%{_kf6_datadir}/plasma/look-and-feel/org.kde.breeze.mobile
%{_kf6_datadir}/plasma/mobileinitialstart
%{_kf6_datadir}/applications/*.desktop
%{_kf6_datadir}/knotifications6/plasma_mobile_quicksetting*.notifyrc
%{_kf6_datadir}/kwin/effects/mobiletaskswitcher
%{_kf6_datadir}/kwin/scripts/convergentwindows/contents/ui/main.qml
%{_kf6_datadir}/kwin/scripts/convergentwindows/metadata.json
%{_kf6_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultNavigationPanel/contents/layout.js
%{_kf6_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultNavigationPanel/metadata.json
%{_kf6_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultStatusBar/contents/layout.js
%{_kf6_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultStatusBar/metadata.json
%{_kf6_qmldir}/org/kde/plasma/mm/*
%{_kf6_qmldir}/org/kde/plasma/private/mobileshell
%{_kf6_qmldir}/org/kde/plasma/quicksetting
%{_kf6_qmldir}/org/kde/plasma/mobileinitialstart
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_navigation.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_waydroidintegration.so
%{_datadir}/dbus-1/interfaces/org.kde.plasmashell*.xml
%{_datadir}/dbus-1/system-services/org.kde.plasma.mobileshell*.service
%{_datadir}/dbus-1/system.d/org.kde.plasma.mobileshell*.conf
%{_datadir}/polkit-1/actions/org.kde.plasma.mobileshell*.policy
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_mobileshell.so
%{_kf6_qtplugindir}/plasma/applets/*.so
%{_kf6_qtplugindir}/kf6/kded/kded_plasma_mobile_start.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_mobile_*.so
%{_kf6_qtplugindir}/kf6/kded/kded_plasma_mobile_autodetect_apn.so

%files -n plasma-lookandfeel-fedora-mobile
%{_kf6_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.mobile

%changelog
* Mon May 25 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.6.5-1
- Update to KDE Plasma 6.6.5

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.5-1
- Import
