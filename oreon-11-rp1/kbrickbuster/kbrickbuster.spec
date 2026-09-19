%global source0_hash bcf8844996fc5c49dff82e52e219d773e05d61181f895bfad19c44e79a2c6d34

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kbrickbuster
Summary: Destroy bricks with a ball
Version: 25.12.0
Release: 2%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://apps.kde.org/kbreakout/

# Upstream source. Cannot be used because we need to *PATCH* the sources
#Source:  https://download.kde.org/%%{stable_kf6}/release-service/%%{version}/src/kbreakout-%%{version}.tar.xz
Source:  kbrickbuster-%{version}.tar.xz
# This patch is needed to modify upstream sources. They must be uploaded to the
# side-cache
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

%autosetup -n %{name}-%{version} -p1

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
