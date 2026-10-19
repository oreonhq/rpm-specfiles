%global source0_hash 723a806681faeb3d4aa2fbc93e11392f6fbb66d8bfadcc5508c355d2eaa893ee
%global _changelog_trimtime %(date +%s -d "1 year ago")
ExcludeArch: %{ix86}
Name:    yakuake
Version: 26.08.1
Release:        1%{?dist}
Summary:        A drop-down terminal emulator
License: GPL-2.0-only OR GPL-3.0-only
URL: https://kde.org/applications/system/org.kde.yakuake
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       konsole-part%{?_isa} >= %{version}
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  xcb-util-devel
# /oreon:deps
%description
Yakuake is a drop-down terminal emulator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%check

%if 0%{?appstream_validate}
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.yakuake.appdata.xml
%endif
desktop-file-validate  %{buildroot}%{_kf6_datadir}/applications/org.kde.yakuake.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
