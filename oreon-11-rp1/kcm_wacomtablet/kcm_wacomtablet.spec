%global source1_hash 8d21cab9aafa27c7440075160e2737ff3d2d43f65029a6615d108068bc000599
%global source0_hash f668f1dbd18d5f9060b016dbc5667619b214e4e6ac0456be7d322214c20e9cbe
ExcludeArch: %{ix86}
Name:    kcm_wacomtablet
Summary:        KDE Control module for Wacom Graphictablets
Version: 6.7.5
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/system/wacomtablet
Source0:        https://download.kde.org/stable/plasma/%{version}/wacomtablet-%{version}.tar.xz
Source1: https://download.kde.org/stable/plasma/%{version}/wacomtablet-%{version}.tar.xz.sig
ExcludeArch: s390 s390x
Obsoletes: kcm-wacomtablet < 1.3.7-2
Provides:  kcm-wacomtablet = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-wacom)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
# /oreon:deps
%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button/pen layouts per profile.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir wacomtablet-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
