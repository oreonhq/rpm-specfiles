%global source0_hash bbea67e19d3236724cfc1067f414f9bcf50364f1b4fd18e9478640288448b154

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdf
Summary: View disk usage
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://apps.kde.org/kdf/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)

%description
KDiskFree displays the available file devices (hard drive partitions,
floppy and CD/DVD drives, etc.) along with information on their capacity,
free space, type and mount point.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/kdf
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_datadir}/icons/hicolor/*/apps/*
%{_kf6_bindir}/kwikdisk
%{_kf6_libdir}/libkdfprivate.so.*
%{_kf6_datadir}/applications/org.kde.kdf.desktop
%{_kf6_datadir}/applications/org.kde.kwikdisk.desktop
%{_kf6_datadir}/applications/kcm_kdf.desktop
%{_kf6_metainfodir}/org.kde.*.appdata.xml
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kdf.so

%changelog
%autochangelog
