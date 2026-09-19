%global source0_hash 18ad9dba43cb524458ad1f38097212fdaf5d01e3d5d71931b341026a48d3dcd0

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    sweeper
Summary: Clean unwanted traces the user leaves on the system
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://invent.kde.org/utils/%{name}
Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(PlasmaActivitiesStats)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)

Requires: hicolor-icon-theme

%description
Sweeper helps to clean unwanted traces the user leaves on the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.sweeper.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.sweeper.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/sweeper
%{_kf6_datadir}/qlogging-categories6/sweeper*
%{_kf6_datadir}/applications/org.kde.sweeper.desktop
%{_kf6_metainfodir}/org.kde.sweeper.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.sweeper.xml
%{_datadir}/icons/hicolor/scalable/apps/sweeper.svg

%changelog
%autochangelog
