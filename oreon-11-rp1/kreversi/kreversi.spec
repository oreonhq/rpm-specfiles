%global source0_hash 2dbb1e9b0e6aed1632a6499e75396f3eac9a0c1030e8175f1b71af19bdf87687

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kreversi
Summary: Reversi board game
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/games/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)

%description
Kreversi is a simple one player strategy game played against the
computer. The playing field is an 8 by 8 square board divided into 64
squares. The game pieces used are two sided stones, where each side has
its own, distinctive color. If a piece is captured by an opposing player,
that piece is turned over to reveal the color of that player. A winner
is declared when one player has more pieces of his own color on the
board and there are no more possible moves.

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
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/knotifications6/%{name}.notifyrc

%changelog
%autochangelog
