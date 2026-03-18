%global orig_name org.kde.plasma.nano


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-nano
Version: 6.6.2
Release: 1%{?dist}
License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/plasma/plasma-nano

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

Summary: Minimalist Plasma shell for developing custom experiences on embedded devices

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libappstream-glib
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils

# KDE Frameworks
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KWinDBusInterface)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6KirigamiPlatform)

# Qt
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)

# Plasma
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KWayland)

Requires: libplasma
Requires: kwayland
Requires: kf6-kwindowsystem
Requires: kf6-kservice
Requires: kf6-kcoreaddons
Requires: kf6-kpackage
Requires: qt6-qtdeclarative


%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang plasma_shell_%{orig_name} --all-name


%files -f plasma_shell_%{orig_name}.lang
%license LICENSES/*.txt
%doc README.md

%{_kf6_qmldir}/org/kde/plasma/private/nanoshell
%{_kf6_datadir}/plasma/shells/%{orig_name}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
