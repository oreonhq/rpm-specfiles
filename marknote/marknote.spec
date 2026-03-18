Name:          marknote
Version:       1.4.1
Release:       2%{?dist}
License:       BSD-3-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-only
Summary:       A simple markdown note management app for KDE
URL:           https://apps.kde.org/%{name}/

Source0:       https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6BreezeIcons)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(KPim6Mime)

BuildRequires: cmake(md4c)

Requires:      hicolor-icon-theme
Requires:      qt6qml(org.kde.iconthemes)
Requires:      qt6qml(org.kde.kirigamiaddons.components)
Requires:      qt6qml(org.kde.kitemmodels)
Requires:      qt6qml(org.kde.sonnet)
Requires:      qt6qml(org.kde.desktop)
Requires:      qt6qml(org.kde.kirigami)

%description
Marknote lets you create rich text notes and easily organize them
into notebooks. You can personalize your notebooks by choosing an
icon and accent color for each one, making it easy to distinguish
between them and keep your notes at your fingertips.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.marknote.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/marknote
%{_kf6_datadir}/applications/org.kde.marknote.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.marknote.svg
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/marknote.categories

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.1-2
- Prepare for Oreon 11 (RP1)
