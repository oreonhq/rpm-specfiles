%global framework qqc2-desktop-style

Name:    kf5-%{framework}
Version: 5.116.1
Release: 5%{?dist}
Summary: QtQuickControls2 style for consistency between QWidget and QML apps
License: LGPL-2.0-or-later AND (LGPL-3.0-only OR GPL-2.0-or-later) AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
Source:  https://download.kde.org/%{stable_kf5}/frameworks/%{majmin_ver_kf5}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires: extra-cmake-modules >= %{majmin_ver_kf5}
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5LinguistTools)

BuildRequires: cmake(KF5Config) >= %{majmin_ver_kf5}
BuildRequires: cmake(KF5ConfigWidgets) >= %{majmin_ver_kf5}
BuildRequires: cmake(KF5Kirigami2) >= %{majmin_ver_kf5}
BuildRequires: cmake(KF5IconThemes) >= %{majmin_ver_kf5}

Requires: kf5-kirigami2%{?_isa} >= %{majmin_ver_kf5}
Requires: kf5-sonnet%{?_isa} >= %{majmin_ver_kf5}
Requires: qt5-qtquickcontrols2%{?_isa}

# renamed
Provides:  %{framework} = %{version}-%{release}
Provides:  %{framework}%{?_isa} = %{version}-%{release}
Obsoletes: %{framework} < %{version}-%{release}

%description
This is a style for QtQuickControls 2 that uses QWidget's QStyle for
painting, making possible to achieve an higher degree of consistency
between QWidget-based and QML-based apps.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
%find_lang_kf5 qqc2desktopstyle5_qt


%files -f qqc2desktopstyle5_qt.lang
%doc README.md
%license LICENSES/*.txt
%dir %{_kf5_plugindir}/kirigami/
%{_kf5_plugindir}/kirigami/org.kde.desktop.so
%{_kf5_qmldir}/QtQuick/Controls.2/org.kde.desktop/
%{_kf5_qmldir}/org/kde/qqc2desktopstyle/
%{_kf5_libdir}/cmake/KF5QQC2DeskopStyle/
%{_kf5_libdir}/cmake/KF5QQC2DesktopStyle/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.1-5
- Prepare for Oreon 11 (RP1)
