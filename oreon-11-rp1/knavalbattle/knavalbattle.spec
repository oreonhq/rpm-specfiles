%global source0_hash 3836446f6c797ee8e664877383aa1f7bd001e2938b107a9bea82e7d9f96d78e5

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    knavalbattle
Summary: A ship sinking game
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

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kdnssd-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-knotifyconfig-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  kf6-rpm-macros
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6TextWidgets)

#BuildRequires:  libappstream-glib
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires:  libkdegames-devel >= %{majmin_ver}
BuildRequires:  pkgconfig(Qt6Widgets)

%description
Naval Battle is a ship sinking game for KDE. Ships are placed on a board
which represents the sea. Players try to hit each others ships in turns
without knowing where they are placed. The first player to destroy all
ships wins the game.

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
%license COPYING*
%{_kf6_bindir}/%{name}
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/qlogging-categories6/%{name}*

%changelog
%autochangelog
