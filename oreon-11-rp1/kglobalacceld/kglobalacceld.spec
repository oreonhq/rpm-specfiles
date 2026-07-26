%global source0_hash c0a7ebc420c11206ffc0bea1cc4b51654fc2d235b07ccb3c5f0ae9713049d12c

Name:    kglobalacceld
Summary: Daemon providing Global Keyboard Shortcut functionality
Version: 6.6.4
Release: 1%{?dist}

License: CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0:  https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:  https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-gui
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  systemd
Requires:  kf6-filesystem

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*.txt
%{_sysconfdir}/xdg/autostart/kglobalacceld.desktop
%{_userunitdir}/plasma-kglobalaccel.service
%{_libdir}/libKGlobalAccelD.so.*
%dir %{_qt6_plugindir}/org.kde.kglobalacceld.platforms
%{_qt6_plugindir}/org.kde.kglobalacceld.platforms/KGlobalAccelDXcb.so
%{_libexecdir}/kglobalacceld
%{_kf6_datadir}/qlogging-categories6/kglobalacceld.categories

%files devel
%{_includedir}/KGlobalAccelD/
%{_libdir}/cmake/KGlobalAccelD/

%changelog
%autochangelog
