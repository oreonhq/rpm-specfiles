%global source0_hash 362c9d376c4ff451d42777f8f8f9f21f2042cecb117f1b5cf2da77b10a43c9df

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    yakuake
Version: 25.12.3
Release: 1%{?dist}
Summary: A drop-down terminal emulator

# KDE e.V. may determine that future GPL versions are accepted
License: GPL-2.0-only OR GPL-3.0-only
URL: https://kde.org/applications/system/org.kde.yakuake
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream fixes

# konsolepart
Requires:       konsole-part%{?_isa} >= %{version}

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel

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
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KWayland)

%if 0%{?fedora}
%global appstream_validate 1
BuildRequires:  libappstream-glib
%endif

%description
Yakuake is a drop-down terminal emulator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
%if 0%{?appstream_validate}
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.yakuake.appdata.xml
%endif
desktop-file-validate  %{buildroot}%{_kf6_datadir}/applications/org.kde.yakuake.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license LICENSES/*
%{_kf6_bindir}/yakuake
%{_kf6_datadir}/knsrcfiles/yakuake.knsrc
%{_kf6_metainfodir}/org.kde.yakuake.appdata.xml
%{_kf6_datadir}/applications/org.kde.yakuake.desktop
%{_kf6_datadir}/knotifications6/yakuake.notifyrc
%{_kf6_datadir}/yakuake/
%{_kf6_datadir}/icons/hicolor/*/apps/yakuake.*
%{_kf6_datadir}/dbus-1/services/org.kde.yakuake.service

%changelog
%autochangelog
