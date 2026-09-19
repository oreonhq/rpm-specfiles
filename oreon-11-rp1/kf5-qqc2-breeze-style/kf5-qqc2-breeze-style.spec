%global source0_hash fdb971b7eb7a3ca0438abf236d38a5f23d2c8c9414895550b0bd603e68e3610f

# Strictly speaking, this is not a framework, but part of Plasma.
# However unlike plasma-breeze, qqc2-breeze-style only builds a Qt6
# version, but there are still applications using Qt5QuickControl2 and
# KF5Kirigami2 which can use this.
%global component qqc2-breeze-style

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:     kf5-%{component}
Version:  5.27.11
Release:  6%{?dist}
Summary:  Qt5QuickControls2 breeze style

License:  LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only) AND (LGPL-3.0-only OR GPL-2.0-or-later)
URL:      https://invent.kde.org/plasma/%{component}
Source:   https://download.kde.org/stable/plasma/%{version}/%{component}-%{version}.tar.xz

## upstream patches

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5QuickTemplates2)
BuildRequires: cmake(Qt5X11Extras)

BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5IconThemes)

Requires: kf5-kirigami2%{?_isa}
Requires: qt5-qtquickcontrols2%{?_isa}

%description
This is a pure Qt Quick/Kirigami Qt5 Quick Controls style.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{component}-%{version} -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_plugindir}/kirigami/org.kde.breeze.so
%{_qt5_qmldir}/QtQuick/Controls.2/org.kde.breeze
%{_qt5_qmldir}/org/kde/breeze/
%{_qt5_qmldir}/org/kde/kirigami.2/styles/org.kde.breeze/
%{_kf5_libdir}/cmake/KF5QQC2BreezeStyle/

%changelog
%autochangelog
