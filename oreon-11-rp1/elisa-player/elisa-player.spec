%global source0_hash e6a36f4c6cd8b775cc8f60f41dc950db86c45107ef74672616c8c683611aecc1
%global stable_kf6 stable
%global base_name elisa
ExcludeArch: %{ix86}
Name:       elisa-player
Version:    26.08.1
Release:        1%{?dist}
Summary:        Elisa music player
License:    LGPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:        https://community.kde.org/Elisa
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
Requires:       dbus-common
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}
Requires:       qt6-qt5compat%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
Elisa is a simple music player aiming to provide a nice experience for its
users.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir elisa-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang elisa --all-name --with-kde --with-html
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.elisa.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.elisa.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
