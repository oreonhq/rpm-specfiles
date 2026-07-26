%global source0_hash eb84a40a83d7c2392f0100e91ca14547ab7ec2eebe15f02a08ce4a60358e3629

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kshisen
Summary: Shisen-Sho Mahjongg-like tile game
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
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Crash)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}
BuildRequires: libkmahjongg-devel >= %{majmin_ver}
BuildRequires: phonon-qt6-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: libappstream-glib

%description
Shisen-Sho is a solitaire-like game played using the standard set of Mahjong
tiles. Unlike Mahjong however, Shisen-Sho has only one layer of scrambled tiles.
You can remove matching pieces if they can be connected with a line with at most
two bends in it. At the same time, the line must not cross any other tiles.
To win a game of Shisen-Sho the player has to remove all the tiles from the
game board

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
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/sounds/%{name}
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_kf6_datadir}/icons/hicolor/*/*/*

%changelog
%autochangelog
