
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           plasmatube
Version:        25.12.3
Release:        1%{?dist}
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC0-1.0 AND CC-BY-SA-4.0
Summary:        YouTube video player based on QtMultimedia and youtube-dl
Url:            https://apps.kde.org/plasmatube/
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# Upstream patches
# Remove appstream duplicate release version
# https://invent.kde.org/multimedia/plasmatube/-/merge_requests/109
Patch0:         109.patch

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(MpvQt)
BuildRequires:  cmake(Qt6Keychain)

Requires:       hicolor-icon-theme
# QML module dependencies
Requires:       kf6-kcoreaddons%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
Requires:       kf6-kitemmodels%{?_isa}
Requires:       kf6-knotifications%{?_isa}
Requires:       kf6-purpose%{?_isa}
Requires:       qt6-qt5compat%{?_isa}

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSES/*

%{_kf6_bindir}/%{name}

%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/actions/%{name}-*
%{_kf6_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*

%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/qlogging-categories6/plasmatube.categories

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
