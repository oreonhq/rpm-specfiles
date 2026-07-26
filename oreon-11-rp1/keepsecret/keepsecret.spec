%global source0_hash d3360caaa527af41f49f2758a93edd83b932a1de2d0993572c958b1eec6f0fe9

Name:           keepsecret
Version:        1.0.0
Release:        2%{?dist}
Summary:        Client for a Secret Service compatible provider

License:        BSD-2-Clause AND BSD-3-Clause AND CC-BY-4.0 AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://apps.kde.org/keepsecret/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

# Fixes the keep secret icon using the kwalletmanager5 one
# https://invent.kde.org/utilities/keepsecret/-/merge_requests/15
Patch0:         15.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6DBusAddons)

BuildRequires:  pkgconfig(libsecret-1)

Requires:       qt6qml(org.kde.kirigamiaddons.components)
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)
Requires:       qt6qml(org.kde.config)
Requires:       qt6qml(org.kde.coreaddons)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kitemmodels)
Requires:       hicolor-icon-theme

%description
KeepSecret is a Password manager GUI intended to be a
client for a Secret Service compatible provider.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.keepsecret.*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.keepsecret.desktop

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/keepsecret
%{_kf6_datadir}/applications/org.kde.keepsecret.desktop
%{_kf6_metainfodir}/org.kde.keepsecret.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/keepsecret.categories
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.keepsecret.svg

%changelog
%autochangelog
