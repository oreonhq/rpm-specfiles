
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           calindori
Version:        25.12.3
Release:	2%{?dist}
Summary:        Calendar application for Plasma Mobile
License:        BSD-2-Clause AND CC-BY-4.0 AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://apps.kde.org/%{name}/
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6DBus)

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6People)
BuildRequires: cmake(KF6DBusAddons)


Requires:      hicolor-icon-theme
Requires:      kf6-kirigami
Requires:      qt6-qtwayland

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name}
%find_lang calindac
cat %{name}.lang calindac.lang > %{name}-full.lang

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}-full.lang
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%{_kf6_bindir}/calindac
%{_kf6_datadir}/knotifications6/calindac.notifyrc
%{_kf6_sysconfdir}/xdg/autostart/org.kde.calindac.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.calindac.service

%license LICENSES/*

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
