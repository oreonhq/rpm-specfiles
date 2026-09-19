%global source0_hash 0b3e9bdaf3a9f2766efb7007dff9bb1278d4753eaa05eca138f24231ac485de2

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kcron
Summary: Cron KDE configuration module
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/system/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6PrintSupport)

BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6KirigamiAddons)

%description
Systemsettings module for the cron task scheduler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%doc README
%{_kf6_datadir}/qlogging-categories6/kcron*
%{_kf6_metainfodir}/org.kde.kcron.metainfo.xml
%{_kf6_libexecdir}/kauth/kcron_helper
%{_kf6_datadir}/dbus-1/system-services/local.kcron.crontab.service
%{_kf6_datadir}/dbus-1/system.d/local.kcron.crontab.conf
%{_kf6_datadir}/polkit-1/actions/local.kcron.crontab.policy
%{_kf6_datadir}/applications/kcm_cron.desktop
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_cron.so

%changelog
%autochangelog
