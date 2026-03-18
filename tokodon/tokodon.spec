Name:           tokodon 
Version:        25.12.3
Release:        1%{?dist}
# Automatically converted from old format: GPLv3 and CC0 and BSD and LGPLv2+ and GPLv3+ and GPLv2 - review is highly recommended.
License:        GPL-3.0-only AND CC0-1.0 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+ AND GPL-3.0-or-later AND GPL-2.0-only
# For a breakdown of the licensing, see PACKAGE-LICENSING
Summary:        Kirigami-based mastodon client
Url:            https://invent.kde.org/network/tokodon
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  appstream

BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6WebView)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(KUnifiedPush)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(QCoro6)

BuildRequires:  cmake(MpvQt)
# Should not be required, but mpv is built against it, so...
BuildRequires:  pkgconfig(jack)
# ---
BuildRequires:  pkgconfig(openssl)

Requires:       hicolor-icon-theme
# QML module dependencies
Requires:       kf6-kcoreaddons%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
Requires:       kf6-kitemmodels%{?_isa}
Requires:       kf6-knotifications%{?_isa}
Requires:       kf6-purpose%{?_isa}
Requires:       kf6-sonnet%{?_isa}
Requires:       qt6-qt5compat%{?_isa}
Requires:       qt6-qtwebview%{?_isa}

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch: %{qt6_qtwebengine_arches}

%description
Tokodon is a Mastodon client for Plasma and Plasma Mobile.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf6 %{?flatpak:-DQT_BUILD_CMAKE_PREFIX_PATH=%{_libdir}/cmake}
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_plugindir}/purpose/tokodonplugin.so
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_datadir}/knotifications6/tokodon.notifyrc
%{_kf6_datadir}/qlogging-categories6/tokodon.categories
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/dbus-1/services/org.kde.tokodon.service

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
