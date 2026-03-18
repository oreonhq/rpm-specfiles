
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           koko
Version:        25.12.3
Release:        1%{?dist}
# Automatically converted from old format: GPLv2+ and GPLv3 and LGPLv2 and LGPLv2+ and CC0 and BSD - review is highly recommended.
License:        GPL-2.0-or-later AND GPL-3.0-only AND LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-LGPLv2+ AND CC0-1.0 AND LicenseRef-Callaway-BSD
Summary:        An Image gallery application
Url:            https://apps.kde.org/koko/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:        https://download.geonames.org/export/dump/cities1000.zip
Source2:        https://download.geonames.org/export/dump/admin1CodesASCII.txt
Source3:        https://download.geonames.org/export/dump/admin2Codes.txt

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6KirigamiAddons)

BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-atom)

# QML module dependencies
Requires:      kf6-kcoreaddons%{?_isa}
Requires:      kf6-kdeclarative%{?_isa}
Requires:      kf6-kirigami%{?_isa}
Requires:      kf6-kirigami-addons%{?_isa}
Requires:      kf6-purpose%{?_isa}
Requires:      kquickimageeditor-qt6%{?_isa}
Requires:      qt6-qtmultimedia%{?_isa}

Obsoletes:     %{name}-devel < 24.01.80

%description
%{summary}.

%prep
%autosetup
# Copying these to src dir as per https://invent.kde.org/graphics/koko/-/blob/master/README.md Packaging section.
cp %{_topdir}/SOURCES/cities1000.zip src/
cp %{_topdir}/SOURCES/admin1CodesASCII.txt src/
cp %{_topdir}/SOURCES/admin2Codes.txt src/

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%{_kf6_bindir}/%{name}

%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
%{_kf6_datadir}/knotifications6/*
%{_kf6_datadir}/%{name}
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
