%global source0_hash c5d768313baa3325a9bc64b6a8a9d7075861c052bc72235bf9aa6c96158ce16a

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kiriki
Summary: A dice game
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
BuildRequires:  libappstream-glib

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  kf6-rpm-macros
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}

%description
Kiriki is an addictive and fun dice game for KDE, designed to be played by as
many as six players. Participants have to collect points by rolling five dice
for up to three times per single turn. Each roll generates a specific
combination of numbers which the player is free to either accept or decline.
However, each specific combination of numbers can be accepted only once.
After thirteen turns the game ends and the scores are compared.
The player with the largest amount of points wins the game.

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

%changelog
%autochangelog
