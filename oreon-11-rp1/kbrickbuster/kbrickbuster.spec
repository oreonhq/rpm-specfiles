%global source0_hash f550cf8750e7f818e6b5b60c04e14024ed760a8ace70f7b9ce4bb85d3d5c6d1e
ExcludeArch: %{ix86}
Name:    kbrickbuster
Summary:        Destroy bricks with a ball
Version: 25.12.0
Release:        1%{?dist}
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://apps.kde.org/kbreakout/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/kbreakout-%{version}.tar.xz
Source1: patch.sh
Provides:  kbreakout = 1:%{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KDEGames6)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_datadir}/metainfo/org.kde.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
