%global source1_hash 23c6bead7f3c15ddee0e680fc2a85c7cc5c46c4b4ce709f87522d3e643565958
%global source0_hash e25d53707be3bf86aad2b2712bcdcb9133f7c75a54c434724de5663aa78b773f
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:           plasma-mobile
Version:        6.7.5
Release:        1%{?dist}
License:        CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-only AND MIT
Summary:        General UI components for Plasma Phone including shell, containment and applets
Url:            https://invent.kde.org/plasma/plasma-mobile
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/plasma-mobile-%{version}.tar.xz.sig
Source15:        fedora-lookandfeel.json
Patch1001:      plasma-mobile-load-fedora-wallpaper.patch
Patch1002:      plasma-mobile-select-fedora-lookandfeel.patch
%global plasma_version %(echo %{version} | cut -d. -f1-3)
Requires: feedbackd
Requires: kf6-bluez-qt
Requires: kf6-kactivities
Requires: kf6-kdeclarative
Requires: kf6-kirigami2
Requires: kpipewire
Requires: kscreen
Requires: kwin
Requires: plasma-milou
Requires: plasma-nano
Requires: plasma-nm
Requires: plasma-pa
Requires: plasma-workspace >= %{plasma_version}
Requires: qqc2-breeze-style
Requires: qt6-qtwayland
Requires: plasma-lookandfeel-fedora-mobile = %{version}-%{release}
Requires: system-backgrounds-kde
Obsoletes: plasma-nm-mobile < 5.27.81
# oreon:deps
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6ModemManagerQt)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPipeWire)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kwin-devel
BuildRequires:  libappstream-glib
BuildRequires:  libepoxy-devel
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  system-backgrounds-kde
BuildRequires:  wayland-devel
# /oreon:deps
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
%oreon_autofiles plasma-lookandfeel-fedora-mobile usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.plasma.mobileshell.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_{mobile_info,mobile_time,mobileshell,navigation,waydroidintegration}.desktop
%files -f %{oreon_filedir}/main.list
%files -n plasma-lookandfeel-fedora-mobile -f %{oreon_filedir}/plasma-lookandfeel-fedora-mobile.list

%changelog

* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.7.4-1
- Latest upstream release

* Mon May 25 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.6.5-1
- Update to KDE Plasma 6.6.5

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.5-1
- Import
