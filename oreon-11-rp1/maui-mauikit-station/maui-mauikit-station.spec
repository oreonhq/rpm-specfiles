%global source0_hash 8834adb7474e924ac1a4dd0981c237fd5cc4e2902c2c94268314e9c24c5285e0

Name:          maui-mauikit-station
Version:       4.0.0
Release:       4%{?dist}
License:       MIT AND GPL-3.0-or-later
Summary:       Convergent terminal emulator written using Maui
URL:           https://mauikit.org/apps/station/

Source0:       https://download.kde.org/stable/maui/station/%{version}/maui-station-%{version}.tar.xz

# Added missing licenses, removed unused license
# https://invent.kde.org/maui/maui-station/-/merge_requests/8
Patch0:        8.patch

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)

BuildRequires: cmake(MauiKitTerminal4)
BuildRequires: cmake(MauiKitFileBrowsing4)
BuildRequires: cmake(MauiKit4)

Requires:      hicolor-icon-theme

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n maui-station-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang station --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.station.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f station.lang
%license LICENSES/*
%{_bindir}/station
%{_datadir}/applications/org.kde.station.desktop
%{_datadir}/icons/hicolor/scalable/apps/station.svg
%{_metainfodir}/org.kde.station.appdata.xml

%changelog
%autochangelog
