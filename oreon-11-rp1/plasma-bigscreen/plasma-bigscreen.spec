%global source0_hash fd00b8ffd6a1c0fd7058acd06098110b00b5ca1dc720167058fad65d2ab50bdc
%global stable_kf6 stable
Name:          plasma-bigscreen
Version:        6.7.5
Release:        1%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later and CC-BY-SA-4.0
Summary:        A big launcher giving you access to any installed apps and skills
Url:           https://invent.kde.org/plasma/plasma-bigscreen
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Requires:   %{name}-wayland = %{version}-%{release}
Requires:   qt6qml(org.kde.plasma.private.nanoshell)
# oreon:deps
BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaActivitiesStats)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(SDL3)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libcec)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  wayland-devel
# /oreon:deps
%package  wayland
Summary:   Wayland support for %{name}
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}
Requires:  plasma-workspace-wayland >= %{version}
Obsoletes: %{name}-x11 < %{version}-%{release}
Conflicts: %{name}-x11 < %{version}-%{release}
%description wayland
%{summary}

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang all --with-man --with-qt --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kcm_mediacenter_*.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/plasma-bigscreen-swap-session.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.bigscreen.{inputhandler,uvcviewer}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n plasma-bigscreen-wayland -f %{oreon_filedir}/plasma-bigscreen-wayland.list

%changelog

%autochangelog
* Mon May 25 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.6.5-1
- Update to KDE Plasma 6.6.5

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.5.80^20260218.085444.a1b44a8-4
- Import
