%global source0_hash bbf1e147e9f89d222404eda2be3ad146ca0ed7c7415a03f96183c84db28ea4b4

# 
ExcludeArch: %{ix86}

Name:           krecorder
Version:        26.08.1
Release:        1%{?dist}
License:        BSD-3-Clause AND CC-BY-4.0 AND CC0-1.0 AND GPL-3.0-or-later
Summary:        Convergent KDE audio recording application
Url:            https://invent.kde.org/utilities/krecorder
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  kf6-kio-devel

Requires:       kf6-kirigami
Requires:       gstreamer1-plugins-good
Requires:       hicolor-icon-theme
Requires:       kf6-kirigami-addons

%description
Audio recorder for Plasma Mobile and other platforms

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg

%changelog
%autochangelog
