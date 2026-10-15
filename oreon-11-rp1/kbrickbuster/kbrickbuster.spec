%global source0_hash f550cf8750e7f818e6b5b60c04e14024ed760a8ace70f7b9ce4bb85d3d5c6d1e

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kbrickbuster
Summary: Destroy bricks with a ball
Version: 25.12.0
Release: 2%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://apps.kde.org/kbreakout/

Source:  https://download.kde.org/stable/release-service/%{version}/src/kbreakout-%{version}.tar.xz
Source1: patch.sh

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)

BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6DocTools)

BuildRequires: cmake(KDEGames6)

Provides:  kbreakout = 1:%{version}-%{release}

%description
The objective KBrickbuster game is to destroy as many bricks as possible
without losing the ball.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

bash %{SOURCE1} %{SOURCE0}
%setup -T -c -q -n %{name}-%{version}
tar Jxf /tmp/%{name}-%{version}.tar.xz --strip-components=1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_datadir}/metainfo/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/qlogging-categories6/%{name}.categories

%changelog
%autochangelog
