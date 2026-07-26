%global source0_hash 00f77e240c22594706e1beb282ab0f5447f422d7a830efa640b7938680243c9a

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kcm_wacomtablet
Summary: KDE Control module for Wacom Graphictablets
Version: 6.6.4
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/system/wacomtablet
Source0: http://download.kde.org/%{stable_kf6}/plasma/%{version}/wacomtablet-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/plasma/%{version}/wacomtablet-%{version}.tar.xz.sig

## upstream patches

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KirigamiPlatform)
BuildRequires: cmake(Plasma5Support)
BuildRequires: cmake(Plasma)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: kf6-rpm-macros

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel

BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xorg-wacom)
BuildRequires: pkgconfig(xrandr)

ExcludeArch: s390 s390x

Obsoletes: kcm-wacomtablet < 1.3.7-2
Provides:  kcm-wacomtablet = %{version}-%{release}

%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button/pen layouts per profile.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n wacomtablet-%{version} 

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%doc AUTHORS
%license COPYING*
%{_datadir}/dbus-1/interfaces/org.kde.Wacom*.xml
%{_kf6_bindir}/kde_wacom_tabletfinder
%{_kf6_datadir}/applications/kcm_wacomtablet.desktop
%{_kf6_datadir}/applications/kde_wacom_tabletfinder.desktop
%{_kf6_datadir}/knotifications6/wacomtablet.notifyrc
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.wacomtablet/
%{_kf6_datadir}/plasma5support/services/wacomtablet.operations
%{_kf6_datadir}/wacomtablet/
%{_kf6_datadir}/qlogging-categories6/wacomtablet.categories
%{_kf6_metainfodir}/org.kde.wacomtablet.metainfo.xml
%{_qt6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_wacomtablet.so
%{_kf6_plugindir}/kded/wacomtablet.so
%{_qt6_plugindir}/plasma5support/dataengine/plasma_engine_wacomtablet.so

%changelog
%autochangelog
