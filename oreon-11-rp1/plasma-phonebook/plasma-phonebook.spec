Name:           plasma-phonebook
Version:        24.02.0
Release:        6%{?dist}
License:        CC0 and GPLv2 and GPLv3 and GPLv3+ and LGPLv2+
Summary:        Convergent Plasma Mobile phonebook application
Url:            https://invent.kde.org/plasma-mobile/%{name}
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz


BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  appstream
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6KirigamiAddons)

Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.components)
Requires:       qt6qml(org.kde.people)
Requires:       qt6qml(Qt5Compat.GraphicalEffects)


%description
Contacts application which allows adding, modifying and removing contacts.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSES/{CC0-1.0.txt,GPL-2.0-only,GPL-3.0-only,GPL-3.0-or-later,LGPL-2.0-or-later,LicenseRef-KDE-Accepted-GPL}.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.phonebook.svg
%{_kf6_datadir}/applications/org.kde.phonebook.desktop
%{_kf6_metainfodir}/org.kde.phonebook.metainfo.xml
%{_qt6_plugindir}/kpeople/actions/phonebook_kpeople_plugin.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 24.02.0-6
- Prepare for Oreon 11 (RP1)
