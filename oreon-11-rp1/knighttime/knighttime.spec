%global source0_hash 97f612eb6cae0ee39ad3579bb9124d701751c83fd02cd3f5ed120896b1313a21

%global stable_kf6 stable


Name:           knighttime
Version: 6.7.0
Release:        5%{?dist}
Summary:        Plasma day and night cycle scheduling daemon
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/knighttime
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  systemd-rpm-macros

Requires:       kf6-filesystem

%description
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n knighttime-%{version} -p1


%build
# Autotests pull extra runtime; ORBS/mock often lacks D-Bus/X11 for them
%cmake_kf6 -DBUILD_TESTING=OFF
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
# Soname is libKNightTime.so.0 but the versioned file is libKNightTime.so.<upstream-version>
%{_libdir}/libKNightTime.so.*
%{_libdir}/libKNightTime.so
%{_includedir}/KNightTime/
%{_libdir}/cmake/KNightTime/
%{_libexecdir}/knighttimed
%{_kf6_datadir}/applications/org.kde.knighttimed.desktop
%{_datadir}/dbus-1/interfaces/org.kde.NightTime.xml
%{_datadir}/dbus-1/services/org.kde.NightTime.service
%{_kf6_datadir}/qlogging-categories6/knighttime.categories
%{_userunitdir}/plasma-knighttimed.service


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Add knighttime for Plasma
