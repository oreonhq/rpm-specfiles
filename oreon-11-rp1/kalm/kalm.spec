%global source0_hash c664e4f96419712df40cd85ae71a9eeb3b5dbfbb161c9a5b18ee9b38c432e643

%global app_id  org.kde.kalm

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           kalm
Version:        25.12.3
Release:        1%{?dist}
Summary:        Breathing techniques app
# LGPL: code
# CC0: metadata
License:        LGPL-2.1-or-later AND CC0-1.0
URL:            https://apps.kde.org/kalm/
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# Qt dependencies
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
# KF dependencies
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)

Requires:       hicolor-icon-theme
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)

%description
Kalm can teach you different breathing techniques.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt LICENSES/CC0-1.0.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_metainfodir}/%{app_id}.appdata.xml

%changelog
%autochangelog
