
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           kongress
Version:        25.12.3
Release:	2%{?dist}
# Automatically converted from old format: CC0 and CC-BY-SA and BSD and GPLv3+ - review is highly recommended.
License:        CC0-1.0 AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-BSD AND GPL-3.0-or-later
Summary:        A companion application for conferences made by KDE
Url:            https://apps.kde.org/kongress/
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KOSMIndoorMap)

Requires:      kf6-kirigami-addons%{?_isa}
Requires:      kf6-kirigami%{?_isa}
Requires:      kosmindoormap%{?_isa}
Requires:      qt6-qtlocation%{?_isa}
Requires:      qt6-qtpositioning%{?_isa}

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%{_kf6_bindir}/%{name}ac

%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.kongressac.service
%{_kf6_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
%{_kf6_datadir}/knotifications6/kongressac.notifyrc

%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%license LICENSES/*

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
