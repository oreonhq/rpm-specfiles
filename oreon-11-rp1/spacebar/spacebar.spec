Name:           spacebar
Epoch:          1
Version:        6.6.2
Release:        1%{?dist}
License:        GPLv2+ and GPLv3 and GPLv2
Summary:        Messaging app for Plasma Mobile
Url:            https://invent.kde.org/plasma-mobile/spacebar
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz.sig

ExclusiveArch:  %{java_arches}

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel

BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Sql)

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6ModemManagerQt)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(libphonenumber)

BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  cmake(FutureSQL6)

Requires:       hicolor-icon-theme
Requires:       kf6-kirigami
Requires:       telepathy-mission-control

%description
Spacebar is a telepathy-qt based SMS application that primarily targets Plasma Mobile.

%prep
%autosetup -n spacebar-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/{GPL-2.0-or-later,LicenseRef-KDE-Accepted-GPL}.txt
%{_kf6_bindir}/%{name}
%{_kf6_bindir}/spacebar-fakeserver
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_datadir}/knotifications6/%{name}.notifyrc

%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_libexecdir}/%{name}-daemon
%{_sysconfdir}/xdg/autostart/org.kde.%{name}.daemon.desktop

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
