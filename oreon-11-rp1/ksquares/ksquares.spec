%global source0_hash 0c5f2fdf2cae5b1eb6a693f4d19c22c025746707e9e964fa23a5fc4e7a510a31

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ksquares
Summary: Connect the dots to create squares
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
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)

BuildRequires: pkgconfig(phonon4qt6)
BuildRequires: pkgconfig(Qt6Widgets) pkgconfig(Qt6Test)
#BuildRequires: libappstream-glib
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}

%description
The idea behind KSquares is to construct squares by interconnecting
the dots on the grid. Up to four players can play this game together,
taking turns. The trick is – regardless of who has constructed most
of the square, it is the player who completes the square that gets the
point for it.
To win the game round player has to collect the most points by covering
the most area with the squares of player's own color.

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
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/config.kcfg/%{name}.kcfg

%changelog
%autochangelog
