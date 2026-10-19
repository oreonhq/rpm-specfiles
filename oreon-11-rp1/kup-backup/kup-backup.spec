%global source0_hash f2bbd69d7782c9fb274a8bfdb28d48f0176ab4490ff0caf2f66e8aa9fe40a53e
%global gitcommit 92115c258d04282e79c63c41de01644fe0b04d3b
%global gitdate 20260214.094327
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global projectname kup
Name:           kup-backup
Version:        0.10.0^git%{gitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        Backup scheduler for the Plasma desktop
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
URL:            https://apps.kde.org/%{projectname}/
Source0:        https://invent.kde.org/system/%{projectname}/-/archive/%{gitcommit}/%{projectname}-%{gitcommit}.tar.gz
Requires:       hicolor-icon-theme
Requires:       qt6qml(org.kde.kcmutils)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kquickcontrolsaddons)
Requires:       qt6qml(org.kde.plasma.components)
Requires:       qt6qml(org.kde.plasma.core)
Requires:       qt6qml(org.kde.plasma.extras)
Requires:       qt6qml(org.kde.plasma.plasma5support)
Requires:       qt6qml(org.kde.plasma.plasmoid)
Requires:       qt6qml(QtQuick)
Requires:       qt6qml(QtQuick.Layouts)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libgit2)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{projectname}-%{gitcommit} -p1

%build

%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{projectname}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_kup.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kup.appdata.xml ||:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
