%global source0_hash 7059b1341d4ff142388ed502f903256262722c2fbe4f73c1b288e4d713c8d261

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kapman
Summary: A collecting game
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
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)

BuildRequires: pkgconfig(Qt6Widgets) pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(phonon4qt6)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}
# uses libkdegames-private
BuildRequires: libkdegames-private-devel

%description
Kapman is a collecting game. You must go through the levels escaping
ghosts in a maze. You lose a life when a ghost eats you, but you can eat
the ghosts for a few seconds when eating an energizer. You win points
when eating pills, energizers, and bonus, and you win one life for
each 10,000 points. When you have eaten all the pills and energizers
of a level, you go to the next level, and the player and ghost speeds
increase. The game ends when you have lost all your lives.

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
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop ||:

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/sounds/%{name}/

%changelog
%autochangelog
