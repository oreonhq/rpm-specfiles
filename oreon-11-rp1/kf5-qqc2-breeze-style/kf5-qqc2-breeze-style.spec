%global source0_hash fdb971b7eb7a3ca0438abf236d38a5f23d2c8c9414895550b0bd603e68e3610f
%global component qqc2-breeze-style
ExcludeArch: %{ix86}
Name:     kf5-%{component}
Version:  5.27.11
Release:        1%{?dist}
Summary:        Qt5QuickControls2 breeze style
License:  LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only) AND (LGPL-3.0-only OR GPL-2.0-or-later)
URL:      https://invent.kde.org/plasma/%{component}
Source0:        https://download.kde.org/stable/plasma/%{version}/%{component}-%{version}.tar.xz
Requires: kf5-kirigami2%{?_isa}
Requires: qt5-qtquickcontrols2%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5QuickTemplates2)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
