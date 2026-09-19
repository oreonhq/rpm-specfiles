%global source0_hash 5e42f87474452d128f8091715f6b0582afa45da7dd7266b0bc20108f860d0c99

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    klines
Summary: Color lines game
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
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(KDEGames6)

%description
The goal of Kolor Lines is quite plain. The player has to move the
colored balls around the game board, gathering them into the lines
of the same color by five. Once the line is complete it is removed
from the board, therefore freeing precious space. In the same time
the new balls keep arriving by three after each move, filling up the
game board.  

Kolor Lines cannot be won, and is played against the high score
exclusively. The game ends once the whole game board is filled up with
balls

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
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_kf6_datadir}/qlogging-categories6/%{name}*

%changelog
%autochangelog
