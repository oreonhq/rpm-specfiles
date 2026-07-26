%global source0_hash 75b9e1a26f0f468d016b2dc3cd2d8fd31412ac968c5c3e7551a7502f7cfac476

%bcond tests 1

Name:    kronometer
Summary: A stopwatch application by KDE
Version: 2.3.0
Release: 10%{?dist}

# code is GPLv2, appdata file is CC0
License: GPL-2.0-or-later AND CC0-1.0
URL:     https://userbase.kde.org/Kronometer

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable}/%{name}/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-F07D85CAA18ACF46A346FD017C7FC6EA8633B4EA.gpg

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: gnupg2
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt5Core) >= 5.15.0
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)

# kf5
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)

%if %{with tests}
BuildRequires: cmake(Qt5Test)
%endif

Requires: kde-filesystem
Requires: hicolor-icon-theme

%description
Kronometer is a stopwatch application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?with_tests:ON}%{!?with_tests:OFF}
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-man
zcat %{buildroot}%{_kf5_datadir}/icons/hicolor/scalable/apps/kronometer.svgz > %{buildroot}%{_kf5_datadir}/icons/hicolor/scalable/apps/kronometer.svg
rm %{buildroot}%{_kf5_datadir}/icons/hicolor/scalable/apps/kronometer.svgz

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%if %{with tests}
export QT_QPA_PLATFORM=offscreen
%ctest --extra-verbose
%endif

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt LICENSES/CC0-1.0.txt
%{_kf5_datadir}/applications/org.kde.kronometer.desktop
%{_kf5_bindir}/kronometer
%{_kf5_datadir}/config.kcfg/kronometer.kcfg
%{_kf5_metainfodir}/org.kde.kronometer.appdata.xml
%{_kf5_datadir}/icons/hicolor/*/apps/kronometer.*
%{_mandir}/man1/kronometer.1*

%changelog
%autochangelog
